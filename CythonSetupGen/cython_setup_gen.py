#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import json
import jinja2
import traceback
from pathlib import Path


DEBUG = False
TEMPLATE_DIRNAME = 'templates'
SETUP_TEMPLATE_FILENAME = 'setup.py.j2'


def generate(setup_data, output_filepath):
    src = Path(__file__).parent.resolve() / TEMPLATE_DIRNAME / SETUP_TEMPLATE_FILENAME
    dst = Path(output_filepath)
    templateLoader = jinja2.FileSystemLoader(searchpath=str(src.parent))
    templateEnv = jinja2.Environment(loader=templateLoader,
                                     trim_blocks=True,
                                     lstrip_blocks=True,
                                     newline_sequence='\n',
                                     keep_trailing_newline=True)
    template = templateEnv.get_template(src.name)
    content = template.render(setup_data)
    
    dst.touch(exist_ok=True)
    with open(dst, 'r+') as file:
        if content != file.read():
            file.truncate(0)
            file.write(content)
            print(f'{dst.resolve()} file generated.')
        else:
            print(f'{dst.resolve()} up-to-date.')


def prepare_setup_data(raw_data):
    cython_srcs = raw_data['cython_srcs'].split(';')
    cython_srcs = [f'{item}' for item in cython_srcs]
    raw_data['cython_srcs'] = cython_srcs
    
    libs = raw_data['libs'].split(';')
    libs = [f'{item}' for item in libs]
    libs = list(filter(lambda x: x != '-Wl,--whole-archive' and x != '-Wl,--no-whole-archive', libs))
    libs.append(raw_data['target_name'])
    raw_data['libs'] = libs
    
    build_type = raw_data['build_type']
    project_bin_dir = raw_data['project_bin_dir']
    all_inc_dirs = raw_data['all_inc_dirs'].split(';')

    lib_dirs = []
    inc_dirs = []
    inc_path = []
    for item in all_inc_dirs:
        try:
            Path(item).relative_to(project_bin_dir)
            lib_dirs.append(f'{item}/{build_type}')
        except:
            inc_dirs.append(item)
            inc_path.append(f'{item}/cython')
    
    raw_data['lib_dirs'] = lib_dirs
    raw_data['inc_dirs'] = inc_dirs
    raw_data['inc_path'] = inc_path
    
    return raw_data
    

if __name__ == '__main__':
    if not DEBUG and (sys.argv.__len__() < 3):
        sys.exit('Invalid parameters count!')
    elif DEBUG:
        input_filepath = 'setup_data.json'
        output_filepath = 'setup.py'
    else:
        input_filepath = sys.argv[1]
        output_filepath = Path(sys.argv[2]).resolve()
        output_filepath.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(input_filepath, 'r') as file:
            setup_data_raw = json.load(file)
        
        setup_data = prepare_setup_data(setup_data_raw)
        
        generate(setup_data, output_filepath)
    except:
        traceback.print_exc()
        sys.exit('Unknown error!')
    
