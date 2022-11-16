import turtle

#ventana
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#jugador A
jugadorA= turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid=5, stretch_len=1)

#jugadorB
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350, 0)
jugadorB.shapesize(stretch_wid=5, stretch_len=1)

#Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
#variables para velocidad de la pelota
pelota.dx = 1 
pelota.dy = 1  

#Linea Division
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)

#Marcador
marcadorA = 0
marcadorB = 0

#pen
pen=turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador A: 0		jugador B: 0", align="center", font=("Courier", 25, "normal"))


#funciones
def jugadorA_up():
    y = jugadorA.ycor()
    y += 60
    jugadorA.sety(y)
    
def jugadorA_down(): 
    y = jugadorA.ycor()
    y -= 60
    jugadorA.sety(y)
    
def jugadorB_up():
    y = jugadorB.ycor()
    y += 60
    jugadorB.sety(y)
    
def jugadorB_down():
    y = jugadorB.ycor()
    y -= 60
    jugadorB.sety(y)


#Teclado
wn.listen()
wn.onkeypress(jugadorA_up, "w" or "W")
wn.onkeypress(jugadorA_down, "s" or "S")
wn.onkeypress(jugadorB_up, "Up")
wn.onkeypress(jugadorB_down, "Down")

while True:
    wn.update()
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
    #bordes
    #bordes derecha/izquierda
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() <-290:
        pelota.dy *= -1
    
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorA += 1
        pen.clear()
        pen.write(f"Jugador A: {marcadorA}		jugador B: {marcadorB}", align="center", font=("Courier", 25, "normal"))       
    if pelota.xcor() < -390:  
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorB += 1
        pen.clear()
        pen.write(f"Jugador A: {marcadorA}		jugador B: {marcadorB}", align="center", font=("Courier", 25, "normal"))
        
        
    #colisiones con paletas
    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
        and (pelota.ycor() < jugadorB.ycor()+50
        and pelota.ycor()  > jugadorB.ycor()-50)):
        pelota.dx *= -1

    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
        and (pelota.ycor() < jugadorA.ycor() + 50
        and pelota.ycor() > jugadorA.ycor()-50)):
        pelota.dx *= -1



  

