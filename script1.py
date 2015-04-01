# Mateusz Gawron, grupa sroda 8:00
# Zadanie zrobione w 100%
# Sposob uruchamiania:
# podanie sciezki katalogu do wylistowania jako
# pierwszy i jedyny argument skryptu
# np. python script1.py C:/test_dir

import sys
import os

def print_dir(path, level):
	print level * "-",
	print path
	for entry in os.listdir(path):
		if os.path.isdir(path+"/"+entry):
			print_dir(path+"/"+entry, level+1)
		else:
			print (level+1) * '-',
			print entry

if sys.argv.__len__() == 2:
	if os.path.isdir(sys.argv[1]):
		print_dir(sys.argv[1], 0)
	else:
		print "Podany argument nie jest katalogiem"
else:
	print "Podaj poprawna liczbe argumentow skryptu"
	

	