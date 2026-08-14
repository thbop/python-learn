from pyglm import glm

from dataclasses import dataclass


@dataclass(frozen=True)
class Mesh:
    vertices: list[glm.vec3]
    indices: list[tuple[int, int, int]]