from math import e
from random import randint
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

X1 =[[1],[0],[0],
     [1],[0],[1],
     [1],[0],[0],
     [0],[0],[0]]
T1 = [1,1]
X2 =[[0],[1],[1],
     [0],[0],[1],
     [1],[0],[0],
     [0],[0],[0]]
T2 = [1,1]
X3 =[[1],[0],[0],
     [1],[1],[1],
     [1],[0],[0],
     [0],[0],[0]]
T3 = [1,1]
X4 =[[0],[0],[0],
     [0],[0],[1],
     [1],[0],[1],
     [0],[0],[1]]
T4 = [0,0]
X5 =[[0],[0],[0],
     [0],[0],[1],
     [1],[0],[0],
     [1],[1],[0]]
T5 = [0,0]
X6 =[[0],[0],[0],
     [0],[1],[1],
     [1],[1],[1],
     [0],[0],[1]]
T6 = [0,0]
W1_2 = [[0.702, 0.753, 0.842, 0.838, 0.112, 0.966, 0.5, 0.104, 0.033, 0.033, 0.975, 0.612],
    [0.31, 0.106, 0.157, 0.438, 0.048, 0.678, 0.355, 0.536, 0.399, 0.493, 0.748, 0.493],
    [0.937, 0.981, 0.7, 0.539, 0.493, 0.535, 0.62, 0.748, 0.788, 0.748, 0.493, 0.748], 
      [0.495, 0.773, 0.806, 0.2, 0.932, 0.975, 0.06, 0.612, 0.776, 0.493, 0.355, 0.355]]
W2_3 = [[0.544, 0.915, 0.84, 0.598], [0.358, 0.569, 0.114, 0.832], [0.358, 0.569, 0.114, 0.832], [0.358, 0.569, 0.114, 0.832]]

W3_4 = [[0.544, 0.915, 0.84, 0.598], [0.358, 0.569, 0.114, 0.832]]
index = 0
E = 0.7
A = 0.3
deltaW3_4 = [[0 for p in range(len(W3_4[0]))] for i in range(len(W3_4))]
deltaW2_3 = [[0 for p in range(len(W2_3[0]))] for i in range(len(W2_3))]
deltaW1_2 = [[0 for p in range(len(W1_2[0]))] for i in range(len(W1_2))]
for i in range(200):
  if index == 0:
    X = X1.copy()
    T = T1.copy()
    index += 1
  elif index == 1:
    X = X2.copy()
    T = T2.copy()
    index += 1
  elif index == 2:
    X = X3.copy()
    T = T3.copy()
    index += 1
  elif index == 3:
    X = X4.copy()
    T = T4.copy()
    index += 1
  elif index == 4:
    X = X5.copy()
    T = T5.copy()
    index += 1
  elif index == 5:
    X = X6.copy()
    T = T6.copy()
    index = 0

  L2 = matmult(W1_2,X) 
  fun_activation(L2)
  #print("L2: " + str(L2))

  L3 = matmult(W2_3,L2)
  fun_activation(L3)
  #print("L3: " + str(L3))

  #L4 = matmult(W3_4,L3)
  #fun_activation(L4)
  #print("L4: " + str(L4))

  #L5 = matmult(W4_5,L4) 
  #fun_activation(L5)
  #print("L5: " + str(L5))

  #L6 = matmult(W5_6,L5)
  #fun_activation(L6)
  #print("L6: " + str(L6))

  #L7 = matmult(W6_7,L6)
  #fun_activation(L7)
  #print("L7: " + str(L7))

  O = matmult(W3_4,L3)
  fun_activation(O)
  #print("O: " + str(O))
  #print("T: " + str(T))

  # learning

  Oe = table_errors(O,T)
  #print("Oe: " + str(Oe))
  #def learning(Li,e,Wi_j,what,E,A,deltaWi_j):

  Hd1 = learning(L3,Oe,W3_4,"3_4",E,A,deltaW3_4)

  Hd2 = learning(L2,Hd1,W2_3,"2_3",E,A,deltaW2_3)

  learning(X,Hd2,W1_2,"1_2",E,A,deltaW1_2)
print("W3_4: " + str(W3_4))
print("W2_3: " + str(W2_3))
print("W1_2: " + str(W1_2))