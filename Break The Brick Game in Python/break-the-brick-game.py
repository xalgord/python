"""
###################################
Developer: Xalgord (Krishna Kaushal)

Youtube: https://youtube.com/xalgord
github: https://github.com/xalgord
Instagram: https://instagram.com/xalgord
website: https://xalgord.in

###################################
"""
import random
from tkinter import CENTER
import numpy
# using pygame python GUI
import pygame

pygame.init()

# Setting the width and height of the screen [width, height]
screen = pygame.display.set_mode()
w, h = pygame.display.get_surface().get_size()


class Ball(object):
    def __init__(self, screen, radius, x, y):
        self.__screen = screen
        self._radius = radius
        self._xLoc = x
        self._yLoc = y
        self.__xVel = 7
        self.__yVel = 2.5
        w, h = pygame.display.get_surface().get_size()
        self.__width = w
        self.__height = h

    def getXVel(self):
        return self.__xVel

    def getYVel(self):
        return self.__yVel

    def draw(self):
        # draws the ball onto the screen.
        pygame.draw.circle(screen, (255, 255, 255),
                           (self._xLoc, self._yLoc), self._radius)   # ball color

    def update(self, paddle, brickwall):
        # collision detection and moves the ball at the screen.
        self._xLoc += self.__xVel
        self._yLoc += self.__yVel
        # left screen wall bounce
        if self._xLoc <= self._radius:
            self.__xVel *= -1
        # right screen wall bounce
        elif self._xLoc >= self.__width - self._radius:
            self.__xVel *= -1
        # top wall bounce
        if self._yLoc <= self._radius:
            self.__yVel *= -1
        # bottom drop out
        elif self._yLoc >= self.__width - self._radius:
            return True

        if brickwall.collide(self):
            self.__yVel *= -1

        paddleW = paddle._width
        paddleH = paddle._height
        paddleX = paddle._xLoc
        paddleY = paddle._yLoc
        ballX = self._xLoc
        ballY = self._yLoc

        if ((ballX + self._radius) >= paddleX and ballX <= (paddleX + paddleW)) \
                and ((ballY + self._radius) >= paddleY and ballY <= (paddleY + paddleH)):
            self.__yVel *= -1

        return False

# class for representing a paddle


class Paddle(object):
    def __init__(self, screen, width, height, x, y):
        self.__screen = screen
        self._width = width
        self._height = height
        self._xLoc = x
        self._yLoc = y
        w, h = pygame.display.get_surface().get_size()
        self.__W = w
        self.__H = h

    def draw(self):
        # draws the paddle.
        pygame.draw.rect(screen, (0, 255, 0), (self._xLoc, self._yLoc,
                                               self._width, self._height), 0, 10)   # base color

    def update(self):
        # moves the paddle via mouse
        x, y = pygame.mouse.get_pos()
        if x >= 0 and x <= (self.__W - self._width):
            self._xLoc = x


# simple Brick class.

class Brick(pygame.sprite.Sprite):
    def __init__(self, screen, width, height, x, y):
        self.__screen = screen
        self._width = width
        self._height = height
        self._xLoc = x
        self._yLoc = y
        w, h = pygame.display.get_surface().get_size()
        self.__W = w
        self.__H = h
        self.__isInGroup = False

    def draw(self):
        # draws the brick
        pygame.draw.rect(screen, (random.randint(100, 255), random.randint(50, 250), random.randint(50, 250)), (self._xLoc,
                                                                                                                self._yLoc, self._width, self._height), 0)

    def add(self, group):
        # adds this brick to a given group.
        group.add(self)
        self.__isInGroup = True

    def remove(self, group):
        # removes this brick from the given group.
        group.remove(self)
        self.__isInGroup = False

    def alive(self):
        # returns true when this brick belongs to the brick wall else false.
        return self.__isInGroup

    def collide(self, ball):
        # collision detection between ball and this brick
        brickX = self._xLoc
        brickY = self._yLoc
        brickW = self._width
        brickH = self._height
        ballX = ball._xLoc
        ballY = ball._yLoc
        ballXVel = ball.getXVel()
        ballYVel = ball.getYVel()

        if ((ballX + ball._radius) >= brickX and (ballX + ball._radius) <= (brickX + brickW)) \
                and ((ballY - ball._radius) >= brickY and (ballY - ball._radius)
                     <= (brickY + brickH)):
            return True
        else:
            return False


# brick wall class
class BrickWall(pygame.sprite.Group):
    def __init__(self, screen, x, y, width, height):
        self.__screen = screen
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._bricks = []

        X = x
        Y = y
        for i in range(12):
            for j in range(25):
                self._bricks.append(Brick(screen, width, height, X, Y))
                X += width + (width / 7.0)
            Y += height + (height / 7.0)
            X = x

    def add(self, brick):
        # adds a brick to this group
        self._bricks.append(brick)

    def remove(self, brick):
        # removes a brick from this BrickWall group
        self._bricks.remove(brick)

    def draw(self):
        # draws all bricks.
        for brick in self._bricks:
            if brick != None:
                brick.draw()

    def update(self, ball):
        # checks collision between ball and bricks.
        for i in range(len(self._bricks)):
            if ((self._bricks[i] != None) and self._bricks[i].collide(ball)):
                self._bricks[i] = None

        # removes the None-elements from the brick list.
        for brick in self._bricks:
            if brick is None:
                self._bricks.remove(brick)

    def hasWin(self):
        # if player wins the game?
        return len(self._bricks) == 0

    def collide(self, ball):
        # check collisions
        for brick in self._bricks:
            if brick.collide(ball):
                return True
        return False


# objects
ball = Ball(screen, 9, random.randint(1, 700), 400)
paddle = Paddle(screen, 150, 10, 250, 880)
brickWall = BrickWall(screen, 10, 10, 55.5, 25)

isGameOver = False  # determines whether game is lose
gameStatus = True  # game is still running

score = 0  # score for the game.

pygame.display.set_caption("Break-The-Brick Game")

# Loop until the user clicks the close button.
done = False

# to manage how fast the screen updates
clock = pygame.time.Clock()

# for displaying text in the game
pygame.font.init()  # you have to call this at the start,
# if you want to use this module.

# message for game over
mgGameOver = pygame.font.SysFont('comicsans', 50)

# message for winning the game.
mgWin = pygame.font.SysFont('comicsans', 50)

# message for score
mgScore = pygame.font.SysFont('comicsans', 30)

textsurfaceGameOver = mgGameOver.render('Game Over!', False, (255, 0, 0))
textsurfaceWin = mgWin.render("You win!", False, (0, 255, 0))
textsurfaceScore = mgScore.render(
    "score: " + str(score), False, (255, 255, 255))


#### Main Program Loop ####
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill("#1c1c1c")
    if gameStatus:

        # first draws ball for appropriate displaying the score.
        brickWall.draw()

        # for counting and displaying the score
        if brickWall.collide(ball):
            score += 10
        textsurfaceScore = mgScore.render(
            "score: " + str(score), False, (255, 255, 255))
        screen.blit(textsurfaceScore, (10, 850))

        brickWall.update(ball)

        paddle.draw()
        paddle.update()

        if ball.update(paddle, brickWall):
            isGameOver = True
            gameStatus = False

        if brickWall.hasWin():
            gameStatus = False

        ball.draw()

    else:  # game isn't running.
        if isGameOver:  # player lose
            screen.blit(textsurfaceGameOver, ((w/2)-130, (h/2)-80))
            textsurfaceScore = mgScore.render(
                "score: " + str(score), False, (255, 255, 255))
            screen.blit(textsurfaceScore, ((w/2)-80, (h/2)))
        elif brickWall.hasWin():  # player win
            screen.blit(textsurfaceWin, ((w/2)-100, (h/2)-50))
            textsurfaceScore = mgScore.render(
                "score: " + str(score), False, (255, 255, 255))
            screen.blit(textsurfaceScore, ((w/2)-80, (h/2)))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 120 frames per second
    clock.tick(120)

pygame.quit()
# Close the window and quit.
