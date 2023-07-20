import pygame, math, random





class Enemy:
    def __init__(self,window):

        self.image = []
        

        
        self.num_of_enemies = 10

        self.x = []
        self.y = []

        self.x_change = [] # 3
        self.y_change = [] # 40



        for i in range(self.num_of_enemies):
            self.image.append(pygame.image.load("/Users/dunura/Desktop/Programming/Python_work/Space Invaders/001-alien-pixelated-shape-of-a-digital-game.png"))
            self.x.append(random.randint(0,730))
            self.y.append(random.randint(0,150))
            self.x_change.append(2)
            self.y_change.append(40)

            
            


        


        self.window = window
    


    def draw(self):
        for i in range(self.num_of_enemies):
            self.window.blit(self.image[i],(self.x[i],self.y[i]))



    



class Player:
    def __init__(self,window):

        self.window = window

        self.x = 375
        self.y = 500

        self.x_change = 0

        self.image =  pygame.image.load("/Users/dunura/Desktop/Programming/Python_work/Space Invaders/space-invaders.png")


    


    def draw(self):
        self.window.blit(self.image,(self.x,self.y))
        self.x+=self.x_change
    
        


class Bullet:
    def __init__(self,window):
        self.window = window
        self.image = pygame.image.load("/Users/dunura/Desktop/Programming/Python_work/Space Invaders/bullet.png")



        self.x = -100
        self.y = 520    # 520

        self.y_change = 0
 
    
        self.bullet_state = "ready"

    def draw(self):
        self.window.blit(self.image,(self.x,self.y))
        self.y+=self.y_change
    

        
    





class Game:
    def __init__(self):

        pygame.init()

        self.background = pygame.image.load("/Users/dunura/Desktop/Programming/Python_work/Space Invaders/space_background.jpeg")
        self.score = 0

        # WINDOW
        self.window = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Space Invaders")


        # ICON
        ICON = pygame.image.load("/Users/dunura/Desktop/Programming/Python_work/Space Invaders/space-invaders.png")
        pygame.display.set_icon(ICON)
    

        # PLAYER INSTANCE
        self.player = Player(self.window)

        # ENEMY INSTANCE
        self.enemy = Enemy(self.window)

        # BULLET INSTANCE
        self.bullet = Bullet(self.window)



        
    @staticmethod
    def isCollision(x1,y1,x2,y2):
        distance = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
        return distance
        
    

    def display_score(self):
        font = pygame.font.SysFont("arial",20)
        line1 = font.render(f"SCORE: {self.score}",True,(255,255,255))
        self.window.blit(line1,(20,15))


    def gameOver(self):
        self.window.blit(self.background,(0,0))
        font = pygame.font.SysFont('arial',30)
        line1 = font.render(f"GAME OVER", True, (255,255,255))
        line2 = font.render(f"SCORE: {self.score}",True,(255,255,255))
        line3 = font.render("Press 'return' to play again",True,(255,255,255))
        self.window.blit(line1,(325,200))
        self.window.blit(line2,(345,250))
        self.window.blit(line3,(250,300))
    
    def play(self):
        self.window.blit(self.background,(0,0))

        self.player.draw()
        self.enemy.draw()
        self.bullet.draw()
        self.display_score()


        # PLAYER BOUNDARIES
        if self.player.x >= 736:
            self.player.x = 736
        
        if self.player.x <= 0:
            self.player.x = 0


        # ENEMY MOVEMENT / BOUNDARIES


        for i in range(self.enemy.num_of_enemies):
            if self.enemy.x[i] >= 736:
                self.enemy.y[i]+=self.enemy.y_change[i]
                self.enemy.x_change[i] = -2
            
            if self.enemy.x[i] <= 0:
                self.enemy.y[i]+=self.enemy.y_change[i]
                self.enemy.x_change[i] = 2
            
            if self.isCollision(self.bullet.x,self.bullet.y,self.enemy.x[i],self.enemy.y[i]) < 36:
                self.enemy.x[i] = random.randint(0,730)
                self.enemy.y[i] = random.randint(0,150)
                self.bullet.y = 520
                self.bullet.y_change = 0
                self.bullet.x = -100
                self.bullet.bullet_state = "ready"
                self.score+=1

            if self.enemy.y[i] >= self.player.y:
                raise "Game over"

            self.enemy.x[i] += self.enemy.x_change[i]

        
        # BULLET MECHANICS


        if self.bullet.y <= 0:
            self.bullet.y = 520
            self.bullet.y_change = 0
            self.bullet.x = -100
            self.bullet.bullet_state = "ready"
        








        



    def run(self):
        running = True
        pause = False


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


                if event.type == pygame.KEYDOWN:
    
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    
                    if event.key == pygame.K_RIGHT:
                        self.player.x_change = 3

                    
                    if event.key == pygame.K_LEFT:
                        self.player.x_change = -3

                    if event.key == pygame.K_SPACE:
                        if self.bullet.bullet_state == "ready":
                            self.bullet.x = self.player.x + 16
                            self.bullet.y_change = -5
                            self.bullet.bullet_state = "fire"
                    
                    if event.key == pygame.K_RETURN:
                        self.play()
                        
                            
   
                    

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        self.player.x_change = 0



            self.play()
            pygame.display.update()

                    



            try:
                if not pause:   
                    self.play()
            
            except:
                pause = True
                self.gameOver()




            

if __name__ == "__main__":
    game = Game()
    game.run()


