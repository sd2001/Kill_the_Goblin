import pygame

pygame.init()

win = pygame.display.set_mode((852, 480))

pygame.display.set_caption("Kill_the _Goblin")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
end_picture=pygame.image.load('149-1497185_you-win-hd-png-download(200x134).png')
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()
score=0
jump=pygame.mixer.Sound('Mario Jump - Gaming Sound Effect (HD).wav.wav')
music=pygame.mixer.music.load('Sneaky Snitch (Kevin MacLeod) - Gaming Background Music (HD).mp3')
fire_sound=pygame.mixer.Sound('Bullet Hit Sound Effect.wav')
yahoo=pygame.mixer.Sound('Yahoo sound effect.wav')
pygame.mixer.music.play(-1)
ha=pygame.mixer.Sound('Ha Sound Effect.wav')
nani=pygame.mixer.Sound('Nani! (Sound Effect).wav')
party=pygame.mixer.Sound('Party Horn Sound Effect.wav')
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing =True
        self.hitbox =(self. x +20 ,self.y ,28 ,60)
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0] ,(self.x ,self.y))
            else:
                win.blit(walkLeft[0] ,(self.x ,self.y))
        self.hitbox = (self.x + 20, self. y +11, 29, 52)


    def hit(self):
        self.x=60
        self.y=410
        self.walkCount=0
        font1=pygame.font.SysFont('comicsans',100)
        text=font1.render('-5',1,(255,0,0))
        win.blit(text,(426-text.get_width()/2,200))
        pygame.display.update()
        i=0
        while i<300:
            pygame.time.delay(10)
            i+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    i=301
                    pygame.quit()



class projectile(object):
    def __init__(self ,x ,y ,radius ,colour ,facing):
        self. x =x
        self. y =y
        self.radius =radius
        self.colour =colour
        self.facing =facing
        self.vel = 8 *facing
    def draw(self ,win):
        pygame.draw.circle(win ,self.colour ,(self.x ,self.y) ,self.radius)
class enemy(object):
    e_walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                   pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                   pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png')]
    e_walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                  pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                  pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png')]
    def __init__(self ,x ,y ,height ,end):
        self. x =x
        self. y =y
        self.height =height

        self.end =end
        self.walkCount =0
        self.vel =3
        self.path =[self.x ,self.end]
        self.hitbox = (self.x + 17, self.y, 28, 60)
        self.health=10
        self.visible=True
    def draw(self ,win):
        self.move()
        if self.visible==True:
            pygame.draw.rect(win, (0, 0, 255), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 15, self.y + 2, 31, 57)

            if self.walkCount + 1>=27:
                self.walkCount =0
            if self.vel >0:
                win.blit(self.e_walkRight[self.walkCount //3] ,(self.x ,self.y))
                self.walkCount+=1
            else:
                win.blit(self.e_walkLeft[self.walkCount //3] ,(self.x ,self.y))
                self.walkCount+=1

        #pygame.draw.rect(win ,(255 ,0 ,0) ,self.hitbox ,2)
    def move(self):
        if self.vel >0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel =self.vel *-1
                self.walkCount =0
        else:
            if self. x -self.vel >self.path[0]:
                self. x+=self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
    def hit(self):
        if self.health>0:
            self.health-=1
        elif self.health==0 and score>30:
            self.visible=False

        print('hit')



def redrawGameWindow():
    win.blit(bg, (0, 0))
    text=font.render('Score : '+str(score),1,(0,0,0))
    win.blit(text,(720,10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


# MAIN_LOOP
font=pygame.font.SysFont('comicsans',30,True)
man = player(500, 410, 64, 64)
goblin =enemy(0 ,410 ,64 ,820)
shootLoop =0
if shootLoop >0:
    shootLoop+=1
if shootLoop >3:
    shootLoop =0
bullets =[]
run = True
while run:
    clock.tick(27)
    if man.x==goblin.x:
        ha.play()

    if score==32:
        party.play()
        i=0
        while i<300:
            pygame.time.delay(10)
            i += 1
        yahoo.play()
        i = 0
        party.play()
        m=0
        while m<300:
            pygame.time.delay(10)
            win.blit(end_picture,(270,106))
            pygame.display.update()
            m += 1
        break



    if goblin.health==0 and score<30:
        goblin.health=10



    if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
            nani.play()
            man.hit()
            score -= 5
            goblin.health=10


    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.y-bullet.radius< goblin.hitbox[1] +goblin.hitbox[3]  and bullet.y +bullet.radius >goblin.hitbox[1]:
            if bullet.x + bullet.radius >goblin.hitbox[0] and bullet.x - bullet.radius  <goblin.hitbox[0]+goblin.hitbox[2] :
                fire_sound.play()
                goblin.hit()
                score+=1
                bullets.pop(bullets.index(bullet))


        if bullet.x < 852 and bullet.x > 0:
            bullet.x+=bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

#KEY FUNCTIONS
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and shootLoop==0:
        if man.left:
            facing =-1
        else:
            facing =1
        if len(bullets) < 10:
            bullets.append(projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (255, 0, 0), facing))
        shootLoop =1
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing =False
    elif keys[pygame.K_RIGHT] and man.x < 852 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing =False
    else:
        man.standing =True
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_UP]:
            jump.play()
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0

    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()