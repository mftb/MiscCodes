#!/usr/bin/env python
# -*- coding: latin1 -*-

# script que move alguns arquivos da pasta ~/Disciplinas/MA311 utilizando
# expressões regulares
# por Matheus Boy

# gambi design pattern My Way
# shell script é o caralho

import os

n = ["p1", "p2", "p3", "ex"]
ls = ""

for i in n:
	ls = "ls | grep ma311-" + i + " > a.out"
	os.system(ls)

	a = open("a.out")
	b = a.read()
	a.close()
	b = b.split("\n")
	cmd = ""
	for c in b:
		if c != "":
			cmd = "mv " + c + " " + i + "/"
			os.system(cmd)
os.system("rm a.out")
