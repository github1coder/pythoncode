#file1=open('name.txt','w')
#file1.write('诸葛亮')
#file1.close()

#file2 = open('name.txt')
#print(file2.read())

#file2.close()

#file3=open('name.txt','a')
#file3.write('刘备')
#file3.close

#file4 = open('name.txt')
#print(file4.readline())
#file4.close

#file5 =open('name.txt')
#for line in file5.readlines():
 #   print(line)
  #  print('*****')


file6=open('name.txt')
print(file6.tell())
file6.read(1)
print(file6.tell())
file6.seek(5,0)
print(file6.tell())
