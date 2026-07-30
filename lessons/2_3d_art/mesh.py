from __future__ import annotations
from typing import Self

import glm

from vertex import Vertex

class Mesh:
    def __init__(self, vertices: list[Vertex], indices: list[int]):
        self._position = glm.vec3()
        self._rotation = glm.vec2()
        self._scale = 1.0

        self._transform = glm.mat4([
            [  1.0,  0.0,  0.0,  0.0, ],
            [  0.0,  1.0,  0.0,  0.0, ],
            [  0.0,  0.0,  1.0,  0.0, ],
            [  0.0,  0.0,  0.0,  1.0, ],
        ])

        self._vertices: list[Vertex] = vertices
        self._indices: list[int] = indices

    @property
    def transform(self) -> glm.mat4:
        return self._transform

    @property
    def vertices(self) -> list[Vertex]:
        return self._vertices

    @property
    def indices(self) -> list[int]:
        return self._indices

                