# class Circle():
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def circum(self):
#         return self.pi*self.radius*self.radius

# c1=Circle(2)
# print(c1.circum())
# class Animal(Circle):
#     def __init__(self):
#         Animal.__init__(self)
#         print("i am a animal constructor")

# class Dog():
#     def __init__(self):
#         print("bark")
# class Cat():
#     def __init__(self):
#         print("meow")
# niko=Dog()
# mili=Cat()



# for i in [niko,mili]:
#     print(type(i))


class Animal():

    def __init__(self,name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):

    def __init__(self,name,age,height):
        Animal.__init__(self)
        name = name
        self.age = age
        self.height = height
    def speak(self):
        print("i am dog")


class Cat(Animal):

    def __init__(self,name,age,height):
        Animal.__init__(self,name)
        Animal.name = name
        self.age = age
        self.height = height
    def speak(self):
        print("i am cat")

newdog = Cat("adarsh",13,11) 

newdog.speak()

try:
    f=open('new.txt',mode='w')
    f.write('this is a new file')
except:
    print('an error occured')
else:
    print('all went well')
finally:
    print("all done")




#decorator

    
def my_decorator(func):
    def new():
        print('decorator output 1')
        func()
        print('decortaor output 2')
    return new
@my_decorator
def hii():
    print("ok normal function")


    
hii()
#generATOR 
def cr_cubes(n):
    for i in range(n):
        yield i**3
        
       

for i in cr_cubes(10):  
  print(i)

  
from collections import Counter,defaultdict
#COUNTER CONVERST LIST INTO DICT ON THE ASIS OF INDEX
list1=[1,1,2,3,1,3,4,2,1,2,2,3,4,32]
print(Counter(list1))


d={'A':10}
d=defaultdict(lambda:0)
print(d['c'])



# 