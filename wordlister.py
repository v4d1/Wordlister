#!/usr/bin/env python

# -*- coding: utf-8 -*-
import sys
import os
import collections
import re
import argparse

from unicodedata import normalize




def color(no_color):

	global G, Y, B, R, W
	
	if no_color == False:
		is_windows = sys.platform.startswith('win')

		#colors

		G = '\033[92m'  # green
		Y = '\033[93m'  # yellow
		B = '\033[94m'  # blue
		R = '\033[91m'  # red
		W = '\033[0m'   # white

		# Console Colors
		if is_windows:
			try:
				import win_unicode_console , colorama
				win_unicode_console.enable()
				colorama.init()
			except:
				if printOutput: 
					print("To use colored version in Windows: 'pip install win_unicode_console colorama'")
					print("You can use --no-color to use non colored output")
	else: 
		G = Y = B = R = W = ''



def banner():

	print(B + "__          __           _ _ _     _            \n\ \/" + Y + "adi" + B +"    / /          | | (_)   | |           \n \ \  /\  / /__  _ __ __| | |_ ___| |_ ___ _ __ \n" + Y + "  \ \/  \/ / _ \| '__/ _` | | / __| __/ _ \ '__|\n   \  /\  / (_) | | | (_| | | \__ \ ||  __/ |   \n    \/  \/ \___/|_|  \__,_|_|_|___/\__\___|_| v" + str(version) +"\n\n\t " + B + "\tA tool for...the name speaks for itself")


def parser_error(errmsg):
	color(True)
	banner()

	print("\nUsage: python " + sys.argv[0] + " [Options] use -h for help")
	print(R + "Error: " + errmsg + W)
	sys.exit()


def parse_args():

	parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " --company companyname")
	parser._optionals.title = "OPTIONS"
	parser.error = parser_error
	parser.add_argument('--name', help="Name mode")
	parser.add_argument('--company', help="Company mode")
	parser.add_argument('--no-color', help='Dont print colored output', action='store_true')
	
	return parser.parse_args()


def initialize(palabras):
	dicc = [palabras, palabras + ".", palabras + "!", palabras.capitalize() ,palabras.upper(),palabras.upper() + ".", palabras.upper() + "!", palabras.title(), palabras.title() + ".", palabras.title() + "!"]
	return dicc

def vocal2number(dicc):
	dicc2 = []
	for palabras in dicc:
		dicc2.append(palabras.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0').replace('A', '4').replace('E', '3').replace('I', '1').replace('O', '0'))
	return dicc + dicc2

def addNumEnd(dicc): #GENERA NUMS 0-999 0-9 00-99 000-999
	dicc2 = []
	for palabras in dicc:
		diccaux = []

		for i in range (0,10):
			diccaux.append(palabras + str(i))
			for j in range (0,10):
				diccaux.append(palabras + str(i) + str(j))
				for k in range (0,10):
					diccaux.append(palabras + str(i) + str(j) + str(k))
		dicc2 = dicc2 + diccaux
	return dicc2

def addNumStart(dicc): #GENERA NUMS 0-999 0-9 00-99 000-999
	dicc2 = []
	for palabras in dicc:
		diccaux = []

		for i in range (0,10):
			diccaux.append(str(i) + palabras)
			for j in range (0,10):
				diccaux.append(str(i) + str(j) + palabras)
				for k in range (0,10):
					diccaux.append(str(i) + str(j) + str(k) + palabras)
		dicc2 = dicc2 + diccaux
	return dicc2

def addYear(dicc):
	dicc2 = []
	for palabras in dicc:
		diccaux = []
		for i in range (1950,2025):
			diccaux.append(palabras + "%d" %i)
		dicc2 = dicc2 + diccaux
	return dicc2


def addLongYear(dicc):
	dicc2 = []
	global total2
	for palabras in dicc:
		diccaux = []
		aux1 = ["{0:02}".format(k) for k in range(0,32)]
		aux2 = ["{0:02}".format(k) for k in range(0,13)]
		for j in aux1:
			for k in aux2:
				for i in range (1950,2025):
					diccaux.append(palabras + str(k) + str(j) + str(i))
					diccaux.append(palabras + str(i) + str(j) + str(k))
		dicc2 = dicc2 + diccaux
		diccaux = []
		for j in aux1:
			for k in aux2:
				for i in range (25,50):
					diccaux.append(palabras + str(k) + str(j) + str(i))
					diccaux.append(palabras + str(i) + str(j) + str(k))
		dicc2 = dicc2 + diccaux
	return dicc2


def addYearStart(dicc):
	dicc2 = []
	for palabras in dicc:
		diccaux = []
		for i in range (1930,2030):
			diccaux.append(str(i) + palabras)
		dicc2 = dicc2 + diccaux
	return dicc2

def addDotEnd(dicc):
	dicc2 = []
	for palabras in dicc:
		dicc2.append(palabras + ".")

	return dicc + dicc2


def addSpecialEnd(dicc):

	dicc2 = []
	especial = ["!", ".", "@", ",", "_"]
	for palabras in dicc:
		for esp in especial:
			dicc2.append(palabras + esp)
	return dicc + dicc2

def addPermutation(dicc):
	dicc2 = []
	especial = ["qwerty", "123", "1234", "12345", "123456", "1234567", "12345678", "asd", "asdf", "0000", "1111", "9999", "1234567890", "123456789", "qazwsx", "qaz", "|@#", "!@#"]
	for palabras in dicc:
		for esp in especial:
			dicc2.append(palabras + esp)
	return dicc + dicc2


def addSpecialStart(dicc):
	dicc2 = []
	especial = ["!", ".", "@", "*", "_"]
	for palabras in dicc:
		for esp in especial:
			dicc2.append(esp + palabras)
	return dicc + dicc2

def addCharStart(char, dicc):
	dicc2 = []
	for palabras in dicc:
		dicc2.append(char + palabras)
	return dicc + dicc2

def addCharEnd(char, dicc):
	dicc2 = []
	for palabras in dicc:
		dicc2.append(palabras + char)
	return dicc + dicc2

def insertarpunto(dicc):
	dicc2 = []
	for palabras in dicc:
		for i in range(len(palabras)):
			hashlist = list(palabras)
			hashlist.insert(i, '.')
			dicc2.append(''.join(hashlist))
	return dicc + dicc2



def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s



def initializeName(name):


	n = name.split(' ')
	
	if len(n) != 2:
		print(R + "[-] Invalid name format. Please use Name Surname mode. Example: John Smith")
		exit()

	#COMMENTS BELLOW ARE USE WITH John Smith AS EXAMPLE

	wordlist.append(n[0]) #Adds John
	wordlist.append(n[1]) #Adds Smith
	wordlist.append(n[0] + n[1]) #Adds JohnSmith
	wordlist.append(n[0].lower()) #Adds john
	wordlist.append(n[1].lower()) #Adds smith
	wordlist.append(n[0].lower() + n[1].lower()) #Adds johnsmith
	wordlist.append(n[0].lower() + '.' + n[1].lower()) #Adds john.smith
	wordlist.append(n[0][:1].lower() + n[1][:1].lower()) #Adds js
	wordlist.append(n[0][:1].lower() + n[1][:2].lower()) #Adds jsm
	wordlist.append(n[0][:1].lower() + n[1][:3].lower()) #Adds jsmi
	wordlist.append(n[0][:2].lower() + n[1][:1].lower()) #Adds jos
	wordlist.append(n[0][:2].lower() + n[1][:2].lower()) #Adds josm
	wordlist.append(n[0][:2].lower() + n[1][:3].lower()) #Adds josmi
	wordlist.append(n[0][:3].lower() + n[1][:1].lower()) #Adds johs
	wordlist.append(n[0][:3].lower() + n[1][:2].lower()) #Adds johsm
	wordlist.append(n[0][:3].lower() + n[1][:3].lower()) #Adds johsmi
	wordlist.append(n[0][:1].lower() + '.' + n[1][:3].lower()) #Adds j.smi
	wordlist.append(n[0][:2].lower() + '.' + n[1][:1].lower()) #Adds jo.s
	wordlist.append(n[0][:2].lower() + '.' + n[1][:2].lower()) #Adds jo.sm
	wordlist.append(n[0][:2].lower() + '.' + n[1][:3].lower()) #Adds jo.smi
	wordlist.append(n[0][:3].lower() + '.' + n[1][:1].lower()) #Adds joh.s
	wordlist.append(n[0][:3].lower() + '.' + n[1][:2].lower()) #Adds joh.sm
	wordlist.append(n[0][:3].lower() + '.' + n[1][:3].lower()) #Adds joh.smi
	wordlist.append(n[0][:1] + n[1][:1]) #Adds JS
	wordlist.append(n[0][:1] + n[1][:2]) #Adds JSm
	wordlist.append(n[0][:1] + n[1][:3]) #Adds JSmi
	wordlist.append(n[0][:2] + n[1][:1]) #Adds JoS
	wordlist.append(n[0][:2] + n[1][:2]) #Adds JoSm
	wordlist.append(n[0][:2] + n[1][:3]) #Adds JoSmi
	wordlist.append(n[0][:3] + n[1][:1]) #Adds JohS
	wordlist.append(n[0][:3] + n[1][:2]) #Adds JohSm
	wordlist.append(n[0][:3] + n[1][:3]) #Adds JohSmi
	wordlist.append(n[0][:1] + '.' + n[1][:3]) #Adds J.Smi
	wordlist.append(n[0][:2] + '.' + n[1][:1]) #Adds Jo.S
	wordlist.append(n[0][:2] + '.' + n[1][:2]) #Adds Jo.Sm
	wordlist.append(n[0][:2] + '.' + n[1][:3]) #Adds Jo.Smi
	wordlist.append(n[0][:3] + '.' + n[1][:1]) #Adds Joh.S
	wordlist.append(n[0][:3] + '.' + n[1][:2]) #Adds Joh.Sm
	wordlist.append(n[0][:3] + '.' + n[1][:3]) #Adds Joh.Smi
	wordlist.append(n[0] + n[1][:1]) #Adds JohnS
	wordlist.append(n[0][:1] + n[1]) #Adds JSmith
	wordlist.append(n[0] + '.' + n[1][:1]) #Adds John.S
	wordlist.append(n[0][:1] + '.' + n[1]) #Adds J.Smith
	wordlist.append(n[0].lower() + n[1][:1]) #Adds johnS
	wordlist.append(n[0].lower() + n[1][:1].lower()) #Adds johns
	wordlist.append(n[0][:1] + n[1].lower()) #Adds Jsmith
	wordlist.append(n[0][:1].lower() + n[1]) #Adds jSmith



#				#1  test=Test=TEST
#Block 1		#2	test
#Block 1		#2	test[NUM]
#Block 1		#2	test[NUM][SP]
#Block 1		#3	test[SP][NUM]
#Block 1		#4	test[YEAR][SP]
#Block 1		#5	test[SP][YEAR]

#Block 2		#6	test[SP]
#Block 2		#7	test[SP][SP]


#Block 3		#12	[SP]test[SP]
#Block 3		#13 [SP][NUM]test[SP]
#Block 3		#14 [SP]test[NUM][SP]
#Block 3		#15	[SP]test[YEAR][SP]  

#Block 4		#17 [NUM][SP]test[SP]
#Block 4		#18	[SP]test[YEAR][SP]

#Block 5 		#21 t3st[SP]
#Block 5 		#22 t3st[SP][NUM]
#Block 5 		#23 t3st[SP][YEAR]

#Block 6 		#24 t3st[NUM][SP]
#Block 6 		#25 t3st[YEAR][SP]
#Block 6		#26 test[YEAR][NUM]
#Block 6		#27 test[NUM][YEAR]

#Block 7		#28 test[ESP][LONGYEAR]
#Block 7		#29 test[LONGYEAR]




if __name__ == "__main__":

	version = "0.1"
	wordlist = []

	args = parse_args()
	color(args.no_color)
	banner()



	if args.name and not args.company:
		initializeName(args.name)
	elif args.company and not args.name:
		#Initialize the wordlist with company COMPANY and Company
		initCompany = args.company
		wordlist.append(initCompany.upper())
		wordlist.append(initCompany.lower())
		wordlist.append(initCompany.capitalize())
	elif not args.name and not args.company:
		print(R + "\n[-] Argument error. You need to specify --name or --company")
		exit()
	else:
		print(R + "[-] BOTH MODES SELECTED")
		exit()

	wordlistSpecial = addSpecialEnd(wordlist)

	#print(wordlist)


									#2					#3								#4								#5			
	block1 = addSpecialEnd(addNumEnd(wordlist)) + addNumEnd(wordlistSpecial)	+ addSpecialEnd(addYear(wordlist)) + addYear(wordlistSpecial)
				#6 							#7
	block2 = wordlistSpecial + addSpecialEnd(wordlistSpecial) 
							#12									#13 													#14
	block3 = addSpecialStart(wordlistSpecial) + addSpecialStart(addNumStart(wordlistSpecial)) + addSpecialStart(addNumEnd(wordlistSpecial)) + addSpecialStart(addSpecialEnd(addYear(wordlist)))
							#17														#18			
	block4 = addNumStart(addSpecialStart(wordlistSpecial)) + addSpecialStart(addSpecialEnd(addYear(wordlist)))
						#21												#22 								#23
	block5 = vocal2number(wordlistSpecial) + addNumEnd(vocal2number(wordlistSpecial)) + addYear(vocal2number(wordlistSpecial))
							#24														#25 												#26 					#27															
	block6 = addSpecialEnd(addNumEnd(vocal2number(wordlist))) + addSpecialEnd(addYear(vocal2number(wordlist))) + addNumEnd(addYear((wordlist))) + addYear(addNumEnd(wordlist))
						#28								#29
	block7 = addLongYear(wordlistSpecial) + addLongYear(wordlist)

	block_total = block1 + block2 + block3 + block4 + block5 + block6 + block7

	print(len(block_total))

	# open file in write mode
	with open('dicc_output.txt', 'w') as fp:
		for item in block_total:
			fp.write("%s\n" % item)
		print('Done')