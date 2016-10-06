from text_opener import text_opener

def brute_force_optimized_search(texts):
	text = texts[0]
	patch = texts[1]
	patch_first_line = patch.readline().strip('\n')
	text_lines = text.read().split('\n')
	patch_lines = patch.read().split('\n')
	
	found = False	
	for line_number in range(len(text_lines)):
		line = text_lines[line_number]
		if patch_first_line in line:
			index = line_number + 1
			found = True
			for patch_line_number in range(len(patch_lines)):
				if patch_lines[patch_line_number] not in text_lines[index]:
					found = False
					break
				index += 1
		if found:
			break
	return found

# my own asserts <3
assert(brute_force_optimized_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch1.txt')))
assert(brute_force_optimized_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch2.txt')))
assert(brute_force_optimized_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch3.txt')))
assert(not brute_force_optimized_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_not_a_patch.txt')))

# teacher asserts
assert(brute_force_optimized_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra1.txt')))
assert(brute_force_optimized_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra4.txt')))
assert(brute_force_optimized_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra2.txt')))
assert(brute_force_optimized_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra3.txt')))
assert(brute_force_optimized_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra5.txt')))

assert(not brute_force_optimized_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra3.txt')))
assert(not brute_force_optimized_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra2.txt')))
assert(not brute_force_optimized_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra5.txt')))
assert(not brute_force_optimized_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra1.txt')))
assert(not brute_force_optimized_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra4.txt')))
