# nayan > nayan ==> pallindrom string

x = "nayan"
y = "ram"

class B:

    def __init__(self):
        self._result = True
    
    @property
    def pallindrom(self):
        print("return in getter")
        return self._result
    
    @pallindrom.setter
    def pallindrom(self, x):
        print("Check in setter")
        if x != x[::-1]:
            self._result = False
        else:
            self._result = True

my = B()
my.pallindrom = x
print(my.pallindrom)

my = B()
my.pallindrom = y
print(my.pallindrom)
