"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout',
                 dx=0, dy=0):
        self.p_o = paddle_offset
        self.brick_o = brick_offset
        self.brick_w = brick_width
        self.brick_h = brick_height
        self.brick_s = brick_spacing
        self.brick_r = brick_rows
        self.brick_c = brick_cols
        self.ball_r = ball_radius

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = self.paddle.color = "silver"
        self.window.add(self.paddle, x=(self.window_width-paddle_width)/2, y=self.window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.ball.color = self.ball.fill_color = "black"
        self.window.add(self.ball, x=(self.window_width-ball_radius)/2, y=(self.window_height-ball_radius)/2)

        # Default initial velocity for the ball
        self.__dx = dx
        self.__dy = dy

        # Initialize our mouse listeners
        onmousemoved(self.paddle_position)
        onmouseclicked(self.restart)

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                brick = GRect(brick_width, brick_height, x=(brick_width+brick_spacing)*i, y=brick_offset+(brick_height
                                                                                                  +
                                                                                                  brick_spacing)*j)
                brick.filled = True
                if j == 0 or j == 1:
                    brick.fill_color = "red"
                elif j == 2 or j == 3:
                    brick.fill_color = "orange"
                elif j == 4 or j == 5:
                    brick.fill_color = "yellow"
                elif j == 6 or j == 7:
                    brick.fill_color = "green"
                else:
                    brick.fill_color = "blue"
                self.window.add(brick)

        self.brick_number = self.brick_c * self.brick_r

    def paddle_position(self, event):
        if event.x + self.paddle.width/2 >= self.window_width:            # 若paddle要超過視窗右側，paddle會停在最右側
            self.paddle.x = self.window_width - self.paddle.width
        elif event.x - self.paddle.width/2 <= 0:                          # 若paddle要超過視窗左側，paddle會停在最左側
            self.paddle.x = 0
        else:
            self.paddle.x = event.x - self.paddle.width/2
        self.window.add(self.paddle, x=self.paddle.x, y=self.window.height-self.p_o)

    def restart(self, event):
        if self.__dx == 0:          # 點擊時，若速度不為0，不執行任何事
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = - self.__dx

    def stop(self):                 # 將球設定回原位置，且速度為0
        self.window.add(self.ball, x=(self.window_width - self.ball_r) / 2,
                        y=(self.window_height - self.ball_r) / 2)
        self.__dx = self.__dy = 0

    def move_ball(self):            # 移動球
        self.ball.move(self.__dx, self.__dy)

    def change_ball_dx(self):       # x方向反彈
        self.__dx = -self.__dx

    def change_ball_dy(self):       # y方向反彈
        self.__dy = -self.__dy

    def check_for_collision(self):              # 檢查是否撞到paddle或brick
        for i in range(2):
            for j in range(2):
                maybe_obj = self.window.get_object_at(self.ball.x + i*self.ball.width, self.ball.y + j*self.ball.height)
                if maybe_obj is not None:       # 若碰到Object
                    if self.touch_paddle(self.ball.y+self.ball.height):     # 檢查是否為paddle，若是，y方向反彈
                        self.__dy = - self.__dy
                    else:                                                   # 若不是，則為brick
                        # 確認撞擊brick位置
                        if self.touch_brick_top_or_bottom(self.ball.x + i*self.ball.width, self.ball.y + j*self.ball.height):
                            self.__dy = - self.__dy         # 撞到上或下，y方向反彈
                        else:
                            self.__dx = - self.__dx         # 撞到左或右，X方向反彈
                        self.window.remove(maybe_obj)
                        self.brick_number -= 1              # 磚塊數扣1
                    return self.brick_number

    def touch_paddle(self, bottom_y):   # 確認是否撞擊paddle
        if self.window.height-self.p_o+INITIAL_Y_SPEED >= bottom_y >= self.window.height-self.p_o:
            return True
        else:
            return False

    def touch_brick_top_or_bottom(self, vertex_x, vertex_y):        # 確認撞擊Brick位置
        # 以brick左上角為原點
        x = vertex_x % (self.brick_w + self.brick_s)                        # 與brick左側的距離
        y = (vertex_y - self.brick_o) % (self.brick_h + self.brick_s)       # 與brick上面的距離
        if self.__dx < 0:            # 若向左移動，x將紀錄"與brick右側的距離"
            x = self.brick_w - x
        if self.__dy < 0:            # 若向上移動，y將紀錄"與brick下面的距離"
            y = self.brick_h - y
        if x > y:                    # 若 x > y，代表撞擊位置在rick的"上"或"下"，反之，則為"左"或"右"
            return True
        else:
            return False
