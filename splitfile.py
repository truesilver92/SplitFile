import sys

q = raw_input("name of file:");

try:
	file_orig = open(q, "r")
except IOError:
	print("read error")
	sys.exit()

s_orig = file_orig.read();
file_orig.close();
s_len = len(s_orig)
con = True

while (con):
	


