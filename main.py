import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cube Runner")

# Define some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initial position of the rectangle
x, y = 100, 100
speed = 5  # Speed at which the rectangle moves
rect_width, rect_height = 50, 50  # Dimensions of the rectangle

# Initialize Joystick
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

# Make sure a joystick is connected
if joystick_count == 0:
    print("No joystick connected!")
    sys.exit()

# Use the first joystick connected
joystick = pygame.joystick.Joystick(0)
joystick.init()

def quit_game():
    pygame.quit()
    sys.exit()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the state of the keys
    keys = pygame.key.get_pressed()

    # Get joystick axis inputs
    joystick_x = joystick.get_axis(0)  # Left analog stick X axis
    joystick_y = joystick.get_axis(1)  # Left analog stick Y axis

    if joystick.get_button(11):
        quit_game()


    # Move the rectangle based on joystick input
    # Dead zone to prevent drifting when the joystick is centered
    dead_zone = 0.2

    if joystick_x < -dead_zone:
        x -= speed
    if joystick_x > dead_zone:
        x += speed
    if joystick_y < -dead_zone:
        y -= speed
    if joystick_y > dead_zone:
        y += speed

    # Prevent the rectangle from going off the screen
    if x < 0:
        x = 0
    if x + rect_width > 800:
        x = 800 - rect_width
    if y < 0:
        y = 0
    if y + rect_height > 600:
        y = 600 - rect_height

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, RED, (x, y, rect_width, rect_height))

    # Update the display
    pygame.display.update()

    # Control the frame rate
    pygame.time.Clock().tick(120)
