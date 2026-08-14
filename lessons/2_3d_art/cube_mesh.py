from pyglm import glm

from mesh import Mesh


cube = Mesh(
    # 8 Vertices of a cube centered at (0, 0, 0)
    vertices=[
        glm.vec3( 1.0,  1.0,  1.0),  # 0: Right,  Top,    Front
        glm.vec3(-1.0,  1.0,  1.0),  # 1: Left,   Top,    Front
        glm.vec3(-1.0, -1.0,  1.0),  # 2: Left,   Bottom, Front
        glm.vec3( 1.0, -1.0,  1.0),  # 3: Right,  Bottom, Front
        glm.vec3( 1.0,  1.0, -1.0),  # 4: Right,  Top,    Back
        glm.vec3(-1.0,  1.0, -1.0),  # 5: Left,   Top,    Back
        glm.vec3(-1.0, -1.0, -1.0),  # 6: Left,   Bottom, Back
        glm.vec3( 1.0, -1.0, -1.0),  # 7: Right,  Bottom, Back
    ],
    # 12 Triangles defined as 3-index tuples in Counter-Clockwise (CCW) order
    indices=[
        # Front (+Z)
        (0, 1, 2),
        (0, 2, 3),

        # Back (-Z)
        (5, 4, 7),
        (5, 7, 6),

        # Right (+X)
        (4, 0, 3),
        (4, 3, 7),

        # Left (-X)
        (1, 5, 6),
        (1, 6, 2),

        # Top (+Y)
        (4, 5, 1),
        (4, 1, 0),

        # Bottom (-Y)
        (3, 2, 6),
        (3, 6, 7),
    ]
)