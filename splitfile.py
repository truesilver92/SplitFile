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
step = 4096
begin = 0
end = 0

while (con):
	end = end + step
	if (end > s_len - 1):
		end = s_len - 1
		con = False
	
	
	


