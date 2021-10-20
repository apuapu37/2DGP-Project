from pico2d import *

# 바닥
class Grass:
    def __init__(self):
        self.grass = load_image('images\grass.png')

    def draw(self):
        self.grass.draw(400, 30)

# 일시정지
class Pause:
    def __init__(self):
        self.pause = load_image('images\pause.png')

    def draw(self):
        self.pause.draw(400, 300)

# 버섯
class Mushroom:
    def __init__(self):
        self.mushroom = load_image('images\mushroom.png')
        self.x = 0

    def update(self):
        self.x += 5

    def draw(self):
        self.mushroom.draw(self.x, 78)

# 플레이어 캐릭터
class Mario:
    def __init__(self):
        self.mario = load_image('images\mario.png')
        self.frame = 0
        self.x = 800 // 2
        self.y = 95
        self.dir = 0
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 3
        self.x += self.dir * 5

    def draw(self):
        if (self.dir > 0):
            self.mario.clip_draw(189 + self.frame * 64, 0, 60, 68, self.x, self.y)
        elif (self.dir == 0):
            self.mario.clip_draw(2, 0, 60, 68, self.x, self.y)
        elif (self.dir < 0):
            self.mario.clip_draw(2 + self.frame * 64, 0, 60, 68, self.x, self.y)

# 배경이미지
# class BackGround:
#     def __init__(self):
#         self.background = load_image('images\Background.png')
#
#     def draw(self):
#         self.background.draw_now(400, 130)

# 이동
def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                mario.dir += 1
            elif event.key == SDLK_LEFT:
                mario.dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                mario.dir -= 1
            elif event.key == SDLK_LEFT:
                mario.dir += 1

open_canvas()
#hide_lattice()
grass = Grass()
mario = Mario()
mushroom = Mushroom()
pause = Pause()
# background = BackGround()
running = True


# game main loop code
while running:
    handle_events()

    # game logic
    mario.update()
    mushroom.update()

    # game drawing
    clear_canvas()
    mario.draw()
    grass.draw()
    mushroom.draw()
    # background.draw()
    update_canvas()
    delay(0.05)

close_canvas()