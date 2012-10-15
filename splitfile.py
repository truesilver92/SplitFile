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
filecount = 1

while (con):
	end = end + step
	if (end > s_len - 1):
		end = s_len - 1
		con = False
	f = open(str(filecount) + '_' + q, 'w', 4096)	
	s = s_orig[begin:end]
	
	f.write(s)
	f.close()
	
	begin = end
	filecount = filecount + 1	
	
	


