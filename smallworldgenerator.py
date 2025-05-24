import turtle, random

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()
t.speed(100)
i = 1
i2 = 100
blue = "#08D9F1"
green = "#1AAD27"
brown = "#714E0C"
tree = "#18710C"
roadGrey = "#212020"
cloudColourNum = 0
on = True
rco1 = 0
rco2 = 0
addToLog = 0 #When you come back add the save list .append to the draweing features for clouds, lakes and trees.
village = False
sun = False
numberSelector = 0
villageRoads = 20
villagePercent = 0
treeAmmount = 1
treePercent = 0
cLight = 0
cModerate = 0
cDark = 0
cOverall = 0
weather = 0
placeholder = 9999
rangeLower = 0
rangeUpper = 0
maxLoggerCoordinates = 50
maxTries = 0
degreesList = [0,90,180,270,360]
treeList = ["Tree","tree","T","t"]
grassList = ["Grass","grass","Ground","ground","G","g"]
skyList = ["Sky","sky","S","s"]
cloudList = ["Cloud","cloud","C","c"]
randomList = ["Random","random","R","r"]
choiceList = ["Configure","configure","Co","co","CO","cO"]
villageList = ["Village","village","V","v"]
testList = ["Test","test","T","t"]
hotAirOptions = ["ho","Ho","HO","hO"]
weatherList = ["Cloudy", "Rainy", "Stormy"]
sunList = ["Sun","sun","su","Su","sU","SU","Moon","moon","M","m"]
lakeList = ["Lake","lake","L","l"]
cloudColourList = ["#B8BBC3","#989BA0","#77787B"]
skyShadeList = ["#08D9F1","#096DF2"]
canvasSkyRange1 = 0
canvasSkyRange2 = 460
canvasGroundRange1 = -460
canvasGroundRange2 = 0
lakeRange1 = -410
lakeRange2 = -50
cloudListW: list[int] = []
villagePercentList = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
treePercentList = [20,40,60,80,100]
PositionListX: list[int] = []
PositionListY: list[int] = []
villagePositionListX: list[int] = []
villagePositionListY: list[int] = []
saveList: list[int] = []
saveListOptions = ["Save","save"]
loadListOptions = ["Load","load"]
checkerX: bool = False  # Initialize checkerX as a global variable
checkerY: bool = False
checkerY = True
default = "\033[0m"
black = "\033[30m"
red = "\033[31m"
greent = "\033[32m"
yellow = "\033[33m"
bluet = "\033[34m"
purplet = "\033[35m"
cyan = "\033[36m"
whitet = "\033[37m"
devCode = "swg24"
devCodeInput = "N/A"
treeID = 10000
cloudID = 10001
lakeID = 10002
hotAirID = 10003
sunID = 10004
sunTrueID = 10005
skyID = 10006
moonID = 10007
cLightPc = 0
sunOrMoon = 0

def XcheckL():
 global rangeLower
 global rangeUpper
 global checkerX
 print("Checking X Coordinates.")
 for item in PositionListX:
  rangeLower = item - 50
  rangeUpper = item + 50
  if rangeLower <= rco1 <= rangeUpper:
   print("The lake coordinates are on the same X as another lake.")
   checkerX = True
   #drawLake()
  else:
   continue

def YcheckL():
 global rangeUpper
 global rangeLower
 global checkerY
 print("Checking Y coordinates.")
 for item in PositionListY:
  rangeLower = item - 50
  rangeUpper = item + 50
  if rangeLower <= rco1 <= rangeUpper:
   print("The lake coordinates are on the same Y as another lake.")
   checkerY = True
   #drawLake()
  else:
   continue

def XcheckT():
  print("Checking X Coordinates.")
  for item in PositionListX:
    global checkerX
    if rco1 == item:
      print("The tree is on the same X as another object")
      checkerX = True
    else: 
      continue

def YcheckT():
  print("Checking Y coordinates.")
  for item in PositionListY:
    if rco2 == item:
      global checkerY
      print("The tree is on the same Y as another object")
      checkerY = True
    else:
      continue

def XcheckV(): #For next time work out why this isn't working and maybe start working on houses.
 global villagePositionListX
 global checkerX
 print("Checking X coordinates...")
 for item in villagePositionListX:
  if rco1 == item:
    print("Could clash on X axis.")
    checkerX = True
  else:
   continue


def YcheckV():
 global villagePositionListY
 global checkerY
 print("Checking Y coordinates...")
 for item in villagePositionListY:
  if rco2 == item:
    print("Could clash on the Y axis.")
    checkerY = True
  else:
   continue


def drawLand():
 #i = 10
 t.setpos(0,0)
 print("Drawing land...")
 t.setheading(0)
 t.pendown()
 t.color(green)
 t.forward(500)
 t.backward(1000)
 t.pensize(10)
 t.forward(1000)
 for i in range (1,26):
  t.color(green)
  t.pensize(10)
  
  t.right(90)
  t.forward(10)
  t.left(90)
  t.backward(1000)
  t.right(90)
  t.forward(10)
  t.left(90)
  t.forward(1000)



 t.setpos(0,0)
 t.color("black")
 print("Land Complete")

def drawSky():
 global sunOrMoon
 i = 1
 skyShadeNum = 0
 t.setpos(0,0)
 print("Drawing sky...")
 t.setheading(0)
 t.pendown()
 skyShadeNum = random.randint(0,1)
 sunOrMoon = skyShadeNum
 t.color(skyShadeList[skyShadeNum])
 saveList.insert(0,skyID)
 saveList.insert(1,skyShadeNum) #For next time create a moon object and have the moon show when the sky is dark and the sun show when the sky is light. Make is so there is only one prompt and the game decides weather theres a sun or moon.
 t.forward(500)
 t.backward(1000)
 t.pensize(10)
 t.forward(1000)
 for i in range (1,26):
   t.color(skyShadeList[skyShadeNum])
   t.pensize(10)

   t.right(-90)
   t.forward(10)
   t.left(-90)
   t.backward(1000)
   t.right(-90)
   t.forward(10)
   t.left(-90)
   t.forward(1000)

 t.setpos(0,0)
 t.color("black")
 print("Sky Complete")

def drawTrees():
  global checkerY
  global checkerX
 #for i in range(0,treeAmmount):
  print("Drawing tree...")
  t.penup()
  t.color(green)
  t.pensize(10)
  rco1 = random.randint(-500,500)
  rco2 = random.randint(canvasGroundRange1,canvasGroundRange2)
  XcheckT()
  YcheckT()
  if checkerX == True and checkerY == True:
    print("The coordinates clash. Relocating...")
    resetChecker()
    drawTrees()
   
    
  else:
 
   t.goto(rco1,rco2)

   saveList.append(treeID)
   saveList.append(rco1)
   saveList.append(rco2)

   t.setheading(0)
   t.pendown()
   treePercent = treePercentList[0]
   print(treePercent,"%")
   t.color(brown)
   t.left(90)
   t.forward(10)
   treePercent = treePercentList[1]
   print(treePercent,"%")
   t.right(90)
   t.color(tree)
   t.forward(5)
   treePercent = treePercentList[2]
   print(treePercent,"%")
   t.backward(10)
   t.forward(5)
   t.right(90)
   treePercent = treePercentList[3]
   print(treePercent,"%")
   t.backward(5)
   t.hideturtle()
   t.penup()
   treePercent = treePercentList[4]
   print(treePercent,"%")
   t.setpos(0,0)
   print("Tree Complete")

def drawVillage():
  global villageRoads  # Add this line to indicate that villageRoads is a global variable
  global checkerX
  global checkerY
  numberSelectorV = random.randint(0, 4)
  roadTurn = degreesList[numberSelectorV]
  forwardAmmountV = 0
  t.penup()
  rco1 = random.randint(-150, 150)
  rco2 = random.randint(-150, -1)
  villagePositionListX.append(rco1)
  villagePositionListY.append(rco2)
  t.goto(rco1, rco2)
  t.color(roadGrey)
  t.pensize(10)
  t.pendown()
  t.setheading(roadTurn)
  forwardAmmountV = 0 #random.randint(50,120)
  t.forward(forwardAmmountV)
  XcheckV()
  YcheckV()
  if checkerX == True and checkerY == True:
   print("Coordinates clash with another road, redrawing...")
   resetChecker()
   drawVillage()
  else:
   if numberSelectorV == 0:
    villagePositionListX.append(rco1+forwardAmmountV)
    print(villagePositionListX)
   elif numberSelectorV == 1:
    villagePositionListY.append(rco2+forwardAmmountV)
    print(villagePositionListY)
   elif numberSelectorV == 2:
    villagePositionListX.append(rco1-forwardAmmountV)
    print(villagePositionListX)
   elif numberSelectorV == 3:
    villagePositionListY.append(rco2-forwardAmmountV)
    print(villagePositionListX)
   elif numberSelectorV == 4:
    villagePositionListX.append(rco1+forwardAmmountV)
   print(PositionListX)
   for i in range(0,villageRoads):
      numberSelectorV = random.randint(0, 4)
      roadTurn = degreesList[numberSelectorV]
      t.color(roadGrey)
      t.pensize(10)
      t.pendown()
      t.setheading(roadTurn)
      forwardAmmountV = 0 #random.randint(50,120)
      t.forward(forwardAmmountV)
      villageRoads -= 1
      villagePercent = villagePercentList[i]
      print(villagePercent,"%")
      if numberSelectorV == 0:
       villagePositionListX.append(rco1+forwardAmmountV)#HUGE ISSUE!: This code will do the first random coordinate + the forward ammount forever, change this so that it adds it to the new coordinates.
       print(villagePositionListX)
      elif numberSelectorV == 1:
       villagePositionListY.append(rco2+forwardAmmountV)
       print(villagePositionListY)
      elif numberSelectorV == 2:
       villagePositionListX.append(rco1-forwardAmmountV)
       print(villagePositionListX)
      elif numberSelectorV == 3:
       villagePositionListY.append(rco2-forwardAmmountV)
       print(villagePositionListX)
      elif numberSelectorV == 4:
       villagePositionListX.append(rco1+forwardAmmountV)
       print(PositionListX)
 

def drawCloud():
  print("Drawing Cloud...")
  t.penup()
  cloudColourNum = random.randint(0,2)
  t.pendown
  print(cloudColourNum)
  t.color(cloudColourList[cloudColourNum])
  t.pensize(10)
  cloudListW.append(cloudColourNum)
  print("Added to weather decider. (To find current status of weather type in wstatus.)")
  rco1 = random.randint(-500,500)
  rco2 = random.randint(canvasSkyRange1,canvasSkyRange2)
  t.goto(rco1,rco2)

  saveList.append(cloudID)
  saveList.append(rco1)
  saveList.append(rco2)
  saveList.append(cloudColourNum)

  t.setheading(0)
  t.pendown()
  t.forward(15)
  t.pendown
  t.pendown
  t.forward(60)
  t.right(90)
  t.forward(5)
  t.left(90)
  t.forward(15)
  t.right(90)
  t.forward(15)
  t.right(90)
  t.forward(75)
  t.right(90)
  t.forward(15)
  t.right(180)
  t.forward(10)
  t.left(90)
  t.forward(75)
  t.left(90)
  t.forward(5)
  t.left(90)
  t.forward(75)

def drawLake():
 global checkerX
 global checkerY
 global maxTries
 if maxTries == 3:
  print("Max tries reached, please try again.")
  return
 else:
  print("Drawing Lake...")
  rco1 = random.randint(-500,500)
  rco2 = random.randint(lakeRange1,lakeRange2)
  XcheckL()
  YcheckL()
  if checkerX == True and checkerY == True:
   print("Coordinates clash. Redrawing...")
   resetChecker()
   return
  else:
   print("Coordinates do not clash.")
   PositionListX.append(rco1)
   PositionListX.append(placeholder) #placeholder to split the data in the list
   PositionListY.append(rco2)
   PositionListY.append(placeholder) #placeholder to split the data in the list
   print("Object position added to list.")
   print("X List data: ",PositionListX)
   print("Y List data: ",PositionListY)
   t.penup()
   t.goto(rco1,rco2)
    
   saveList.append(lakeID)
   saveList.append(rco1)
   saveList.append(rco2)

   t.pendown()
   t.color("#0074F0")
   t.pensize(10)
   t.forward(40)
   t.right(90)
   t.forward(40)
   t.right(90)
   t.forward(40)
   t.right(90)
   t.forward(40)
   t.back(10)
   t.right(90)
   t.forward(40)
   t.right(90)
   t.forward(10)
   t.right(90)
   t.forward(40)
   t.left(90)
   t.forward(10)
   t.left(90)
   t.forward(40)
   t.forward(40)
   t.right(90)
   t.forward(40)
   t.right(90)
   t.forward(50)
   t.right(90)
   t.forward(40)
   t.right(90)
   t.forward(50)
   #fill square 2
   t.right(90)
   t.forward(10)
   t.right(90)
   t.forward(50)
   t.left(90)
   t.forward(10)
   t.left(90)
   t.forward(50)
   t.right(90)
   t.forward(10)
   t.right(90)
   t.forward(50)
   t.penup()
   t.color("black")

def drawHotAir():
 
 rco1 = random.randint(-500,500)
 rco2 = random.randint(canvasSkyRange1,canvasSkyRange2)

 saveList.append(hotAirID)
 saveList.append(rco1)
 saveList.append(rco2)
 #balloon outline
 t.penup()
 t.goto(rco1,rco2)
 t.pensize(5)
 t.pendown()
 t.setheading(0)
 t.forward(30)
 t.setheading(270)
 t.forward(35)
 t.setheading(180)
 t.forward(30)
 t.setheading(90)
 t.forward(35)

#Ropes attaching to the basket

 t.setheading(270)
 t.penup()
 t.forward(35)
 t.setheading(0)
 t.forward(10) #change this for indentation of rope lines
 t.pensize(3)
 t.pendown()
 t.setheading(270)
 t.forward(20) 
 t.setheading(90)
 t.penup()
 t.forward(20)
 t.setheading(0)
 t.forward(10) #and this can be changed for rope lines indent
 t.setheading(270)
 t.pendown()
 t.forward(20)
 t.pensize(5)
 t.setheading(0)
 
 #basket outline
 t.forward(5)
 t.setheading(180)
 t.forward(20)
 t.setheading(270)
 t.forward(20)
 t.setheading(0)
 t.forward(20)
 t.setheading(90)
 t.forward(20)
 t.penup()
 t.goto(rco1,rco2)
 
 #filling balloon

 t.setheading(270)
 t.color("green")
 t.pendown()
 t.forward(35) #stripe 1 
 
 t.penup()
 t.setheading(0)
 t.forward(5)
 t.color("red")#5.5 dead centre
 t.pendown()
 t.setheading(90)
 t.forward(35) #stripe 2

 t.penup()
 t.setheading(180)
 t.forward(2.25)
 t.setheading(270)
 t.pensize(2)
 t.color("white")
 t.pendown()
 t.forward(35)#small stripe 1

 t.penup()
 t.goto(rco1,rco2)
 t.setheading(0)
 t.forward(10)
 t.pensize(5)
 t.setheading(270)
 t.color("green")
 t.pendown()
 t.forward(35) #stripe 3
 
 t.penup()
 t.setheading(180)
 t.forward(2.25)
 t.setheading(90)
 t.pensize(2)
 t.color("white")
 t.pendown()
 t.forward(35)#small stripe 2

 t.penup()
 t.goto(rco1,rco2)
 t.setheading(0)
 t.forward(15)
 t.setheading(270)
 t.pensize(5)
 t.color("red")
 t.pendown()
 t.forward(35) #stripe 3

 t.penup()
 t.setheading(180)
 t.forward(2.25)
 t.setheading(90)
 t.pensize(2)
 t.color("white")
 t.pendown()
 t.forward(35)#small stripe 3

 t.penup()
 t.goto(rco1,rco2)
 t.setheading(0)
 t.forward(20)
 t.setheading(270)
 t.pensize(5)
 t.color("green")
 t.pendown()
 t.forward(35) #stripe 4

 t.penup()
 t.setheading(180)
 t.forward(2.25)
 t.setheading(90)
 t.pensize(2)
 t.color("white")
 t.pendown()
 t.forward(35)#small stripe 4

 t.penup()
 t.goto(rco1,rco2)
 t.setheading(0)
 t.forward(25)
 t.setheading(270)
 t.pensize(5)
 t.color("red")
 t.pendown()
 t.forward(35) #stripe 5

 t.penup()
 t.setheading(180)
 t.forward(2.25)
 t.setheading(90)
 t.pensize(2)
 t.color("white")
 t.pendown()
 t.forward(35)#small stripe 5

 t.penup()
 t.goto(rco1,rco2)
 t.setheading(0)
 t.forward(30)
 t.setheading(270)
 t.pensize(5)
 t.color("green")
 t.pendown()
 t.forward(35) #stripe 6

 t.penup()
 t.setheading(180)
 t.forward(2.25)
 t.setheading(90)
 t.pensize(2)
 t.color("white")
 t.pendown()
 t.forward(35)#small stripe 6

 #coloring ropes

 t.penup()
 t.goto(rco1,rco2)
 t.setheading(270)
 t.forward(35)
 t.setheading(0)
 t.forward(10)
 t.setheading(270)
 t.pensize(3)
 t.color("brown")
 t.pendown()
 t.forward(20)
 t.penup()
 t.setheading(90)
 t.forward(20)
 t.setheading(0)
 t.forward(10)
 t.setheading(270)
 t.pendown()
 t.forward(20)
 t.penup()
 
 #filling basket
 
 t.setheading(0)
 t.forward(5)
 t.pensize(5)
 t.setheading(270)
 t.color("brown")
 t.pendown()
 t.forward(20)
 t.penup()
 t.setheading(180)
 t.forward(5)
 t.setheading(90)
 t.color("brown")
 t.pendown()
 t.forward(20)
 t.penup()
 t.setheading(180)
 t.forward(5)
 t.setheading(270)
 t.color("brown")
 t.pendown()
 t.forward(20)
 t.penup()
 t.setheading(180)
 t.forward(5)
 t.setheading(90)
 t.color("brown")
 t.pendown()
 t.forward(20)
 t.penup()
 t.setheading(180)
 t.forward(5)
 t.setheading(270)
 t.color("brown")
 t.pendown()
 t.forward(20)
 t.penup()
 t.setheading(180)
 t.forward(5)
 t.setheading(90)
 t.color("brown")
 t.pendown()
 t.penup()

def drawSun():
 global sunOrMoon
 global sun
 sun = True
 rco1 = random.randint(-500,450)#change this to -450,500 if the sun goes off of the canvas. 
 rco2 = random.randint(150,450)
 if sunOrMoon == 0:
  sunSize = 50
  t.pensize(5)
  t.penup()
  t.goto(rco1,rco2)
  t.color("#F77C00")
  t.pendown()
  t.forward(sunSize)
  t.setheading(270)
  t.forward(sunSize)
  t.setheading(180)
  t.forward(sunSize)
  t.setheading(90)
  t.forward(sunSize)
  t.penup()
  t.pensize(10)
  t.color("#F7A400")
  t.goto(rco1+5,rco2-5)
  t.pendown()
  t.setheading(0)
  t.forward(sunSize-10)
  t.setheading(270)
  t.forward(sunSize-10)
  t.setheading(180)
  t.forward(sunSize-10)
  t.setheading(90)
  t.forward(sunSize-10)
  t.penup()
  t.goto(rco1+12.5,rco2-12.5)
  t.color("#F7C100")
  t.pendown()
  t.setheading(0)
  t.forward(sunSize-25)
  t.setheading(270)
  t.forward(sunSize-25)
  t.setheading(180)
  t.forward(sunSize-25)
  t.setheading(90)
  t.forward(sunSize-25)
  t.penup()
  t.goto(rco1+20,rco2-20)
  t.color("#EAC74A")
  t.setheading(0)
  t.pendown()
  t.forward(sunSize-40) #0 is a placeholder
  t.setheading(270)
  t.forward(sunSize-40)
  t.setheading(180)
  t.forward(sunSize-40)
  t.setheading(90)
  t.forward(sunSize-40)
  t.penup()
  t.pensize(10)

  saveList.append(sunID)
  saveList.append(rco1)
  saveList.append(rco2)
  saveList.append(sunTrueID)
 elif sunOrMoon == 1:

  

  sunSize = 50
  t.pensize(5)
  t.penup()
  t.goto(rco1,rco2)
  t.color("#808080")
  t.pendown()
  t.forward(sunSize)
  t.setheading(270)
  t.forward(sunSize)
  t.setheading(180)
  t.forward(sunSize)
  t.setheading(90)
  t.forward(sunSize)
  t.penup()
  t.pensize(10)
  t.color("#8f8d8d")
  t.goto(rco1+5,rco2-5)
  t.pendown()
  t.setheading(0)
  t.forward(sunSize-10)
  t.setheading(270)
  t.forward(sunSize-10)
  t.setheading(180)
  t.forward(sunSize-10)
  t.setheading(90)
  t.forward(sunSize-10)
  t.penup()
  t.goto(rco1+12.5,rco2-12.5)
  t.color("#aba9a9")
  t.pendown()
  t.setheading(0)
  t.forward(sunSize-25)
  t.setheading(270)
  t.forward(sunSize-25)
  t.setheading(180)
  t.forward(sunSize-25)
  t.setheading(90)
  t.forward(sunSize-25)
  t.penup()
  t.goto(rco1+20,rco2-20)
  t.color("#d1cfcf")
  t.setheading(0)
  t.pendown()
  t.forward(sunSize-40) #0 is a placeholder
  t.setheading(270)
  t.forward(sunSize-40)
  t.setheading(180)
  t.forward(sunSize-40)
  t.setheading(90)
  t.forward(sunSize-40)
  t.penup()

  saveList.append(moonID)
  saveList.append(rco1)
  saveList.append(rco2)
  saveList.append(sunTrueID)


def resetChecker():
  global checkerX
  global checkerY
  checkerX = False
  checkerY = False


 # COMPLETED Continue from here next time, try to work out why the logger isn't working properly and also try to fix the tree relocating issue from last time. (For the lake system make it +50 to the rco1 and log each coordinate between that and do the same with -50. Also make sure that the point you are starting the logging from is at the centre of the lake and not off to the side where the origin of the turtle is.)

#drawLand()
#drawSky()
#drawTrees()
print(black,"Generate world with",greent,"Trees",whitet,"Clouds",greent,"Grass",bluet,"Sky","Lakes",whitet,"Hot Air Balloons",black,"&",red,"the Sun",default)



while on == True:
 choice = input("\033[30m Generate object> \033[0m")
 if choice in treeList:
  drawTrees()
  drawTrees()
  drawTrees()
  drawTrees()
  drawTrees()

 elif choice in cloudList:
  print("Drawing Clouds...")
  drawCloud()
  drawCloud()
  drawCloud()
  drawCloud()
  drawCloud()
 elif choice in grassList:
  drawLand()
 elif choice in skyList:
  drawSky()
 elif choice in randomList:
  drawLand()
  drawSky()
  drawSun()
  drawTrees()
  drawTrees()
  drawTrees()
  drawTrees()
  drawTrees()
  drawCloud()
  drawCloud()
  drawCloud()
  drawCloud()
  drawCloud()
  drawCloud()
  drawCloud()
  drawCloud()
  drawLake()
  drawLake()
  drawLake()
  drawHotAir()
  drawHotAir()
 elif choice in choiceList: #For next time make this a choice list rather than a random list and then make a new random list for people who still want randomly generated worlds.
   treeNumberChoice = 0
   lakeNumberCHoice = 0
   print("Preparing world canvas...")
   drawLand()
   drawSky()
   print("World canvas ready.")
   treeNumberChoice = int(input("How many trees would you like (Must be an integer)?> "))
   if isinstance(treeNumberChoice,int):
    print("Succesful")
    for i in range(0,treeNumberChoice):
      drawTrees()
    lakeNumberChoice = int(input("How many lakes would you like in your world(Type 0 for none)?"))
    if isinstance(lakeNumberChoice,int):
     print("Successful")
     for i in range(0,lakeNumberChoice):
      drawLake()
     cloudNumberChoice = int(input("How many clouds would you like?> "))
     if isinstance(cloudNumberChoice,int):
      print("Successful.")
      for i in range(0,cloudNumberChoice):
       drawCloud()
     elif isinstance(cloudNumberChoice,str):
      print("Not an acceptable input.")
    elif isinstance(treeNumberChoice,str):
     print("That is not an acceptable number.")

   elif isinstance(treeNumberChoice,str):
    print("That is not an integer.")

 elif choice in villageList and village == False:
  village = True
  devCodeInput = input("Because this feature is under development and can ruin your world input the developer code> ")
  if devCodeInput == devCode:
   print("Drawing Village...")
   drawVillage()
  else:
   print("Incorrect")

 elif choice in lakeList:
  print("Drawing Lake...")
  drawLake()

 elif choice in sunList:
  if sun == False:
   print("Drawing Sun...")
   drawSun()
  else:
   print("You already have a Sun in your world.")
 elif choice == "wstatus":
  print("Compiling Weather Data...")
  cLight = cloudListW.count(0)
  cModerate = cloudListW.count(1)
  cDark = cloudListW.count(2)
  print("Cloud database compile completed.")
  print("Starting weather calculations...")
  allCloudsNum = cLight + cModerate + cDark
  cLightPc = float((cLight / allCloudsNum)*100)
  cModeratePc = float((cModerate / allCloudsNum)*100)
  cDarkPc = float((cDark / allCloudsNum)*100)
  print("Light: ",cLightPc) 
  print("Moderate: ",cModeratePc)
  print("Dark: ", cDarkPc)
  if cLightPc >= cModeratePc and cLightPc >= cDarkPc:
   print("The weather is Cloudy.")

  elif cModeratePc >= cLightPc and cModeratePc >= cDarkPc:
   print("The weather is Rainy.")

  elif cDarkPc >= cLightPc and cDarkPc >= cModeratePc:
   print("The weather is Stormy.")
  else:
   print("The weather could not be decided. Add more clouds and try again.")
 elif choice in hotAirOptions:
  print("Drawing Hot Air Balloon...")
  drawHotAir()
 elif choice in saveListOptions:
   print(*saveList, sep=', ')
 elif choice in loadListOptions:
  print("Preparing to load a world...")
  drawLand()


  saveCode = input("What is your save code (Paste here)?> ")
  saveCodeStr: list = saveCode.split(",")
  loadList = [int(item) for item in saveCodeStr]
  print("String List: ",saveCodeStr)
  print("")
  print("Int list: ",loadList)

  
  i = 1
  skyShadeNum = 0
  t.setpos(0,0)
  print("Drawing sky...")
  t.setheading(0)
  t.pendown()
  skyShadeNum = loadList[1]
  t.color(skyShadeList[skyShadeNum]) #For next time create a moon object and have the moon show when the sky is dark and the sun show when the sky is light. Make is so there is only one prompt and the game decides weather theres a sun or moon.
  t.forward(500)
  t.backward(1000)
  t.pensize(10)
  t.forward(1000)
  for i in range (1,26):
   t.color(skyShadeList[skyShadeNum])
   t.pensize(10)

   t.right(-90)
   t.forward(10)
   t.left(-90)
   t.backward(1000)
   t.right(-90)
   t.forward(10)
   t.left(-90)
   t.forward(1000)

  t.setpos(0,0)
  t.color("black")
  print("Sky Complete")
  global listposition
  listposition = 0
  while listposition < len(loadList):
   check122 = loadList[listposition]
   if check122 == treeID:
    global loadTreeCo1
    global loadTreeCo2
    coordinateListPos1 = listposition + 1
    coordinateListPos2 = listposition + 2
    loadTreeCo1 = loadList[coordinateListPos1]
    loadTreeCo2 = loadList[coordinateListPos2]
    print("Loaded tree X: ",loadTreeCo1)
    print("Loaded tree Y: ",loadTreeCo2)
    listposition += 1
    print(listposition)
    print("Loading tree...")
    saveList.append(treeID)
    saveList.append(loadTreeCo1)
    saveList.append(loadTreeCo2)
    t.penup()
    t.goto(loadTreeCo1,loadTreeCo2)
    t.color(green)
    t.pensize(10)
    t.setheading(0)
    t.pendown()
    treePercent = treePercentList[0]
    print(treePercent,"%")
    t.color(brown)
    t.left(90)
    t.forward(10)
    treePercent = treePercentList[1]
    print(treePercent,"%")
    t.right(90)
    t.color(tree)
    t.forward(5)
    treePercent = treePercentList[2]
    print(treePercent,"%")
    t.backward(10)
    t.forward(5)
    t.right(90)
    treePercent = treePercentList[3]
    print(treePercent,"%")
    t.backward(5)
    t.hideturtle()
    t.penup()
    treePercent = treePercentList[4]
    print(treePercent,"%")
    t.setpos(0,0)
    continue
   elif check122 ==lakeID:
    global loadLakeCo1
    global loadLakeCo2
    coordinateListPos1 = listposition + 1
    coordinateListPos2 = listposition + 2
    loadLakeCo1 = loadList[coordinateListPos1]
    loadLakeCo2 = loadList[coordinateListPos2]
    print("Loaded Lake X: ",loadLakeCo1)
    print("loaded Lake Y: ", loadLakeCo2)
    t.penup
    t.goto(loadLakeCo1,loadLakeCo2)
    t.pendown()
    t.color("#0074F0")
    t.pensize(10)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.back(10)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(40)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(50)
    #fill square 2
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(50)
    t.penup()
    t.color("black")
    listposition += 1
    continue
   elif check122 == sunID:
    coordinateListPos1 = listposition + 1
    coordinateListPos2 = listposition + 2
    coordinateListPos3 = listposition + 3
    loadSunCo1 = loadList[coordinateListPos1]
    loadSunCo2 = loadList[coordinateListPos2]
    isSunTrue = loadList[coordinateListPos3]
    print("Loaded Sun X: ",loadSunCo1)
    print("Loaded Sun Y: ",loadSunCo2)
    print("You will not be allowed to draw any more suns.")
    
    sunSize = 50
    t.pensize(5)
    t.penup()
    t.goto(loadSunCo1,loadSunCo2)
    t.color("#F77C00")
    t.pendown()
    t.forward(sunSize)
    t.setheading(270)
    t.forward(sunSize)
    t.setheading(180)
    t.forward(sunSize)
    t.setheading(90)
    t.forward(sunSize)
    t.penup()
    t.pensize(10)
    t.color("#F7A400")
    t.goto(loadSunCo1+5,loadSunCo2-5)
    t.pendown()
    t.setheading(0)
    t.forward(sunSize-10)
    t.setheading(270)
    t.forward(sunSize-10)
    t.setheading(180)
    t.forward(sunSize-10)
    t.setheading(90)
    t.forward(sunSize-10)
    t.penup()
    t.goto(loadSunCo1+12.5,loadSunCo2-12.5)
    t.color("#F7C100")
    t.pendown()
    t.setheading(0)
    t.forward(sunSize-25)
    t.setheading(270)
    t.forward(sunSize-25)
    t.setheading(180)
    t.forward(sunSize-25)
    t.setheading(90)
    t.forward(sunSize-25)
    t.penup()
    t.goto(loadSunCo1+20,loadSunCo2-20)
    t.color("#EAC74A")
    t.setheading(0)
    t.pendown()
    t.forward(sunSize-40) #0 is a placeholder
    t.setheading(270)
    t.forward(sunSize-40)
    t.setheading(180)
    t.forward(sunSize-40)
    t.setheading(90)
    t.forward(sunSize-40)
    t.pensize(10)
    t.penup()
    sun = True

    listposition+=1
    continue
   
   elif check122 == cloudID:
    global loadCloudCo1
    global loadCloudCo2
    global loadedCloudColor
    coordinateListPos1 = listposition + 1
    coordinateListPos2 = listposition + 2
    loadedCloudColorPos = listposition + 3
    loadCloudCo1 = loadList[coordinateListPos1]
    loadCloudCo2 = loadList[coordinateListPos2]
    loadedCloudColor = loadList[loadedCloudColorPos]
    print("Loaded Cloud X: ",loadCloudCo1)
    print("Loaded Cloud Y: ",loadCloudCo2)
    print("Loaded Cloud Colour: ",cloudColourList[loadedCloudColor])
    
    t.penup()
    t.goto(loadCloudCo1,loadCloudCo2)
    t.color(cloudColourList[loadedCloudColor])

    t.setheading(0)
    t.pendown()
    t.forward(15)
    t.pendown
    t.pendown
    t.forward(60)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(15)
    t.right(180)
    t.forward(10)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(75)

    listposition += 1
    continue
   
   elif check122 == hotAirID:
    global loadHotAirCo1
    global loadHotAirCo2
    coordinateListPos1 = listposition + 1
    coordinateListPos2 = listposition + 2
    loadHotAirCo1 = loadList[coordinateListPos1]
    loadHotAirCo2 = loadList[coordinateListPos2]
    print("Loaded Hot Air Balloon X: ",loadHotAirCo1)
    print("Loaded Hot Air Balloon Y: ",loadHotAirCo2)

    rco1 = loadHotAirCo1
    rco2 = loadHotAirCo2
    #balloon outline
    t.penup()
    t.goto(rco1,rco2)
    t.pensize(5)
    t.pendown()
    t.setheading(0)
    t.forward(30)
    t.setheading(270)
    t.forward(35)
    t.setheading(180)
    t.forward(30)
    t.setheading(90)
    t.forward(35)

#Ropes attaching to the basket

    t.setheading(270)
    t.penup()
    t.forward(35)
    t.setheading(0)
    t.forward(10) #change this for indentation of rope lines
    t.pensize(3)
    t.pendown()
    t.setheading(270)
    t.forward(20) 
    t.setheading(90)
    t.penup()
    t.forward(20)
    t.setheading(0)
    t.forward(10) #and this can be changed for rope lines indent
    t.setheading(270)
    t.pendown()
    t.forward(20)
    t.pensize(5)
    t.setheading(0)

#basket outline
    t.forward(5)
    t.setheading(180)
    t.forward(20)
    t.setheading(270)
    t.forward(20)
    t.setheading(0)
    t.forward(20)
    t.setheading(90)
    t.forward(20)
    t.penup()
    t.goto(rco1,rco2)

#filling balloon

    t.setheading(270)
    t.color("green")
    t.pendown()
    t.forward(35) #stripe 1 

    t.penup()
    t.setheading(0)
    t.forward(5)
    t.color("red")#5.5 dead centre
    t.pendown()
    t.setheading(90)
    t.forward(35) #stripe 2

    t.penup()
    t.setheading(180)
    t.forward(2.25)
    t.setheading(270)
    t.pensize(2)
    t.color("white")
    t.pendown()
    t.forward(35)#small stripe 1

    t.penup()
    t.goto(rco1,rco2)
    t.setheading(0)
    t.forward(10)
    t.pensize(5)
    t.setheading(270)
    t.color("green")
    t.pendown()
    t.forward(35) #stripe 3

    t.penup()
    t.setheading(180)
    t.forward(2.25)
    t.setheading(90)
    t.pensize(2)
    t.color("white")
    t.pendown()
    t.forward(35)#small stripe 2

    t.penup()
    t.goto(rco1,rco2)
    t.setheading(0)
    t.forward(15)
    t.setheading(270)
    t.pensize(5)
    t.color("red")
    t.pendown()
    t.forward(35) #stripe 3

    t.penup()
    t.setheading(180)
    t.forward(2.25)
    t.setheading(90)
    t.pensize(2)
    t.color("white")
    t.pendown()
    t.forward(35)#small stripe 3

    t.penup()
    t.goto(rco1,rco2)
    t.setheading(0)
    t.forward(20)
    t.setheading(270)
    t.pensize(5)
    t.color("green")
    t.pendown()
    t.forward(35) #stripe 4

    t.penup()
    t.setheading(180)
    t.forward(2.25)
    t.setheading(90)
    t.pensize(2)
    t.color("white")
    t.pendown()
    t.forward(35)#small stripe 4

    t.penup()
    t.goto(rco1,rco2)
    t.setheading(0)
    t.forward(25)
    t.setheading(270)
    t.pensize(5)
    t.color("red")
    t.pendown()
    t.forward(35) #stripe 5

    t.penup()
    t.setheading(180)
    t.forward(2.25)
    t.setheading(90)
    t.pensize(2)
    t.color("white")
    t.pendown()
    t.forward(35)#small stripe 5

    t.penup()
    t.goto(rco1,rco2)
    t.setheading(0)
    t.forward(30)
    t.setheading(270)
    t.pensize(5)
    t.color("green")
    t.pendown()
    t.forward(35) #stripe 6

    t.penup()
    t.setheading(180)
    t.forward(2.25)
    t.setheading(90)
    t.pensize(2)
    t.color("white")
    t.pendown()
    t.forward(35)#small stripe 6

#coloring ropes

    t.penup()
    t.goto(rco1,rco2)
    t.setheading(270)
    t.forward(35)
    t.setheading(0)
    t.forward(10)
    t.setheading(270)
    t.pensize(3)
    t.color("brown")
    t.pendown()
    t.forward(20)
    t.penup()
    t.setheading(90)
    t.forward(20)
    t.setheading(0)
    t.forward(10)
    t.setheading(270)
    t.pendown()
    t.forward(20)
    t.penup()
    
   #filling basket
   
    t.setheading(0)
    t.forward(5)
    t.pensize(5)
    t.setheading(270)
    t.color("brown")
    t.pendown()
    t.forward(20)
    t.penup()
    t.setheading(180)
    t.forward(5)
    t.setheading(90)
    t.color("brown")
    t.pendown()
    t.forward(20)
    t.penup()
    t.setheading(180)
    t.forward(5)
    t.setheading(270)
    t.color("brown")
    t.pendown()
    t.forward(20)
    t.penup()
    t.setheading(180)
    t.forward(5)
    t.setheading(90)
    t.color("brown")
    t.pendown()
    t.forward(20)
    t.penup()
    t.setheading(180)
    t.forward(5)
    t.setheading(270)
    t.color("brown")
    t.pendown()
    t.forward(20)
    t.penup()
    t.setheading(180)
    t.forward(5)
    t.setheading(90)
    t.color("brown")
    t.pendown()
    t.penup()
    listposition += 1
    continue
   elif check122 == moonID:
    global loadMoonCo1
    global loadMoonCo2
    coordinateListPos1 = listposition + 1
    coordinateListPos2 = listposition + 2
    loadMoonCo1 = loadList[coordinateListPos1]
    loadMoonCo2 = loadList[coordinateListPos2]
    print("Loaded Moon X: ",loadMoonCo1)
    print("Loaded Moon Y: ",loadMoonCo2)
    rco1 = loadMoonCo1
    rco2 = loadMoonCo2
    sun = True
    sunSize = 50
    t.pensize(5)
    t.penup()
    t.goto(rco1,rco2)
    t.color("#808080")
    t.pendown()
    t.forward(sunSize)
    t.setheading(270)
    t.forward(sunSize)
    t.setheading(180)
    t.forward(sunSize)
    t.setheading(90)
    t.forward(sunSize)
    t.penup()
    t.pensize(10)
    t.color("#8f8d8d")
    t.goto(rco1+5,rco2-5)
    t.pendown()
    t.setheading(0)
    t.forward(sunSize-10)
    t.setheading(270)
    t.forward(sunSize-10)
    t.setheading(180)
    t.forward(sunSize-10)
    t.setheading(90)
    t.forward(sunSize-10)
    t.penup()
    t.goto(rco1+12.5,rco2-12.5)
    t.color("#aba9a9")
    t.pendown()
    t.setheading(0)
    t.forward(sunSize-25)
    t.setheading(270)
    t.forward(sunSize-25)
    t.setheading(180)
    t.forward(sunSize-25)
    t.setheading(90)
    t.forward(sunSize-25)
    t.penup()
    t.goto(rco1+20,rco2-20)
    t.color("#d1cfcf")
    t.setheading(0)
    t.pendown()
    t.forward(sunSize-40) #0 is a placeholder
    t.setheading(270)
    t.forward(sunSize-40)
    t.setheading(180)
    t.forward(sunSize-40)
    t.setheading(90)
    t.forward(sunSize-40)
    t.penup()


    listposition+=1
    continue
   else:
    listposition += 1
    continue


   
screen.mainloop() 







