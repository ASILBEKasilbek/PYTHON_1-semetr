import turtle

# Ekranni sozlash
screen = turtle.Screen()
screen.title("O'zbekiston bayrog'i")
screen.setup(width=600, height=400)

# Turtle ob'ektini yaratish
t = turtle.Turtle()
t.speed(10)

# Funksiya: to'rtburchak chizish
def draw_rectangle(color, width, height):
    t.begin_fill()
    t.color(color)
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Bayroqni chizish
def draw_uzbekistan_flag():
    # Birinchi qatlam - ko'k
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    draw_rectangle("#1EB53A", 300, 33.3)

    # Ikkinchi qatlam - oq
    t.penup()
    t.goto(-150, 66.7)
    t.pendown()
    draw_rectangle("white", 300, 33.3)

    # Uchinchi qatlam - qizil
    t.penup()
    t.goto(-150, 33.3)
    t.pendown()
    draw_rectangle("#0072C6", 300, 33.3)

    # To'rtinchi qatlam - yashil
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    draw_rectangle("#1EB53A", 300, 33.3)
    
    # Oy va yulduzlarni chizish
    t.penup()
    t.goto(-130, 83)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    
    t.penup()
    t.goto(-120, 83)
    t.color("#0072C6")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    
    t.penup()
    t.goto(-110, 83)
    t.color("white")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

# Bayroqni chizishni boshlash
draw_uzbekistan_flag()

# Ekranni saqlab turish
turtle.done()
