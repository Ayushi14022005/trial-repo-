print('this declarative code is used to find sum of numbers from 1 to 10')

start = 1
end = 10

def findsumnos(num):
     if num == start:
          return num
               else :
          return num + findsumnos(num-1)
     
sumofnums=(findsumnos(10))

print (sumofnums)


