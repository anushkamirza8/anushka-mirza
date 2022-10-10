import pygame
import button

#create display window
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Menu')

#load button images
game_img = pygame.image.load('Images/gamesign.png').convert_alpha()
quiz_img = pygame.image.load('Images/quizsign.png').convert_alpha()
instructions_img = pygame.image.load('Images/instructionssign.png').convert_alpha()
information_img = pygame.image.load('Images/informationsign.png').convert_alpha()

#create button instances
game_button = button.Button(100, 200, game_img, 1)
quiz_button = button.Button(100, 300, quiz_img, 1)
instructions_button = button.Button(100, 400, instructions_img, 2)
information_button = button.Button(100, 500, information_img, 2)

#game loop
run = True
while run:

	screen.fill((202, 228, 241))

	if game_button.draw(screen):
		print('Loading game')
		import runningoutoftime.py
	if instructions_button.draw(screen):
		print('Goodbye!')
		import instructionsbg.py
	if information_button.draw(screen):
		print('loading information')
		import info.py
	if quiz_button.draw(screen):
		print('loading quiz')
		import quiz.py
	
	

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
