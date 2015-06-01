from text_opener import text_opener

def knuth_morris_pratt_search(texts):
	text = texts[0].read().strip('\n')
	patch = texts[1].read().strip('\n')

	