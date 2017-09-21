import math

s0 = 10013
seed = s0
multiplier = 16807.0
modulus = 2147483647.0
randomtable = None

def park_miller_randomizer():
  global seed
  seed = (multiplier * seed) % modulus
  return seed / modulus

def rseed(n):
  if n:
    seed = n
  else:
      seed = s0
  randomtable = None

def r ():
  global randomtable
  if randomtable == None:
    randomtable = []
    for i in range(1,98):
      randomtable.append(park_miller_randomizer())
  x = park_miller_randomizer()
  i = math.floor(97*x)
  x, randomtable[int(i)] = randomtable[int(i)], x
  return x