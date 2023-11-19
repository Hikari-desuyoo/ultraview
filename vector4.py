import pygame

class Vector4:
    def __init__(self, x, y, z, ux):
        self.x = x
        self.y = y
        self.z = z
        self.ux = ux

    def xyz_vector3(self):
        return pygame.math.Vector3(self.x, self.y, self.z)
