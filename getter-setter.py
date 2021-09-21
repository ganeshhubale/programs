#https://www.geeksforgeeks.org/getter-and-setter-in-python/
#In Python, getters and setters are not the same as those in other object-oriented programming languages. Basically, the main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation. Private variables in python are not actually hidden fields like in other object oriented languages. Getters and Setters in python are often used when:

#We use getters & setters to add validation logic around getting and setting a value.
#To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user

class getme:
    
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        print("getter method called")
        return self._age
    
    @age.setter
    def age(self, a):
        print("Setter called")
        if (a < 18):
            raise ValueError("You are below age limit")
        print("set age")
        self._age = a

new = getme()
new.age = 19
print(new.age)

        
