import pygame
from time import time
from functions import bezier

class PyEngine():
    def __init__(self, resolution:tuple, caption="Game"):
        
        # init
        pygame.init()
        self._screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption(caption)
        self._clock = pygame.time.Clock()
        self._running = True

        # update
        self._prevTime = time()
        self._dt = 0
        self._FPS = 0

        # controls
        self._keys = {"UP":False, "DOWN":False, "LEFT":False, "RIGHT":False, "ACTION":False, "QUIT":False, "MOUSE":False}
        self._configKeys = {"UP":pygame.K_w, "DOWN":pygame.K_s, "LEFT":pygame.K_a, "RIGHT":pygame.K_d, "ACTION":pygame.K_SPACE, "QUIT":pygame.K_ESCAPE}

        # draw
        self._squarePos = [[160, 360], [160, 120], [480, 120], [480, 360]]

    def draw(self):
        

        for x, y in self._squarePos:
            self.drawCircle(x, y, radius=7, color=(255, 0, 0))

        for i in range(0, 101, 5):
            x = bezier(self._squarePos[0][0], self._squarePos[1][0], self._squarePos[2][0], self._squarePos[3][0], i/100)
            y = bezier(self._squarePos[0][1], self._squarePos[1][1], self._squarePos[2][1], self._squarePos[3][1], i/100)
            self.drawCircle(x, y)



    def drawCircle(self, x:int, y:int, radius:int=5, color:tuple=(255, 255, 255)):
        pygame.draw.circle(self._screen, color, (x, y), radius, )


    def update(self):
        pass


    def move(self):
        if self._keys["MOUSE"]:
            # print("\nreset----")
            
            n = 0
            for xS, yS in self._squarePos:
                x, y = pygame.mouse.get_pos()
                # print(xS, yS, x, y, " - ", abs(x - xS), abs(y - yS))
                if 10 > abs(x - xS) and 10 > abs(y - yS):
                    self._squarePos[n] = [x, y]
                n += 1


    def controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._keys["QUIT"] = True
                self._running = False

            if event.type == pygame.KEYDOWN:
                for keyPressed in self._configKeys:
                    if event.key == self._configKeys[keyPressed]:
                        self._keys[keyPressed] = True
                if self._keys["QUIT"]:
                    self._running = False

            if event.type == pygame.KEYUP:
                for keyPressed in self._configKeys:
                    if event.key == self._configKeys[keyPressed]:
                        self._keys[keyPressed] = False
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                self._keys["MOUSE"] = True
            if event.type == pygame.MOUSEBUTTONUP:
                self._keys["MOUSE"] = False


    def game(self):
        while self._running:
            now = time()
            self._dt = now - self._prevTime
            self._prevTime = now
            self._clock.tick(self._FPS)

            self._screen.fill("black")
            self.controls()
            self.move()
            self.update()
            self.draw()
            pygame.display.update()

        pygame.quit()

    def get_dt(self):
        return self._dt