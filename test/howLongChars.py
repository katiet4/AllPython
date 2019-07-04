chars = input('Chars: ')
how_long = 1
next_char = ''
length = int(len(chars)-1)
EndArray = ''
for i in range(length):
	back_char = chars[i+1]
	if  back_char == chars[i]:
		how_long += 1
	else:
		EndArray += chars[i]+str(how_long)
		how_long = 1
EndArray += chars[length]+str(how_long)
print(EndArray)