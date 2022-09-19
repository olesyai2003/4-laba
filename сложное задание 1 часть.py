word = input('Введите слова: ').split()

list_a = []


for item_a_get in word:
	list_match = []
	self_get = False


	for item_a in item_a_get:
		list_match.append(item_a)
	count_i = 0
	for item in list_match:
		count_i += 1
		count_g = 0
		for x in list_match:
			count_g += 1
			if x == item and count_i != count_g:
				self_get = True

	if self_get == True:
		list_a.append(item_a_get)
		

print(list_a)