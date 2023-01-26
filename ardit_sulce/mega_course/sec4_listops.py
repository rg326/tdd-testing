# List Operations and Atrributes

monday_temps = [9.1, 8.8, 7.5]

#Append - Append object to the end of the list (push)

monday_temps.append(8.1)

#append(self, object, /)

#First parameter of the append method is actually "self", which refers to the class list of which append is a part of.
monday_temps = (9.6)

#Index - Return first index of value. Raises ValueError if the value is not present.
monday_temps.index(8.8)

#index(self, value, start = 0, stop = 0)

#Clear - Remove all items from the list
monday_temps.clear()

#clear(self, /)

# Get item with index #
monday_temps.__getitem__(1)
# Alt
monday_temps[1]

len(monday_temps)

# Item Slices
monday_temps[1:4]

# This will give you items # - # (upper limit exclusive)

# Access last item on the list, since there are only 4 items in the list
monday_temps[3:5]

# More intuitive, still has same result
monday_temps[3:]

monday_temps[:4]

# Neg Indexing
monday_temps[-1]

##access last item in list

# list slicing using neg indexing
monday_temps[-2:]

monday_temps[-4,-2]

#start from beginning of list
monday_temps[-5,-2]

monday_temps[-5,-1]