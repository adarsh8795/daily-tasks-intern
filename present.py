import deadlock


with open('new.txt',mode='w') as f:
    f.write('hello wor')
    deadlock.funt()
with open('new.txt',mode='r') as myfile:
   print (myfile.read())

