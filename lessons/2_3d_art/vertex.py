from __future__ import annotations


from dataclasses import dataclass, field

import glm
from pygame import Color

@dataclass(frozen=True)
class Vertex:
    position: glm.vec4 = glm.vec4()
    color: Color = field(default_factory=lambda: Color("white"))

    def transformed(self, transform: glm.mat4) -> Vertex:
        return Vertex(
            position = transform * self.position,
            color = self.color
        )