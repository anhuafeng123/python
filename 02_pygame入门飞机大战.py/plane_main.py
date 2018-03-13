#encoding = ‘GBK’
import pygame


from plane_sprites import *
HERO_FIRE_EVENT = pygame.USEREVENT + 1
#音乐
pygame.init()
pygame.mixer.music.load(
	)
pygame.mixer.music.play()
#主程序类
class PlaneGame(object):
	#初始化
	def __init__(self):
		#创建游戏窗口
		self.screen = pygame.display.set_mode((SCREEN_RECT.width,SCREEN_RECT.height))
		#创建游戏时钟
		self.clock = pygame.time.Clock()
		#调用私有方法，精灵和精灵组的创建
		self.__create_sprites()
		#设置一个定时期事件
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
		#设置一个英雄发射子弹事件
		pygame.time.set_timer(HERO_FIRE_EVENT,200)

	#游戏开始
	def start_game(self):
		print('游戏开始')
		while True:
			#1.刷新帧率
			self.clock.tick(60)
			#2.监听事件
			self.__event_handler()
			#3.碰撞检测
			self.__check_collide()
			#4.更新精灵和精灵组，相当于我们原来说的blit绘制
			self.__update_sprites()
			#5.刷新屏幕
			pygame.display.update()
	#精灵。精灵组
	def __create_sprites(self):
		'''创建精灵和精灵组'''
		bg1 = Background('./images/background.png')
		bg2 = Background('./images/background.png')
		bg2.rect.y = -bg2.rect.height
		self.back_group = pygame.sprite.Group(bg1,bg2)
		self.hero= Hero('./images/life.png')
		self.hero_group = pygame.sprite.Group(self.hero)
		self.hero_er = Hero_er('./images/life.png')
		self.hero_er_group = pygame.sprite.Group(self.hero_er)
		self.enemy = Enemy('./images/enemy1.png')
		self.enemy_group = pygame.sprite.Group(self.enemy)
	#事件监听
	def __event_handler(self):
		#你所有的事件 都会被监听到 并且以列表的形式返回
		for event in pygame.event.get():
			print(event)
			#判断事件类型 pygame.quit
			if event.type == pygame.QUIT:
				self.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				self.enemy_group.add(Enemy('./images/enemy1.png'))

			elif event.type == HERO_FIRE_EVENT:
				#将精灵添加到精灵组
				self.hero.fire()
				self.hero_er.zid()			

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.hero.panduan = True
				elif event.key == pygame.K_DOWN:
					self.hero.panduana = True
				elif event.key == pygame.K_LEFT:
					self.hero.panduanb = True
				elif event.key == pygame.K_RIGHT:
					self.hero.panduanc = True

				elif event.key == pygame.K_w:
					self.hero_er.panduand = True
				elif event.key == pygame.K_s:
					self.hero_er.panduane = True
				elif event.key == pygame.K_a:
					self.hero_er.panduanf = True
				elif event.key == pygame.K_d:
					self.hero_er.panduang = True

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					self.hero.panduan = False
				elif event.key == pygame.K_DOWN:
					self.hero.panduana = False
				elif event.key == pygame.K_LEFT:
					self.hero.panduanb = False
				elif event.key == pygame.K_RIGHT:
					self.hero.panduanc = False

				elif event.key == pygame.K_w:
					self.hero_er.panduand = False
				elif event.key == pygame.K_s:
					self.hero_er.panduane = False
				elif event.key == pygame.K_a:
					self.hero_er.panduanf= False
				elif event.key == pygame.K_d:
					self.hero_er.panduang = False
 

	#碰撞检测
	def __check_collide(self):
		#子弹摧毁敌机
		pygame.sprite.groupcollide(self.hero.bullet_group,self.enemy_group,True,True)
		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		pygame.sprite.groupcollide(self.hero_er.bullets_group,self.enemy_group,True,True)
		enemiesa = pygame.sprite.spritecollide(self.hero_er,self.enemy_group,True)
		if len(enemies) > 0 :
			self.hero.kill()
		elif len(enemiesa) > 0:
			self.hero_er.kill()

			
		
			

	#精灵组更新和绘制
	def __update_sprites(self):
		self.back_group.update()
		self.back_group.draw(self.screen)
		self.hero_group.update()
		self.hero_group.draw(self.screen)
		self.hero_er_group.update()
		self.hero_er_group.draw(self.screen)
		self.enemy_group.update()
		self.enemy_group.draw(self.screen)
		self.hero.bullet_group.update()
		self.hero.bullet_group.draw(self.screen)
		self.hero_er.bullets_group.update()
		self.hero_er.bullets_group.draw(self.screen)

	#游戏结束
	def __game_over(self):
		print('游戏结束')
		pygame.quit()
		exit()

if __name__ == '__main__':
	#使用游戏，创建一个游戏对象
	game = PlaneGame()
	#开始游戏
	game.start_game()
