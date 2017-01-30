'''
Created on 30.01.2017

@author: Haz
'''

import os
import sys

input_file_name = sys.argv[1]
scritDirectory = os.path.dirname(sys.argv[0])

output_file_name = "BinArray.c"

bin_list = []

with open(input_file_name, 'r') as f:
    byte = f.read(1)
    while byte != "":
        bin_list.append(byte)
        byte = f.read(1)
    

output_content = ""
output_content += "#include \"stdint.h\"\n\n"
output_content += "static uint8_t BinArray[] =\n{ \n"
output_content += "  "

item_iterator = 0
for item in bin_list:
    byte_string = hex(ord(item))
    output_content += byte_string + ", "
    item_iterator += 1
    if item_iterator == 20:
        output_content += "\n  "
        item_iterator = 0
    
output_content = output_content[:-2]
output_content += "\n" 
output_content += "};"

open(scritDirectory + '\\' + output_file_name, 'wb').write(output_content)
