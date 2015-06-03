from text_opener import text_opener

#based upon http://stackoverflow.com/questions/22216948/python-rabin-karp-algorithm-hashing
#and https://www.topcoder.com/community/data-science/data-science-tutorials/introduction-to-string-searching-algorithms/
def rabin_karp_search(texts):
	text = texts[0].read().strip('\n')
	patch = texts[1].read().strip('\n')
	text_len = len(text)
	patch_len = len(patch)
	modulator = 1000000007
	multiplier = 19
	
	text_hash = 0
	patch_hash = 0

	final_multiplier =  multiplier ** (patch_len - 1)
	values_dict = {}
	for ind in range(patch_len):
		text_hash = (text_hash * multiplier + ord(text[ind])) % modulator
		patch_hash = (patch_hash * multiplier + ord(patch[ind])) % modulator
		
	found = False
	for index in range(text_len - patch_len):
		if patch_hash == text_hash:
			found = True
			if patch != text[index:index + patch_len]:
				found = False 
		if found:
			break
		if text[index] in values_dict:
			old_value = values_dict[text[index]]
		else:
			old_value = (ord(text[index]) * final_multiplier) % modulator
			values_dict[text[index]] = old_value 		
		
		text_hash = (text_hash - old_value) % modulator
		text_hash = (text_hash * multiplier) % modulator
		text_hash = (text_hash + ord(text[index + patch_len])) % modulator
	
	index += 1
	if patch_hash == text_hash and not found:
		found = True
		if patch != text[index:index + patch_len]:
			found = False
	return found

# my own asserts <3
assert(rabin_karp_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch1.txt')))
assert(rabin_karp_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch2.txt')))
assert(rabin_karp_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_patch3.txt')))
assert(not rabin_karp_search(text_opener('resources/samples/neil_gaiman.txt', 'resources/samples/neil_gaiman_not_a_patch.txt')))

# #teacher asserts
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
