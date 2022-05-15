"""
File:
Name:王崇銘
----------------------
TODO:
晚餐:漢堡
口味:臭貓！再弄倒電視rrrrr
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GArc, GPolygon
from campy.graphics.gwindow import GWindow


window = GWindow()


def main():
    """
    Title : 我的晚餐

    口味:臭貓！再弄倒電視啊!!!!
    """
    background = GRect(window.width, window.height)
    background.filled = True
    background.fill_color = "azure"
    window.add(background)

    hamburger_down = GArc(200, 100, 180, 180)
    hamburger_down.filled = True
    hamburger_down.fill_color = hamburger_down.color = "orangered"
    window.add(hamburger_down, x=100, y=200 + 75)

    hamburger1_down = GOval(200, 15)
    hamburger1_down.filled = True
    hamburger1_down.fill_color = hamburger1_down.color = "orange"
    window.add(hamburger1_down, x=100, y=200 + 91)

    cat_hand = GPolygon()
    cat_hand.add_vertex((25, 17))
    cat_hand.add_vertex((30, 30))
    cat_hand.add_vertex((7, 23))
    cat_hand.filled = True
    cat_hand.fill_color = "gray"
    cat_hand.color = "darkgray"
    window.add(cat_hand, x=100 + 100, y=200 + 80)

    cat_foot = GPolygon()
    cat_foot.add_vertex((25, 17))
    cat_foot.add_vertex((30, 30))
    cat_foot.add_vertex((7, 30))
    cat_foot.filled = True
    cat_foot.fill_color = "gray"
    cat_foot.color = "darkgray"
    window.add(cat_foot, x=100, y=200 + 70)

    cat_body = GOval(130, 80)
    cat_body.filled = True
    cat_body.fill_color = cat_body.color = "gray"
    window.add(cat_body, x=100 + 10, y=200 + 30)

    cat_body = GOval(50, 30)
    cat_body.filled = True
    cat_body.fill_color = "black"
    cat_body.color = "gray"
    window.add(cat_body, x=100 + 60, y=200 + 70)

    cat_body = GPolygon()
    cat_body.add_vertex((25, 17))
    cat_body.add_vertex((30, 30))
    cat_body.add_vertex((20, 35))
    cat_body.add_vertex((7, 30))
    cat_body.add_vertex((10, 20))
    cat_body.filled = True
    cat_body.fill_color = "burlywood"
    cat_body.color = "gray"
    window.add(cat_body, x=100+80, y=200 + 50)

    cat_body = GOval(50, 30)
    cat_body.filled = True
    cat_body.fill_color = "burlywood"
    cat_body.color = "gray"
    window.add(cat_body, x=100 + 30, y=200 + 40)

    cat_ear1 = GPolygon()
    cat_ear1.add_vertex((20, 20))
    cat_ear1.add_vertex((24, 35))
    cat_ear1.add_vertex((37, 23))
    cat_ear1.filled = True
    cat_ear1.fill_color = "darkgray"
    window.add(cat_ear1, x=100 + 175, y=200 + 20)

    cat_hand = GOval(90, 80)
    cat_hand.filled = True
    cat_hand.fill_color = "gray"
    cat_hand.color = "darkgray"
    window.add(cat_hand, x=100 + 120, y=200 + 30)

    cat_ear1 = GPolygon()
    cat_ear1.add_vertex((20, 20))
    cat_ear1.add_vertex((20, 30))
    cat_ear1.add_vertex((7, 23))
    cat_ear1.filled = True
    cat_ear1.fill_color = "darkgray"
    window.add(cat_ear1, x=100 + 115, y=200 + 28)

    cat_eye = GOval(8, 6)
    cat_eye.filled = True
    cat_eye.fill_color = "white"
    cat_eye.color = "white"
    window.add(cat_eye, x=100 + 185, y=200 + 60)

    cat_eye = GOval(3, 3)
    cat_eye.filled = True
    cat_eye.fill_color = "black"
    window.add(cat_eye, x=100 + 189, y=200 + 63)

    cat_eye = GOval(8, 6)
    cat_eye.filled = True
    cat_eye.fill_color = "white"
    cat_eye.color = "white"
    window.add(cat_eye, x=100 + 150, y=200 + 65)

    cat_eye = GOval(3, 3)
    cat_eye.filled = True
    cat_eye.fill_color = "black"
    window.add(cat_eye, x=100 + 154, y=200 + 68)

    cat_mouse = GArc(8, 15, 200, 160)
    window.add(cat_mouse, x=100 + 165, y=200 + 80)

    cat_mouse = GArc(8, 15, 200, 160)
    window.add(cat_mouse, x=100 + 173, y=200 + 80)



    hamburger_up = GArc(200, 150, 0, 180)
    hamburger_up.filled = True
    hamburger_up.fill_color = hamburger_up.color = "orangered"
    window.add(hamburger_up, x=100, y=200)

    hamburger_up1 = GArc(200, 50, 180, 180)
    hamburger_up1.filled = True
    hamburger_up1.fill_color = hamburger_up1.color = "orangered"
    window.add(hamburger_up1, x=100, y=200 + 25)

    sesame = GOval(5, 7)
    sesame.filled = True
    sesame.fill_color = sesame.color = "darkorange"
    window.add(sesame, x=100 + 40, y=200 + 25)

    sesame = GOval(5, 7)
    sesame.filled = True
    sesame.fill_color = sesame.color = "darkorange"
    window.add(sesame, x=100 + 70, y=200 + 30)

    sesame = GOval(5, 7)
    sesame.filled = True
    sesame.fill_color = sesame.color = "darkorange"
    window.add(sesame, x=100 + 60, y=200 + 15)

    sesame = GOval(5, 7)
    sesame.filled = True
    sesame.fill_color = sesame.color = "darkorange"
    window.add(sesame, x=100 + 95, y=200 + 26)

    sesame = GOval(5, 7)
    sesame.filled = True
    sesame.fill_color = sesame.color = "darkorange"
    window.add(sesame, x=100 + 110, y=200 + 17)

    sesame = GOval(5, 7)
    sesame.filled = True
    sesame.fill_color = sesame.color = "darkorange"
    window.add(sesame, x=100 + 130, y=200 + 30)

    sesame = GOval(5, 7)
    sesame.filled = True
    sesame.fill_color = sesame.color = "darkorange"
    window.add(sesame, x=100 + 150, y=200 + 15)

    sesame = GOval(5, 7)
    sesame.filled = True
    sesame.fill_color = sesame.color = "darkorange"
    window.add(sesame, x=100 + 160, y=200 + 20)




if __name__ == '__main__':
    main()
