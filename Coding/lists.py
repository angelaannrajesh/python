# routine = ["wake", "brush", "wash", "eat"]
# random = ["HELLO", 12, 0.1, False, True, [], 0.43, -3]
name = ["Jessica", "Katie", "Scarlette", "Molly"]
# name[0] = "Sophie"
# name.append("Olivia")
print(name.append('ABC'))

name = ["Jessica", "Katie", "Scarlette", "Molly"]
print(name.extend("ABC"))
# name.extend("ABC")

print(name[3])
list(range(1,5)) # [1, 2, 3, 4]
list("HI")# ["H","I"]
list() # []
routine = []
type(routine) # It's still a list

# Append and Extend

numbers = ["1", "2", "3"]
numbers.append("4")
print(numbers)
# ['1', '2', '3', '4']

alphabets = ["a","b","c","d"]
alphabets.extend("e")
print(alphabets)
# ['a', 'b', 'c', 'd', 'e']

letters = ["f","g"]
alphabets.extend(letters)
print(alphabets)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

family1 = ["Rajesh","Donna"]
family2 = ["Angela","Andrea"]
family1.append(family2)
print(family1)
# ['Rajesh', 'Donna', ['Angela', 'Andrea']]

# Insert

names = ["Amelia", "Bella", "Carlos", "Esther"]
names.insert(3,"Daniel")
print(names)
# ['Amelia', 'Bella', 'Carlos', 'Daniel', 'Esther']

number = ["one","two","three","four","five","six","seven","eight","nine"]
number.insert(9,"ten")
print(number)
# ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

# List Slices

rooms = ["toilet","kitchen","entrance","garage","dining","bedroom"]
print(rooms[0:4])
print(rooms[0:])
# ['toilet', 'kitchen', 'entrance', 'garage']
# ['toilet', 'kitchen', 'entrance', 'garage', 'dining', 'bedroom']

words = ["Hello","Umbrella","Pencil","You"]
words[1:3] = ["Animal","Blue"]
print(words)
# ['Hello', 'Animal', 'Blue', 'You']
# Deletation Methods

nums = [1,4,2,6,4,7,3,8]
nums.remove(4)

