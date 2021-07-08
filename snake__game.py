import random
import turtle
import time

delay = 0.15

pencere = turtle.Screen()
pencere.title("Snake Game")
pencere.bgcolor("purple")
pencere.setup(width=600, height=600)
pencere.tracer(0)

kenar = turtle.Turtle()
kenar.shape("square")
kenar.color("black")
kenar.penup()
kenar.goto(-300, 0)
kenar.shapesize(30, 0.50)

kenar1 = turtle.Turtle()
kenar1.shape("square")
kenar1.color("black")
kenar1.penup()
kenar1.goto(292, 0)
kenar1.shapesize(30, 0.50)

kenar2 = turtle.Turtle()
kenar2.shape("square")
kenar2.color("black")
kenar2.penup()
kenar2.goto(0, 300)
kenar2.shapesize(0.50, 30)

kenar3 = turtle.Turtle()
kenar3.shape("square")
kenar3.color("black")
kenar3.penup()
kenar3.goto(0, -292)
kenar3.shapesize(0.50, 30)

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("circle")
kafa.color("black")
kafa.penup()
kafa.goto(0, 10)
kafa.direction = "stop"

yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("square")
yemek.color("red")
yemek.penup()
yemek.shapesize(0.70, 0.70)
yemek.goto(0, 100)

yemek1 = turtle.Turtle()
yemek1.speed(0)
yemek1.shape("square")
yemek1.color("red")
yemek1.penup()
yemek1.shapesize(0.70, 0.70)
yemek1.goto(150, 0)

yemek2 = turtle.Turtle()
yemek2.speed(0)
yemek2.shape("square")
yemek2.color("red")
yemek2.penup()
yemek2.shapesize(0.70, 0.70)
yemek2.goto(-200, 200)

yemek3 = turtle.Turtle()
yemek3.speed(0)
yemek3.shape("square")
yemek3.color("red")
yemek3.penup()
yemek3.shapesize(0.70, 0.70)
yemek3.goto(55, -200)

kuyruklar = []
puan = 0

yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape("square")
yaz.color("white")
yaz.penup()
yaz.hideturtle()
yaz.goto(-180, 230)
yaz.write("Scor:{}".format(puan), align="center", font=("Courier", 35, "normal"))

def move():
    if kafa.direction == "up":
        y = kafa.ycor()
        kafa.sety(y + 20)
    if kafa.direction == "down":
        y = kafa.ycor()
        kafa.sety(y - 20)
    if kafa.direction == "right":
        x = kafa.xcor()
        kafa.setx(x + 20)
    if kafa.direction == "left":
        x = kafa.xcor()
        kafa.setx(x - 20)

def go_up():
    if kafa.direction != "down":
        kafa.direction = "up"

def go_down():
    if kafa.direction != "up":
        kafa.direction = "down"

def go_right():
    if kafa.direction != "left":
        kafa.direction = "right"

def go_left():
    if kafa.direction != "right":
        kafa.direction = "left"

pencere.listen()
pencere.onkey(go_up, "Up")
pencere.onkey(go_down, "Down")
pencere.onkey(go_right, "Right")
pencere.onkey(go_left, "Left")

while True:
    pencere.update()

    if kafa.xcor() > 275 or kafa.xcor() < -280 or kafa.ycor() > 285 or kafa.ycor() < -275:
        time.sleep(1)
        bitti = turtle.Turtle()
        bitti.speed(0)
        bitti.shape("square")
        bitti.color("white")
        bitti.penup()
        bitti.hideturtle()
        bitti.goto(0, 0)
        bitti.write("GAME OVER", align="center", font=("Courier", 35, "normal"))
        time.sleep(0.5)
        bitti.clear()
        kafa.goto(0, 0)
        kafa.direction = "stop"

        for kuyruk in kuyruklar:
            kuyruk.goto(1000, 1000)
        kuyruklar = []

        puan = 0
        delay = 0.1

        yaz.clear()
        yaz.write("Scor:{}".format(puan), align="center", font=("Courier", 35, "normal"))

    if kafa.distance(yemek) < 15:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek.goto(x, y)

        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("circle")
        yeni_kuyruk.color("black")
        yeni_kuyruk.penup()
        kuyruklar.append(yeni_kuyruk)

        delay -= 0.001

        puan = puan + 10
        yaz.clear()
        yaz.write("Scor:{}".format(puan), align="center", font=("Courier", 35, "normal"))

    if kafa.distance(yemek1) < 15:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek1.goto(x, y)

        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("circle")
        yeni_kuyruk.color("black")
        yeni_kuyruk.penup()
        kuyruklar.append(yeni_kuyruk)

        delay -= 0.001

        puan = puan + 10
        yaz.clear()
        yaz.write("Scor:{}".format(puan), align="center", font=("Courier", 35, "normal"))

    if kafa.distance(yemek2) < 15:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek2.goto(x, y)

        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("circle")
        yeni_kuyruk.color("black")
        yeni_kuyruk.penup()
        kuyruklar.append(yeni_kuyruk)

        delay -= 0.001

        puan = puan + 10
        yaz.clear()
        yaz.write("Scor:{}".format(puan), align="center", font=("Courier", 35, "normal"))

    if kafa.distance(yemek3) < 15:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek3.goto(x, y)

        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("circle")
        yeni_kuyruk.color("black")
        yeni_kuyruk.penup()
        kuyruklar.append(yeni_kuyruk)

        delay -= 0.001

        puan = puan + 10
        yaz.clear()
        yaz.write("Scor:{}".format(puan), align="center", font=("Courier", 35, "normal"))

    for index in range(len(kuyruklar) - 1, 0, -1):
        x = kuyruklar[index - 1].xcor()
        y = kuyruklar[index - 1].ycor()
        kuyruklar[index].goto(x, y)

    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x, y)

    move()

    for segment in kuyruklar:
        if segment.distance(kafa) < 20:
            time.sleep(1)
            bitti = turtle.Turtle()
            bitti.speed(0)
            bitti.shape("square")
            bitti.color("white")
            bitti.penup()
            bitti.hideturtle()
            bitti.goto(0, 0)
            bitti.write("GAME OVER", align="center", font=("Courier", 35, "normal"))
            time.sleep(0.5)
            bitti.clear()
            kafa.goto(0, 0)
            kafa.direction = "stop"
            for segment in kuyruklar:
                segment.goto(1000, 1000)
            kuyruklar = []
            puan = 0
            yaz.clear()
            yaz.write('Scor:{}'.format(puan), align='center', font=('Courier', 35, 'normal'))
            delay = 0.15

    time.sleep(delay)

