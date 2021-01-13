#Declaring and Printing Lists
print("Section 1")
sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
print(sea_creatures)
print()

#Indexing Lists
print("Section 2")
print(sea_creatures[1])
print()

print("Section 3")
print(sea_creatures[0], end = ' ')
print(sea_creatures[1], end = ' ')
print(sea_creatures[2], end = ' ')
print(sea_creatures[3], end = ' ')
print(sea_creatures[4])

sea_creatures[0] = 'shark'
sea_creatures[1] = 'cuttlefish'
sea_creatures[2] = 'squid'
sea_creatures[3] = 'mantis shrimp'
sea_creatures[4] = 'anemone'

print()

#If we call the list sea_creatures with an index number of any that is greater than 4, it will be out of range as it will not be valid:
#print(sea_creatures[18])
#print()
#Output = IndexError: list index out of range

print("Section 4")
print('Sammy is a ' + sea_creatures[0])
print()

#Modifiying List Items
print("Section 5")
sea_creatures[1] = 'octopus'
print(sea_creatures)
print()

#Adding List Items
print("Section 6")
sea_creatures = ['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone']
print("Current sea creatures list", sea_creatures)
print()

add_creature = input("Please enter the name of the creature you would like to add ")
sea_creatures.append(add_creature)
print()

print("New list of sea creatures", sea_creatures)
print()

#Removing List Items
print("Section 7")
sea_creatures = ['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone', 'yeti crab']

del sea_creatures[1]
print(sea_creatures)