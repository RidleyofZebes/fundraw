"""------------------------------------------------------------------------------------------#
# "FunDraw" v1.0.0 - A simple shape painting toy written in Python with PyGame               #
# By Douglas J. Honeycutt                                                                    #
# https://withacact.us/ | https://github.com/RidleyofZebes/ | https://twitter.com/RidleyZahn #
#------------------------------------------------------------------------------------------"""

import pygame

pygame.init()

window_resolution = (1280, 720)
FPS = 60

window = pygame.display.set_mode(window_resolution)
pygame.display.set_caption("FunDraw")
clock = pygame.time.Clock()


colors = [(0, 0, 0),
          (128, 128, 128),
          (192, 192, 192),
          (255, 255, 255),
          (128, 0, 0),
          (255, 0, 0),
          (128, 128, 0),
          (255, 255, 0),
          (0, 128, 0),
          (0, 255, 0),
          (0, 128, 128),
          (0, 255, 255),
          (0, 0, 128),
          (0, 0, 255),
          (128, 0, 128),
          (255, 0, 255)]


def main():
    running = True
    polygons = []
    polygon_points = []
    color_index = 3
    window.fill((0, 0, 0))
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            mouse_position = pygame.mouse.get_pos()

            window.fill((0, 0, 0))
            for polygon in polygons[::1]:
                pygame.draw.polygon(window, colors[polygon[0]], polygon[1])

            if len(polygon_points) == 1:
                pygame.draw.line(window, colors[color_index], polygon_points[0], mouse_position)
            if len(polygon_points) >= 2:
                pygame.draw.polygon(window, colors[color_index], polygon_points + [mouse_position])

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                polygon_points.append(mouse_position)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                polygons.append([color_index, polygon_points])
                polygon_points = []

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                if color_index + 1 >= len(colors):
                    color_index = 0
                else:
                    color_index = color_index + 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                if color_index - 1 < 0:
                    color_index = len(colors) - 1
                else:
                    color_index = color_index - 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                    filename = "./pictures/" + input("Choose file name: ") + ".png"
                    pygame.image.save(window, filename)
                    print("Saved image as '%s'" % filename)

        clock.tick(FPS)
        pygame.display.update()


if __name__ == '__main__':
    main()
