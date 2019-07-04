from math import e
from random import random
# произведение матриц(возвращает произведение матриц)
# функция активации(изменяет переданную матрицу)
# (матрица слоя)
def fun_activation(put):
  for i in range(0,len(put)):
    put[i][0] = 1/(1+e**(-put[i][0]))
  return put
def matmult(a,b):
  answer = [[] for i in range(0,len(a))]
  number = 0
  for i in range(0,len(a)):
    for p in range(0,len(b[0])):
      for r in range(0,len(a[0])):
        number += a[i][r]*b[r][p]
      answer[i].append(number)
      number = 0
  return fun_activation(answer)



# сумма матриц(возвращает сумму матриц)
def matsum(a,b):
  answer = [[] for i in range(0,len(a))]
  for i in range(0,len(a)):
    for p in range(0,len(a[0])):
      answer[i].append(a[i][p]+b[i][p])
  return answer



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