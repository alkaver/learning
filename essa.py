import pygame
import random



class bird(object):
    def __init__(self, start, color=(255,0,0)):
        self.pos = start
        self.dirx = 1
        self.color = color
        self.speedx = 7
        self.speedy = 0
        self.gravity = 0.2
        self.jump = False
        self.speed = 1.6


    def body(self, screen):
        i = self.pos[0]
        j = self.pos[1]
        width = 40
        pygame.draw.rect(screen, self.color, (i-20,j-20,width,width))
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.speedy = 0
                self.jump = True
        if self.jump == False:
            self.pos = (self.pos[0]+self.speedx*self.dirx, self.pos[1]+self.speedy)
            self.speedy += self.gravity
        else:
            self.pos = (self.pos[0]+self.speedx*self.dirx, self.pos[1]+self.speedy)
            self.speedy -= self.speed
            self.speed -= self.gravity
            if self.speedy > 0:
                self.speed = 1.6
                self.speedy = 0
                self.jump = False



    def check(self):
        if self.pos[0] >= 580 and self.dirx==1:
            self.pos = (580, self.pos[1])
            self.dirx = -1
        elif self.pos[0] <= 20 and self.dirx==-1:
            self.pos = (20, self.pos[1])
            self.dirx = 1










def redrawWindow(screen):
    screen.fill((0,0,0))
    b.body(screen)
    pygame.display.update()

def drawspikes(screen, x=0):
    positions = []
    spikes = random.randint(1, 8)
    for i in range(spikes):
        while True:
            essa = random.randint(0, 9)
            if essa not in positions:
                positions.append(essa)
                y = essa * 80
                break
        pygame.draw.polygon(screen, (255, 255, 255), [(x, y), (x, y + 80), (x + 80, y + 40)])






def main():
    global b
    pygame.init()
    screen=pygame.display.set_mode((600,800))
    pygame.display.set_caption('My first programme')
    clock = pygame.time.Clock()
    flag=True
    b = bird((200,400))



    while flag==True:
        b.check()
        b.move()
        clock.tick(60)
        redrawWindow(screen)





main()