from functools import wraps
from random import randint
def retun_word(func)->'function':
	key_and_word = {}
	@wraps(func)
	def make_word(*args,**kwargs)->'function':
		print('2')
		s = 5
		return func()
	return make_word()
@retun_word
def word(*args,**kwargs):
	print('1')
	print(args)
print(dir(Exception))