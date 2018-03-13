import pygame
import random
#游戏屏幕大小
SCREEN_RECT = pygame.Rect(0,0,480,600)
#定时常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

#派生精灵子类
class GameSprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed=1):
		#调用父类的初始化方法
		super().__init__()
		#加载图片
		self.image = pygame.image.load(image_name)

		#设置尺寸。image的get_rect()方法可以返回pygame.Rect(0,0,图像宽,图像高)的对象
		self.rect = self.image.get_rect()
		#记录速度
		self.speed = speed

	def update(self,*args):
		#默认在垂直方向移动
		self.rect.y += self.speed


class Background(GameSprite):
	def __init__(self,image_name):
		super().__init__(image_name)

	def update(self):
		super().update()
		if self.rect.y == SCREEN_RECT.height:
			self.rect.y = -self.rect.height



class Hero(GameSprite):
	def __init__(self,image_name):
		super().__init__(image_name)
	 	#初始化位置
	 	#英雄的宽度中心点位置
		self.rect.centerx = 351
	 	#英雄底部距离屏幕高度
		self.rect.bottom = SCREEN_RECT.bottom-20
		self.panduan = False
		self.panduana = False
		self.panduanb = False
		self.panduanc = False
		self.bullet_group = pygame.sprite.Group()


	def update(self):
		if self.panduan == True and self.rect.y > 0:
			self.rect.y -= 5
		if self.panduana == True and self.rect.y<SCREEN_RECT.height-self.rect.height:
			self.rect.y += 5
		if self.panduanb == True and self.rect.x > 0:
			self.rect.x -= 5
		if self.panduanc == True and self.rect.x<SCREEN_RECT.width-self.rect.height:
			self.rect.x += 5
		



	def fire(self):
		for i in (1,2,3):
			#创建子弹精灵
			#bullet = Bullet()
			#设置精灵的位置
			bullets = Bullet('./images/bullet1.png')
			bullets.image = pygame.transform.scale(bullets.image,(3,7))
			bullets.rect.bottom = self.rect.y - 15*i
			bullets.rect.centerx = self.rect.centerx
			self.bullet_group.add(bullets)
#敌机类
class Enemy(GameSprite):
	
	def __init__(self,image_name):
		super().__init__(image_name)
		#设计敌机的随机速度
		self.speed = random.randint(1,3)
		#设置敌机初始位置
		self.rect.bottom = 0
		#这里是屏幕的宽减去敌机的宽
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)



	def update(self):
		super().update()
		#判断飞机是否飞出屏幕，飞出需从精灵组中删除
		if self.rect.y >= SCREEN_RECT.height:
			self.kill()

			


#子弹精灵
class Bullet(GameSprite):
	def __init__(self,image_name):
		super().__init__(image_name,-10)

	def update(self):
		super().update()
		if self.rect.bottom < 0 :
			self.kill()


#英雄2类
class Hero_er(GameSprite):

	def __init__(self,image_name):
		super().__init__(image_name)
		#初始位置
		self.rect.centerx = 117
		self.rect.bottom = SCREEN_RECT.bottom - 20
		self.panduand = False
		self.panduane = False
		self.panduanf = False
		self.panduang = False
		self.bullets_group = pygame.sprite.Group()
	def update(self):
		if self.panduand == True and self.rect.y > 0:
			self.rect.y -= 5
		elif self.panduane == True and self.rect.y < SCREEN_RECT.height-self.rect.height:
			self.rect.y += 5
		elif self.panduanf == True and self.rect.x > 0:
			self.rect.x -= 5
		elif self.panduang == True and self.rect.x < SCREEN_RECT.width-self.rect.width:
			self.rect.x += 5

	def zid(self):
		for i in (1,2,3):
				#创建子弹精灵
			#bullet = Bullet()
			#设置精灵的位置
			bulleta = Bullet('./images/bullet1.png')
			bulleta.image = pygame.transform.scale(bulleta.image,(3,7))
			bulleta.rect.bottom = self.rect.y - 15*i
			bulleta.rect.centerx = self.rect.centerx
			self.bullets_group.add(bulleta)
