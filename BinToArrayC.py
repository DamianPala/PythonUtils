'''
Created on 30.01.2017

@author: Haz
'''

import os
import sys

if len(sys.argv) > 1:
    input_file_name = sys.argv[1]
else:
    input_file_name = "FSB_TouchReaderManager.bin"
scritDirectory = os.path.dirname(sys.argv[0])


output_file_name = "BinArray.c"

bin_list = []

with open(input_file_name, 'rb') as f:
    while True:
        b = f.read(1)
        if not b:
            # eof
            break
        bin_list.append(b)


output_content = ""
output_content += "#include \"stdint.h\"\n\n"
output_content += "static uint32_t BinArraySize = " + str(len(bin_list)) + ";\n"
output_content += "static uint8_t BinArray[] =\n{ \n"
output_content += "  "
 
item_iterator = 0
for item in bin_list:
    byte_string = '0x' + hex(ord(item))[2:].zfill(2)
    output_content += byte_string + ", "
    item_iterator += 1
    if item_iterator == 20:
        output_content += "\n  "
        item_iterator = 0
     
output_content = output_content[:-2]
output_content += "\n" 
output_content += "};"
 
print output_content
 
open(scritDirectory + '\\' + output_file_name, 'wb').write(output_content)
