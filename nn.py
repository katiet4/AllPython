
from math import e
def atNumber(put,number):
  answer = [[] for i in range(0,len(put))]
  for i in range(len(put)):
    for r in range(len(put[0])):
      answer[i].append(put[i][r]*number)
  return answer
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
def fun_activation(put):
  for i in range(0,len(put)):
    put[i][0] = 1/(1+e**(-put[i][0]))
def table_errors(put,true):
  answer = [[] for i in range(0,len(put))]
  for i in range(len(put)):
    answer[i].append(true[i] - put[i][0])
  return answer
def transpanation(put):
  between = [[] for i in range(len(put[0]))]
  for y in range(len(between)):
    for x in range(len(put)):
      between[y].append(put[x][y])
  return between
def table_errors_for_hidden(xi_j,errorsback):
  between = [[] for i in range(len(xi_j))]
  summ = 0
  for p in range(len(xi_j)):
    for i in range(len(xi_j[0])):
     for r in range(len(xi_j[0])):
      summ += xi_j[p][r]
     between[p].append(round(xi_j[p][i]/summ,2))
     summ = 0
  between2 = transpanation(between)
  xi_j = between.copy()
  print(between)
  one = xi_j[0][0]
  if(len(errorsback) == 1 and len(errorsback[0]) == 1):
    answer = atNumber(between2,one)
  else:
    answer = matmult(between2,errorsback)
  return (answer,xi_j)

x1_2 = [[4.2,2.8],
        [1.24,8.76]]

x2_3 = [
        [2.8,4.2],
        [1.4,5.6] 
                      ]

y = [ [1],
      [0] ]

true=[2.48,1.5]

for i in range(1):
  hidden = matmult(x1_2,y)
  fun_activation(hidden)
  print("hidden: "+str(hidden))

  hidden2 = matmult(x2_3,hidden)
  fun_activation(hidden2)
  print("hidden2: "+str(hidden2))

  e1 = table_errors(hidden2,true)
  print("e1: "+str(e1))
  s = table_errors_for_hidden(x2_3,e1)
  e2,x2_3 = s[0],s[1].copy()
  print(x2_3)
  print("e2: "+str(e2))
  s = table_errors_for_hidden(x1_2,e2)
  print(x1_2)
  e3,x1_2 = s[0],s[1].copy()
  print(x1_2)
  print("e3: "+str(e3))
  
  