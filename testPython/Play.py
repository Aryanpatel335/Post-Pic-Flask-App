# Importing necessary libraries
import time
import sys

# Define the Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def has_item(self, item):
        return item in self.inventory

# Define the Scene base class
class Scene:
    def enter(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def exit_scene(self):
        print("Exiting the scene...")
        time.sleep(2)

# Define specific scenes
class StartScene(Scene):
    def enter(self):
        print("Welcome to the adventure game!")
        player_name = input("Enter your name: ")
        player = Player(player_name)
        print(f"Hello, {player.name}! Your adventure begins now...")
        time.sleep(2)
        return 'forest'

class ForestScene(Scene):
    def enter(self, player):
        print("You are in a dark, eerie forest.")
        action = input("Do you go left or right? (left/right): ")
        if action == 'left':
            return 'lake'
        elif action == 'right':
            return 'mountain'
        else:
            print("Invalid action.")
            return 'forest'

class LakeScene(Scene):
    def enter(self, player):
        print("\nYou arrive at a serene lake. The water is crystal clear.")
        print("A mysterious figure appears and offers you a choice.")
        action = input("Do you accept the gift from the figure? (yes/no): ")

        if action.lower() == 'yes':
            print("You accept the gift and feel a surge of strength.")
            player.add_item('Mystic Amulet')
            print("Mystic Amulet added to your inventory.")
            return 'forest'
        elif action.lower() == 'no':
            print("You refuse the gift and the figure vanishes.")
            return 'forest'
        else:
            print("Confused, you stand still. The figure waits.")
            return 'lake'


class MountainScene(Scene):
    def enter(self, player):
        print("\nYou approach a towering mountain with a treacherous path.")
        if player.has_item('Mystic Amulet'):
            print("Your Mystic Amulet glows, making the climb easier.")
            print("You reach the summit and find a treasure chest.")
            player.add_item('Mountain Treasure')
            print("Mountain Treasure added to your inventory.")
            return 'forest'
        else:
            print("The climb is difficult. Do you wish to continue? (yes/no): ")
            action = input()

            if action.lower() == 'yes':
                print("You struggle but eventually reach the summit.")
                print("However, you are too exhausted to search for any treasure.")
                return 'forest'
            else:
                print("You decide not to risk the climb and head back.")
                return 'forest'

# More scenes can be added here

# Define the Map class
class Map:
    scenes = {
        'start': StartScene(),
        'forest': ForestScene(),
        'lake': LakeScene(),
        'mountain': MountainScene()
        # More scenes can be added to the map
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

# Define the Engine class
class Engine:
    def __init__(self, game_map):
        self.game_map = game_map

    def play(self):
        current_scene = self.game_map.next_scene(self.game_map.start_scene)
        last_scene = self.game_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.game_map.next_scene(next_scene_name)

        # Enter the last scene
        current_scene.enter()

# Main function to start the game
def main():
    game_map = Map('start')
    game_engine = Engine(game_map)
    game_engine.play()

if __name__ == "__main__":
    main()
