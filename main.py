first_name = "Chris"
last_name = "Onsando"
full_name = first_name + last_name

age = 19
age += 1

height = 250.20

human = True

school = 'university'

residence = 'Nairobi'

profession = 'Software Development'

hobbies ='Table Tennis, Swimming, Watching Documentaries'

print("My names "+full_name, end="...")
print("My age is: "+str(age))
print("My height is: "+str(height)+"cm")
print("Are you human: "+str(human))
print("Am currently in the "+str(school))
print("Am currently living in "+str(residence))
print("Am currently in the profession of "+str(profession))
print("Currently my hobbies are: "+str(hobbies))
print(type(age))
print(type(height))
print(type(human))
print(type(school))
print(type(residence))
print(type(profession))
print(type(hobbies))
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
print(0x123)
print('I\'m Chris Python.')
print(True > False)
print(True < False)
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
print(2+2)
print(7//2)
print("skaehub"[:3])
print(r'foo\\bar\nbaz')
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))
print("The Hypotenuse length is", )
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
var = 1
account_balance = 1000.0
client_name = 'Chris Kiki'
print(account_balance, client_name)
print(client_name)
name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

print("\nPress Enter to end the program.")
input()
print("THE END.")
print("What's the next program?")
print("Proceed")
num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ") 
print(num_1 + num_2) 
my_input = input("Enter something: ") 
print(my_input * 3) 
def reverse(string):
	string = "".join(reversed(string))
	return string
s = "Chris"
print ("The reversed string(using reversed) is : ")
print (reverse(s))
thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

  thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

  thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

  thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


import random

print(random.randrange(1, 10))
for x in "chromatography":
  print(x) 
