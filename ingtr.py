# -*- coding: utf-8 -*-
#!/usr/bin/env python
file = open('data.mmsql')
source = file.read()
source = source.splitlines()
ing = [ing.split(':')[0] for ing in source]
file.close()
def dict(ingilizce):
	dict = {}
	for search in ing:
		if (len(search) is len(ingilizce) and search == ingilizce):
			dict[search] = source[ing.index(search)].split(':')[1:][0]
			break
	return dict

