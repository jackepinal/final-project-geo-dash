import random
import pygame 
class obstacle_objects():
  def __init__(self, height, width, x, y):
    self.height = height
    self.width = width
    self.x = x
    self.y = y

class player(obstacle_objects):
  def __init__(self, height, width, x, y):
    super().__init__(self, height, width, x, y)
    self.velocity_x = 15
    self.jump_y = 10
    self.life = True
    self.ground = True

  def jump_ability():
    if not self.ground:
      jump_y += 10
      self.ground = False

class spike(obstacle_objects):
  def __init__(self, height, width, x, y):
    super().__init__(self, height, width, x, y)

  def collision(player, spike):
    if spike(x) == player(x) and spike(y) == player(y):
      self.life = False