import pygame
from pyglm import glm

from utils import *


FOV = 90
FOCAL_LENGTH = fov_to_focal_length(FOV)
WINDOW_SIZE = (1280, 720)
WINDOW_RATIO = WINDOW_SIZE[1] / WINDOW_SIZE[0]

window_size = glm.vec2(WINDOW_SIZE)


# 8 Vertices of a cube centered at (0, 0, 0)
vertices = [
    glm.vec3( 1.0,  1.0,  1.0),  # 0: Right,  Top,    Front
    glm.vec3(-1.0,  1.0,  1.0),  # 1: Left,   Top,    Front
    glm.vec3(-1.0, -1.0,  1.0),  # 2: Left,   Bottom, Front
    glm.vec3( 1.0, -1.0,  1.0),  # 3: Right,  Bottom, Front
    glm.vec3( 1.0,  1.0, -1.0),  # 4: Right,  Top,    Back
    glm.vec3(-1.0,  1.0, -1.0),  # 5: Left,   Top,    Back
    glm.vec3(-1.0, -1.0, -1.0),  # 6: Left,   Bottom, Back
    glm.vec3( 1.0, -1.0, -1.0),  # 7: Right,  Bottom, Back
]

# 6 Faces defined as 4-index tuples (Quads) in Counter-Clockwise (CCW) order
indices = [
    (0, 1, 2, 3),  # Front  (+Z)
    (5, 4, 7, 6),  # Back   (-Z)
    (4, 0, 3, 7),  # Right  (+X)
    (1, 5, 6, 2),  # Left   (-X)
    (4, 5, 1, 0),  # Top    (+Y)
    (3, 2, 6, 7),  # Bottom (-Y)
]



# pygame setup
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
running = True

rot_x = 0
rot_y = 0

def transform(point: glm.vec3) -> glm.vec3:
    point_4d = glm.vec4(point, 1.0)
    point_4d = glm.rotate(rot_x, glm.vec3(1, 0, 0)) * glm.rotate(rot_y, glm.vec3(0, 1, 0)) * point_4d
    point_4d = 0.4 * point_4d
    point_4d += glm.vec4(0, 0, 2, 0)

    return point_4d.xyz

def project(point: glm.vec3) -> pygame.math.Vector2:
    return normalized_coordinates_to_window_coordinates(
        project_3d_point_to_screen(
            point,
            FOCAL_LENGTH
        ),
        glm.vec2(WINDOW_SIZE)
    )

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    screen.fill((0, 0, 0))
    rot_x += 0.01
    rot_y += 0.02

    for quad in indices:
        pygame.draw.aalines(
            surface=screen,
            color="white",
            closed=True,
            points=[project(transform(vertices[i])) for i in quad]
        )
        # pygame.draw.polygon(
        #     surface=screen,
        #     color="white",
        #     points=[project(vertices[i]) for i in quad]
        # )


    pygame.display.flip()

    clock.tick(60)

pygame.quit()