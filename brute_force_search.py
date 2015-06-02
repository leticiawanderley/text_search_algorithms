from text_opener import text_opener

def brute_force_search(texts):
	text = texts[0]
	patch = texts[1]
	
	text = texts[0].read().strip('\n')
	patch = texts[1].read().strip('\n')
	patch_first_char = patch[0]
	found = False	
	for char_number in range(len(text)):
		char = text[char_number]
		index = char_number
		found = True
		for patch_char_number in range(len(patch)):
			if patch[patch_char_number] != text[index]:
				found = False
				break
			index += 1
		if found:
			break
	return found

# my own asserts <3
assert(brute_force_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch1.txt')))
assert(brute_force_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch2.txt')))
assert(brute_force_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch3.txt')))
assert(not brute_force_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_not_a_patch.txt')))

#teacher asserts
assert(brute_force_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra1.txt')))
assert(brute_force_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra4.txt')))
assert(brute_force_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra2.txt')))
assert(brute_force_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra3.txt')))
assert(brute_force_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra5.txt')))

assert(not brute_force_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra3.txt')))
assert(not brute_force_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra2.txt')))
assert(not brute_force_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra5.txt')))
assert(not brute_force_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra1.txt')))
assert(not brute_force_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra4.txt')))
