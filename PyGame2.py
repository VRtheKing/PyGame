import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Demo")

x = 50
y = 50
width = 50
height = 60
vel = 20

is_jump = False
jumpCount = 10 

run = True

while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > 0:
		x -= vel

	if keys[pygame.K_RIGHT] and x < 500 - width:
		x += vel

	if not(is_jump):

		if keys[pygame.K_UP] and y > 0:
			y -= vel

		if keys[pygame.K_DOWN] and y < 500 - height:
			y += vel

		if keys[pygame.K_SPACE]:
			is_jump = True

	else:
		if jumpCount >= -10:
			pos = 1
			if jumpCount < 0:
				pos = -1
			y -= (jumpCount ** 2) * 0.5 * pos
			jumpCount -= 1
		else:
			jumpCount = 10
			is_jump = False		

	win.fill((0, 0, 0))
	pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
	pygame.display.update()	

pygame.quit()
