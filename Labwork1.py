import math

#1
radius = float(input("Enter circle radius? "))
area = math.pi * (radius ** 2)
print(f"Circle area = {area}")

#2
celsius = float(input("Enter the temperature in Celsius? "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius} (C) = {fahrenheit} (F)")

#3
def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


num = int(input("Enter a number? "))
if is_prime(num):
  print(f"{num} is a prime number")
else:
  print(f"{num} is a NOT prime number")

#4
def is_perfect(n):
  if n <= 1:
    return False
  for i in range(1, n):
    divisors = []
    if(n%i ==0 ):
      divisors = divisors + []
  return divisors


num = int(input("Enter a number? "))
if is_perfect(num):
  print(f"{num} is a perfect number")
else:
  print(f"{num} is a NOT perfect number")

#5
color_list = ["Blue", "Yellow", "Green", "Red", "Purple"]
fav_color = input("What is your favorite color? ")

if fav_color in color_list:
  idx = color_list.index(fav_color)
  print(f"Your colod is at index {idx} in my list")
else:
  print("Sorry, I could not find your color")

#6:
print("range1", list(range(7)))
print("range2", list(range(1, 12, 3)))
print("range3", list(range(5, 0, -1)))
print("range4", list(range(6, -3, -2)))

#7
def remove_dollar_sign(s):
  return s.replace("$", "")


input_str = input("Type String: ")
result = remove_dollar_sign(input_str)

#8
def extract_even(l):
  even = []
  for i in l:
    if (i%2==0):
      even = even + [i]
  return even

print(extract_even([1, 4, 5, -1, 10]))

#9:
def factorial(n):
  kq = 1
  for i in range(1, n + 1):
    if (i == 0 ) | (i==1):
       kq == 1
    else: kq *= i
  return kq

print(factorial(5)) 
#10
def get_divisors(n):
  divisors = []
  for i in range(1, n + 1):
    if n % i == 0:
      divisors.append(i)  

  return divisors

print(get_divisors(12))

#11:
import math


def compute_distance(p1, p2):
  return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

print(compute_distance((0, 0), (3, 4)))  

#12:
def print_rectangle(m, n):
  for i in range(m):
    for j in range(n):
      if i == 0 or i == m - 1 or j == 0 or j == n - 1:
        print("*", end=" ") 
      else:
        print(" ", end=" ")
    print()  
print_rectangle(5, 8)


