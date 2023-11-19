class Cube:
    def __init__(self, position, material):
        """
        Initializes a Cube object.

        Parameters:
        - position (pygame.math.Vector3): The position of the cube in 3D space.
        - material (str): The material of the cube.
        """
        self.position = position
        self.material = material
