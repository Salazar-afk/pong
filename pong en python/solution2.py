from turtle import width
import turtle

#ventana
wn = turtle.Screen()
wn.title("Pong by Mauro")
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
pelota.dx = 3
pelota.dy = 3

#Linea Division
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)

#funciones
def jugadorA_up():
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)
    
def jugadorA_down():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)
    
def jugadorB_up():
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)
    
def jugadorB_down():
    y = jugadorB.ycor()
    y -= 20
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
    #Revisa colisiones con los bordes de la ventana
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() <-290:
        pelota.dy *=-1
        
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        
    if pelota.xcor() < -300:  
        pelota.goto(0,0)
        pelota.dx *= -1
        
    
    #bordes derecha/izquierda
    



