import pygame

screen = pygame.display.set_mode((1200,600))
screen.fill((255,255,255))
pygame.display.update()

The_Crow = pygame.image.load("The Crow.png")
Legally_Blonde = pygame.image.load("Legally Blonde.png")
Rio = pygame.image.load("Rio.png")
Ratatouille = pygame.image.load("Ratatouille.png")

The_Crow = pygame.transform.scale(The_Crow, (100,100))
Legally_Blonde = pygame.transform.scale(Legally_Blonde, (100,100))
Rio = pygame.transform.scale(Rio, (100,100))
Ratatouille = pygame.transform.scale(Ratatouille, (100,100))
pygame.display.update()

screen.blit(The_Crow, (200,0))
screen.blit(Legally_Blonde, (400,0))
screen.blit(Rio, (600,0))
screen.blit(Ratatouille, (800,0))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()