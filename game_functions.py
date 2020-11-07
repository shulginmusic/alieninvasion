import sys
from time import sleep
import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, stats, screen,
 play_button, ship, bullets_group, aliens_group, sb):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	for event in pygame.event.get(): #pygame.event.get() accesses the methods in pygame
		if event.type == pygame.QUIT:
			record_high_score(stats)
			sys.exit()
		if event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets_group,
	stats, play_button, mouse_x, mouse_y, aliens_group, sb)
		if event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		if event.type == pygame.MOUSEBUTTONDOWN:#activated only when clicked
			 #Get the position of the mouse
			check_play_button(stats, screen, ai_settings, play_button,
	 			mouse_x, mouse_y, aliens_group, bullets_group, ship, sb)

def check_play_button(stats, screen, ai_settings, play_button,
	 mouse_x, mouse_y, aliens_group, bullets_group, ship, sb):
	#Start a new game when the player clicks Play
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y) #if play button rect collides with mouse's x and y when clicked
	if button_clicked and not stats.game_active: #Only start the game when game_active is False, so the mouse event can't restar the game in the middle of it
		start_game(stats, screen, ai_settings, play_button,
	 mouse_x, mouse_y, aliens_group, bullets_group, ship, sb)


def start_game(stats, screen, ai_settings, play_button,
	 mouse_x, mouse_y, aliens_group, bullets_group, ship, sb):
	ai_settings.initialize_dynamic_settings()
	#Hide the cursor!: Cursor reappears once the game ends, see ship_hit()
	pygame.mouse.set_visible(False)
	#Reset game stats
	stats.reset_stats()
	stats.game_active = True

	sb.prep_score()
	sb.prep_high_score()
	sb.prep_level()
	sb.prep_ships()


	#Empty the list of aliens and bullets
	aliens_group.empty()
	bullets_group.empty()

	#Create new fleet and center the ship
	create_fleet(ai_settings, screen, ship, aliens_group)
	ship.center_ship()


def check_keydown_events(event, ai_settings, screen, ship, bullets_group,
	stats, play_button, mouse_x, mouse_y, aliens_group, sb):
	if event.type == pygame.KEYDOWN: #this part listens to the KEYDOWN
		#events
		if event.key == pygame.K_RIGHT:#Move the ship to the right
			ship.moving_right = True #Don't forget to add ship as argument!
		if event.key == pygame.K_LEFT:
			ship.moving_left = True
		#Fire the bullets
		if event.key == pygame.K_SPACE:
			fire_bullets(ai_settings, screen, ship, bullets_group)
			shot = pygame.mixer.Sound('shot.wav')
			if stats.game_active:
				shot.play()
		if event.key == pygame.K_q:
			record_high_score(stats)
			sys.exit()
		if event.key == pygame.K_p and not stats.game_active:
			# print('test')
			start_game(stats, screen, ai_settings, play_button,
	 mouse_x, mouse_y, aliens_group, bullets_group, ship, sb)

def check_keyup_events(event, ship):
	if event.type == pygame.KEYUP:#KEYUP Events
		if event.key == pygame.K_RIGHT:
			ship.moving_right = False
		if event.key == pygame.K_LEFT:
			ship.moving_left = False

def update_screen(ai_settings, screen, stats,
 ship, aliens_group, bullets, play_button, sb):
	screen.fill(ai_settings.bg_color)#Fill the screen with color
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()#Draw the ship on the screen
	aliens_group.draw(screen)#Pygame automatically draws each element to the screen, based on rect
	sb.show_score()
	#Draw the play button if the game is inactive
	if not stats.game_active:
		play_button.draw_button()
	pygame.display.flip() #this keeps updating the screen as the game
		#changes

def update_bullets(ai_settings, screen, ship, aliens_group,
 bullets_group, stats, sb):
	bullets_group.update()
	#Get rid of bullets that have disappeared
	for bullet in bullets_group.copy():
		if bullet.rect.bottom <= 0:
			bullets_group.remove(bullet)
	check_bullet_collisions(ai_settings, screen, ship,
	 bullets_group, aliens_group, stats, sb)

def check_bullet_collisions(ai_settings, screen, ship,
 bullets_group, aliens_group, stats, sb):
	collisions = pygame.sprite.groupcollide(bullets_group,
	 aliens_group, True, True)

	if collisions:#use this loop to loop trhough each alien in the collisions dictionary, therefore getting points for every single one
		explosion = pygame.mixer.Sound('explosion.wav')
		explosion.play()
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
			check_high_score(stats, sb)
			# print(collisions)
			# dictionary example: (you are looping through the value, which is a list)
			# {<Bullet sprite(in 0 groups)>: [<Alien sprite(in 0 groups)>, <Alien sprite(in 0 groups)>, <Alien sprite(in 0 groups)>]}

	if len(aliens_group) == 0:
		bullets_group.empty()
		ai_settings.increase_speeds()
		stats.level += 1
		sb.prep_level()
		create_fleet(ai_settings, screen, ship, aliens_group) 
	
def update_aliens(ai_settings, stats, screen, ship,
 aliens_group, bullets_group, sb):
	check_fleet_edges(ai_settings, aliens_group)
	aliens_group.update()
	if pygame.sprite.spritecollideany(ship, aliens_group):
		ship_hit(ai_settings, stats, screen, ship, aliens_group,
		 bullets_group, sb)


	check_aliens_bottom(ai_settings, stats, screen, ship,
	 aliens_group, bullets_group, sb)

def ship_hit(ai_settings, stats, screen, ship, aliens_group,
 bullets_group, sb):
	#Respond to ship being hit by alien

	#Update number of ships left
	stats.ships_left -= 1
	#Empty the list of aliens and bullets
	if stats.ships_left > 0:
		sb.prep_ships()
		aliens_group.empty()
		bullets_group.empty()
		#Create a new fleet and center the ship
		create_fleet(ai_settings, screen, ship, aliens_group)
		ship.center_ship()
		#Pause
		sleep(1.0)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship,
 aliens_group, bullets_group, sb):
	#Check if any aliens have reached the bottom of the screen
	screen_rect = screen.get_rect()
	for alien in aliens_group.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings, stats, screen, ship,
			 aliens_group, bullets_group, sb)
			break #Break the loop because you only need one alien to reach the bottom to lose the round

def check_fleet_edges(ai_settings, aliens_group):
	#Respond appropriately if any aliens have reached an edge:
	for alien in aliens_group.sprites():
		if alien.check_edges():#is true
			change_fleet_direction(ai_settings, aliens_group)
			break

def change_fleet_direction(ai_settings, aliens_group):
	# Drop the entire fleet
	for alien in aliens_group.sprites():
		alien.rect.y += ai_settings.alien_vertical_speed
	#Change direction
	ai_settings.fleet_direction *= -1

def fire_bullets(ai_settings, screen, ship, bullets_group):
	bullets_allowed = ai_settings.bullets_allowed
	# x = bullets_allowed - len(bullets)
	# x = str(x)
	# print("Bullets available: " + x)
	if len(bullets_group) < bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets_group.add(new_bullet)

#Create a full fleet of aliens:
#Create an alien and find the number of aliens in a row
#Spacing between aliens equals to one alien width
def create_fleet(ai_settings, screen, ship, aliens_group):
	alien = Alien(ai_settings, screen)
	num_of_aliens = get_num_aliens(ai_settings, screen)
	num_of_rows = get_number_rows(ai_settings, ship.rect.height,
		alien.rect.height)
	#Create the fleet of aliens: 
	for row_number in range(num_of_rows):
		for alien_number in range(num_of_aliens):
			create_alien(ai_settings, screen,
			 aliens_group, alien_number, row_number)

def get_num_aliens(ai_settings, screen):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	space_available = ai_settings.screen_width - (alien_width * 2)
	num_of_aliens = space_available / (alien_width * 2)
	num_of_aliens = int(num_of_aliens)
	# num_of_aliens = 500
	return num_of_aliens

def get_number_rows(ai_settings, ship_height, alien_height):
	screen_height = ai_settings.screen_height
	available_space_y = (screen_height - (3 * alien_height) - ship_height)
	number_rows = available_space_y / (2 * alien_height)
	number_rows = int(number_rows)
	return number_rows

def create_alien(ai_settings, screen, aliens_group, alien_number, row_number):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien.rect.width + 2 * alien_width * alien_number
	alien.rect.x = alien.x #THIS IS IMPORTANT
	# 2 HOURS WORHT OF SEARCHING FOR THIS FLOAT error!
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens_group.add(alien)

def check_high_score(stats, sb):
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()

def record_high_score(stats):
	filename = 'high_score.txt'
	with open(filename, 'w') as file_object:
		str_hi_score = str(stats.high_score)
		file_object.write(str_hi_score)
















