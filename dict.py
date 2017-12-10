# -*- coding: utf-8 -*-
#!/usr/bin/env python
file = open('dict.data')
source = file.read()
source = source.splitlines()
dict = [dict.split(':')[0:] for dict in source]
file.close()
def sozluk(string):
	for test in dict:
		for extend in test:
			extend = extend + extend
		if string in extend:
			return test[0]
		if test[0] == string:
			return test[1:]
