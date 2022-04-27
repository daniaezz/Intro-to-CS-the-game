#Music Library, Random Library, Path Library 
add_library('minim')
import random 
import os 

WIDTH = 1280
HEIGHT = 700
path = os.getcwd()
player = Minim(this)

class Spaceship:
    def __init__(self):
      self.img = loadImage(path + "/images/" + "spaceship.png")
      self.pew = loadImage(path + "/images/" + "pewpew.png") #Loads Spaceship Attack
      self.x = 200
      self.y = 200
      self.vy = 0 #y velocity of ship
      self.vx = 0 #x velocity of ship
      self.addedvx = 0 #added velocity if speedup purchased
      self.addedvy = 0
      self.px = 5 #attack velocity
      self.xshift = WIDTH/2 #parallax effect variable
      self.shift = False
      self.border = False
      self.border2 = False
      self.border3 = False #border collision with dimensions of screen
      self.pewlocx = self.x +10 #location of attack
      self.keyhandler = {UP: False, RIGHT: False, DOWN: False, LEFT: False, SHIFT: False} #key inpt         
      
    def move(self): #movement of ship
      if self.x < 0:
        self.vx = 0 
        self.border = True
      elif self.x > 0:
        self.border = False  
      if self.y < 0:
        self.vy = 0 
        self.border2 = True
      elif self.y > 0:
        self.border2 = False    
      if self.y > 499:
        self.vy = 0
        self.border3 = True
      elif self.y < 499:
        self.border3 = False       
      if self.keyhandler[RIGHT] == True and self.x < WIDTH//2:
        self.vx = 5 + self.addedvx
        self.vy = 0
      elif self.keyhandler[LEFT] == True and self.border == False:
        self.vx = -5 - self.addedvx
        self.vy = 0
        self.border = True
      elif self.keyhandler[UP] == True and self.border2 == False:
        self.vy = -5 - self.addedvy
        self.vx = 0
        self.border2 = False
      elif self.keyhandler[DOWN] == True and self.border3 == False:
        self.vy = 5 + self.addedvy
        self.vx = 0
        self.border3 = False
    
      self.y += self.vy
      self.x += self.vx
      
      if self.x >= WIDTH//2: #parallax effect
          self.vx = 0
          game.xshift = 5 + self.addedvx
          #print(str(game.xshift))
      elif self.x <= WIDTH//2:
          game.xshift = 0

    def display(self):
      self.move()
      image(self.img, self.x, self.y, 100, 100) #displays spaceship
      
class FinalBoss:
    def __init__(self, img, x,y, hearts): # x, y location of boss and health
        self.img = loadImage(path + "/images/" + img + ".png")
        self.x = x #(3*WIDTH) + 1000
        self.y = y
        self.bosshealth = []
        self.bossheart = loadImage(path + "/images/" + "bossHeart.png")
        for i in range (hearts):
            self.bosshealth.append(self.bossheart)
        
    def display(self, w, h):
        if self.x > WIDTH - 450:
            self.x = self.x - game.xshift
        image(self.img, self.x, self.y, w, h)
        if len(self.bosshealth)>15: #displays health in multiple rows
            for i in range(15):
                image(self.bosshealth[i], self.x + 30*i, 500, 25, 25)
            for i in range(len(self.bosshealth)-15):
                image(self.bosshealth[i], self.x + 30*i, 550, 25, 25)
        else: #displays health in one row
            for heart in range(len(self.bosshealth)):
                image(self.bosshealth[heart], self.x + 30*heart, 550, 25, 25)
        
class BattleshipAttac: #class for first boss attack
    def __init__(self):
        self.x = WIDTH - 225
        self.y = random.randint(150,400)
        self.img = loadImage(path + "/images/" + "battleAttack.png")
        self.vx = 5
        
    def displayattack(self):
        image(self.img, self.x, self.y, 50, 25)
        self.x -= self.vx

class Connect4Attac: #class for second boss attack
    def __init__(self, y):
        self.x = WIDTH - 225
        self.y = y
        self.imgRed = loadImage(path + "/images/" + "4rAttac.png")
        self.imgYellow = loadImage(path +"/images/4yattac.png")
        
        if random.randint(0,1) == 0: #alternates between yellow and red discs
            self.img = self.imgRed
        else:
            self.img = self.imgYellow
            
        self.vx = 5
        
    def displayattack(self):
        image(self.img, self.x, self.y, 40, 40)
        self.x -= self.vx

class SnekAttac: #class for third boss attack
    def __init__(self):
        self.x = WIDTH - 370
        self.y = random.randint(150,250)
        self.one = loadImage(path + "/images/" + "snekAttac.png") #image going straight
        self.two = loadImage(path + "/images/snekAttac2.png") #image going down
        self.three = loadImage(path + "/images/snekAttac3.png") #image going up
        self.vx = 5
        self.rand = random.randint(1,3)
        if self.rand ==1: #alternates between angle of attacks
            self.img = self.one
        elif self.rand ==2:
            self.img = self.two 
        else:
            self.img = self.three
    
    def displaySnekAttac(self):
        image(self.img,self.x, self.y,50,50)
        if self.rand == 1:
            self.x -= self.vx
        elif self.rand == 2:
            self.x -= random.randint(1,10)
            self.y += random.randint(1,10)
        else:
            self.x -= random.randint(1,10)
            self.y -= random.randint(1,10)
            
class FinalAttac: #class for fourth boss attack
    def __init__(self):
        self.x = WIDTH - 400
        self.y = random.randint(150, 400)
        self.uno = loadImage(path + "/images/" + "Fgrades.png")
        self.dos = loadImage(path + "/images/" + "assignment.png")
        self.tres = loadImage(path +"/images/" + "Fgrades.png")
        self.vx = 10 
        self.rand = random.randint(1,3)
        
    def displayFinalAttac(self): 
        if self.rand == 1:
            image(self.uno, self.x, self.y, 150, 150)
            self.x -= self.vx
        elif self.rand == 2:
            image(self.dos, self.x, self.y, 75, 75)
            self.x -= self.vx
        elif self.rand == 3:
            image(self.tres, self.x, self.y, 150, 150)
            self.x -= self.vx

class Attac: #class for spaceship attack
    def __init__(self,x,y):
        self.spaceship = Spaceship()
        self.x = x+100
        self.y = y+40
        self.img = loadImage(path+"/images/pewpew.png")
        self.vx = 8
        
    def displayAttac(self):
        image(self.img,self.x, self.y,50,30)
        self.x += self.vx

class Item: #superclass for items (bugs and kp)
    def __init__(self, img):
        self.img = loadImage(path + "/images/" + img + ".png")

class BugsBunny(Item):
    def __init__(self, x, y):
        Item.__init__(self, "bugs")
        self.x = x 
        self.y = y 
        
    def displayBug(self):
        self.x = self.x - game.xshift
        image(self.img, self.x, self.y, 50, 50)
           
class Knowledge(Item):
    def __init__(self, x, y):
        Item.__init__(self, "python")
        self.x = x 
        self.y = y 
        
    def displayKP(self):
        self.x = self.x - game.xshift
        image(self.img, self.x, self.y, 50, 50)

class Game:
    def __init__(self, w, h, ground, level, bugs, kp, begen):
        self.bgImage = loadImage(path+"/images/bg.png")
        self.beginimg = loadImage(path+"/images/"+"start.png")
        self.bg_sound = player.loadFile(path + "/sounds/bg.mp3")
        self.attacSound = player.loadFile(path + "/sounds/attack.mp3")
        self.bg_sound.loop()
        self.buying = player.loadFile(path + "/sounds/buying.mp3")
        self.winning = player.loadFile(path + "/sounds/win.mp3")
        self.damage = player.loadFile(path + "/sounds/takingDamage.mp3")
        self.inflicting = player.loadFile(path + "/sounds/inflictingDamage.mp3")        
        self.w = w
        self.h = h
        self.won = loadImage(path + "/images/gameWon.png")
        self.knowledge = kp
        self.begin = begen
        self.next = loadImage(path+ "/images/" + "next.png")
        self.buggy = bugs
        self.xshift = 0
        self.ground = ground
        self.level = level
        self.win = False
        self.hmeeting = False
        self.pmeeting = False
        self.bg = loadImage(path + "/images/" + "bg.png")
        self.end = loadImage(path+"/images/" +"end.jpg")
        self.spaceship = Spaceship()
        self.hazem = loadImage(path + "/images/" + "hazemZoom.png")
        self.potsch = loadImage(path + "/images/" + "ProfZoom.png")
        self.heartimg = loadImage(path + "/images/" + "heart.png")
        self.firstboss = FinalBoss("battleship", (3*WIDTH) + 1000, 150, 12)
        self.secondboss = FinalBoss("connect4", (3*WIDTH) + 2000, 150, 18)
        self.thirdboss = FinalBoss("snek", (3*WIDTH)+4000, 150, 25)
        self.fourthboss = FinalBoss("T_Hfinal", (3*WIDTH)+5000, 50, 30)
        self.icons = loadImage(path+"/images/icons.png")
        self.bcounter = 0 
        self.kcounter = 0
        self.ammo = 15 
        self.endgame = False
        self.kp = []
        self.bugs =[]
        self.attacs=[]
        self.health = []
        self.battleshipattack = []
        self.connect4attack = []
        self.snekattack= []
        self.finalattack = []
        for i in range (self.buggy):#number of bugs per level
            self.bugs.append(BugsBunny(random.randint(550, 3*WIDTH + ((self.level-1) * WIDTH)), random.randint(0, 500)))
        for n in range (self.knowledge): #number of kp per level
            self.kp.append(Knowledge(random.randint(550, 3*WIDTH + ((self.level-1) * WIDTH)), random.randint(0, 500)))
        for k in range(10): #health of spaceship
            self.health.append(self.heartimg)
            
    def display(self):
        #parallax effect
        x_shift = 0
        cnt = 0
        if cnt == 0:
            x_shift = self.xshift//4
        elif cnt == 1:
            x_shift = self.xshift//3
        elif cnt == 2:
            x_shift = self.xshift//2
        else:
            x_shift = self.xshift
        width_right = x_shift % self.w
        width_left = self.w - width_right
        image(self.bg, 0, 0, width_left, self.h, width_right, 0, self.w, self.h)
        image(self.bg, width_left, 0, width_right, self.h, 0, 0, width_right, self.h)
        cnt += 1
        myFont = createFont("PressStart2P-Regular",20)
        fill(0,0,0)
        if self.bcounter < 11: #first level condition if bugs are 10 or less
            if frameCount % 60 == 0 and self.firstboss.x <= WIDTH - 450 and self.level == 1:
                self.battleshipattack.append(BattleshipAttac())
        elif self.bcounter > 10:
            if frameCount % 30 == 0 and self.firstboss.x <= WIDTH - 450 and self.level == 1:
                self.battleshipattack.append(BattleshipAttac())
        if self.level == 1: #first level display of battleship attack and collision between boss attack and spaceship (repeats for next levels)
            for attac in self.battleshipattack:
                attac.displayattack()
                if dist(attac.x+25, attac.y+12.5, self.spaceship.x+50, self.spaceship.y+50)<60:
                    self.battleshipattack.remove(attac)
                    self.health.pop()
                    self.damage.play()
                    self.damage.rewind()
                    
        elif self.level == 2: 
            self.c4y = random.randint(150,400) # stands for connect4 y coordinate
            if self.bcounter < 8:
                if frameCount % 60 == 0 and self.secondboss.x <= WIDTH - 450:
                    for i in range(4):
                        self.connect4attack.append(Connect4Attac(self.c4y+i*50))
            elif self.bcounter > 8:
                if frameCount % 30 == 0 and self.secondboss.x <= WIDTH - 450:
                    for i in range(4):
                        self.connect4attack.append(Connect4Attac(self.c4y+i*50))
            
            for attac in self.connect4attack:
                attac.displayattack()
                if dist(attac.x+25, attac.y+12.5, self.spaceship.x+50, self.spaceship.y+50)<60:
                    self.connect4attack.remove(attac)
                    self.health.pop()
                    self.damage.play()
                    self.damage.rewind()
                    
        elif self.level == 3: 
            if self.bcounter < 6:
                if frameCount % 10 == 0 and self.thirdboss.x <= WIDTH - 450:
                    self.snekattack.append(SnekAttac())
            elif self.bcounter > 5:
                if frameCount % 2 == 0 and self.thirdboss.x <= WIDTH - 450:
                    self.snekattack.append(SnekAttac())

            for attac in self.snekattack:
                attac.displaySnekAttac()
                if dist(attac.x+25, attac.y+12.5, self.spaceship.x+50, self.spaceship.y+50)<60:
                    self.snekattack.remove(attac)
                    self.health.pop()
                    self.damage.play()
                    self.damage.rewind()
            
        elif self.level == 4:
            if self.bcounter > 0:
                if frameCount % 5 == 0 and self.fourthboss.x <= WIDTH - 450:
                    self.finalattack.append(FinalAttac())
            elif self.bcounter == 0:
                if frameCount % 25 == 0 and self.fourthboss.x <= WIDTH - 450:
                    self.finalattack.append(FinalAttac())
            for attac in self.finalattack:
                attac.displayFinalAttac()
                if dist(attac.x+75, attac.y+75, self.spaceship.x+50, self.spaceship.y+50)<85:
                    self.finalattack.remove(attac)
                    self.health.pop()
                    self.damage.play()
                    self.damage.rewind()

        self.spaceship.display()
        
        for bug in self.bugs: #displays bugs and collision between bugs and spaceship
            bug.displayBug()
            if frameCount % 12 == 0 and dist(bug.x + 25, bug.y + 25, self.spaceship.x + 50, self.spaceship.y + 50) < 60:
                self.bcounter += 1
                self.bugs.remove(bug)
                if self.bcounter % 2 == 0:
                    self.health.pop()
                    self.damage.play()
                    self.damage.rewind()
                    
        for kp in self.kp: #displays kp and collision between kp and spaceship
            kp.displayKP()
            if frameCount % 12 == 0 and dist(kp.x + 25, kp.y + 25, self.spaceship.x + 50, self.spaceship.y + 50) < 60:
                self.kcounter += 5
                self.kp.remove(kp)
        
        if self.spaceship.keyhandler[SHIFT] == True and frameCount % 10 ==0 and self.ammo > 0: #spaceship attack
            self.attacSound.play()
            self.attacSound.rewind()
            self.attacs.append(Attac(self.spaceship.x, self.spaceship.y))
            self.ammo -= 1
            
        if self.level == 1: #first level collision between your attack and final boss, repeats for every level
            for i in self.attacs:
                i.displayAttac()
                if dist(i.x+25,i.y+15, self.firstboss.x+225, self.firstboss.y+225)<70 or dist(i.x+25,i.y+15, self.firstboss.x+225, self.firstboss.y+75)<100:
                    self.attacs.remove(i)
                    self.firstboss.bosshealth.pop()
                    self.inflicting.play()
                    self.inflicting.rewind()
        elif self.level == 2:
            for i in self.attacs:
                i.displayAttac()
                if dist(i.x+25,i.y+15, self.secondboss.x+225, self.secondboss.y+150)<250:
                    self.attacs.remove(i)
                    self.secondboss.bosshealth.pop()
                    self.inflicting.play()
                    self.inflicting.rewind()
        elif self.level ==3:
            for i in self.attacs:
                i.displayAttac()
                if dist(i.x+25,i.y+15, self.thirdboss.x+225, self.thirdboss.y+150)<250:
                    self.attacs.remove(i)
                    self.thirdboss.bosshealth.pop()
                    self.inflicting.play()
                    self.inflicting.rewind()
        elif self.level ==4:
            for i in self.attacs:
                i.displayAttac()
                if dist(i.x+25,i.y+15, self.fourthboss.x+250, self.fourthboss.y+250)<200:
                    self.attacs.remove(i)
                    self.fourthboss.bosshealth.pop()
                    self.inflicting.play()
                    self.inflicting.rewind()
        fill(132, 132, 132)
        strokeWeight(0)
        #image(self.bg, 0,0,1280,700)
        rect(0, self.ground, self.w, self.h)
        fill(0,0,0)
        image(self.icons,790,self.ground, WIDTH-790, HEIGHT-self.ground)
        rect(450, self.ground, 10, HEIGHT-self.ground)
        rect(780, self.ground, 10, HEIGHT-self.ground)
        text("INTRO TO CS:", 500, self.ground+50)
        text("THE GAME",540, self.ground+85)
        fill(0,0,0)
        text("HP:",50,625)
        textFont(myFont)
        text("Bugs:" + str(self.bcounter), 200,655)
        text("KP:" + str(self.kcounter), 50,655)
        text("Energy:", 50, 685)
        strokeWeight(0)
        rect(185,663, 150, 25)
        fill(113,189,107)
        rect(185,663, 10*self.ammo, 25)
        for heart in range(len(self.health)): #displays your health
            image(self.health[heart], 125+30*heart, 600, 25, 25)
            
        if self.level == 1: #displays final boss, repeats every level
            self.firstboss.display(450, 300)
        elif self.level == 2:
            self.secondboss.display(300, 450)
        elif self.level ==3:
            self.thirdboss.display(300,300)
        elif self.level == 4:
            self.fourthboss.display(500,500)

        if key == 'h' or key == 'H': #Hazem meeting 
            image(self.hazem, 0, 0, 1280, 700)
            for heart in range(len(self.health)):
                image(self.health[heart], 325+25*heart, 660, 25, 25)
            fill(255,255,255)
            text("HP:", 250,685)
            text("KP:" + str(self.kcounter), 750, 685)
            text("Bugs:"+ str(self.bcounter), 900, 685)
            self.hmeeting = True
        if key == 'p' or key == 'P': #Professor Potsch Meeting
            image(self.potsch, 0, 0, 1280, 700)
            fill(255,255,255)
            text("KP:" + str(self.kcounter), 750, 685)
            text("Energy:", 250, 685)
            fill(113,189,107)
            rect(390, 663, 10*self.ammo, 25)
            self.pmeeting = True
        if (key == 'x' or key == 'X') and self.hmeeting == True and self.kcounter > 9 and len(self.health) < 10: #Health
            self.buying.play()
            self.buying.rewind()
            self.health.append(self.heartimg)
            self.kcounter -= 10
            self.hmeeting = False
        if (key == 't' or key == 'T') and self.hmeeting == True and self.kcounter > 49: #Debug
            self.buying.play()
            self.buying.rewind()
            self.hmeeting = False
            self.bcounter -= 1
            self.kcounter -= 50
        if (key == 'e' or key == 'E') and self.pmeeting == True and self.kcounter > 19 and self.ammo < 20: #Energy
            self.buying.play()
            self.buying.rewind()
            self.ammo += 4
            self.kcounter -= 20
            self.pmeeting = False
        if (key == 's' or key == 'S') and self.pmeeting == True and self.kcounter > 29: #Powerup
            self.buying.play()
            self.buying.rewind()
            self.spaceship.addedvx = 3
            self.spaceship.addedvy = 3
            self.kcounter -= 30
            self.pmeeting = False
        if len(self.health) == 0: #Ends game if no health
            image(self.end, 0, 0, WIDTH, HEIGHT)
            noLoop()
            self.endgame = True
        if len(self.firstboss.bosshealth) == 0 or len(self.secondboss.bosshealth) == 0 or len(self.thirdboss.bosshealth) == 0: #advances game if you win against first, second or third boss
            background(0,255,0)
            self.winning.play()
            self.winning.rewind()
            image(self.next, 0, 0, WIDTH, HEIGHT)
            self.win = True
            self.level += 1
            self.bg_sound.pause()
            noLoop()
        if self.ammo == 0 and self.kcounter == 0: #ends game if you have no ammo and no kp
            image(self.end, 0, 0, WIDTH, HEIGHT)
            self.endgame = True
            noLoop()
        if self.kcounter < 20 and self.ammo == 0: #ends game if you do not have enough kp to purchase ammo
            image(self.end, 0, 0, WIDTH, HEIGHT)
            self.endgame = True
            noLoop()
        if len(self.fourthboss.bosshealth) == 0: #ends game if you win it all
            image(self.won, 0, 0, WIDTH, HEIGHT)
            noLoop()

        if self.begin == True: #displays start screen
            image(self.beginimg, 0, 0, 1280, 700)

game = Game(1280, 700, 585, 1, 30, 50, True) #initializes game

def setup():
  size(WIDTH, HEIGHT)
  background(0,0,0)

def draw():
    background(0,0,0)
    game.display()

def keyPressed():
    if keyCode == LEFT:
        game.spaceship.keyhandler[LEFT] = True
    elif keyCode == RIGHT:
        game.spaceship.keyhandler[RIGHT] = True
    elif keyCode == UP:
        game.spaceship.keyhandler[UP] = True
    elif keyCode == DOWN:
        game.spaceship.keyhandler[DOWN] = True
    elif keyCode == SHIFT:
        game.spaceship.keyhandler[SHIFT] = True

    
def keyReleased():
    if keyCode == LEFT:
        game.spaceship.keyhandler[LEFT] = False
    elif keyCode == RIGHT:
        game.spaceship.keyhandler[RIGHT] = False
    elif keyCode == UP:
        game.spaceship.keyhandler[UP] = False
    elif keyCode == DOWN:
        game.spaceship.keyhandler[DOWN] = False
    elif keyCode == SHIFT:
        game.spaceship.keyhandler[SHIFT] = False
        
def mouseClicked():
    if game.begin == True: #starts game if mouse clicked
        game.begin = False
    if game.endgame == True: #ends game and repeats from the beginning if lost
        game.__init__(WIDTH, HEIGHT, 585, 1, 20, 50, False)
        loop()
    if game.win == True and game.level == 2: #advances to next level, repeats every level
        game.__init__(WIDTH, HEIGHT, 585, 2, 35, 70, False)
        loop()
    if game.win == True and game.level == 3:
        game.__init__(WIDTH, HEIGHT, 585, 3, 45, 80, False)
        loop()
    if game.win == True and game.level == 4:
        game.__init__(WIDTH, HEIGHT, 585, 4, 60, 100, False)
        loop()

        
        
        
