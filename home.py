import pygame
import wynk
pygame.init()

#window 
displayWindow = pygame.display.set_mode((800,600))
pygame.display.set_caption('Emotated Music')

#color
white = (52, 73, 94)

#images
camera = pygame.image.load('camera.png').convert()
camera.set_colorkey((255,255,255))
wyn = pygame.image.load('wynk.png').convert()
wyn.set_colorkey((255,255,255))

#text and font
headFont = pygame.font.SysFont('comicsansms',72)
headText = headFont.render("Emotated Music",True,(146, 43, 33))

buttonFont = pygame.font.SysFont('comicsansms',23)
buttonText = buttonFont.render("Click Me",True,(255,255,255))

toClose = True

while toClose:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            toClose = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if x in range((400-94//2),(400-94//2)+95) and y in range(450,491):
                toClose=True
                wynk.playSongs()
                #pass
    displayWindow.fill((204, 209, 209))
    displayWindow.blit(headText, (400-(headText.get_width()/2),50))
    displayWindow.blit(camera,(400-camera.get_width(),50+headText.get_height()+45))
    displayWindow.blit(wyn,(405,50+headText.get_height()+70))
    #pygame.draw.arc(displayWindow,white,[330,450,120,45],0.5,1)
    pygame.draw.circle(displayWindow,white,((400-94//2),470),20)
    pygame.draw.circle(displayWindow,white,(((400-94//2)+94),470),20)
    pygame.draw.rect(displayWindow,white,((400-94//2),450,94,40))
    displayWindow.blit(buttonText, ((400-94//2)+1,452))
    pygame.display.flip()
pygame.quit()

