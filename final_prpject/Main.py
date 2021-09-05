import pygame
import Objects
import ScreenEngine
import Logic
import Service
from Constants import *


class MyHeroFactory(Objects.AbstractHeroFactory):
    # Абстрактна фабрика, що створює героїв
    def create(self):
        sprite = Service.ObjectsLib.textures["hero"]["sprite"]
        return Objects.Hero(BASE_STATS, sprite)


def repaint(game_display, pygame_obj, drawer_obj):
    game_display.blit(drawer_obj, (0, 0))
    drawer_obj.draw(gameDisplay)
    pygame_obj.display.update()


def quit_game(pygame_obj):
    pygame_obj.display.quit()
    pygame_obj.quit()
    exit(0)


def create_game(sprite_size, pygame_obj):
    dict_dirs = {"objects": OBJECT_TEXTURE, "ally": ALLY_TEXTURE,
                 "enemies": ENEMY_TEXTURE, "textures": OTHER_TEXTURE}

    Service.ObjectsLib.set_generators(Service.GraphicalLib(pygame_obj, sprite_size, dict_dirs),
                                      Service.ActionLib())
    Service.ObjectsLib.load(MAP_TEXTURES)
    with open("objects.yml", "r") as file:
        Service.ObjectsLib.append(file.read())

    Service.LevelGenerator.set_libs(Service.ObjectsLib)
    Service.LevelGenerator.load("levels.yml")
    Service.LevelGenerator.levels.append({'map': Service.EndMapSurface("EndMap"),
                                          'obj': Service.EmptyMapSpawn("EndMap")})

    engine_obj = Logic.GameEngine()
    engine_obj.sprite_size = sprite_size

    # Генератор героя
    engine_obj.hero_generator = MyHeroFactory()
    # Генератор рівнів
    engine_obj.level_generator = Service.LevelGenerator
    # Підписка на події
    engine_obj.subscribe(Service.ObjectsLib)
    # Загрузка початкового рівня
    engine_obj.start()

    return engine_obj


if not KEYBOARD_CONTROL:
    print("Only keyboard control")
    exit(0)

pygame.init()
gameDisplay = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption("MyRPG")
pygame.key.set_repeat(15, 200)

engine = create_game(BASE_SPRITE_SIZE, pygame)

drawer = ScreenEngine.Screen_Handle((0, 0))
drawer = ScreenEngine.HelpWindow((700, 500), pygame.SRCALPHA, (0, 0), drawer)
drawer = ScreenEngine.MiniMap((164, 164), pygame.SRCALPHA, (50, 50), drawer)
drawer = ScreenEngine.InfoWindow((160, 600), (490, 14), drawer)
drawer = ScreenEngine.ProgressBar((640, 120), (640, 0), drawer)
drawer = ScreenEngine.GameSurface((640, 480), pygame.SRCALPHA, (0, 480), drawer)

drawer.connect_engine(engine)

while engine.working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            engine.working = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                # Допоміжне вікно
                engine.show_help = not engine.show_help
                repaint(gameDisplay, pygame, drawer)
                break
            if event.key == pygame.K_m:
                # Мінікарта
                engine.show_minimap = not engine.show_minimap
                repaint(gameDisplay, pygame, drawer)
                break
            if event.key == pygame.K_F12:
                engine.level_next()
            if event.key == pygame.K_r:
                # Перезапуск гри
                engine.sprite_size = BASE_SPRITE_SIZE
                engine.start()
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                engine.level_reset()
            if event.key == pygame.K_ESCAPE:
                engine.working = False
            if engine.game_process:
                if event.key == pygame.K_UP:
                    engine.move_up()
                elif event.key == pygame.K_DOWN:
                    engine.move_down()
                elif event.key == pygame.K_LEFT:
                    engine.move_left()
                elif event.key == pygame.K_RIGHT:
                    engine.move_right()

        repaint(gameDisplay, pygame, drawer)

quit_game(pygame)
