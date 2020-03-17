#i=j

#try:
 #   i=j
#except NameError:
 #   print('年份')

#a=123
#a.append()

#except  (AttributeError,NameError)
try :
     print(1/0)
except Exception as e:
    print('%s' %e)
    
try:
    raise NameError('helloerror')
except  Exception :
    print('my custom error')

finally:
