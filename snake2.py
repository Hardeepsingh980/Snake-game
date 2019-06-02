from tkinter import *
import pygame
import random
pygame.init()


    

def high():
    f=open('highscore.txt', 'r')
    s = f.read(100)

    win4 = Tk()
    win4.geometry('200x200')
    win4.resizable(0,0)
    top = Label(win4, text='Highscore', font=('arial black', 20),bg='green', height=1, width=50)
    top.pack()

    Label(win4, text='Your Highscore Is :\n ',font=('arial black',13)).pack()
    Label(win4, text=s, font=('arial black',20)).pack()
    
    
    win.mainloop()





def sp():
    sspeed = slider.get()
    win3.destroy()

    global set_value
    set_value = sspeed
    
    
    global speed
    speed = sspeed
    
    global mspeed
    mspeed = - sspeed


        

    
    








def adspeed():
    global win3
    win3 = Tk()
    win3.geometry('200x200')
    win3.resizable(0,0)


    top = Label(win3,bg='green',width=30, height=1, text='Adjust Speed', font=('arial black',15))
    top.pack()

    Label(win3,text='').pack()

    global slider
    slider = Scale(win3, from_=1,to=20,orient=HORIZONTAL,length=150,width=10,sliderlength=20)
    slider.pack()
    try:
        slider.set(set_value)
    except:
        slider.set(5)

    Label(win3,text='').pack()

    fast = Button(win3, text='Apply',bd=5, font=('arial black',15), command =sp)
    fast.pack()

    






    win3.mainloop()










def snake(*args):
    try:
        win.destroy()
    except:
        win2.destroy()
    # Colors
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)

    # Creating window
    screen_width = 300
    screen_height = 300
    gameWindow = pygame.display.set_mode((screen_width, screen_height))

    # Game Title
    pygame.display.set_caption("Snakes")
    pygame.display.update()

    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(50, screen_width/4)
    food_y = random.randint(50, screen_height/4)
    snake_size = 10

   

    fps = 30
    score = 0

    clock = pygame.time.Clock()

    snk_list = []
    snk_length = 1

    font = pygame.font.SysFont(None, 40)
    def text(text, color, x, y):
        screen_text = font.render(text, True, color)
        gameWindow.blit(screen_text, (x,y))

    def plot_snake(gameWindow, color, snk_list, snake_size):
        for x,y in snk_list:

            pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])


    def gameloop():


        # Game specific variables
        exit_game = False
        game_over = False
        snake_x = 45
        snake_y = 55
        velocity_x = 0
        velocity_y = 0
        food_x = random.randint(20, screen_width/2)
        food_y = random.randint(20, screen_height/2)
        snake_size = 10

        fps = 30
        global score
        score = 0

        clock = pygame.time.Clock()

        snk_list = []
        snk_length = 1
        # Game Loop
        while not exit_game:

            file = open('highscore.txt', 'r')
            h_score = file.read(100)


            if game_over:
                gui2()
                exit_game = True










            else:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
                        gui2()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            try:
                                velocity_x = speed
                                velocity_y = 0
                            except:
                                velocity_x = 5
                                velocity_y = 0

                        if event.key == pygame.K_LEFT:
                            try:
                                velocity_x = mspeed
                                velocity_y = 0
                            except:
                                velocity_x = -5
                                velocity_y = 0

                        if event.key == pygame.K_UP:
                            try:
                                velocity_y = mspeed
                                velocity_x = 0
                            except:
                                velocity_y = -5
                                velocity_x = 0

                        if event.key == pygame.K_DOWN:
                            try:
                                velocity_y = speed
                                velocity_x = 0
                            except:
                                velocity_y = 5
                                velocity_x = 0

                        
                        

                        #if event.key == pygame.K_U:
                            #velocity_y = 5
                            #velocity_x = 0

                snake_x = snake_x + velocity_x
                snake_y = snake_y + velocity_y

                if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                    score += 1

                    food_x = random.randint(0, screen_width)
                    food_y = random.randint(0, screen_height)

                    snk_length += 3

                    if score > int(h_score):
                        file = open('highscore.txt', 'w')
                        file.write(str(score))







                gameWindow.fill(white)
                text('SCORE : ' + str(score), black, 0,20)

                pygame.draw.rect(gameWindow,red , [food_x, food_y, snake_size, snake_size])


                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)

                if len(snk_list) > snk_length:
                    del snk_list[0]

                if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                    game_over = True

                if head in snk_list[:-1]:
                    game_over = True

                #pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
                plot_snake(gameWindow, black, snk_list, snake_size)

            pygame.display.update()
            clock.tick(fps)


        pygame.quit()

    gameloop()













def gui():
    global win
    win = Tk()
    win.geometry('400x400')
    win.resizable(0,0)

    top = Label(win, text = 'Snake', width=50, height=1, bg='green', font=('arial black',55,'bold'))
    top.pack()

    Label(win, text='').pack()

    start = Button(win, text='  Start Game ', bd=5, font=('arial black', 18), command=snake)
    start.pack()

    adjust = Button(win, text='Adjust Speed',bd=5, font=('arial black',18),command = adspeed )
    adjust.pack()

    highscore = Button(win, text='   Highscore  ',bd=5, font=('arial black', 18),command = high )
    highscore.pack()

    quit = Button(win, text='       Quit        ',bd=5, font=('arial black', 18),command=lambda: win.destroy())
    quit.pack()

    win.bind('<Return>', snake)

    win.mainloop()















def gui2():
    global win2
    win2 = Tk()
    win2.geometry('400x400')
    win2.resizable(0,0)

    top = Label(win2, text = 'Game Over', width=50, height=1, bg='green', font=('arial black',40,'bold'))
    top.pack()

    Label(win2, text='').pack()

    start = Button(win2, text='Restart Game', bd=5, font=('arial black', 18), command=snake)
    start.pack()

    adjust = Button(win2, text='Adjust Speed',bd=5, font=('arial black',18) ,command = adspeed)
    adjust.pack()

    highscore = Button(win2, text='   Highscore  ',bd=5, font=('arial black', 18),command = high )
    highscore.pack()

    quit = Button(win2, text='       Quit        ',bd=5, font=('arial black', 18),command=lambda: win2.destroy())
    quit.pack()

    win2.bind('<Return>', snake)


    win.mainloop()






gui()


