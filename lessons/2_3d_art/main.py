import pygame
import glm

from mesh import Mesh
from utils import (
    fov_to_focal_length,
    project_3d_point_to_screen,
    normalized_coordinates_to_window_coordinates,
)
from vertex import Vertex

FOV = 120
FOCAL_LENGTH = fov_to_focal_length(FOV)
WINDOW_SIZE = (1280, 720)

# pygame setup
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
running = True


cube_vertices = [
    Vertex(position=glm.vec4(-1.0, -1.0, -1.0,  1.0)), # Bottom-Left-Ba
    Vertex(position=glm.vec4( 1.0, -1.0, -1.0,  1.0)), # Bottom-Right-B
    Vertex(position=glm.vec4( 1.0,  1.0, -1.0,  1.0)), # Top-Right-Back
    Vertex(position=glm.vec4(-1.0,  1.0, -1.0,  1.0)), # Top-Left-Back
    Vertex(position=glm.vec4(-1.0, -1.0,  1.0,  1.0)), # Bottom-Left-Fr
    Vertex(position=glm.vec4( 1.0, -1.0,  1.0,  1.0)), # Bottom-Right-F
    Vertex(position=glm.vec4( 1.0,  1.0,  1.0,  1.0)), # Top-Right-Fron
    Vertex(position=glm.vec4(-1.0,  1.0,  1.0,  1.0)), # Top-Left-Front
]

cube_indices = [
  0, 2, 1,   0, 3, 2, # Back Face (-Z)
  4, 5, 6,   4, 6, 7, # Front Face (+Z)
  0, 4, 7,   0, 7, 3, # Left Face (-X)
  1, 6, 5,   1, 2, 6, # Right Face (+X)
  0, 1, 5,   0, 5, 4, # Bottom Face (-Y)
  3, 7, 6,   3, 6, 2, # Top Face (+Y)
]

cube = Mesh(cube_vertices, cube_indices)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for triangle_index in range(len(cube.indices) // 3):
        positions: list[pygame.math.Vector2] = [
            normalized_coordinates_to_window_coordinates(
                point=project_3d_point_to_screen(
                    cube.vertices[
                        cube.indices[triangle_index * 3 + i]
                    ].transformed(cube.transform).position,
                    FOCAL_LENGTH
                ),
                window_size=glm.vec2(WINDOW_SIZE)
            )
            for i in range(3)
        ]
        colors: list[pygame.Color] = [
            cube.vertices[cube.indices[triangle_index * 3 + i]].color
            for i in range(3)
        ]

        pygame.draw.line(screen, colors[0], positions[0], positions[1])
        pygame.draw.line(screen, colors[1], positions[1], positions[2])
        pygame.draw.line(screen, colors[2], positions[2], positions[0])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()