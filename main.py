counter = 0
find = int(input('Find Number:  '))
list = [5,3,2,4,16,6,1,2,8,9]

length = len(list)
found = False
while found == False and counter < length:
  if list[counter] == find:
    found = True
    print ('Found at position:  ', counter +1)
  else:
    counter = counter + 1
if found == False:
  print('Item not found')