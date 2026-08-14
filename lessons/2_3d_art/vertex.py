from abc import abstractmethod

from pyglm import glm

from dataclasses import dataclass


@dataclass(frozen=True)
class VertexIn:
    position: glm.vec3
    color: glm.vec3 = glm.vec3(1)

@dataclass(frozen=True)
class VertexOut:
    position: glm.vec2
    color: glm.vec3 = glm.vec3(1)

