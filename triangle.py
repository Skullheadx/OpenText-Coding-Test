import pygame # graphics rendering library
window = pygame.display.set_mode((720,720)) # create the window
def triangle(x,y,m,n): # function that draws a right angle triangle at (x,y) with height m and base n
    pygame.draw.line(window, (255,255,255), (x,y), (x,x+n))
    pygame.draw.line(window, (255,255,255), (x,y+n), (x+m,x+n))
    pygame.draw.line(window, (255,255,255), (x,y), (x+m,x+n))
while True:
    if pygame.event.peek(pygame.QUIT): # detect when window closes
        break
    triangle(0,0,3 * 100,4 * 100) # draw the triangle
    pygame.display.flip() # update the display