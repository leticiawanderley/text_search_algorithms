def brute_force_search(text_path, patch_path):
	text = open(text_path, 'r')
	patch = open(patch_path, 'r')

	patch_first_line = patch.readline()
	found = False

	for line in text:
		if not found and line == patch_first_line:
			found = True
		elif found:
			patch_new_line = patch.readline()
			if patch_new_line == '':
				break
			elif line != patch_new_line:
				found = False
	return found


print(brute_force_search('neil_gaiman.txt', 'neil_gaiman_patch.txt'))

