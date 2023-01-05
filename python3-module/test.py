#/home/runner/SSON/lib/p
from SSON import SSON
class hello:
  def __init__(self):
    self.name = "world"
  def hello(self):
    return "hello, " + self.name

hi = hello()

file = SSON("hi")