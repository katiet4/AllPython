from math import e
from random import randint, random
from PIL import Image, ImageDraw
from os import listdir
# произведение матриц(возвращает произведение матриц)
def matmult(a,b):
  answer = [[] for i in range(0,len(a))]
  number = 0
  for i in range(0,len(a)):
    for p in range(0,len(b[0])):
      for r in range(0,len(a[0])):
        number += a[i][r]*b[r][p]
      answer[i].append(number)
      number = 0
  return answer

# сумма матриц(возвращает сумму матриц)
def matsum(a,b):
  answer = [[] for i in range(0,len(a))]
  for i in range(0,len(a)):
    for p in range(0,len(a[0])):
      answer[i].append(a[i][p]+b[i][p])
  return answer

# функция активации(изменяет переданную матрицу)
# (матрица слоя)
def fun_activation(put):
  for i in range(0,len(put)):
    put[i][0] = 1/(1+e**(-put[i][0]))

# поиск ошибок выходного слоя(возвращает матрицу ошибок)
# (матрица слоя, у которого надо найти ошибки;
# массив правильных ответов)
def table_errors(O,T):
  answer = [[] for i in range(len(O))]
  for i in range(len(O)):
    for r in range(len(O[0])):
      answer[i].append((T[i]-O[i][0])*((1-O[i][0])*O[i][0]))
  return answer

# поиск ошибок скрытого слоя(возвращает матрицу ошибок)
# (матрица слоя, у которого надо найти ошибки;
# матрица ошибок следующего слоя;
# матрица весов между слоями)
def table_errors2(O,Oe,Wi_j):
  summ = 0
  answer = [[] for i in range(len(O))]
  for i in range(len(answer)):
    for r in range(1):
      for g in range(len(Wi_j)):
        summ += Wi_j[g][i]*Oe[g][0]
    Fin = (1 - O[i][0])*O[i][0] 
    answer[i].append(Fin* summ)
    summ = 0
  return answer

# поиск градиента (возвращает матрицу градиентов весов)
# (матрица ошибок слоя, в который выходят синапсы;
# матрица выхода слоя;
# матрица весов)
def Grad(DB,OutA,Wi_j):
  answer = [[] for i in range(len(Wi_j))]
  for r in range(len(DB)):
    for k in range(len(OutA)):
      answer[r].append(DB[r][0] * OutA[k][0])
  return answer

def deltaWi(E, A, GradWi_j,delWi):
  answer = [[] for i in range(len(GradWi_j))]
  for i in range(len(GradWi_j)):
    for r in range(len(GradWi_j[0])):
      answer[i].append(E*GradWi_j[i][r]+A*delWi[i][r])
  return answer


# матрица для транспонации(matrix for transponation)
# (матрица для транспонации)
def transponation(put):
  between = [[] for i in range(len(put[0]))]
  for y in range(len(between)):
    for x in range(len(put)):
      between[y].append(put[x][y])
  return between

def learning(Li,e,Wi_j,what,E,A,deltaWi_j):
  Hd = table_errors2(Li, e, Wi_j)
  #print("Hd: " + str(Hd))

  Gi_j = Grad(e, Li, Wi_j)
  #print("G"+what+": " + str(Gi_j))

  deltaWi_jC = deltaWi(E, A, Gi_j, deltaWi_j)
  #print("delta"+what+": " + str(deltaWi_jC))
  for i in range(len(deltaWi_jC)):
    deltaWi_j[i] = deltaWi_jC[i]

  Wi_jC = matsum(deltaWi_j,Wi_j)
  #print("W"+what+": " + str(Wi_jC))
  for i in range(len(Wi_jC)):
    Wi_j[i] = Wi_jC[i]

  return Hd

lastCheck = {'Й': [[0], [0], [0], [0], [0], [0], [0], [1]],
             'Ц': [[0], [0], [0], [0], [0], [0], [1], [0]], 
             'У': [[0], [0], [0], [0], [0], [0], [1], [1]], 
             'К': [[0], [0], [0], [0], [0], [1], [0], [0]], 
             'Е': [[0], [0], [0], [0], [0], [1], [0], [1]], 
             'Н': [[0], [0], [0], [0], [0], [1], [1], [0]], 
             'Г': [[0], [0], [0], [0], [0], [1], [1], [1]], 
             'Ш': [[0], [0], [0], [0], [1], [0], [0], [0]], 
             'Щ': [[0], [0], [0], [0], [1], [0], [0], [1]], 
             'З': [[0], [0], [0], [0], [1], [0], [1], [0]], 
             'Х': [[0], [0], [0], [0], [1], [0], [1], [1]], 
             'Ъ': [[0], [0], [0], [0], [1], [1], [0], [0]], 
             'Ф': [[0], [0], [0], [0], [1], [1], [0], [1]], 
             'Ы': [[0], [0], [0], [0], [1], [1], [1], [0]], 
             'В': [[0], [0], [0], [0], [1], [1], [1], [1]], 
             'А': [[0], [0], [0], [1], [0], [0], [0], [0]], 
             'П': [[0], [0], [0], [1], [0], [0], [0], [1]], 
             'Р': [[0], [0], [0], [1], [0], [0], [1], [0]], 
             'О': [[0], [0], [0], [1], [0], [0], [1], [1]], 
             'Л': [[0], [0], [0], [1], [0], [1], [0], [0]], 
             'Д': [[0], [0], [0], [1], [0], [1], [0], [1]], 
             'Ж': [[0], [0], [0], [1], [0], [1], [1], [0]], 
             'Э': [[0], [0], [0], [1], [0], [1], [1], [1]], 
             'Ч': [[0], [0], [0], [1], [1], [0], [0], [0]], 
             'С': [[0], [0], [0], [1], [1], [0], [0], [1]], 
             'М': [[0], [0], [0], [1], [1], [0], [1], [0]], 
             'И': [[0], [0], [0], [1], [1], [0], [1], [1]], 
             'Т': [[0], [0], [0], [1], [1], [1], [0], [0]], 
             'Ь': [[0], [0], [0], [1], [1], [1], [0], [1]], 
             'Б': [[0], [0], [0], [1], [1], [1], [1], [0]], 
             'Ю': [[0], [0], [0], [1], [1], [1], [1], [1]],
             'Я': [[0], [0], [1], [0], [0], [0], [0], [0]],
             'Ё': [[0], [0], [1], [0], [0], [0], [0], [1]]}
TrueAnswer ={'Й': [0, 0, 0, 0, 0, 0, 0, 1], 'Ц': [0, 0, 0, 0, 0, 0, 1, 0],
             'У': [0, 0, 0, 0, 0, 0, 1, 1], 'К': [0, 0, 0, 0, 0, 1, 0, 0],
             'Е': [0, 0, 0, 0, 0, 1, 0, 1], 'Н': [0, 0, 0, 0, 0, 1, 1, 0], 
             'Г': [0, 0, 0, 0, 0, 1, 1, 1], 'Ш': [0, 0, 0, 0, 1, 0, 0, 0], 
             'Щ': [0, 0, 0, 0, 1, 0, 0, 1], 'З': [0, 0, 0, 0, 1, 0, 1, 0], 
             'Х': [0, 0, 0, 0, 1, 0, 1, 1], 'Ъ': [0, 0, 0, 0, 1, 1, 0, 0], 
             'Ф': [0, 0, 0, 0, 1, 1, 0, 1], 'Ы': [0, 0, 0, 0, 1, 1, 1, 0], 
             'В': [0, 0, 0, 0, 1, 1, 1, 1], 'А': [0, 0, 0, 1, 0, 0, 0, 0], 
             'П': [0, 0, 0, 1, 0, 0, 0, 1], 'Р': [0, 0, 0, 1, 0, 0, 1, 0], 
             'О': [0, 0, 0, 1, 0, 0, 1, 1], 'Л': [0, 0, 0, 1, 0, 1, 0, 0], 
             'Д': [0, 0, 0, 1, 0, 1, 0, 1], 'Ж': [0, 0, 0, 1, 0, 1, 1, 0], 
             'Э': [0, 0, 0, 1, 0, 1, 1, 1], 'Ч': [0, 0, 0, 1, 1, 0, 0, 0], 
             'С': [0, 0, 0, 1, 1, 0, 0, 1], 'М': [0, 0, 0, 1, 1, 0, 1, 0], 
             'И': [0, 0, 0, 1, 1, 0, 1, 1], 'Т': [0, 0, 0, 1, 1, 1, 0, 0], 
             'Ь': [0, 0, 0, 1, 1, 1, 0, 1], 'Б': [0, 0, 0, 1, 1, 1, 1, 0],
             'Ю': [0, 0, 0, 1, 1, 1, 1, 1], 'Я': [0, 0, 1, 0, 0, 0, 0, 0],
             'Ё': [0, 0, 1, 0, 0, 0, 0, 1]}
X = []
allFiles =listdir("C:\\abd")
img = Image.open("C:\\abd\\"+allFiles[0])
pix = img.load()
for i in range(50):
  for r in range(50):
    a = pix[i,r][0]
    b = pix[i,r][1]
    c = pix[i,r][2]
    if a != 255 or b != 255 or c != 255:
      X.append([1])
    else:
      X.append([0])
T = TrueAnswer[allFiles[0][0:1].upper()]



W1_2 = [[random() for r in range(2500)] for i in range(12)]
W5_6 = [[random() for r in range(12)] for i in range(14)]
W6_7 = [[random() for r in range(14)] for i in range(12)]
W7_8 = [[random() for r in range(12)] for i in range(8)]
with open("log.txt",'w') as write:
  print("W1_2 = " + str(W1_2) + "\n" +  "W2_3 = " + str(W2_3) + "\n" + "W3_4 = " + str(W3_4) + "\n" +
    "W4_5 = " + str(W4_5) + "\n" + "W5_6 = " + str(W5_6) + "\n" + "W6_7 = " + str(W6_7) + "\n" +
    "W7_8 = " + str(W7_8),file = write)
index = 1
E = 0.2
A = 0.2
deltaW7_8 = [[0 for p in range(len(W7_8[0]))] for i in range(len(W7_8))]
deltaW6_7 = [[0 for p in range(len(W6_7[0]))] for i in range(len(W6_7))]
deltaW5_6 = [[0 for p in range(len(W5_6[0]))] for i in range(len(W5_6))]
deltaW1_2 = [[0 for p in range(len(W1_2[0]))] for i in range(len(W1_2))]
for i in range(1500):

  L2 = matmult(W1_2,X) 
  fun_activation(L2)
  #print("L2: " + str(L2))

  L6 = matmult(W5_6,L5)
  fun_activation(L6)
  #print("L6: " + str(L6))

  L7 = matmult(W6_7,L6)
  fun_activation(L7)
  #print("L7: " + str(L7))

  O = matmult(W7_8,L7)
  fun_activation(O)
  #print("O: " + str(O))
  #print("T: " + str(T))

  # learning

  Oe = table_errors(O,T)
  #print("Oe: " + str(Oe))
  #def learning(Li,e,Wi_j,what,E,A,deltaWi_j):

  Hd1 = learning(L7,Oe,W7_8,"7_8",E,A,deltaW7_8)
  Hd2 = learning(L6,Hd1,W6_7,"6_7",E,A,deltaW6_7)
  Hd3 = learning(L5,Hd2,W5_6,"5_6",E,A,deltaW5_6)
  Hd4 = learning(L4,Hd3,W4_5,"4_5",E,A,deltaW4_5)
  Hd5 = learning(L3,Hd4,W3_4,"3_4",E,A,deltaW3_4)
  Hd6 = learning(L2,Hd5,W2_3,"2_3",E,A,deltaW2_3)
  learning(X,Hd6,W1_2,"1_2",E,A,deltaW1_2)

  if index >= len(allFiles):
    index = 0
  X.clear()
  img = Image.open("C:\\abd\\"+allFiles[index])
  pix = img.load()
  for j in range(50):
    for r in range(50):
      a = pix[j,r][0]
      b = pix[j,r][1]
      c = pix[j,r][2]
      if a != 255 or b != 255 or c != 255:
        X.append([1])
      else:
        X.append([0])
  T = TrueAnswer[allFiles[index][0:1].upper()]
  index+=1
  print(i)
#print("W7_8: " + str(W7_8))
#print("W6_7: " + str(W6_7))
#print("W5_6: " + str(W5_6))
#print("W4_5: " + str(W4_5))
#print("W3_4: " + str(W3_4))
#print("W2_3: " + str(W2_3))
#print("W1_2: " + str(W1_2))

with open("log2.txt",'w') as write:
  print(str(W1_2)+"|" + str(W2_3) + "|" + str(W3_4) +"|"
   + str(W4_5) +"|" + str(W5_6) +"|" + str(W6_7) +"|"
    + str(W7_8),file = write)