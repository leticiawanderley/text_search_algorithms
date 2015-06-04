import sys, collector
from text_opener import text_opener
from brute_force_search import brute_force_search
from rabin_karp_search import rabin_karp_search
from knuth_morris_pratt_search import knuth_morris_pratt_search

text_path = sys.argv[3]
patch_path = sys.argv[2]
texts = text_opener(text_path, patch_path)

technique = sys.argv[1]
collector = collector.Collector()
collector.start_profile()

search_result = (False, 0)

if technique == 'forcabruta':
	search_result = brute_force_search(texts)
elif technique == 'knuthmorrispratt':
	search_result = knuth_morris_pratt_search(texts)
elif technique == 'rabinkarp':
	search_result = rabin_karp_search(texts)

profile_result = collector.stop_profile()
operation_count = search_result[1]
found = search_result[0]

if found:
	exists = 'contem'
else:
	exists = 'nao contem'

print("texto_buscado:%s texto_busca:%s resultado: %s tempo_execucao: %f consumo_memo:%f num_operacaoes: %i"%(text_path, patch_path, exists, profile_result[0], profile_result[1], operation_count))
