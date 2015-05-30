def brute_force_search(text_path, patch_path):
	text = open(text_path, 'r')
	patch = open(patch_path, 'r')

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


assert(brute_force_search('neil_gaiman.txt', 'neil_gaiman_patch1.txt'))
assert(brute_force_search('neil_gaiman.txt', 'neil_gaiman_patch2.txt'))
assert(brute_force_search('neil_gaiman.txt', 'neil_gaiman_patch3.txt'))
assert(not brute_force_search('neil_gaiman.txt', 'neil_gaiman_not_a_patch.txt'))
