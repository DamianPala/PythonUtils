#!/usr/bin/env python
# -*- coding: utf-8 -*-


import jinja2
from pathlib import Path


def generate(filename, component_name):
    CWD = Path(__file__).parent
    src = CWD / 'templates' / f'{filename}.j2'
    dst = CWD / filename
    templateLoader = jinja2.FileSystemLoader(searchpath=str(src.parent))
    templateEnv = jinja2.Environment(loader=templateLoader,
                                     trim_blocks=True,
                                     lstrip_blocks=True,
                                     newline_sequence='\r\n',
                                     keep_trailing_newline=True)
    template = templateEnv.get_template(src.name)
    template.stream(component_name=component_name).dump(str(dst))
    
    print(f'File {filename} generated.')

if __name__ == '__main__':
    print('The folder when you store a project must have the same name as Project Name')

    component_name = input("Enter Project Name: ")
    eclipse_project_filename = '.project'
    eclipse_cproject_filename = '.cproject'
    
    generate('.project', component_name)
    generate('.cproject', component_name)
