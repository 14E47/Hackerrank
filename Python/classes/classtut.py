class Dog:
    def __init__(self,name):

        self.name=name

    def bark(self):
        print("woof")

    def meet(self,d2):
        print(self.name)
        print(d2.name)

    def __add__(self,d2):
        print(self.name+d2.name)


a = Dog('abc')
b = Dog ('cde')

a.bark()
a.meet(b)
a+b