print("hi")
print("ramu ")
print(2+2)
print(2**4)
print((7/10)+(9/10)-(16/10))
mystring="how are you ashu"
print(mystring[:5])    #to print the string before index 5
print(mystring[2:])      #to print the string after index 1
print(mystring[3:6])       #to print the string between indexes     //slicing
print(mystring[2:7:2])     #to print the string in gaps
print(mystring.upper())
 #to print in upper case

print(mystring.split())    #to split by spaces
print(mystring.split('o')) 
print('the {} {} {}'.format('how ','are','you')) #to append the data 
print('the {1} {2} {0}'.format('how ','are','you'))
print("the rsult is %6.2f" %(100/177)) #to limit the decimal spaces
name='ashu'
age=22
print(f'{name} is {age} year old') #new method of format
mylist=['one','two','three']  #list
mylist.append('five')
print(mylist)
mylist.pop()
print(mylist)
mylist.reverse()
print(mylist)
mydict={'name':'Ashu','age':22,'last_name':'gupta'}
print(mydict)
print(mydict.keys()) #to pint the keys
print(mydict.values()) #TO PRINT THE VALUES
print(mydict.items())   #to print the key value in pairs use items 
myset=set()
myset.add(1)
#txtfile=open('new.txt')  #to open files\
#print('new.txt'.read())   #not allowed
#print(txtfile.read())
#txtfile.seek(0)    #to read again we need to move our cursor to 0 index
#print(txtfile.read())
#with open('new.txt',mode='r') as myfile:
 #  print (myfile.read())
loc='bank'
if loc=='axis':
    print('true')
elif loc=='noida':
    print('no')
else:
    print('false')
newlist=[1,2,3,4,5,6,7,8,9]
for i in newlist:  
   if i%2==0:
     print('even')
x=0
for i in newlist:
    x=x+i
print(x)    
a=mystring.upper()
print(a)
#txtfile.seek(0)
#print(txtfile.readlines())

currentlist=[(1,2,3),(4,5,6),(7,8,4)]
print(len(currentlist))
for a,b,c in currentlist:
    print(a,b,c)
d={'key1':1,'key2':2,'key3':3}
for i in d:
    print(i)
for i in d.items() :  
    pass
    print(i)
for i in range(2,10,3):
 print(i)
print(list(range(2,8,2)))
word='adarsh'
for i,j in enumerate(word):
    print(i)
    print(j)
list1=[1,3,6,7]
list2=['ab','bc','cd','ef','hg']
list3=['bca','cda','gfd','hgs','yru'] 
for item in zip(list1,list2,list3):
   print(item)
print(list(zip(list1,list2,list3)))

min(list1)
max(list2)


#result =input('what is your name:')
#print(result)
#print(type(result))
#age=int(input('what is your age:'))
curlist=[x for x in 'how was your day']   #list comprehension
print(curlist)

nwlist=[x**2 for x in range(0,11) if x%2==0] #list comprehension

m=[]
for x in range(0,10):    # this is what we do in list comprehension
    m.append(x)
n=[x for x in range(0,11) if x%2==0]
print(n)
print(list(range(0,11,2)))

l=[]
for x in range(1,101):
    if x%3==0 and x%5==0:
        l.append('fizzbuzz') 
    elif x%3==0:
        l.append('fizz')
    elif x%5==0:
        l.append('buzz')  
    
print(l)
st='hi ashu how are you '
o=[x[0] for x in st.split() ]
print(o)

#functions 
def fun(name):
    print(f'hii {name}')
result = fun('ram')  #something new
#tuple unpacking 
alist=[('a','b'),('b','c'),('c','d'),('d','e')]
for x,y in alist:
    print(x)

#args=tuple and kargs=dict
def fun(*args):        #we can provide as many arguments as much we need
    print(sum(args)*0.5)
def fun1(**kwarg):
    if 'fruit' in kwarg:
        print(kwarg['fruit'])

fun1(fruit='apple',veggie='loki')

#mAP it will iterate every item in list and apply funtion to it 
lo=[1,2,34,5]
def square(num):
    return num**2
print(list(map(square,lo)))

#difference between map and filter
i=[1,2,3,4,5,6]
def even(num):
    if num%2==0:
        return num
print(list(map(even,i)))
print(list(filter(even,i)))


   


