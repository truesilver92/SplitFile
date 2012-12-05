import sys
import math
import os

#This is the interpretation of the command line

if len(sys.argv) > 2:
	#Combine mode instead of split mode
	print "Combine mode"
	c = sys.argv[2]
	print "Seed file: " + c
	if int(c[0]) == 1:
		print "c[0] == 1 is true"
		continuebool = True
		currentfilecount = 1
		rawfilename = c[2:]
		print "rawfilename = " + rawfilename
		f = open(rawfilename, 'w')
		
		while continuebool:
			temp = open(str(currentfilecount) + '_' + rawfilename, 'r')
			currentfilecount = currentfilecount + 1
			f.write(temp.read())
			temp.close()
			if not(os.path.exists(str (currentfilecount) + '_' + rawfilename)):
				continuebool = False
	#End the program after Combination mode
	sys.exit()
	
else:
	print "Split mode"
	q = sys.argv[1]

print q

try:
	file_orig = open(q, "r")
except IOError:
	print("read error")
	sys.exit()

s_orig = file_orig.read();
file_orig.close();
s_len = len(s_orig)
con = True
step = 4096
begin = 0
end = 0
filecount = 1
digets = math.ceil(math.log10(s_len / step + 1))

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

	f = open(addstring + '_' + q, 'w', 4096)	
	s = s_orig[begin:end]
	
	f.write(s)
	f.close()
	
	begin = end
	filecount = filecount + 1	

