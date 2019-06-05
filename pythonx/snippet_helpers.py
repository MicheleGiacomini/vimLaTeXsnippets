import vim
import re
import os
import string
import random


texmathZones = ['texmathZone'+x for x in ['A', 'AS', 'B', 'BS', 'C',
'CS', 'D', 'DS', 'E', 'ES', 'F', 'FS', 'G', 'GS', 'H', 'HS', 'I', 'IS',
'J', 'JS', 'K', 'KS', 'L', 'LS', 'DS', 'V', 'W', 'X', 'Y', 'Z']]

texmathZones += ['texmathSubscript']

texIgnoremathZones = ['texmathText']

texmathZoneIds = vim.eval('map('+str(texmathZones)+", 'hlID(v:val)')")
texIgnoremathZoneIds = vim.eval('map('+str(texIgnoremathZones)+", 'hlID(v:val)')")

ignore = texIgnoremathZoneIds[0]

def math():
	synstackids = vim.eval("synstack(line('.'), col('.') - (col('.')>=2 ? 1 : 0))")
	try:
		first = next(
            i for i in reversed(synstackids)
            if i in texIgnoremathZoneIds or i in texmathZoneIds
        )
		return first != ignore
	except StopIteration:
		return False
