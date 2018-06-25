# import datetime as datetime
# import math
# import time
# from tkinter import Tk
# from turtle import Canvas
#
# root = Tk()
#
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
#
# canvas = Canvas(root, width=screen_width, height=screen_height, bg="black")
# canvas.pack()
#
# canvas.create_rectangle(screen_width / 3, screen_height / 3, screen_width * 2 / 3, screen_height * 2 / 3, fill="green")
#
# root.mainloop()
#
#
# def draw_hand(angle, someradius, some_thinkness, some_color):
#     canvas.create_line(screen_width / 2,
#                        screen_height / 2,
#                        screen_width / 2 + math.cos(angle) * someradius,
#                        screen_height / 2 + math.sin(angle) * someradius,
#                        width=some_thinkness,
#                        fill=some_color)
#
#
# def draw_clock():
#     canvas.create_rectangle(screen_width / 3, screen_height / 3, screen_width * 2 / 3, screen_height * 2 / 3,
#                             fill="green")
#
#     radius = screen_height / 4
#     canvas.create_rectangle(screen_width / 2 - 100, screen_height / 2 - 100, screen_width / 2 + 100,
#                             screen_height / 2 + 100,
#                             fill="gray")
#     now = datetime.datetime.now()
#     hour_angle = 2 * math.pi * now.hour / 12 - math.pi / 2
#     drawhand(hour_angle, radius / 4, 4, "red")
#     minute_angle = 2 * math.pi * now.minute / 60 - math.pi / 2
#     drawhand(hour_angle, radius / 3, 3, "blue")
#     seconds_angle = 2 * math.pi * now.second / 60 - math.pi / 2  # clock zero angle starts at top
#     draw_hand(seconds_angle, radius / 3, 1, "yellow")
#
#
# while (1 < 2):  # loop forever
#     canvas.delete("all")
#     draw_clock()
#     canvas.update()
#     time.sleep(0.01)
#
# # must be the last line before exit for TKinter
# root.mainloop()

#Draw a Clock
#create the drawing system
import datetime as datetime
import math
import time
from tkinter import Tk
from turtle import Canvas

root = Tk()

# main dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#  canvas is a white piece of paper on which you can draw
canvas = Canvas(root, width=screen_width, height=screen_height, bg="black")
canvas.pack()


def draw_hand(angle, someradius, some_thinkness, some_color):
    # this function draws a hand with a certain angle and radius
    canvas.create_line(screen_width / 2,  # x1
                       screen_height / 2,  # y1
                       screen_width / 2 + math.cos(angle) * someradius,  # x2
                       screen_height / 2 + math.sin(angle) * someradius,  # y2
                       width=some_thinkness,  # line thickness
                       fill=some_color)  # line color


def draw_clock():
    # draw a clock background
    canvas.create_rectangle(screen_width / 3, screen_height / 3, screen_width * 2 / 3, screen_height * 2 / 3,
                            fill='green')

    # draw the clock itself
    radius = screen_height / 4
    canvas.create_oval(screen_width / 2 - 100, screen_height / 2 - 100, screen_width / 2 + 100, screen_height / 2 + 100,
                       fill="gray")

    # draw all hands
    now = datetime.datetime.now()
    hour_angle = 2 * math.pi * now.hour / 12 - math.pi / 2  # clock zero angle starts at top
    draw_hand(hour_angle, radius / 4, 4, "red")
    minute_angle = 2 * math.pi * now.minute / 60 - math.pi / 2  # clock zero angle starts at top
    draw_hand(minute_angle, radius / 3, 3, "blue")
    seconds_angle = 2 * math.pi * now.second / 60 - math.pi / 2  # clock zero angle starts at top
    draw_hand(seconds_angle, radius / 3, 1, "yellow")


while (1 < 2):  # loop forever
    canvas.delete("all")
    draw_clock()
    canvas.update()
    time.sleep(0.01)

# must be the last line before exit for TKinter
root.mainloop()