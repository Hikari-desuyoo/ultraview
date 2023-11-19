import sys
import pygame
import environment as env
from cube import Cube
from render import render

def get_screen_size(scale):
    return scale * 3, scale

screen_scale = 600
width, height = screen_size = get_screen_size(screen_scale)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Ultraview')

whole = pygame.Surface(get_screen_size(2000))

clock = pygame.time.Clock()

running = True
player_speed = 1

while running:
    keys = pygame.key.get_pressed()
    ctrl = keys[pygame.K_LCTRL]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                env.get_ultrapoint(env.cursor.ux).insert_cube(Cube(env.cursor.xyz_vector3(), env.current_material))
                env.get_ultrapoint(env.cursor.ux).sort_cubes()
            elif event.button == 3:
                env.get_ultrapoint(env.cursor.ux).remove_cube(env.cursor.xyz_vector3())
            elif event.button == 4:
                if ctrl and env.render_distance_ux > 1:
                    env.render_distance_ux -= 1
                elif env.render_distance_xyz > 1:
                    env.render_distance_xyz -= 1
            elif event.button == 5:
                if ctrl:
                    env.render_distance_ux += 1
                else:
                    env.render_distance_xyz += 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                env.cursor.z -= player_speed
            elif event.key == pygame.K_s:
                env.cursor.z += player_speed
            elif event.key == pygame.K_a:
                env.cursor.x += player_speed
            elif event.key == pygame.K_d:
                env.cursor.x -= player_speed
            elif event.key == pygame.K_e:
                env.cursor.ux += player_speed
            elif event.key == pygame.K_q:
                env.cursor.ux -= player_speed
            elif event.key == pygame.K_SPACE:
                env.cursor.y += player_speed
            elif event.key == pygame.K_LSHIFT:
                env.cursor.y -= player_speed
            elif event.key == pygame.K_1:
                env.current_material = "brick"
            elif event.key == pygame.K_2:
                env.current_material = "grass"
            elif event.key == pygame.K_3:
                env.current_material = "glass"

    render(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
