from graphics import *

centre1 = Point(50, 50)
centre2 = Point(400, 100)
offset = Point(10, 10)

win = GraphWin("New Window", 960, 540)
win.setBackground(color_rgb(28, 40, 68))
e = Rectangle(Point(40, 40), Point(60, 60))
t1 = Text(centre1, "X1")
c = Circle(centre2, 20)
t2 = Text(centre2, "C1")
l = Line(centre1, centre2)

e.setOutline("white")
e.draw(win)
t1.draw(win)
c.draw(win)
t2.draw(win)
l.draw(win)
