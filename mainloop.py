from Utils.objdraw import *
from Utils.draw import draw_pixels, line_coordinates, array_draw, clear_screen
from Utils.quickrender import ortho_cord, get_cube
import os
import time

while True:
    main_disp = create_array(50, 30)
    '''
    for i in range(51):
        ln = draw_line(0, 0, i, i)
        draw(main_disp, ln)
        print("", end="", flush=True)  # Flush stdout buffer
        time.sleep(0.1)
        clear_screen(main_disp)
    '''

    for list in get_cube(0, 0, 10, 1, 1, 1, 0, 0, 0):
        draw(main_disp, str())
        print("", end="", flush=True)
        time.sleep(0.1)
        clear_screen(main_disp)