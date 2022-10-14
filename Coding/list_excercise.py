# It's race day and our starting grid is set! Charles sits on pole and Lando brings up the rear.
# drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George","Lando"]
# Oh dear, we've misspelled "Valtteri" as "Valterri".  Update the drivers list to include the correct spelling!
# Esteban makes it out of the pits and joins the pack just in time.  Add "Esteban" to the end of the drivers list!
# What's this? There's another group of drivers that comes out of nowhere to join the race! Add each element from the others list to the end of the drivers list. others = ["Blue", "Elton", "Colt"]
# Colt looks lost out there! He has a horrible fiery crash.  Remove the last element from the drivers list ("Colt")
# Oh dear, there's a huge crash at the front! Remove the first element from the driver's list
# And again the leader of the pack runs into trouble! He's not out of the race, but he's now moved to last place.  Remove the first driver in the list, store it in variable, and then add it to the end of the list.
# My idiotic cat, Blue, is in the middle of the pack.  Delete "Blue" from the drivers list using the remove method!
# My dog, Elton, is making a remarkable charge up the leadboard! Remove Elton from his current position in the list and insert him at index 2.
# The race is over! It's time for the podium ceremony.  Create a new list called podium that contains the first 3 elements from the drivers list. (use a slice!)
# Loop over the drivers list and print out a leadboard that includes a driver's finishing position and their name, like this:
# 1. Valtteri
# 2. Lewis
# 3. Elton
# 4. George
# 5. Lando
# 6. Esteban
# 7. Pierre

drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George","Lando"]
drivers[2] = "Valtteri"
drivers.append("Esteban")
others = ["Blue", "Elton", "Colt"]
drivers.append(others)
drivers.pop()
drivers.pop(0)
leader = drivers.pop(0)
drivers.append(leader)
others.remove("Blue")
others.remove("Elton")
drivers.insert(2, "Elton")
podium = drivers[:3]
print(podium)
print("1. Valtteri")
print("2. Lewis")
print("3. Elton")
print("4. George")
print("5. Lando")
print("6. Esteban")
print("7. Pierre")
