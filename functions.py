def hello():
    print("Hello")

hello()

def sum(num1 = 0, num2 = 1):
    return num1 + num2

print(sum(3,4))

def fibo(n=0):
  if n<=1: return n
  return fibo(n-1 ) + fibo(n -2)
    
fibo(5)

#scope 

def mainfunction():
   color = "blue"
   def greeting(name):
      print(color)
      print (name)
   greeting("Dave")

mainfunction()

# closure

def parent_function(person):
   coins = 3
   def play_game():
      nonlocal coins
      coins -=1
      if coins > 0:
         print("\n" + person + "has" + str(coins) + "left")
   return play_game()

parent_function("Steve")