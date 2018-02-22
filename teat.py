# -*- coding: utf-8 -*-
import pygame
import random
from sys import exit
#向sys模块借一个exit函数用来退出程序

class enemy:
	"""docstring for enemy"""
	def restart(self):
		self.x=random.randint(50,400)
		self.y=random.randint(-200,-50)
		self.speed=random.random()+0.1

	def __init__(self):
		self.restart()
		self.image = pygame.image.load('img\\enemy.jpg').convert_alpha()

	def move(self):
		if self.y<800:
			self.y+=self.speed
		else:
			self.restart()

class bullet:
	"""docstring for bullet"""
	def __init__(self):
		self.x=0
		self.y=-1
		self.image=pygame.image.load('img\\bullet.jpg').convert_alpha()
		self.active=False

	def move(self):
		#激活状态向上动
		if self.active:
			self.y-=3
		#超出屏幕变为不激活
		if self.y<0:
			self.active=False

	def restart(self):
		mouseX,mouseY=pygame.mouse.get_pos()
		self.x=mouseX-self.image.get_width()/2
		self.y=mouseY-self.image.get_height()/2
		self.active=True

pygame.init()
screen=pygame.display.set_mode((600,800),0,32)
pygame.display.set_caption("Hello world!")
background=pygame.image.load('img\\m.jpg').convert()
plane=pygame.image.load('img\\plane.jpg').convert_alpha()
bullets=[]
#add 5 bullets
for i in range(5):
	bullets.append(bullet())
count_b=len(bullets)
#即将激活的子弹序号
index_b=0
#发射间隔时间
interval_b=0

enemys=[]
for i in range(5):
	enemys.append(enemy())

def checkhit(enemy,bullet):
			if(bullet.x > enemy.x and bullet.x < enemy.x + enemy.image.get_width()) and (bullet.y > enemy.y and bullet.y < enemy.y + enemy.image.get_height()):
				enemy.restart()
				bullet.active=False

while True:
#游戏主循环
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			#接收到退出事件退出
			pygame.quit()
			exit()
		if event.type==pygame.MOUSEBUTTONDOWN:
			background=pygame.image.load('img\\2.jpg').convert()
		screen.blit(background,(0,0))
		#画背景图片
#绘制子弹
		#发射时间间隔递减
		interval_b-=1
		#间隔《0激活一颗
		if interval_b<0:
			bullets[index_b].restart()
			interval_b=100
			#序号递增
			index_b=(index_b+1)%count_b
		#判断子弹状态
		for b in bullets:
			#处于激活状态的移动绘制
			if b.active:
				for e in enemys:
					checkhit(e,b)
				b.move()
				screen.blit(b.image,(b.x,b.y))
#绘制敌机
		for e in enemys:
			e.move()
			screen.blit(e.image,(e.x,e.y))

		x,y=pygame.mouse.get_pos()
		#get 鼠标位置
		#飞机位置为鼠标位置
		x-=plane.get_width()/2
		y-=plane.get_height()/2
		screen.blit(plane,(x,y))
		#draw plane
		pygame.display.update()
		#刷新画面
		
