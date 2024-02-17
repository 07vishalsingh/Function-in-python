'''
5. Problem: Write a function that greets a user.If no name is provided, it should greet with a default name.
'''

def greet_user(name='guest'):
    return "Namaste, " + name + " !"
print(greet_user('vishal'))
print(greet_user())