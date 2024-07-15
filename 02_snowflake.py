import turtle

def koch_curve(t:turtle.Turtle, recur_level: int, size: int):
    if recur_level == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, recur_level - 1, size / 3)
            t.left(angle)

def draw_koch_curve(recur_level: int, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, recur_level, size)
        t.left(-120)

    window.mainloop()

# Виклик функції
draw_koch_curve(3)