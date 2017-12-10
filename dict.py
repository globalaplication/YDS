# -*- coding: utf-8 -*-
#!/usr/bin/env python
file = open('dict.data')
source = file.read()
source = source.splitlines()
dict = [dict.split(':')[0:] for dict in source]
file.close()
def sozluk(kelime):
	for test in dict:
		for extend in test:
			extend = extend + extend
		if kelime in extend:
			return test[0]
		if test[0] == kelime:
			for extend in test[1:]:
				extend = extend + extend
			return extend.split(',')
