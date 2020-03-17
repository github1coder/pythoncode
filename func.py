#print('abc',end='\n')


#def func (a,b,c):
 #    print('%s'%a)
  #   print('%s' %b)
   #  print('%s'%c)


#func(1,c=3,b=2)


#def howlong(first ,* other):
 #   return 1+len (other)

#print(howlong(123,234,235))

#global var1
#var1=456

#list1 = [1 ,2,3]
#it = iter(list1)
#print(next(it))


#for i in range(10,20,2):
 #   print(i)

#def  frange(start,stop,step):
 #   x = start
  #  while x<stop :
   #     yield x
    #  x+=step

#for i in frange(10,20,0.5):
   # print(i)

#add=lambda x,y : x+y
#print(add(2,3))

#help(filter)

# a=[1,2,3,4,5,6,7]
# list(filter(lambda x:x>2 , a))

# a=[1,2,3]
# b=[5,6,7]
# print(list(map(lambda x,y:x+y  ,a,b)))

# from functools import reduce
# print(reduce(lambda x,y:x+y , [2,3,4]),1)

# for i in zip((1,2,3),(4,5,6)):
#    print(i)

dicta={'a':'aa' , 'b':'bb'}
dictb=zip(dicta.values(),dicta.keys())
print(dict(dictb))