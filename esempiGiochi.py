import pygame
import sys

DIMENSIONI = (600, 600)

#colori
NERO = (0,0,0)
BIANCO = (255,255,255)


def disegnaGriglia():
    dimensione = 50

    for x in range(0,DIMENSIONI[0], dimensione):
        for y in range(0, DIMENSIONI[1], dimensione):
            rettangolo = pygame.Rect(x, y, dimensione, dimensione)
            pygame.draw.rect(schermo, BIANCO, rettangolo, 1)



def main():
    global schermo
    pygame.init()
    schermo = pygame.display.set_mode(DIMENSIONI)
    schermo.fill(NERO)



    while True:
        disegnaGriglia()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pass 


        pygame.display.update()


if __name__ == "__main__":
    main()