from mnist import MNIST
import time
from functionsOFLerningNN import *
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
X = []


mndata = MNIST('g')
images, labels = mndata.load_training()


X = [[i/255] for i in images[0]]

T = TrueAnswer[str(labels[0])]


W1_2 = [[random() for r in range(784)] for i in range(16)]
W2_3 = [[random() for r in range(16)] for i in range(10)]
index = 1
E = 0.7
A = 0.3
deltaW2_3 = [[0 for p in range(len(W2_3[0]))] for i in range(len(W2_3))]
deltaW1_2 = [[0 for p in range(len(W1_2[0]))] for i in range(len(W1_2))]
epohe = 0
downloadIter = 0
downloadEpoh = "<"
while epohe < 3:
  
  L2 = matmult(W1_2,X) 
  #print("L2: " + str(L2))
  #print("L6: " + str(L6))
  O = matmult(W2_3,L2)
  # print("O: " + str(O))
  # print("T: " + str(T))
  # print("\n\n\n\n")
  print("Index:"+str(index))
  downloadIter = index / 60000
  print("%"+str(downloadIter))
  print(downloadEpoh)
  # learning
  Oe = table_errors(O,T)
  #print("Oe: " + str(Oe))
  #def learning(Li,e,Wi_j,what,E,A,deltaWi_j):
  
  Hd2 = learning(L2,Oe,W2_3,"2_3",E,A,deltaW2_3)
  p = time.time()
  learning(X,Hd2,W1_2,"1_2",E,A,deltaW1_2)
  print(time.time()-p)
  if index >= 60000:
    print("O: " + str(O))
    print("T: " + str(T))
    print("\n\n\n\n")
    index = 0
    epohe+=1
    downloadEpoh+="="
  X.clear()
 
  X = [[i/255] for i in images[index]]
  
  T = TrueAnswer[str(labels[index])]
  index+=1

#print("W7_8: " + str(W7_8))
#print("W6_7: " + str(W6_7))
#print("W5_6: " + str(W5_6))
#print("W4_5: " + str(W4_5))
#print("W3_4: " + str(W3_4))
#print("W2_3: " + str(W2_3))
#print("W1_2: " + str(W1_2))

with open("log8.txt",'w') as write:
  print(str(W1_2) +"|" + str(W2_3),file = write)