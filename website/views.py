from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import  login_required, current_user
from . import db
from website.auth import login
from .forms import PostForm, CommentForm
from .models import Post, Comments
import cloudinary
import cloudinary.uploader
import timeago, datetime

views = Blueprint('views', __name__)
ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg", "gif"]
def time_ago(date):
        now=datetime.datetime.utcnow() + datetime.timedelta(seconds = 60 * 3.4)
        
        return timeago.format(date, now)

        
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    
    form = PostForm()
    all_posts = Post.query.all()
    
    if request.method == "POST":
        
        user_id = current_user.id 
        title = form.title.data
        description= form.description.data
        img_name_main = form.img_file.data

        if img_name_main.filename.split(".")[-1].lower() in ALLOWED_EXTENSIONS:    
            upload_result = cloudinary.uploader.upload(img_name_main,use_filename = True, unique_filename = False)
            
            new_post = Post(title=title, description=description, img_name=upload_result.get("secure_url"), user_id=user_id)
        
            db.session.add(new_post)
            db.session.commit()

            flash('Post created', category='success')
            return redirect(url_for('views.home'))
        else:
            flash('Please Enter a Valid Image Type', category='error')
            

    return render_template("home.html", user=current_user, time_ago= time_ago,form=form, posts=all_posts, postable=True)



    


@views.route('/delete_post/<int:user_id>/<int:post_id>')
@login_required
def delete_post(user_id, post_id):
   #from the Item model, fetch the item with primary key item_id to be deleted
   
   if user_id == current_user.id:
        delete_post = Post.query.get(post_id)
        #using db.session delete the item
        db.session.delete(delete_post)
        #commit the deletion
        db.session.commit()
        return redirect(url_for('views.home'))
   return redirect(url_for('views.home'))

@views.route('/update_post/<int:user_id>/<int:post_id>', methods=["GET", "POST"])
@login_required
def update_post(user_id, post_id):
    form = PostForm()
    
    all_posts = Post.query.all()
    if user_id == current_user.id:
        post_to_update= Post.query.get(post_id)
        if request.method=="POST":
            post_to_update.title= form.title.data
            post_to_update.description = form.description.data
            try:
                db.session.commit()
                flash('Post Updated', category='success')
                return redirect(url_for('views.home'))
            except:
                flash('Post Could Not Be Updated', category='error')



    return render_template("home.html", user=current_user, time_ago=time_ago, form=form, posts=all_posts, post_update=post_to_update, postable=False)


        


@views.route('/comments/<int:postId>', methods=["GET", "POST"])
@login_required
def comments(postId):
    form = CommentForm()
    post = Post.query.get(postId)
    comments= Comments.query.filter_by(post_id = post.id).all()
    if request.method=="POST":
        comment = form.comment.data

        
        new_comment = Comments(comment=comment, post_id= postId, user_commenter_id = current_user.id )
        db.session.add(new_comment)
        db.session.commit()
        flash('Comment Posted', category='success')
        return redirect(url_for('views.comments', postId=postId))
    




    return render_template("view_comments.html", user=current_user, post=post, form=form,comments=comments)
