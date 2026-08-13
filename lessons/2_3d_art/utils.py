import math
from pyglm import glm
import pygame


def fov_to_focal_length(fov: float) -> float:
    """Converts a Field of View in degrees to focal length in world units."""
    return 1.0 / math.tan(math.radians(fov) * 0.5)

def project_3d_point_to_screen(point: glm.vec3, focal_length: float) -> glm.vec2:
    return glm.vec2(
        point.x * focal_length / point.z,
        point.y * focal_length / point.z,
    )

def normalized_coordinates_to_window_coordinates(point: glm.vec2, window_size: glm.vec2) -> pygame.math.Vector2:
    """Converts normalized coordinates to window coordinates.
    
    Normalized coordinates place the center of the window (0, 0), the left
    edge at -1, right at 1, bottom at -1, and top at 1.
    """

    ratio = window_size.y / window_size.x

    return pygame.math.Vector2(
        (point.x * ratio + 1.0) * window_size.x * 0.5,
        (-point.y + 1.0) * window_size.y * 0.5,
    )

