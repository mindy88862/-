def reverse_str(s):
	return s[::-1]

def reverse_word(s):
	word_list = s.split(' ')
	for i in range(len(word_list)):
		word_list[i] = word_list[i][::-1] #reverse_str
	return ' '.join(word_list)
a = input('problem1-A:')
print(reverse_str(a))
b = input('problem1-B:')
print(reverse_word(b))