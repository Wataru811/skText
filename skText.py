#!/usr/bin/python


# skText.py
# extract text string from  sketch file
# $ python skText page.json 
#


import json
import sys



# check  argument
arguments = len(sys.argv) 
if( arguments < 2 ): 
	print( "Invalide argument.\n\n" )
	print( "## ------------------------------" )
	print( "## Sketch text string extractor" )
	print( "## written by W.Ishizuka" )
	print( "$ skText <sketch-page-json>\n\n" )
	exit(0)

## input
try:
	f = open( sys.argv[1], 'r')
except OSError as e:
	print(e)
	exit(0)

try:
	json_dict = json.load(f)
except e:
	print("invalid json format")
	print(e)
	exit(0)

## print('json_dict:{}'.format(type(json_dict)))
ly = json_dict["layers"]
res = []
for item in ly:
	if "attributedString" in item:
		res.append( item["attributedString"]["string"] )
	else:
		res.append( item["name"] )
res = sorted(res) ;

## output
for ss in res:
	print( ss );




