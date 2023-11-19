from ultrapoint import Ultrapoint
from vector4 import Vector4

cursor = Vector4(0, 0, 0, 1)
render_distance_ux = 4
render_distance_xyz = 5

ultrapoints = {}

current_material = 'brick'

def get_ultrapoint(ux):
    ultrapoint = ultrapoints.get(ux)
    if not ultrapoint:
        ultrapoints[ux] = ultrapoint = Ultrapoint([])
    return ultrapoint
