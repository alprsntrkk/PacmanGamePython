import turtle
import random
ekran=turtle.Screen()
ekran.bgcolor("black")
ekran.title("Pacman")
ekran.setup(1000,1000)
ekran.tracer(0)

turtle.register_shape("kucukpac.gif")
turtle.register_shape("kirmizi.gif")
class Kalem(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.shapesize()
        self.color("blue")
        self.penup()
        self.speed(0)
class Oyuncu(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("kucukpac.gif")
        self.shapesize(24,24)
        self.penup()
        self.speed(0)
        self.altin=0
    def yukari_git(self):
        gidilen_yerin_x=oyuncu.xcor()
        gidilen_yerin_y=oyuncu.ycor()+24
        if(gidilen_yerin_x,gidilen_yerin_y) not in duvarlar:
            self.goto(gidilen_yerin_x,gidilen_yerin_y)
    def asagi_git(self):
        gidilen_yerin_x=oyuncu.xcor()
        gidilen_yerin_y=oyuncu.ycor()-24
        if(gidilen_yerin_x,gidilen_yerin_y) not in duvarlar:
            self.goto(gidilen_yerin_x,gidilen_yerin_y)
    def saga_git(self):
        gidilen_yerin_x=oyuncu.xcor()+24
        gidilen_yerin_y=oyuncu.ycor()
        if(gidilen_yerin_x,gidilen_yerin_y) not in duvarlar:
            self.goto(gidilen_yerin_x,gidilen_yerin_y)
    def sola_git(self):
        gidilen_yerin_x=oyuncu.xcor()-24
        gidilen_yerin_y=oyuncu.ycor()
        if(gidilen_yerin_x,gidilen_yerin_y) not in duvarlar:
            self.goto(gidilen_yerin_x,gidilen_yerin_y)           
    def carpisti_mi(self,other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance=(a**2)+(b**2)
        if distance<25:
            return True
        else:
            return False
        
class Dusman(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("kirmizi.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(x,y)
        self.direction=random.choice(["yukari","asagi","saga","sola"])
    def hareket_et(self):
        if self.direction=="yukari":
            dx=0
            dy=24
        elif self.direction=="asagi":
            dx=0
            dy=-24
        elif self.direction=="saga":
            dx=24
            dy=0
        elif self.direction=="sola":
            dx=-24
            dy=0
        else:
            dx=0
            dy=0
        if self.yakin_mi(oyuncu):
            if oyuncu.xcor()<self.xcor():
                self.direction="sola"
            elif oyuncu.xcor()>self.xcor():
                self.direction="saga"
            elif oyuncu.ycor()>self.ycor():
                self.direction="yukari"
            elif oyuncu.xcor()<self.xcor():
                self.direction="asagi"
                    
        move_to_x=self.xcor()+dx
        move_to_y=self.ycor()+dy
        if(move_to_x,move_to_y) not in duvarlar:
            self.goto(move_to_x,move_to_y)
#            self.direction=random.choice(["yukari","asagi","saga","sola"])
        else:
            self.direction=random.choice(["yukari","asagi","saga","sola"])
        
        turtle.ontimer(self.hareket_et,t=random.randint(100,300))
        
    def yok_et(self):
        self.goto(2000,2000)
        self.hideturtle()
    def yakin_mi(self,digeri):
        a=self.xcor()-digeri.xcor()
        b=self.ycor()-digeri.ycor()
        uzaklik=a**2+b**2
        if uzaklik<5500:
            return True
        else:
            return False

class Yem(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.shapesize(1/3,1/3)
        self.penup()
        self.speed(0)
        self.altin=100
        self.goto(x,y)
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
harita=["XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "XYYYYYYYYYYYYYXXYYYYYYYYYYYYYX",
        "XYYXXXYYXXXXYYXXYYXXXXYYXXXYYX",
        "XYYXXXYYXXXXYYXXYYXXXXYYXXXYYX",
        "XYYYYYYYYYYYYYYYYYYYYYYYYYYYYX",
        "XYYXXXYYXYYXXXXXXXXYYXYYXXXYYX",
        "XYYYYYYYXYYYYYXXYYYYYXYYYYYYYX",
        "XXXXXXYYXXXXYYXXDYXXXXYYXXXXXX",
        "     XYYXYYYYYD DYYYYXYYX     ",
        "XXXXXXYYXYYXXXXXXXXYYXYYXXXXXX",
        "YYYYYYYYYYYX      XYYYYYYYYYYY",
        "XXXXXXYYXYYXXXXXXXXYYXYYXXXXXX",
        "     XYYXYYYYY OYYYYYXYYX     ",
        "XXXXXXYYXYYXXXXXXXXYYXYYXXXXXX",
        "XYYYYYYYYYYYYYXXYYYYYYYYYYYYYX",
        "XYYXXXYYXXXXYYXXYYXXXXYYXXXYYX",
        "XYYYYXYYYYYYYYYYYYYYYYYYXYYYYX",
        "XXXYYXYYXYYXXXXXXXXYYXYYXYYXXX",
        "XYYYYYYYXYYYYYXXYYYYYXYYYYYYYX",
        "XYYXXXXXXXXXYYXXYYXXXXXXXXXYYX",
        "XYYYYYYYYYYYYYYYYYYYYYYYYYYYYX",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]
def labirent_ciz(harita):
    for y in range(len(harita)):
        for x in range(len(harita[y])):
            character=harita[y][x]
            screen_x=-288+(x*24)
            screen_y=288-(y*24)
            if character == "X":
                kalem.goto(screen_x,screen_y)
                kalem.stamp()
                duvarlar.append((screen_x,screen_y))
            if character == "O":
                oyuncu.goto(screen_x,screen_y)
            if character=="Y":
                yemler.append(Yem(screen_x,screen_y))
            if character=="D":
                dusmanlar.append(Dusman(screen_x,screen_y))
                
dusmanlar=[]
duvarlar=[]
yemler=[]
kalem=Kalem()
oyuncu=Oyuncu()
labirent_ciz(harita)
turtle.listen()
turtle.onkey(oyuncu.sola_git,"a")
turtle.onkey(oyuncu.saga_git,"d")
turtle.onkey(oyuncu.yukari_git,"w")
turtle.onkey(oyuncu.asagi_git,"s")

for dusman in dusmanlar:
    turtle.ontimer(dusman.hareket_et, t=250)


while True:
    for yem in yemler:
        if oyuncu.carpisti_mi(yem):
            oyuncu.altin+=yem.altin
            print("Oyuncunun Altin Miktari: {}".format(oyuncu.altin))
            yem.destroy()
            yemler.remove(yem)
    for dusman in dusmanlar:
        if oyuncu.carpisti_mi(dusman):
            print("Oyuncu kaybetti!")
    ekran.update()
