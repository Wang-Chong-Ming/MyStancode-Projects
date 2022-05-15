"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 60  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    num_live = NUM_LIVES
    brick_number = 1
    # Add the animation loop here!
    while num_live != 0 and brick_number != 0:          # 若生命為0，或brick全部消除，結束遊戲
        pause(FRAME_RATE)
        graphics.move_ball()
        if graphics.ball.x <= 0 or \
                graphics.ball.x+graphics.ball.width >= graphics.window_width:        # 撞到左/右牆，反彈
            graphics.change_ball_dx()
        if graphics.ball.y <= 0:                                                     # 撞到上牆，反彈
            graphics.change_ball_dy()
        brick_number = graphics.check_for_collision()
        if graphics.ball.y - graphics.ball.height >= graphics.window_height:         # 撞到下牆，生命扣1，回到初始位置
            graphics.stop()
            num_live -= 1


if __name__ == '__main__':
    main()
