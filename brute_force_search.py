from text_opener import text_opener

def brute_force_search(texts):
	operation_count = 0
	text = texts[0]
	patch = texts[1]
	
	text = texts[0].read().strip('\n')
	patch = texts[1].read().strip('\n')
	patch_first_char = patch[0]
	found = False	
	for char_number in range(len(text)):
		operation_count += 1
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
	return (found, operation_count)
