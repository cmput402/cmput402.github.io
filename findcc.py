import os
from unicodedata import category
for root, dirs, files in os.walk('.'):
	for file in files:
		if file.endswith(".md"):
			filename = os.path.join(root, file)
			with open(filename) as fd:
				i = 0
				for l in fd:
					i+=1
					for c in l:
						if c not in '\r\n\t' and 'C' in category(c):
							print(filename, i, repr(l))
