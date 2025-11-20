destinations = []
print("Please enter your 5 travel destinations:")
destinations.append(input("Destination 1: "))
destinations.append(input("Destination 2: "))
destinations.append(input("Destination 3: "))
destinations.append(input("Destination 4: "))
destinations.append(input("Destination 5: "))

print("\nOriginal Travel Itenary:")
print("1. " + destinations[0])
print("2. " + destinations[1])
print("3. " + destinations[2])
print("4. " + destinations[3])
print("5. " + destinations[4])

print("\nLet's update your 2nd and 5th destinations.")
new_pos2 = input("Enter a new destination for position 2: ")
new_pos5 = input("Enter a new destination for position 4: ")

print("\nUpdated Travel Itenary:")
print("1." + destinations[0])
print("2.",new_pos2)
print("1. " + destinations[2])
print("4. " + destinations[3])
print("5.",new_pos5)


