# Insert

waitlist = ["rosa","belinda","colt","angela","danya","umar","nivaan","isaac"
            ]
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


nums = [2,4,6,9,3,2,4]
nums.remove(4)
print(nums)

waitlist = ["rosa","belinda","colt","angela","danya","umar","nivaan","isaac"]
waitlist.pop()
waitlist.pop()
print(waitlist)

waitlist = ["rosa","belinda","colt","angela","danya","umar","nivaan","isaac"]
waitlist.pop(3)
print(waitlist)

a = 10
if a != \1:
    print("Boolean value of a is True")