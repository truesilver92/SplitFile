import sys
import math
import os
import string

#A function for printing out progress
def progressReport(done, toGo, lastFinishedFile):
	print str(done) + " of " + str(toGo) + " completed " + lastFinishedFile

#This is the interpretation of the command line

if sys.argv[1] == 'c':
	#Combine mode instead of split mode
	print "Combine mode"
	c = sys.argv[2]
	print "Seed file: " + c
	
	continuebool = True
	currentfilecount = 1
	#fix rawfilename to find after the number for the part		
	#find identifyer "_" and cut the string for the name		
	rawfilename = c[string.find(c, "_") + 1:]
	#get number of parts	
	totalfilecount = int(c[:string.find(c, "_")])
	#get number of digits from totalfilecount
	digits = int(math.floor(math.log10(totalfilecount))) + 1
	print "rawfilename = " + rawfilename
	f = open(rawfilename, 'w')
	
	while continuebool:
		#get the part name correct			
		numberofzerostoadd = digits - (int(math.floor(math.log10(currentfilecount))) + 1)
		digitoffset = ""

		while numberofzerostoadd > 0:
			digitoffset = digitoffset + "0"
			numberofzerostoadd = numberofzerostoadd - 1

		temp = open(digitoffset + str(currentfilecount) + '_' + rawfilename, 'r')
		progressReport(currentfilecount, totalfilecount, temp.name)
		currentfilecount = currentfilecount + 1
		f.write(temp.read())
		temp.close()
		
		#get the part name correct			
		numberofzerostoadd = digits - (int(math.floor(math.log10(currentfilecount))) + 1)
		digitoffset = ""

		while numberofzerostoadd > 0:
			digitoffset = digitoffset + "0"
			numberofzerostoadd = numberofzerostoadd - 1			

		if not(os.path.exists(digitoffset + str(currentfilecount) + '_' + rawfilename)):
			continuebool = False
	#End the program after Combination mode
	sys.exit()
	
else:
	print "Split mode"
	q = sys.argv[2]

print q

try:
	file_orig = open(q, "r")
except IOError:
	print("read error")
	sys.exit()

#s_orig = file_orig.read();
#file_orig.close();
#s_len = len(s_orig)
s_len = os.path.getsize(q)
con = True
step = int(sys.argv[1])
#4 megabytes for big test
#step = 4194304
begin = 0
end = 0
filecount = 1
digets = int(math.log10(s_len / step)) + 1
totalfiles = int(s_len / step) + 1

while (con):
	end = end + step
	if (end > s_len - 1):
		end = s_len - 1
		con = False
	
	addstring = str(filecount)
	addstringlen = len(addstring)

	while addstringlen < digets:
		addstring = '0' + addstring
		addstringlen = addstringlen + 1

	temp = addstring + '_' + q

	f = open(temp, 'w', step)	
	s = file_orig.read(step)
	
	f.write(s)
	f.close()
	
	progressReport(filecount, totalfiles, temp)

	begin = end
	filecount = filecount + 1	

file_orig.close()

