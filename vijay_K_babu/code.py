# --------------
# Code starts here
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
# Create the lists 
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class = class_1 + class_2
print(new_class)

# Append the list
new_class.append('Peter Warden')
print(new_class)
# Print updated list

new_class.remove('Carla Gentry')

# Remove the element from the list
print(new_class)
# Print the list


# Create the Dictionary
courses = {'Math' : 65, 'English' : 70, 'History' : 80, 'French' : 70, 'Science' : 60}


# Slice the dict and stores the all subjects marks in variable
variable = courses.values()

# Store the all the subject in one variable `Total`
total = sum(variable)
# Print the total
print(total)
# Insert percentage formula
percentage = (total/5)
# Print the percentage
print(percentage)



# Create the Dictionary
 
mathematics = {'Geoffrey Hinton' : 78,
'Andrew Ng' : 95,
'Sebastian Raschka' : 65,
'Yoshua Benjio'	: 50,
'Hilary Mason' : 70,
'Corinna Cortes' : 66,
'Peter Warden' : 75}


# Given string
topper = max(mathematics,key = mathematics.get)

# Create variable first_name 
first_name = topper.split()[0]

# Create variable Last_name and store last two element in the list
last_name = topper.split()[1]


# Concatenate the string
full_name = last_name + " " + first_name

# print the full_name
print(full_name)

# print the name in upper case
certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


