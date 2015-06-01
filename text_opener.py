def text_opener(text_path, patch_path):
	text = open(text_path, 'r')
	patch = open(patch_path, 'r')

	return text, patch