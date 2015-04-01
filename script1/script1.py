# Mateusz Gawron, grupa sroda 8:00
# Sposob uruchamiania:
# python script1.py C:/test_dir
# lub
# python script1.py C:/test_dir wynik.txt

import sys
import os

def print_dir(path, level):
	print (2*level * "-")+'>', path
	for entry in os.listdir(path):
		if os.path.isdir(path+"/"+entry):
			print_dir(path+"/"+entry, level+1)
		else:
			print (2*(level+1) * '-')+'>',
			print entry
			
def print_dir_to_file(path, level, file):
	file.write( (2*level * "-")+'> ' + path + '\n')
	for entry in os.listdir(path):
		if os.path.isdir(path+"/"+entry):
			print_dir_to_file(path+"/"+entry, level+1, file)
		else:
			file.write( (2*(level+1) * '-')+'>' + entry + '\n')

if __name__ == "__main__":
	if sys.argv.__len__() == 2:
		if os.path.isdir(sys.argv[1]):
			print_dir(sys.argv[1], 1)
		else:
			print "Podany argument nie jest katalogiem"
	elif sys.argv.__len__() == 3:
		if os.path.isdir(sys.argv[1]):
			try:
				with open(sys.argv[2], "w") as file: 
					print_dir_to_file(sys.argv[1], 1, file)
				print "Wynik zostal zapisany do pliku: " + sys.argv[2]
			except IOError:
				print "Blad zapisu do pliku"
		else:
			print "Podany argument nie jest katalogiem"
	else:
		print "Podaj poprawna liczbe argumentow skryptu"
	

	