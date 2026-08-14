from __future__ import annotations
from dataclasses import dataclass
import math
from pyglm import glm

def fov_to_focal_length(fov: float) -> float:
    """Converts a Field of View in degrees to focal length in world units."""
    return 1.0 / math.tan(math.radians(fov) * 0.5)

def project_3d_point_to_screen(point: glm.vec3, focal_length: float) -> glm.vec2:
    return glm.vec2(
        point.x * focal_length / point.z,
        point.y * focal_length / point.z,
    )

def normalized_coordinates_to_window_coordinates(point: glm.vec2, window_size: glm.vec2) -> glm.vec2:
    """Converts normalized coordinates to window coordinates.
    
    Normalized coordinates place the center of the window (0, 0), the left
    edge at -1, right at 1, bottom at -1, and top at 1.
    """

    ratio = window_size.y / window_size.x

    return glm.vec2(
        (point.x * ratio + 1.0) * window_size.x * 0.5,
        (-point.y + 1.0) * window_size.y * 0.5,
    )

def rotate_left_90deg(direction: glm.vec2) -> glm.vec2:
    return glm.vec2(-direction.y, direction.x)

@dataclass(frozen=True)
class AABB2d:
    top_left: glm.vec2
    bottom_right: glm.vec2

    @staticmethod
    def from_polygon(polygon: list[glm.vec2]) -> AABB2d:
        min_x = min([point.x for point in polygon])
        max_x = max([point.x for point in polygon])
        min_y = min([point.y for point in polygon])
        max_y = max([point.y for point in polygon])

        return AABB2d(
            top_left=glm.vec2(min_x, min_y),
            bottom_right=glm.vec2(max_x, max_y)
        )


    def is_inside(self, point: glm.vec2) -> bool:
        """Defaults to pygame coordinates where when y decreases we're going up."""
        if self.top_left.x > point.x or point.x > self.bottom_right.x:
            return False
        if self.top_left.y > point.y or point.y > self.bottom_right.y:
            return False

        return True

def is_in_triangle(point: glm.vec2, triangle: list[glm.vec2]) -> bool:
    """Is point inside a CCW triangle."""

    # This could be optimized given its usage
    if not AABB2d.from_polygon(triangle).is_inside(point):
        return False

    return min([
        glm.dot(
            (point - triangle[i]),
            rotate_left_90deg(triangle[((i + 1) % 3)] - triangle[i])
        )
        for i in range(3)
    ]) > 0
