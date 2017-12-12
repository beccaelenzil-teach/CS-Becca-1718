"""
Sprite Collect fishs

Simple program to show basic sprite usage.

Artwork from http://kenney.nl
"""

import random
import arcade

# --- Constants ---
SPRITE_SCALING = 0.2
SPRITE_SCALING_FISH = 0.02
SPRITE_SCALING_SHARK = 0.1
FISH_COUNT = 50
SHARK_COUNT = 5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5



class Fish(arcade.Sprite):
    """
    This class represents the fishs on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the fish to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the fish
        self.center_x -= 1

        # See if the fish has fallen off the bottom of the screen.
        # If so, reset it.
        if self.left < 0:
            self.reset_pos()

class Shark(arcade.Sprite):
    """
    This class represents the fishs on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the fish to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the fish
        self.center_x += 1

        # See if the fish has fallen off the bottom of the screen.
        # If so, reset it.
        if self.right > SCREEN_WIDTH:
            self.reset_pos()

class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyWindow(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.all_sprites_list = None
        self.fish_list = None
        self.shark_list = None

        # Set up the player info
        self.player_sprite = None
        self.floor = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.fish_list = arcade.SpriteList()
        self.shark_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = Player("orca.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)

        #set up a rectangular barrier
        self.floor = arcade.Sprite(None,1,0,0,10,10,SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.all_sprites_list.append(self.floor)

        # Create the fishs
        for i in range(FISH_COUNT):

            # Create the fish instance
            # fish image from kenney.nl
            fish = Fish("fish.png", SPRITE_SCALING_FISH)

            # Position the fish
            fish.center_x = random.randrange(SCREEN_WIDTH)
            fish.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the fish to the lists
            self.all_sprites_list.append(fish)
            self.fish_list.append(fish)

        for i in range(SHARK_COUNT):

            # Create the fish instance
            # fish image from kenney.nl
            shark = Shark("fish2.png", SPRITE_SCALING_SHARK)

            # Position the fish
            shark.center_x = random.randrange(SCREEN_WIDTH)
            shark.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the fish to the lists
            self.all_sprites_list.append(shark)
            self.shark_list.append(shark)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()

        # draw the floor
        arcade.draw_rectangle_filled(SCREEN_WIDTH/2,SCREEN_HEIGHT/10,SCREEN_WIDTH,SCREEN_HEIGHT/10, arcade.color.WHITE)

        self.all_sprites_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.all_sprites_list.update()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.fish_list)

        shark_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.shark_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for fish in hit_list:
            fish.kill()
            self.score += 1

        for shark in shark_hit_list:
            shark.kill()
            self.score -= 5



def main():
    window = MyWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
