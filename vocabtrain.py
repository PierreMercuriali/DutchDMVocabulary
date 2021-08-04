import io, time
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl
import PySimpleGUI as sg
import random

#	AESTHETICS
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#	FUNCTIONS
def quickSaveUnicode(content, fn):
	with io.open(fn, "w", encoding="utf-8") as f:
		f.write(content)
def quickAppendUnicode(content, fn):
	with io.open(fn, "a", encoding="utf-8") as f:
		f.write(content)
def preprocess(text):
	r = ""
	for character in text:
		if not character in '“”{}[]()?,.;!:\"\'':
			r+=character
	return r.lower()
def bow(text):
	return set([p for p in preprocess(text).split(" ") if len(p)>1])

print("Loading vocabulary...")
with io.open("delftse methode.csv", 'r', encoding='utf-8') as f:
	raw = f.read().splitlines()

print("Formatting...")
vocsize		= len(raw)
nl 			= [line.split(',')[0]  for line in raw]
ipa 		= [line.split(',')[1]  for line in raw]
en 			= [line.split(',')[2]  for line in raw]
print(f"  {vocsize} words loaded.")
print("Loading GUI...")

displayNL	= True
displayIPA	= True
displayEN	= False
counter 	= 0

TITLE					= "Simple Vocabulary Trainer"
LAYOUT_text_column		= [
							[sg.Text(size=(48, 2),  key="-NL-")],
							[sg.Text(size=(48, 2),  key="-IPA-")],
							[sg.Text(size=(48, 2),  key="-EN-")],
						  ]
LAYOUT_buttons_column1	= [
	[sg.Button("toggleNL")],
	[sg.Button("toggleIPA")],
	[sg.Button("toggleEN")],
	]
LAYOUT_buttons_column2	= [
	[sg.Button("NEXT")],
	[sg.Button("SHOW")],
	[sg.Button("QUIT")],	
	]
LAYOUT = [
	[
		sg.Column(LAYOUT_buttons_column1),
		sg.VSeparator(),
		sg.Column(LAYOUT_text_column),
		sg.VSeparator(),
		sg.Column(LAYOUT_buttons_column2),
	]
]

MARGINS		= (96, 32)
window		= sg.Window(title=TITLE, layout=LAYOUT, margins=MARGINS)
wordID = 0

while True:
	event, values = window.read()
#	print(f"nl: {displayNL}, ipa: {displayIPA}, en: {displayEN}")
	if event== 'toggleNL':
		displayNL = not displayNL
	if event== 'toggleIPA':
		displayIPA = not displayIPA
	if event== 'toggleEN':
		displayEN = not displayEN
	if event == 'NEXT':
		wordID = random.randint(0,vocsize-1)	
		counter+=1
		#window["-INFO"].update(f"{counter} words seen in the current session")
		if displayNL:
			window["-NL-"].update(nl[wordID])
		else:
			window["-NL-"].update("#"*len(nl[wordID]))
		if displayIPA:
			window["-IPA-"].update(ipa[wordID])
		else:
			window["-IPA-"].update("#"*len(ipa[wordID]))
		if displayEN:
			window["-EN-"].update(en[wordID])
		else:
			window["-EN-"].update("#"*len(en[wordID]))			
	if event == 'SHOW':
		window["-NL-"].update(nl[wordID])
		window["-IPA-"].update(ipa[wordID])
		window["-EN-"].update(en[wordID])
	if event=='QUIT' or event==sg.WIN_CLOSED:
		print("Closing...")
		break

window.close()

