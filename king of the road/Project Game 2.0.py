from gamelib import *    #JON'S STATION thats the company name

game=Game(800,600,"King Of The Road") #this is the game name

bk=Image("images\\bk.jpg",game)
bk.resizeTo(game.width,game.height)
bk.setSpeed(5,180)

game.setBackground(bk)

car=Image("images\\car.png",game) #the car has to get between the bombs and win the game
car.setSpeed(10,180)

fuel=700 #the fuel is decreasing every sencond

title=Image("images\\bk.jpg",game)
title.resizeTo(game.width,game.height)
bk.draw()
title.draw()
game.drawText("King Of The Road",323,180,Font(white,50,white))
game.drawText("By:Jon's Station",325,215,Font(white,50,white))
game.drawText("Press [SPACE] to play ",600,400)
game.update(1)
game.wait(K_SPACE)

gameover = Image("images\\bk.jpg",game)
gameover.resizeBy(-80)


firstkit=[]   #after the car hits the bomb this help the car get its health back

for times in range(2):
    firstkit.append(Image("images\\firstkit.png",game))

for f in firstkit:
    f.resizeBy(-85)
    #f.setSpeed(5,180)
    #x=randint(200,600)
    #y=randint(200,200)
   
    f.setSpeed(5,180)
    x=randint(200,700)
    y=randint(400,600)
    f.moveTo(x,y)
gas=[]   #give the car more fuel

for times in range(10):
    gas.append(Image("images\\fuel.png",game))

for t in gas:
    x=randint(100,700)
    y=randint(-1000,-100)
    t.moveTo(x,y)
    t.setSpeed(5,180)
    t.resizeBy(-65)
    t.moveTo(x,y)

bomb=[]    #the bomb is decreasing the health of the car 

for times in range (10):
    bomb.append(Image("images\\bomb.png",game))

for b in bomb:  #keep getting index error 
    b.resizeBy(-90)
    #x=randint(250,650)
    #y=randint(1000,1000)
    #b.setSpeed(5,180)
    x = randint(100,700)
    y = randint (-100,100)
    b.setSpeed(5,180)
    b.moveTo(x,y)

while not game.over:
    game.processInput()
    game.scrollBackground("down",5)
    car.draw()
    fuel-=1
    


    for f in firstkit:
        f.move()

        if car.collidedWith(f):
            car.health+=25
            f.visible=False
            
        if f.isOffScreen("bottom"):
            f.setSpeed(5,180)
            x=randint(100,700)
            y=randint(-100,100)
            f.moveTo(x,y)
            f.move()
            #x=randint(200,600)
            #y=randint(50,200)
            #f.moveTo(x,y)
            '''x=randint(200,700)
            y=randint(400,1000)
            f.setSpeed(5,180)
            f.moveTo(x,y)'''
            
    '''if car.collidedWith(b):
        car.health -=50
        b.visible=False'''
        
    if car.isOffScreen("bottom"):
        game.over=True


    if car.isOffScreen("top"):
        car.moveTo(400,250)
        
    for t in gas:
        t.move()

        if car.collidedWith(t):
            fuel+=50
            t.visible=False

        if t.isOffScreen("bottom"):
            t.setSpeed(5,180)
            x = randint(100,700)
            y = randint (-100,100)
            t.moveTo(x,y)
            t.move()
                  
                
    for b in bomb:
        b.move()
        '''x = randint(100,700)
        y = randint (-100,100)
        b.setSpeed(5,180)
        b.moveTo(x,y)'''
        if car.collidedWith(b):
            car.health-=20
            b.visible=False

        if b.isOffScreen("bottom"):
            x=randint(100,700)
            y=randint(-100,100)
            b.moveTo(x,y)

    if keys.Pressed[K_LEFT]:
        car.x-= 5
                
    if keys.Pressed[K_RIGHT]:
        car.x+= 5
                
    if keys.Pressed[K_UP]:
        car.y-= 5
                
    if keys.Pressed[K_DOWN]:
        car.y+= 5
                
    if car.health<=0 or fuel<=0:
        game.over=True

    

    game.drawText("Health: " + str(car.health),5,5)
                
    game.drawText("Fuel: " + str(fuel),500,5)
    
    
    game.update(40)
game.quit()
