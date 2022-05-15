"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img:
    :param figure_img:
    :return:
    """
    new_img = SimpleImage.blank(figure_img.width, figure_img.height)
    background_img.make_as_big_as(figure_img)
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            pixel = figure_img.get_pixel(x, y)
            pixel2 = background_img.get_pixel(x, y)
            pixel_new = new_img.get_pixel(x, y)
            bigger = max(pixel.red, pixel.blue)
            if pixel.green > 1.5 * bigger:
                pixel_new.red = pixel2.red
                pixel_new.green = pixel2.green
                pixel_new.blue = pixel2.blue
            else:
                pixel_new.red = pixel.red
                pixel_new.green = pixel.green
                pixel_new.blue = pixel.blue
    return new_img


def main():
    """
    創作理念:和地球合照~
    """
    space_ship = SimpleImage("image_contest/Moon.png")
    figure = SimpleImage("image_contest/Owen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
