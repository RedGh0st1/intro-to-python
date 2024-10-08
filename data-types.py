# Starting with the following list...
planeteers = ["Earth", "Wind", "Captain Planet", "Fire", "Water"]

# Access the second value in `planeteers`
print(planeteers[1])


# Add "Heart" to the end of `planeteers`
planeteers.append("heart")
print(planeteers)

# or 
# this Creates a new list
# planeteers_new = planeteers + ["hearts"]
# print(planeteers_new)
      
# Remove "Captain Planet" from the list
planeteers.remove("Captain Planet")

# Combine `planeteers` with `rangers = ["Red", "Blue", "Pink", "Yellow", "Black"]` and save the result in a variable called `heroes`
rangers = ["Red", "Blue", "Pink", "Yellow", "Black"]
# planeteers.append(rangers) 
heroes = planeteers + rangers
print(heroes)


# Alphabetize the contents of `heroes` using a function
def alphabetize(heroes):
    return heroes.upper()


# Randomize the contents of `heroes` using a function. 
# The Python documentation might help: https://docs.python.org/2/library/random.html
heroes.random()

# Bonus: Select a random element from `heroes` using a function
# The Python documentation might help: https://docs.python.org/2/library/random.html



# Initialize a dictionary called `ninja_turtle` with the properties `name`, `weapon` and `radical`
# They should have values of "Michelangelo", "Nunchuks" and a true boolean, respectively


# Add a key `age` to `ninja_turtle`. Set it to whatever numerical value you'd like


# Remove the `radical` key-value pair from `ninja_turtle`


# Add a key `pizza_toppings` to `ninja_turtle`. Set it to an list of strings (e.g., `["cheese", "pepperoni", "peppers"]`)


# Access the first element of `pizza_toppings`


# Produce an list containing all of `ninja_turtle`'s keys using a function. 
# The Python documentation might help: https://docs.python.org/3/tutorial/datastructures.html


# Produce a list containing all of `ninja_turtle`'s values using a function


# Bonus: Write a function that prints out each key-value pair in the following format - "KEY is equal to VALUE"
#  The Python documentation might help: https://docs.python.org/3/tutorial/datastructures.html
