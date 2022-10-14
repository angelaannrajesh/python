# def angela(name, job):
#     print(f"MY NAME IS {name}, I am a {job}")
# angela("Donna","nurse")

# def my_function(*kids):
#   print("The youngest child is " + kids[2])
#
# my_function("Emil", "Tobias", "Linus")

# def fruits(*args):
#     print(f'The fourth fruit is {args[3]}')
#
# fruits("Apple","Banana","Mango","Orange")
#
# def name(*args):
#     print(f"The youngest child is {args[1]}")
#
# name("Angela","Andrea","Rajesh")


def family(**kwargs):
    print(f'name is {kwargs["name"]}')

family(name="Rajesh", age=21)