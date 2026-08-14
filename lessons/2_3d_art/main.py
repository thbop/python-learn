import pygame
from pyglm import glm

from utils import *
from vertex import *

from cube_mesh import cube


FOV = 90
FOCAL_LENGTH = fov_to_focal_length(FOV)
WINDOW_SIZE = (1280, 720)
WINDOW_RATIO = WINDOW_SIZE[1] / WINDOW_SIZE[0]


# pygame setup
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
running = True

rot_x = 0
rot_y = 0

def process_vertex(data: VertexIn) -> VertexOut:
    point_4d = glm.vec4(data.position, 1.0)
    point_4d = glm.rotate(rot_x, glm.vec3(1, 0, 0)) * glm.rotate(rot_y, glm.vec3(0, 1, 0)) * point_4d
    point_4d = 0.4 * point_4d
    point_4d += glm.vec4(0, 0, 2, 0)

    point_2d = normalized_coordinates_to_window_coordinates(
        project_3d_point_to_screen(
            point_4d,
            FOCAL_LENGTH
        ),
        glm.vec2(WINDOW_SIZE)
    )

    return VertexOut(
        position=point_2d,
        color=data.color
    )


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    screen.fill((0, 0, 0))
    rot_x += 0.01
    rot_y += 0.02

    for triangle in cube.indices:
        vertex_outs = [
            process_vertex(VertexIn(position=cube.vertices[i]))
            for i in triangle
        ]

        should_cull = (
            (vertex_outs[1].position.x - vertex_outs[0].position.x) *
            (vertex_outs[2].position.y - vertex_outs[0].position.y) - 
            (vertex_outs[2].position.x - vertex_outs[0].position.x) *
            (vertex_outs[1].position.y - vertex_outs[0].position.y)
        ) < 0

        if not should_cull:
            pygame.draw.aalines(
                surface=screen,
                color="white",
                closed=True,
                points=[vertex_out.position for vertex_out in vertex_outs]
            )
        # pygame.draw.polygon(
        #     surface=screen,
        #     color="white",
        #     points=[project(vertices[i]) for i in quad]
        # )


    pygame.display.flip()

    clock.tick(60)

pygame.quit()