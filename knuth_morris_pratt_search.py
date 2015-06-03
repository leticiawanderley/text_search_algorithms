from text_opener import text_opener

def knuth_morris_pratt_search(texts):
	text = texts[0].read().strip('\n')
	patch = texts[1].read().strip('\n')

	shifts = [1] * (len(patch) + 1)
	shift = 1
	for index in range(len(patch)):
		while shift <= index and patch[index] != patch[index-shift]:
			shift += shifts[index - shift]
		shifts[index + 1] = shift 
	
	size_found = 0
	text_index = 0
	while text_index + size_found < len(text):
		if patch[size_found] == text[text_index + size_found]:
			size_found += 1
			if size_found == len(patch):
				return True
		else:
			if size_found == 0:
				text_index += 1
			else:
				text_index += size_found - shifts[size_found]
	return False
		
# my own asserts <3
assert(knuth_morris_pratt_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch1.txt')))
assert(knuth_morris_pratt_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch2.txt')))
assert(knuth_morris_pratt_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch3.txt')))
assert(not knuth_morris_pratt_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_not_a_patch.txt')))

#teacher asserts
#assert(knuth_morris_pratt_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra1.txt')))
#assert(knuth_morris_pratt_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra4.txt')))
#assert(knuth_morris_pratt_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra2.txt')))
#assert(knuth_morris_pratt_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra3.txt')))
#assert(knuth_morris_pratt_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra5.txt')))

#assert(not knuth_morris_pratt_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra3.txt')))
#assert(not knuth_morris_pratt_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra2.txt')))
#assert(not knuth_morris_pratt_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra5.txt')))
#assert(not knuth_morris_pratt_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra1.txt')))
#assert(not knuth_morris_pratt_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra4.txt')))
