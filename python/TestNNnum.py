from functionsOFLerningNN import *
from PIL import Image
def Reading(what,file):
  strT = ''
  with open(file,'r') as read:
    for i in read:
      strT+=i
  arr = strT.split("|")
  bigArr = arr[what][1:len(arr[what])-1]
  smallArr = []
  bo = False
  s = ""
  for i in bigArr:
    if i == '[':
      s = ''
      s+='['
      bo = True
    elif i == ']':
      s+=']'
      bo == False
      smallArr.append(s)
      s=""
    elif bo:
      s+=i

  if smallArr[-1] == ']':
    smallArr.pop(-1)

  big = []
  small = []
  for i in smallArr:
    a = i[1:len(i)-1]
    aAr = a.split(', ')
    #print(aAr)
    for p in aAr:
      small.append(float(p))
    big.append(small.copy())
    small.clear()
  return big
lastCheck = {'1': [[1], [0], [0], [0], [0], [0], [0], [0], [0], [0]], 
             '2': [[0], [1], [0], [0], [0], [0], [0], [0], [0], [0]], 
             '3': [[0], [0], [1], [0], [0], [0], [0], [0], [0], [0]], 
             '4': [[0], [0], [0], [1], [0], [0], [0], [0], [0], [0]], 
             '5': [[0], [0], [0], [0], [1], [0], [0], [0], [0], [0]], 
             '6': [[0], [0], [0], [0], [0], [1], [0], [0], [0], [0]], 
             '7': [[0], [0], [0], [0], [0], [0], [1], [0], [0], [0]], 
             '8': [[0], [0], [0], [0], [0], [0], [0], [1], [0], [0]], 
             '9': [[0], [0], [0], [0], [0], [0], [0], [0], [1], [0]], 
             '0': [[0], [0], [0], [0], [0], [0], [0], [0], [0], [1]]}
TrueAnswer ={'1': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
              '2': [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], '3': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
              '4': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], '5': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
              '6': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], '7': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
              '8': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], '9': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
              '0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]}

W1_2 = Reading(0,'log8.txt')
W2_3 = Reading(1,'log8.txt')
X = []
img = Image.open("C:\\numbers.png")
pix = img.load()
for i in range(28):
  for r in range(28):
    a = pix[i,r][0]
    b = pix[i,r][1]
    c = pix[i,r][2]
    if a != 255 or b != 255 or c != 255:
      g = (a+b+c)/3
      X.append([((g*100)/255)/100])
    else:
      X.append([0])

L2 = matmult(W1_2,X) 
#print("L2: " + str(L2))
#print("L6: " + str(L6))
O = matmult(W2_3,L2)

check = [[], [], [], [], [], [], [], [], [], []]

for i in range(10):
  if O[i][0]>0.5:
   check[i].append(1)
  else:
    check[i].append(0)
print(check)
for i in lastCheck:
  if lastCheck[i] == check:
    print(i)