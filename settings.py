import math


# game settings
width = 1200
height = 800
half_width = width // 2
half_height = height // 2
FPS = 60
tile = 100

# ray casting settings
fov = math.pi / 3
half_fov = fov / 2
num_rays = 100
max_depth = 800
delta_angle = fov / num_rays


# player settings
player_pos = (half_width, half_height)
player_angle = 0
player_speed = 2


# colors
black = (0, 0, 0)
green = (0, 255, 0)