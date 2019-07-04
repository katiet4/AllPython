from mnist import MNIST
import numpy as np
mndata = MNIST('g')

images, labels = mndata.load_training()
X = []
s = 0
for i in images:
	print(s)
	for r in i:
		X.append([r/255]) 
	s+=1
print(X[0])