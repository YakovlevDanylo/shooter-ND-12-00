from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update(self, screen):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 630:
            self.rect.x += self.speed

window = display.set_mode((700, 500))
display.set_caption("Шутер")

background = transform.scale(image.load("galaxy.jpg"), (700, 500))
player = Player("rocket.png", 5, 400, 70,100, 10)
clock = time.Clock()
fps = 60

mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(background, (0, 0))

    player.update(window)
    player.reset(window)

    display.update()
    clock.tick(fps)
