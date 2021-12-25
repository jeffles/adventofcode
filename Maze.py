from collections.abc import Hashable
from pygame.locals import *
import pygame
import math

ROOM = 0
WALL = 1
DOOR = 2
START = 3
VISITED = 4 # Or more



class memoized(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, Hashable):
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        return self.func.__doc__

    def __get__(self, obj, objtype):
        return function.partial(self.__call__, obj)

@memoized
def get_groups(queue):
    # print(len(queue), queue)
    groups = []
    open_p = 1
    group = ''

    while open_p >= 1:
        next_command = queue[0]
        queue = queue[1:]
        if next_command == '(':
            open_p += 1
        elif next_command == ')':
            open_p -= 1

        if open_p > 1:
            group += next_command
        elif next_command == '|':
            groups.append(group)
            group = ''
        else:
            group += next_command
    groups.append(group[:-1])
    # for i in range(len(groups)):
    #     groups[i] += queue
    groups[0]+= queue
    # print('Found', groups)
    return groups


class Player:
    x = 44
    y = 44
    speed = 1

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed

    def setXY(self, x, y):
        self.x = x
        self.y = y



class Maze:
    def __init__(self):
        self.x = 0
        self.y = 0
        data = open('input').read().split('\n')
        self.queue = [{'c': data[0][1:-1], 'x': 0, 'y': 0}]
        self.maze = maze = [[3]]
        self.padded = False
        self.solve_x = -1
        self.solve_y = -1
        self.solved = False
        self.solve_queue = False
        self.num_1000 = 0

    def draw(self, display_surf, image_surf):
        for y in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                if self.maze[y][x] == 1:
                    display_surf.blit(image_surf, (x * 6, y * 6))
                elif self.maze[y][x] >= 3:
                    heat_diffa = (self.maze[y][x] % 255)
                    heat_diffb = (self.maze[y][x] % 155) + 100
                    heat_diffc = (self.maze[y][x] % 105) + 150
                    display_surf.fill((255-heat_diffa, 255-heat_diffb, 255-heat_diffc), (x*6, y*6, 6, 6))

        myfont = pygame.font.SysFont("VeraMono.ttf", 16)
        textsurface = myfont.render('Some Text', False, (255, 255, 255))
        display_surf.blit(textsurface, (1350, 0))
        textsurface = myfont.render('Some Text 2', False, (0, 100, 100))
        display_surf.blit(textsurface, (1350, 50))
        textsurface = myfont.render('Some Text 3', False, (0, 100, 100))
        display_surf.blit(textsurface, (1350, 100))
        # print(pygame.font.get_fonts())

    def pad_maze(self):
        if self.padded:
            return
        for row in self.maze:
            row.insert(0, WALL)
            row.append(WALL)
        self.maze.insert(0, [WALL] * len(self.maze[0]))
        self.maze.append([WALL] * len(self.maze[0]))
        self.padded = True

    def make_maze(self):
        # num_steps = 0
        # max_steps = 2000
        if not self.queue:
            self.pad_maze()
            return 0, 0
        command = self.queue.pop()
        order = command['c']
        x = command['x']
        y = command['y']
        # print(f'Make maze x:{x} y:{y} o:{order}')
        while order:
            next_command = order[0].upper()
            # print(next_command, order)
            order = order[1:]
            # num_steps += 1

            if next_command == 'W':
                if x == 0:
                    (x, y) = self.grow_maze('W', x, y)
                    for i in range(len(self.queue)):
                        self.queue[i]['x'] += 2
                x -= 1
                self.maze[y][x] = DOOR
                x -= 1
            elif next_command == 'N':
                if y == 0:
                    (x, y) = self.grow_maze('N', x, y)
                    for i in range(len(self.queue)):
                        self.queue[i]['y'] += 2
                y -= 1
                self.maze[y][x] = DOOR
                y -= 1
            elif next_command == 'E':
                if x == len(self.maze[0])-1:
                    (x, y) = self.grow_maze('E', x, y)
                x += 1
                self.maze[y][x] = DOOR
                x += 1
            elif next_command == 'S':
                if y == len(self.maze)-1:
                    (x, y) = self.grow_maze('S', x, y)
                y += 1
                self.maze[y][x] = DOOR
                y += 1
            elif next_command == '(':
                groups = get_groups(order)
                for group in groups:
                    if len(group) >= len(order):
                        print('WHAT?')
                        exit()
                    # print('->', len(group))
                    command = {'c': group, 'x': x, 'y': y}
                    self.queue.append(command)
                    # print(len(queue))
                order = ''
            else:
                print('FAIL', next_command)
                return x, y

            # if s == max_steps:
            #     self.queue.append({'c':order, 'x':x, 'y':y})
            #     return x, y
                # exit()
        return x, y

    def grow_maze(self, direction, x, y):
        if direction == 'W':
            for row in self.maze:
                if row[0] == ROOM or row[0] == START:
                    row.insert(0, WALL)
                    row.insert(0, ROOM)
                else:
                    row.insert(0, WALL)
                    row.insert(0, WALL)
            x += 2
        if direction == 'N':
            self.maze.insert(0, [WALL] * len(self.maze[0]))
            new_wall = [ROOM]
            while len(new_wall) < len(self.maze[0]):
                new_wall += [WALL, ROOM]
            self.maze.insert(0, new_wall)
            y += 2
        if direction == 'E':
            for row in self.maze:
                if row[-1] == ROOM or row[-1] == START:
                    row.append(WALL)
                    row.append(ROOM)
                else:
                    row.append(WALL)
                    row.append(WALL)
        if direction == 'S':
            self.maze.insert(len(self.maze), [WALL] * len(self.maze[0]))
            new_wall = [ROOM]
            while len(new_wall) < len(self.maze[0]):
                new_wall += [WALL, ROOM]
            self.maze.insert(len(self.maze), new_wall)

        return x, y

    def get_start(self):
        if self.solve_x >=0:
            return self.solve_x, self.solve_y
        for y in range(len(self.maze)):
            for x in range(len(self.maze)):
                if self.maze[y][x] == 3:
                    self.solve_x = x
                    self.solve_y = y
                    return x, y


    def maze_explore(self):
        if len(self.solve_queue) == 0:
            self.solved = True
            print('END')
            print(self.num_1000)
            return 0,0
        node = self.solve_queue.pop(0)
        x = node['x']
        y = node['y']
        steps = node['depth']

        # print(x, y, steps)
        if self.maze[y][x] < 4 + steps and self.maze[y][x] != 0:
            return x, y
        print(steps)
        if steps >= 1000:
            self.num_1000 += 1
        self.maze[y][x] = 4 + steps

        if self.maze[y - 1][x] == DOOR:
            self.maze[y-1][x] = 4 + steps
            self.solve_queue.append({'x': x, 'y': y - 2, 'depth': steps+1})
        if self.maze[y][x - 1] == DOOR:
            self.maze[y][x-1] = 4 + steps
            # self.maze_explore(x - 2, y, steps + 1)
            self.solve_queue.append({'x': x - 2, 'y': y, 'depth': steps + 1})
        if self.maze[y][x + 1] == DOOR:
            self.maze[y][x+1] = 4 + steps
            self.solve_queue.append({'x': x + 2, 'y': y, 'depth': steps + 1})
        if self.maze[y + 1][x] == DOOR:
            self.maze[y + 1][x] = 4 + steps
            self.solve_queue.append({'x': x, 'y': y + 2, 'depth': steps + 1})
        return x, y

    def solve_maze(self):
        x, y = self.get_start()
        self.maze[y][x] = 4
        if self.solved:
            return
        if not self.solve_queue:
            self.solve_queue = [{'x': x, 'y': y, 'depth': 0}]
        for _ in range(15):
            x, y = self.maze_explore()
        # max_size = 0
        # for i in range(len(self.maze)):
        #     for j in range(len(self.maze[0])):
        #         if self.maze[j][i] > max_size:
        #             max_size = self.maze[j][i]
        # print('max', max_size - 4)
        return x, y


class App:
    windowWidth = 2400
    windowHeight = 1300
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.player = Player()
        self.maze = Maze()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE )

        pygame.display.set_caption('Advent of code 2018 Day 20')
        self._running = True
        self._block_surf = pygame.image.load("sm_brick.png").convert()
        self._image_surf = pygame.image.load("player.png").convert()


    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(self._image_surf, (self.player.x, self.player.y))
        self.maze.draw(self._display_surf, self._block_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[K_k]:
                for _ in range(5):
                    x, y = self.maze.make_maze()
                    self.player.setXY(x * 6, y * 6)

            if keys[K_s]:
                x, y = self.maze.solve_maze()
                self.player.setXY(x * 6, y * 6)

            if (keys[K_RIGHT]):
                self.player.moveRight()

            if (keys[K_LEFT]):
                self.player.moveLeft()

            if (keys[K_UP]):
                self.player.moveUp()

            if (keys[K_DOWN]):
                self.player.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
