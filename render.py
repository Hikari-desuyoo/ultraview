import pygame
import environment as env
from get_asset import get_asset
from cube import Cube # remove after testing

black = (0, 0, 0)
ultrapoint_padding = 100

cube_size = get_asset('brick/+z.png').get_size()
ultrapoint_size = get_asset('ultrapoint_frame/back.png').get_size()

surface_cache = {
    'ultrapoint': {
        'used': 0,
        'existing' : [],
        'size': ultrapoint_size
    },
}

cursor_surface = get_asset('cursor.png')
cursor_fg_surface = get_asset('cursor_fg.png')

def reset_cache(surface_name):
    cache = surface_cache[surface_name]
    cache['existing'] = []

def pull_from_cache(surface_name):
    cache = surface_cache[surface_name]

    try:
        cached_surface = cache['existing'][cache['used']]
    except IndexError:
        cached_surface = pygame.Surface(cache['size'])
        cache['existing'].append(cached_surface)

    cache['used'] += 1
    cached_surface.fill((0,0,0,0))
    return cached_surface

def cube_coordinate(cube_position, xyz_cursor):
    render_distance = env.render_distance_xyz
    cube_w, cube_h = cube_size
    return (
        (cube_w / 2) * (render_distance - cube_position.x     + cube_position.z     - 1               + xyz_cursor.x     - xyz_cursor.z),
        (cube_h / 2) * (render_distance + cube_position.x / 2 + cube_position.z / 2 - cube_position.y - xyz_cursor.x / 2 - xyz_cursor.z / 2 + xyz_cursor.y)
    )

def render_ultrapoint_surface(ultrapoint, ux):
    xyz_cursor = env.cursor.xyz_vector3()
    render_distance = env.render_distance_xyz

    back_frame = get_asset('ultrapoint_frame/back.png')
    front_frame = get_asset('ultrapoint_frame/front.png')

    ultrapoint_surface = pull_from_cache('ultrapoint')
    ultrapoint_surface.blit(back_frame, (0, 0))

    cursor_need_draw = ux == env.cursor.ux

    cubes_surface = None
    if cursor_need_draw:
        cube_w, cube_h = cube_size
        cubes_surface = pygame.Surface((
            (cube_w * render_distance),
            (((cube_h) * render_distance) + cube_h),
        ), pygame.SRCALPHA)

    for cube in ultrapoint.cubes:
        if not (
            cube.position.x in range(int(xyz_cursor.x - render_distance / 2), int(xyz_cursor.x + render_distance / 2)) and
            cube.position.y in range(int(xyz_cursor.y - render_distance / 2), int(xyz_cursor.y + render_distance / 2)) and
            cube.position.z in range(int(xyz_cursor.z - render_distance / 2), int(xyz_cursor.z + render_distance / 2))):
            continue

        cube_image = get_asset(f"{cube.material}/+z.png")

        if not cubes_surface:
            cube_w, cube_h = cube_image.get_size()
            cubes_surface = pygame.Surface((
                (cube_w * render_distance),
                (((cube_h) * render_distance) + cube_h),
            ), pygame.SRCALPHA)

        if cursor_need_draw and (cube.position.z > xyz_cursor.z or cube.position.y > xyz_cursor.y or cube.position.x > xyz_cursor.x):
            cubes_surface.blit(cursor_surface, cube_coordinate(xyz_cursor, xyz_cursor))
            cursor_need_draw = False

        cubes_surface.blit(cube_image, cube_coordinate(cube.position, xyz_cursor))

        if cursor_need_draw and cube.position == xyz_cursor:
            cubes_surface.blit(cursor_surface, cube_coordinate(xyz_cursor, xyz_cursor))
            cursor_need_draw = False

    if cursor_need_draw:
        cubes_surface.blit(cursor_surface, cube_coordinate(xyz_cursor, xyz_cursor))
        cursor_need_draw = False

    if ux == env.cursor.ux:
        cubes_surface.blit(cursor_fg_surface, cube_coordinate(xyz_cursor, xyz_cursor))

    if cubes_surface:
        ultrapoint_rect = ultrapoint_surface.get_rect()
        cubes_rect = cubes_surface.get_rect()
        cubes_rect.w = ultrapoint_rect.w
        cubes_rect.h = int((cubes_rect.w / cubes_surface.get_width()) * cubes_rect.h)
        cubes_rect.center = ultrapoint_rect.center
        ultrapoint_surface.blit(pygame.transform.smoothscale(cubes_surface, cubes_rect.size), cubes_rect.topleft)

    ultrapoint_surface.blit(front_frame, (0, 0))

    return ultrapoint_surface

def render(screen):
    for cache in surface_cache.values():
        cache['used'] = 0

    screen.fill(black)

    distance = env.render_distance_ux

    ultrapoint_range_start = env.cursor.ux - distance // 2
    ultrapoint_range_end = ultrapoint_range_start + distance

    ultrapoints_surface = None

    for ux in range(ultrapoint_range_start, ultrapoint_range_end):
        ultrapoint_surface = render_ultrapoint_surface(env.get_ultrapoint(ux), ux)

        if not ultrapoints_surface:
            width = distance * (ultrapoint_surface.get_width() + ultrapoint_padding)
            height = ultrapoint_surface.get_height()
            ultrapoints_surface = pygame.Surface((width, height))

        position = ((ux - ultrapoint_range_start) * (ultrapoint_surface.get_width() + ultrapoint_padding), 0)
        ultrapoints_surface.blit(ultrapoint_surface, position)

    screen_rect = screen.get_rect()
    ultrapoints_rect = ultrapoints_surface.get_rect()
    ultrapoints_rect.w = screen_rect.w
    ultrapoints_rect.h = int((ultrapoints_rect.w / ultrapoints_surface.get_width()) * ultrapoints_rect.h)
    ultrapoints_rect.center = screen_rect.center

    screen.blit(pygame.transform.smoothscale(ultrapoints_surface, ultrapoints_rect.size), ultrapoints_rect.topleft)
