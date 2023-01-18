import pgzrun

TITLE = "Arkanoid"
WIDTH = 800
HEIGHT = 500
START_SPEED = 3
START_BALL_X = 100
START_BALL_Y = 300
START_PADDLE_X = 120
START_PADDLE_Y = 420
AMOUND_BLOCKS = 8
MAX_HEARTS = 3

class Paddle():
    def __init__(self,image,x,y):
        actor = Actor(image)
        actor.x = x
        actor.y = y
        self.x = actor.x
        self.y = actor.y
        self.actor = actor
    def colliderect(self,object):
        actor = self.actor
        if actor.colliderect(object.actor):
            return True
        else:
            return False
    def draw(self):
        self.actor.draw()

class Ball():
    def __init__(self,image,x,y):
        actor = Actor(image)
        actor.x = x
        actor.y = y
        self.x = actor.x
        self.y = actor.y
        self.actor = actor
    def colliderect(self,object):
        actor = self.actor
        if object.colliderect(actor):
            return True
        else:
            return False
    def draw(self):
        self.actor.draw()

class Obstacle():
    def __init__(self,image,x,y):
        actor = Actor(image)
        actor.x = x
        actor.y = y
        self.x = actor.x
        self.y = actor.y
        self.actor = actor
    def colliderect(self,object):
        actor = self.actor
        if object.colliderect(actor):
            return True
        else:
            return False
    def draw(self):
        self.actor.draw()

class Heart():
    def __init__(self,image,x,y):
        actor = Actor(image)
        actor.x = x
        actor.y = y
        self.x = actor.x
        self.y = actor.y
        self.actor = actor
    def draw(self):
        self.actor.draw()

paddle = Paddle('paddleblue.png', START_PADDLE_X, START_PADDLE_Y)
ball = Ball('ballblue.png', START_BALL_X, START_BALL_Y)

ball_x_speed = START_SPEED
ball_y_speed = START_SPEED
hearts = MAX_HEARTS
bars_list = []
heart_list = []

def draw():
    if len(bars_list)<1:
        screen.clear()
        screen.blit("win.png", (0, 0))
    elif hearts <= 0:
        screen.clear()
        screen.blit("gameover.png", (0, 0))
    else:
        screen.blit("background.png", (0, 0))
        paddle.draw()
        ball.draw()
        for bar in bars_list:
            bar.draw()
        for heart in heart_list:
            heart.draw()


def place_bars(x,y,image):
    bar_x = x
    bar_y = y
    for i in range(AMOUND_BLOCKS):
        bar = Obstacle(image,bar_x,bar_y)
        bar_x += 70
        bars_list.append(bar)

def place_hearts(x,y,image):
    heart_x = x
    heart_y = y
    for i in range(MAX_HEARTS):
        heart = Heart(image,heart_x,heart_y)
        heart_x += 70
        heart_list.append(heart)


def update():
    global ball_x_speed, ball_y_speed, hearts
    if keyboard.left:
        paddle.x = paddle.x - 5
    if keyboard.right:
        paddle.x = paddle.x + 5
    update_ball()
    for bar in bars_list:
        if ball.colliderect(bar):
            bars_list.remove(bar)
            ball_y_speed *= -1
    if paddle.colliderect(ball):
        ball_y_speed *= -1
        #ball_x_speed *= -1
    if hearts <=0:
        draw()
    if len(bars_list)<1:
        draw()

def update_ball():
    global ball_x_speed, ball_y_speed,hearts,heart_list
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if (ball.x >= WIDTH) or (ball.x <=0):
        ball_x_speed *= -1
    if (ball.y <=0):
        ball_y_speed *= -1
    if (ball.y >= HEIGHT):
        ball_x_speed = START_SPEED
        ball_y_speed = START_SPEED
        ball.x = START_BALL_X
        ball.y = START_BALL_Y
        hearts -= 1
        heart_list.remove(heart_list[len(heart_list)-1])
    ball.actor.x = ball.x
    ball.actor.y = ball.y

coloured_box_list = ["element_blue_rectangle_glossy.png", "element_green_rectangle_glossy.png","element_red_rectangle_glossy.png"]
#coloured_box_list = ["element_blue_rectangle_glossy.png"]
bar_x = 120
bar_y = 100
for coloured_box in coloured_box_list:
    place_bars(bar_x, bar_y, coloured_box)
    bar_y += 50
heart_x = 30
heart_y = 30
place_hearts(heart_x, heart_y, "pixel-heart.png")
pgzrun.go()
