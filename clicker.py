import pygame


win_width = 800
win_height = 640
pygame.init()  # инициализирую pygame
win = pygame.display.set_mode((win_width, win_height))
# -----------
wiskas = pygame.image.load('D:\\JustMonika\\_Clicker(2)\\wiskas.png')
image_button = pygame.image.load('D:\\JustMonika\\_Clicker(2)\\Button_Cartoon.png')
image_button_active = pygame.image.load('D:\\JustMonika\\_Clicker(2)\\Button_Cartoon_active.png')
wiskas = pygame.transform.scale(wiskas, (120,200))
escape = pygame.image.load('D:\\JustMonika\\_Clicker(2)\\escape.png')
escape_active = pygame.image.load('D:\\JustMonika\\_Clicker(2)\\escape_active.png')
escape = pygame.transform.scale(escape, (40,40))
escape_active = pygame.transform.scale(escape_active, (40,40))
#image_button_shop_product = pygame.image.load('D:\\JustMonika\\_Clicker(2)\\Button_shop_1.png')
#image_button_shop_product = pygame.transform.scale(image_button_shop_product, (280,114))
# -----------
clock = pygame.time.Clock()
scores = 0
multiplier = 1
spc = 1
click_press = True
long_number = 20
long_numbers = 10
shop = False
price_paw = 45
money_count = 50
money_count_key = False
price_cat_ears = 445
price_cat_tail = 3455
price_kitten = 13455


class Button:

	def __init__(self, width, height, active_button = (200,200,200), unactive_button = (200,200,255), link = None):
		self.width = width
		self.height = height
		self.active_button = active_button
		self.unactive_button = unactive_button
		self.link = link
	def draw_rect(self, x, y,):
		global click_press
		mouse = pygame.mouse.get_pos() # print(mouse) >>> [x, y]
		click = pygame.mouse.get_pressed() # print(click) >>> [0, 0]


		if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
			pygame.draw.rect(win, self.active_button, (x, y, self.width, self.height))
		
			if click[0] == 1 and self.link != None and click_press:
				click_press = False
				self.link()
			if click[0] != 1:
				click_press = True
			
		else:
			pygame.draw.rect(win, self.unactive_button, (x, y, self.width, self.height))	

	def load_image(self, x, y, image):
		global click_press
		mouse = pygame.mouse.get_pos() # print(mouse) >>> [x, y]
		click = pygame.mouse.get_pressed() # print(click) >>> [0, 0]


		if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
			win.blit(image, (x,y))
		
			if click[0] == 1 and self.link != None and click_press:
				click_press = False
				self.link()
			if click[0] != 1:
				click_press = True	
		else:
			win.blit(image, (x,y))	

	def load_anim_image(self, x, y, image_1,image_2):
		global click_press
		mouse = pygame.mouse.get_pos() # print(mouse) >>> [x, y]
		click = pygame.mouse.get_pressed() # print(click) >>> [0, 0]


		if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
			win.blit(image_2, (x,y))
		
			if click[0] == 1 and self.link != None and click_press:
				click_press = False
				self.link()
			if click[0] != 1:
				click_press = True
		else:
			win.blit(image_1, (x,y))	

	def link_(self, x, y):
		global click_press
		mouse = pygame.mouse.get_pos() # print(mouse) >>> [x, y]
		click = pygame.mouse.get_pressed() # print(click) >>> [0, 0]


		if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
			if click[0] == 1 and self.link != None and click_press:
				click_press = False
				self.link()
			if click[0] != 1:
				click_press = True



			

def draw_game():
	win.fill((255,255,255))
	button_click.load_image(340,220, wiskas)
	load_shopgame_button()
	button_go_shop.link_(158,96)
	print_text('*chonk*', 155, 93)
	print_text('Shop', 100, 30)
	print_scores()
	button_escape.load_anim_image(win_width-40,0,escape, escape_active)
	if money_count_key:
		no_money()
	pygame.display.update()
	
	



def draw_shop():
	global click_press, shop, money_count_key
	win.fill((255,255,255))
	load_shopgame_button()
	print_text('*chonk*', 155, 93)
	print_text('Back to game', 60, 30)
	print_scores()
	button_escape.load_anim_image(win_width-40,0,escape, escape_active)
	load_shop_button_1()
	load_shop_button_2()
	load_shop_button_3()
	load_shop_button_4()
	Button_shop_1.link_(565, 93)
	Button_shop_2.link_(565, 218)
	Button_shop_3.link_(565, 338)
	Button_shop_4.link_(565, 458)
	if money_count_key:
		no_money()

	pygame.display.update()

	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if 158 < mouse[0] < 253 and 96 < mouse[1] < 125:
		if click[0] == 1 and click_press:
			click_press = False
			shop = False
		if click[0] != 1:
			click_press = True


def game():

	game = True
	while game:
		clock.tick(30)
		draw_game()
		for event in pygame.event.get(): # Выход из игры
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

def shop():
	global shop, click_press
	click_press = False
	shop = True
	while shop:
		clock.tick(30)
		draw_shop()
		for event in pygame.event.get(): # Выход из игры
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()


def print_text(message, x, y, font_color = (0,0,0), font_size = 30, font_type = "D:\\JustMonika\\_RunFatCat(1)\\ara\\langue.ttf"):
	font = pygame.font.Font(font_type, font_size)
	text = font.render(message, True, font_color) 
	win.blit(text, (x, y))

def count_scores():
	global scores, multiplier, spc
	scores += spc * multiplier

def print_scores():
	global long_numbers, long_number
	if long_numbers <= scores:
		long_numbers = long_numbers * 10
		long_number = long_number + 19
		print_text(str(scores),win_width - long_number, 45) # ПОМЕНЯТЬ МЕСТАМИ
	elif len(str(scores)) < len(str(long_numbers)) - 1:
		long_numbers = long_numbers // 10
		long_number = long_number - 19
		print_text(str(scores),win_width - long_number, 45)
	else:
		print_text(str(scores),win_width - long_number, 45)

def leave():
	pygame.quit()
	quit()

def load_shopgame_button():
	mouse = pygame.mouse.get_pos() # print(mouse) >>> [x, y] 
	if 158 < mouse[0] < 158 + 95 and 96 < mouse[1] < 96 + 29:
		win.blit(image_button_active, (10,10))
	else:
		win.blit(image_button, (10,10))

def load_shop_button_1():
	mouse = pygame.mouse.get_pos() # print(mouse) >>> [x, y] 
	if 565 < mouse[0] < 565 + 95 and 93 < mouse[1] < 93 + 29:
		win.blit(image_button_active, (420,10))
		print_text("Paw 10 KG",440,20)
		print_text("+3 SPC",600,25)
		print_text("Price:" + str(price_paw),470,46)
		print_text('*chonk*', 565, 93)
	else:
		win.blit(image_button, (420,10))
		print_text("Paw 10 KG",440,20)
		print_text("Price:" + str(price_paw),470,46)
		print_text('*chonk*', 565, 93)

def no_money():
	global money_count, money_count_key
	if money_count > 0:
		print_text(message = "You don't have need money", x = 150, y = 320, font_color = (155,0,0), font_size = 50, font_type = "D:\\JustMonika\\_RunFatCat(1)\\ara\\langue.ttf")
		money_count -= 1
	else:
		money_count_key = False
		money_count = 45

def buy_1():
	global spc, money_count_key, scores, price_paw
	if scores >= price_paw:
		scores = scores - price_paw
		price_paw *= 1.5
		price_paw = int(price_paw)
		spc += 3
	else:
		money_count_key = True

def load_shop_button_2():
	mouse = pygame.mouse.get_pos() # print(mouse) >>> [x, y] 
	if 565 < mouse[0] < 565 + 95 and 218 < mouse[1] < 218 + 29:
		win.blit(image_button_active, (420,135))
		print_text("Cat ears",440,145)
		print_text("+9 SPC",600,145)
		print_text("Price:" + str(price_cat_ears),470,171)
		print_text('*chonk*', 565, 218)
	else:
		win.blit(image_button, (420,135))
		print_text("Cat ears",440,145)
		print_text("Price:" + str(price_cat_ears),470,171)
		print_text('*chonk*', 565, 218)

def buy_2():
	global spc, money_count_key, scores, price_cat_ears
	if scores >= price_cat_ears:
		scores = scores - price_cat_ears
		price_cat_ears *= 1.5
		price_cat_ears = int(price_cat_ears)
		spc += 9
	else:
		money_count_key = True

def load_shop_button_3():
	mouse = pygame.mouse.get_pos() # print(mouse) >>> [x, y] 
	if 565 < mouse[0] < 565 + 95 and 338 < mouse[1] < 338 + 29:
		win.blit(image_button_active, (420,255))
		print_text("Cat tail",440,265)
		print_text("+27 SPC",600,265)
		print_text("Price:" + str(price_cat_tail),470,291)
		print_text('*chonk*', 565, 338)
	else:
		win.blit(image_button, (420,255))
		print_text("Cat tail",440,265)
		print_text("Price:" + str(price_cat_tail),470,291)
		print_text('*chonk*', 565, 338)
def buy_3():
	global spc, money_count_key, scores, price_cat_tail
	if scores >= price_cat_tail:
		scores = scores - price_cat_tail
		price_cat_tail *= 1.5
		price_cat_tail = int(price_cat_tail)
		spc += 27
	else:
		money_count_key = True

def load_shop_button_4():
	mouse = pygame.mouse.get_pos() # print(mouse) >>> [x, y] 
	if 565 < mouse[0] < 565 + 95 and 458 < mouse[1] < 458 + 29:
		win.blit(image_button_active, (420,375))
		print_text("Kitten",440,385)
		print_text("+81 SPC",600,385)
		print_text("Price:" + str(price_kitten),470,411)
		print_text('*chonk*', 565, 458)
	else:
		win.blit(image_button, (420,375))
		print_text("Kitten",440,385)
		print_text("Price:" + str(price_kitten),470,411)
		print_text('*chonk*', 565, 458)
def buy_4():
	global spc, money_count_key, scores, price_kitten
	if scores >= price_kitten:
		scores = scores - price_kitten
		price_kitten *= 1.5
		price_kitten = int(price_kitten)
		spc += 81
	else:
		money_count_key = True










		
	return False
# ------- Кнопочки
button_click = Button(width = 120, height = 200, active_button = (200,200,200), unactive_button = (200,200,255), link = count_scores)
button_go_shop = Button(width = 95, height = 29, active_button = (200,200,200), unactive_button = (200,200,255), link = shop)
button_escape = Button(width = 40, height = 40, active_button = (200,200,200), unactive_button = (200,200,255), link = leave)
anim_button = Button(width = 95, height = 29, active_button = (1,1,1), unactive_button = (1,1,1), link = None)
Button_shop_1 =  Button(width = 95, height = 29, active_button = (200,200,200), unactive_button = (200,200,255), link = buy_1)
Button_shop_2 =  Button(width = 95, height = 29, active_button = (200,200,200), unactive_button = (200,200,255), link = buy_2)
Button_shop_3 =  Button(width = 95, height = 29, active_button = (200,200,200), unactive_button = (200,200,255), link = buy_3)
Button_shop_4 =  Button(width = 95, height = 29, active_button = (200,200,200), unactive_button = (200,200,255), link = buy_4)


while game():
	pass


