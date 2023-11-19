from cube import Cube
import pygame

class Ultrapoint:
    def __init__(self, cubes):
        self.cubes = cubes

    def remove_cube(self, cube_position):
        for existing_cube in self.cubes:
            if existing_cube.position.x == cube_position.x and existing_cube.position.y == cube_position.y and existing_cube.position.z == cube_position.z:
                self.cubes.remove(existing_cube)
                return True
        return False

    def insert_cube(self, cube):
        insert_index = 0
        for existing_cube in self.cubes:
            if (
                cube.position.x > existing_cube.position.x or
                (cube.position.x == existing_cube.position.x and cube.position.y > existing_cube.position.y) or
                (cube.position.x == existing_cube.position.x and cube.position.y == existing_cube.position.y and cube.position.z > existing_cube.position.z)
            ):
                insert_index += 1
            else:
                break
        self.cubes.insert(insert_index, cube)

    def sort_cubes(self):
        self.cubes.sort(key=lambda cube: (cube.position.x, cube.position.y, cube.position.z))

    def cubes_as_dict(self):
        return [
            {
                "x": cube.position.x,
                "y": cube.position.y,
                "z": cube.position.z,
                "material": cube.material
            } for cube in self.cubes
        ]

    @classmethod
    def from_dict(cls, ultrapoint_dict):
        cubes = [
            Cube(
                pygame.math.Vector3(cube_dict["x"], cube_dict["y"], cube_dict["z"]),
                cube_dict["material"]
            ) for cube_dict in ultrapoint_dict["cubes"]
        ]
        return cls(cubes)
