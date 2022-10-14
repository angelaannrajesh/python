#Using If , Elif, Else keyword
name = input("Please enter your name: ")
if name == "Angela":
    print("Nice to meet you Angela")
elif name == "Andrea":
    print("Nice to meet you Andrea")
else:
    print("Sorry , I don't know you")

#Using f string
name = input("Enter your name: ")
print(f"Nice to meet you {name}")

#Using While Loop
hi = input("Please say Hi: ")
while hi != "Hi":
    hi = input("Say Hi: ")

print("Hi to you too !!!")

# Using Range
for i in range(10):
    print(i)

#Using For Loop
word = "Hello"
for letter in word:
    print(letter)

# Using While loop
count = 1
while count <= 5:
    print("Hello")
    count += 1 # We could also do it like : count = count + 1

sum = 0
for i in range(10):
    sum = sum + i
print(sum)

space = " "
name = "Angela"

for i in name:
    space = space + i + " * "
print(space)


