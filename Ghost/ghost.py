import pygame

pygame.init()

#display
WIDTH, HEIGHT = 1920, 1000
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ghost")

#colors
WHITE = (255, 255, 255)

#images
image = pygame.image.load("forest.jpg").convert_alpha()
image2 = pygame.image.load("ghost.png").convert_alpha()
forest = pygame.transform.scale(image, (WIDTH, HEIGHT))
ghost_img = pygame.transform.scale(image2, (100, 100))

#starting values
ghost_x_start = 100
ghost_y_start = 100
ghost_change = 0


FPS = 60
clock = pygame.time.Clock()


def draw():
    win.blit(forest, (0, 0))
    ghost = win.blit(ghost_img, (ghost_x_start, ghost_y_start))
    pygame.display.update()



def main():
    global ghost_x_start
    global ghost_y_start
    run = True
    while run:
        clock.tick(FPS)
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
          
        if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
            ghost_change = 10
            ghost_x_start += ghost_change 
            win.blit(forest, (0, 0))
            win.blit(ghost_img, (ghost_x_start, ghost_y_start))
            
        if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]:
            ghost_change = -10
            ghost_x_start += ghost_change 
            win.blit(forest, (0, 0))
            win.blit(ghost_img, (ghost_x_start, ghost_y_start))
            
        if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:
            ghost_change = -10
            ghost_y_start += ghost_change 
            win.blit(forest, (0, 0))
            win.blit(ghost_img, (ghost_x_start, ghost_y_start))
            
        if pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:
            ghost_change = 10
            ghost_y_start += ghost_change 
            win.blit(forest, (0, 0))
            win.blit(ghost_img, (ghost_x_start, ghost_y_start))


            #if event.type == pygame.MOUSEBUTTONDOWN:
                #pos = pygame.mouse.get_pos()
                #if rect_ghost.collidepoint(pos):
                    #print("Hello")

main()
pygame.quit()
