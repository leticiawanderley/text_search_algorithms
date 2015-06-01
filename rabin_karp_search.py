from text_opener import text_opener

#based on http://stackoverflow.com/questions/22216948/python-rabin-karp-algorithm-hashing
def rabin_karp_search(texts):
	text = texts[0].read().strip('\n')
	patch = texts[1].read().strip('\n')
	text_len = len(text)
	patch_len = len(patch)
	modulator = 11
	multiplier = 101
	
	text_hash = 0
	patch_hash = 0

	for ind in range(patch_len):
		power = patch_len - 1 - ind
		text_hash += (multiplier**power) * ord(text[ind])
		patch_hash += (multiplier**power) * ord(patch[ind])

	found = False
	for index in range(text_len - patch_len):
		if patch_hash == text_hash:
			found = True
			if patch != text[index:index + patch_len]:
				found = False 
		if found:
			break
		text_hash = (multiplier * (text_hash - (ord(text[index]) * (multiplier**(patch_len - 1))))) + ord(text[index + patch_len]) 
	return found

# my own asserts <3
assert(rabin_karp_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch1.txt')))
assert(rabin_karp_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch2.txt')))
assert(rabin_karp_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch3.txt')))
assert(not rabin_karp_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_not_a_patch.txt')))

#teacher asserts
assert(rabin_karp_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra1.txt')))
assert(rabin_karp_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra4.txt')))
assert(rabin_karp_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra2.txt')))
assert(rabin_karp_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra3.txt')))
assert(rabin_karp_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra5.txt')))

assert(not rabin_karp_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra3.txt')))
assert(not rabin_karp_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra2.txt')))
assert(not rabin_karp_search(text_opener('resources/textos/texto1.txt', 'resources/palavras/palavra5.txt')))
assert(not rabin_karp_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra1.txt')))
assert(not rabin_karp_search(text_opener('resources/textos/texto2.txt', 'resources/palavras/palavra4.txt')))
