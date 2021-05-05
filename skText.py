#!/usr/bin/python


# skText.py  
# extract text string from	sketch file
# $ python skText page.json 
#
# v1.0 extract 1st level strings
# v1.1 extranct nexted strings
# v1.11 clean the code

import json
import sys

version="v1.11"
allFlag = False
argFile = 1

def checkArgs():
	# check	argument
	arguments = len(sys.argv) 
	if( arguments < 2 ): 
		print( "Invalide argument.\n\n" )
		print( "# skText / Sketch text string extractor /"+version )
		print( "#                 written by W.Ishizuka\n\nUsage:" )
		print( "$ skText [-all] <sketch-page-json>\n\n" )
		print( "option:" )
		print( "   -all : print nexted strings" );
		print( "   (default: print only top level strings)" );
		return False;
	if( arguments == 3 ): 
		if sys.argv[1].find( "-all" ) == 0:
			allFlag = True
			argFile = 2
	return True;

## input from file -----------------------
def getJsonFile():
	try:
		f = open( sys.argv[argFile], 'r')
	except OSError as e:
		print(e)
		return ( False, None )
		exit(0)
	try:
		data  = json.load(f)
	except e:
		print("invalid json format")
		print(e)
		return ( False, None )
	return (True, data )

def extractTexFromSketchJson():
	if not checkArgs():
		exit(1)
	( ret, json_dict ) = getJsonFile()
	if not ret :
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
	
	## output ----------------
	if allFlag: 
		for ss in res:
			print( "\n\n"+ ss + "\n----------------------" )
			ll = result[ss]
			for str in ll:
				print( str )	
	else:
		for ss in res:
			print( ss )	


def main():
	extractTexFromSketchJson();


if __name__ == "__main__":
	main()


