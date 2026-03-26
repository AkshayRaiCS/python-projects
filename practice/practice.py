# %%

x = int(input("enter x"))
y = int(input("enter y"))
z = x/y
print(f"{z:.2f}")




# %%


# %%
num = int(input("enter number"))
if num%2==0:
  print("even number")
else:
  print("odd number")

# %%
x=int(input("enter x"))
y=int(input("enter y"))


if x>y or x<y:

  print("not equal")
else:
  print("EQUAL")


# %%
score = int(input("enter score"))
if score>=90:
  print("grade a")
elif score>=80:
  print("grade b")
elif score>=70:
  print("grade c")
elif score>=60:
  print("grade d")
else:
 print("grade f")

# %%
x = int(input("enter x"))
y = int(input("enter y"))
z = x/y
print(round(z,2))


# %%
def hello():
  print("hello")
name = input("enter your name:")
hello()
print(name)

# %%
def hello(to):
  print("hello,", to)
name = input("enter your name:")
hello(name)


# %%
def hello():
    print("hello", name)
name = input("enter your name:")

hello()

# %%
name = "akshay"

def test():
    print(name)

name = "ravi"
test()

# %%
x = 10

def test():
    x=5
    print(x)


test()

# %%
def hello(to="world"):
  print("hello,", to)

hello()
name=input("whats your name?:")
hello(name)

# %%
def main():
  name=input("whats your name?")
  hello()

def hello(to):
  print("hello", to)

  main()

# %%
x =float(input("enter x"))
y =float(input("enter y"))
div = x/y
print(round(div,2))

# %%
x =float(input("enter x"))
y =float(input("enter y"))
sum = round(x+y)
print((f"sum is {sum:,}"))

# %%
def cube(n):
    return n**3,n*n,pow(n,1)



def main():
  x = int(input("enter a number:"))
  print("the first 3 powers of number is:", cube(x))

main()

# %%
x = input("enter your statement")

if x=="how are you":
  print("i am fine")
else:
  print("i dont understand")

# %%
def main():
  x = int(input("whats the number g"))
  if (x%2==0):
    print("even")
  else:
    print("odd")
main()






# %%
name = input("whats your name").title()
match name:
  case "name1" | "name2":
    print("1")
  case "name3" | "name5":
    print("2")
  case "name4":
    print("3")
  case _:
    print("WHO??!!")

# %%
i =0
while i<3:
  print("meow")
  i+=1

# %%
for i in range(0,3):
  print("meow")

# %%
i = int(input("number of time the cat meows:"))
print("meow \n"*i, end="")

if(i<=0):
  print("write proper number nigga")

# %%
while True:
  n = int(input("number of time the cat meows:"))
  if n>0:
    break

for i in range(n):
  print("meow")

# %%


# %%
def main():
    n = get_no()
    meow(n)

def get_no():
  while True:
    n = int(input("whats the number of time the cat meows:"))
    if n>0:
      return n
def meow(n):
  for _ in range(n):
    print("meow")



main()

# %%
students = ["name1", "name2", "name3"]
print(students[0])

# %%
students = ["name1", "name2", "name3"]
for student in students:
  print(student)

# %%
students = ["name1", "name2", "name3"]
for i in range(len(students)):
    print(i, students[i])

# %%
students = ["name1", "name2", "name3"]
for x in enumerate(students):
  print(x)

# %%
for x, y in enumerate("hi"):
    print(y, x)

# %%
x,*y,z = (1,3)
print(x,y,z)

# %%
students = {
    "name1":"school1",
    "name2":"school12",
    "name3":"school13",
    "name4":"school14",
}
for student in students:
  print(student, students[student],sep=" - ")


# %%
students = {
    "name1":"school1",
    "name2":"school12",
    "name3":"school13",
    "name4":"school14",
}
for key, value in students.items():
    print(key, value)

# %%

    words = ["ok", "hi"]

print(words[0][0])   # first letter of first word
print(words[1][-1])  # last letter of second word

# %%
words = ["ok", "hi"]
for i, word in enumerate(words):
  if i==0:
    print(word[0])
  else:
    print(word[-1])



# %%
students = [
    {"name":"name1", "school":"school1", "vehicle":"car"},
    {"name":"name2", "school":"school2", "vehicle":"bike"},
    {"name":"name3", "school":"school3", "vehicle":"bus"},
]
for student in students:
  print(student["name"],student["school"],student["vehicle"],sep="-")

# %%
def main():
  print_c(3,3)


def print_c(width,height):
  for i in range(3):
      print("0"*width)
      for j in range(i-1):
        print("0"*height)
main()

# %%
def main():
  print_c(3,3)


def print_c(width,height):
  for i in range(height):
      print("0"*width)
main()

# %%
def main():
  size=int(input("enter size"))
  print_brick(size)

def print_brick(size):
  for i in range(size):
    print("0"*size)

main()

# %%
def main():
  size=int(input("enter size"))
  print_brick(size)

def print_brick(size):
  for i in range(size):
    for j in range(size):
      print("0",end="")
    print()


main()

# %%
try:
  x = int(input("whats x?"))
  print(f"x is {x}")
except ValueError:
  print("x is not an integer")

# %%


# %%
try:
  x = int(input("whats x?"))

except ValueError:
  print("x is not an integer")
else:
  print(f"x is {x}")



# %%
while True:
  try:
    x = int(input("whats x?"))

  except ValueError:
     print("x is not an integer")
  else:
    break

print(f"x is {x}")

# %%
def take_x():
  while True:
    try:
      return int(input("whats x?"))


    except ValueError:
      pass

take_x()


# %%
import random
asi = random.choice(["a bunks his classes tomorrow","a attends all the classes"])
print(asi)



# %%
from random import choice
asi = choice(["a bunks hhis classes tomorrow","a attends all the classes"])
print(asi)

# %%
import random
x = random.randint(5,6)
print(x)

# %%
import random
name1 = input("Enter name 1: ")
name2 = input("Enter name 2: ")
name3 = input("Enter name 3: ")

print(" Ace = 17\n King = 15\n Queen = 13\n Jack = 11")
King = 15
Queen =13
Jack = 11
Ace = 17
cards = [f"{King}",f"{Jack}",f"{Queen}","10","9","8","7",f"{Ace}","6"]
random.shuffle(cards)
a,b,c = cards[0:3],cards[3:6],cards[6:9]
scores = {
    f"{name1}": sum(map(int, a)),
    f"{name2}": sum(map(int, b)),
    f"{name3}": sum(map(int, c))
}

winner = max(scores, key=scores.get)

print("Winner:", winner)


# %%
import random
bombsquad_trio = ["name1","name2","name3"]
random.shuffle(bombsquad_trio)
print("the order of winning be",bombsquad_trio)

# %%
import statistics
print(statistics.mean([95,100]))

# %%
import sys
print("hello, my name is",sys.argv[1])


# %%
import sys
if len(sys.argv) > 2:
  print("too less arguments")
elif len(sys.argv) < 2:
  print("way too many arguments")
else:
  print("my name is,",sys.argv[1])

# %%
#pip is a program which comes with python that allows us to install packages onto device
#packages are 3rd party libraries which can be used by us
#apis - connect to thirdparty and download it and use it in our code
#request libraries allows you to request access on web,net




# %%
import requests
import json

term = input("enter band")

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=40&term=" + term
)

trak = response.json()
for track in trak["results"]:
    print(track["trackName"])




# %%
email = input("enter your email bro:")
username, domain = email.split("@")
if "." in domain and username:
    print("valid")
else: 
    print("invalid")

# %%
import re
email = input("whats your input?").strip()
if re.search(r".+@.+\.edu",email):
    print("valid")
else: 
    print("invalid")


