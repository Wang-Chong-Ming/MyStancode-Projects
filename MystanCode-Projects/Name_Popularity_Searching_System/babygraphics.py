"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE + (width-GRAPH_MARGIN_SIZE*2)/len(YEARS) * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    for j in range(len(lookup_names)):              # 劃出所有名字的排名趨勢
        for i in range(len(YEARS)-1):               # 劃出線的每一小段

            # 定義每一小段線的"起點"x值
            x = get_x_coordinate(CANVAS_WIDTH, i)

            # 定義每一小段線的"終點"x值
            x1 = get_x_coordinate(CANVAS_WIDTH, i+1)

            # 定義每一小段線的"起點"y值
            if str(YEARS[i]) in name_data[lookup_names[j]]:
                y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE - \
                    (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)*(1-int(name_data[lookup_names[j]][str(YEARS[i])])/1000)
                rank = name_data[lookup_names[j]][str(YEARS[i])]
            else:
                y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                rank = "*"

            # 定義每一小段線的"終點"y值
            if str(YEARS[i+1]) in name_data[lookup_names[j]]:
                y1 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE - \
                    (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)*(1-int(name_data[lookup_names[j]][str(YEARS[i+1])])/1000)
                rank1 = name_data[lookup_names[j]][str(YEARS[i+1])]
            else:
                y1 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                rank1 = "*"

            # 加上每一小段線及排名
            canvas.create_line(x, y, x1, y1, width=LINE_WIDTH, fill=COLORS[j % len(COLORS)])
            canvas.create_text(x + TEXT_DX, y + TEXT_DX, text=lookup_names[j] + rank, anchor=tkinter.SW)

            # 加上最後一個年份的排名
            if i == len(YEARS)-2:
                canvas.create_text(x1 + TEXT_DX, y1 + TEXT_DX, text=lookup_names[j] + rank1, anchor=tkinter.SW)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
