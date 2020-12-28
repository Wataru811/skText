#!/usr/bin/python


# skText.py  
# extract text string from	sketch file
# $ python skText page.json 
#
# v1.0 extract 1st level strings
# v1.1 extranct nexted strings
#



import json
import sys


allFlag = False
argFile = 1

# check	argument
arguments = len(sys.argv) 
if( arguments < 2 ): 
	print( "Invalide argument.\n\n" )
	print( "## ------------------------------" )
	print( "## skText / Sketch text string extractor (v1.1)" )
	print( "## written by W.Ishizuka" )
	print( "$ skText [-all] <sketch-page-json>\n\n" )
	print( "option:" )
	print( "   -all : print nexted strings" );
	print( "   (default: print only top level strings)" );
	exit(0)

if( arguments == 3 ): 
	if sys.argv[1].find( "-all" ) == 0:
		allFlag = True
		argFile = 2

## input
try:
	f = open( sys.argv[argFile], 'r')
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
skipstr = [ "step", "Group", "lv" ,"Lv", "Rectangle", "btn", "copy","overlay","Path","segmantControl","Bar" ];
result = {}

for item in ly:
	lbl = ""
	if "attributedString" in item:
		lbl = item["attributedString"]["string"]
	else:
		lbl = item["name"] 
	res.append(lbl )
	lbl2=""
	result[ lbl ] = []
	if "layers" in item:
		subLy = item["layers"]
		for subItem in subLy:
			if "attributedString" in subItem:
				lbl2 = subItem["attributedString"]["string"]
			else:
				lbl2 = subItem["name"]
			flg = True;
			for ss in skipstr:
				if lbl2.find( ss ) == 0:
					flg =False 
					break
			if flg  :
				result[lbl].append( lbl2 );
res = sorted(res) ;

## output
if allFlag: 
	for ss in res:
		print( "\n\n"+ ss + "\n----------------------" )
		ll = result[ss]
		for str in ll:
			print( str )	
else:
	for ss in res:
		print( ss )	





