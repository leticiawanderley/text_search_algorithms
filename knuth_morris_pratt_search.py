from text_opener import text_opener

#based upon http://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
def knuth_morris_pratt_search(texts):
	text = texts[0].read().strip('\n')
	patch = texts[1].read().strip('\n')

	index = 2
	patch_char = 0
	shifts = [1] * (len(patch) + 1)
	shifts[0] = -1
	shifts[1] = 0
	#building the 'partial match' table
	while index < len(patch):
		if patch[index - 1] == patch[patch_char]:
			patch_char += 1
			shifts[index] = patch_char
			index += 1
		elif patch_char > 0:
			patch_char = shifts[patch_char]
		else:
			shifts[index] = 0
			index += 1
	size_found = 0
	text_index = 0
	while text_index + size_found < len(text): 
		if patch[size_found] == text[size_found + text_index]:
			if size_found == len(patch) - 1:
				return True
			size_found += 1
		else:
			if shifts[size_found] > -1:
				text_index = text_index + size_found - shifts[size_found]
				size_found = shifts[size_found]
			else:
				size_found = 0
				text_index += 1
	return False		
		
# my own asserts <3
assert(knuth_morris_pratt_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch1.txt')))
assert(knuth_morris_pratt_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch2.txt')))
assert(knuth_morris_pratt_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch3.txt')))
assert(not knuth_morris_pratt_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_not_a_patch.txt')))

# teacher asserts
assert(knuth_morris_pratt_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra1.txt')))
assert(knuth_morris_pratt_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra4.txt')))
assert(knuth_morris_pratt_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra2.txt')))
assert(knuth_morris_pratt_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra3.txt')))
assert(knuth_morris_pratt_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra5.txt')))

assert(not knuth_morris_pratt_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra3.txt')))
assert(not knuth_morris_pratt_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra2.txt')))
assert(not knuth_morris_pratt_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra5.txt')))
assert(not knuth_morris_pratt_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra1.txt')))
assert(not knuth_morris_pratt_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra4.txt')))
