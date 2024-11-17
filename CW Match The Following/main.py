
import pygame

pygame.init()
screen = pygame.display.set_mode((1000,800))

acura = pygame.image.load("acura.png")
audi = pygame.image.load("audi.png")
bmw = pygame.image.load("bmw.png")
honda = pygame.image.load("honda.png")
porsche = pygame.image.load("porsche.png")

screen.blit(acura, (50,10))
screen.blit(audi, (50, 150))
screen.blit(bmw, (50, 290))
screen.blit(honda, (50, 430))
screen.blit(porsche, (50,570))

CAR_F = pygame.font.SysFont("calibri", 40)

bmwT = CAR_F.render("bmw", 1, (255,255,255))
porscheT = CAR_F.render("porsche", 1, (255,255,255))
hondaT = CAR_F.render("honda", 1, (255,255,255))
acuraT = CAR_F.render("acura", 1, (255,255,255))
audiT = CAR_F.render("audi", 1, (255,255,255))
screen.blit(bmwT, (800,100))
screen.blit(porscheT, (800, 225))
screen.blit(hondaT, (800, 350))
screen.blit(acuraT, (800, 500))
screen.blit(audiT, (800, 650))

pygame.display.update()

while True:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mousePos1 = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (255,0,0), mousePos1, 10, 0)

        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        mousePos2 = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (255,0,0), mousePos2, 10, 0)
        pygame.draw.line(screen, (255,0,0), (mousePos1), (mousePos2), 2,)

        pygame.display.update()
    