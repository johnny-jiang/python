#bmpinfo.py


import sys
import struct


def check_bmp(header):
	head_data=struct.unpack('<ccIIIIIIHH', header)
	print(head_data)
	if head_data[0]==b'B' and head_data[1]==b'M':
		print('bit: %d * %d ,color :%d' %(head_data[6],head_data[7],head_data[9]))
	else:
		print('not a bmp file.')


f=open(sys.argv[1],'rb')
header=f.read(30)
check_bmp(header)