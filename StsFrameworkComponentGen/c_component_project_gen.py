#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import jinja2
import datetime
import re
import prompt_toolkit
from pathlib import Path
from prompt_toolkit.terminal.win32_output import NoConsoleScreenBufferError
from PyInquirer import (style_from_dict, Token, prompt, Validator, ValidationError)


CWD = Path(__file__).parent
UNITTESTS_DIRNAME = 'unittests'
FUNCTIONALTESTS_DIRNAME = 'functionaltests'
MOCKS_DIRNAME = 'mocks'
HEADER_TEMPLATE_NAME = 'Sts_Header.h'
MOCKS_HEADER_TEMPLATE_NAME = 'Sts_Mocks_Header.h'
SOURCE_TEMPLATE_NAME = 'Sts_Source.c'
UT_TEMPLATE_NAME = 'Sts_UnitTest_ut.c'
CMAKELIST_TEMPLATE_NAME = 'CMakeLists.txt'
FTEST_HEADER_GEN_TEMPLATE_NAME = 'Sts_FunctionalTest_Gen_ftest.h'
FTEST_SOURCE_GEN_TEMPLATE_NAME = 'Sts_FunctionalTest_Gen_ftest.c'
FTEST_CMAKELIST_GEN_TEMPLATE_NAME = 'FunctionalTest_Gen_CMakeLists.txt'
FTEST_HEADER_SPEC_TEMPLATE_NAME = 'Sts_FunctionalTest_Spec_ftest.h'
FTEST_SOURCE_SPEC_TEMPLATE_NAME = 'Sts_FunctionalTest_Spec_ftest.c'
FTEST_CMAKELIST_SPEC_TEMPLATE_NAME = 'FunctionalTest_Spec_CMakeLists.txt'

IA_CLI_STYLE = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#42dff4 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#42dff4 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


def generate(template_name, 
             dst_dir, 
             filename, 
             component_name, 
             author, 
             is_mock_header=False,
             ftest_gen_component_name=None):
    template_path = CWD / 'templates' / template_name
    dst = dst_dir / filename
    templateLoader = jinja2.FileSystemLoader(searchpath=str(template_path.parent))
    templateEnv = jinja2.Environment(loader=templateLoader,
                                     trim_blocks=True,
                                     lstrip_blocks=True,
                                     newline_sequence='\r\n',
                                     keep_trailing_newline=True)
    template = templateEnv.get_template(template_path.name)
    template.stream(
        module_name=component_name, 
        MODULE_NAME=name_to_upper_snake(component_name),
        author=author,
        creation_date=datetime.datetime.today().strftime('%Y-%m-%d'),
        is_mock_header=is_mock_header,
        ftest_gen_component_name=ftest_gen_component_name
    ).dump(str(dst))
    
    print(f'File {filename} generated.')


def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def name_to_upper_snake(name):
    name_parts = name.split('_')
    for i in range(len(name_parts)):
        name_parts[i] = camel_to_snake(name_parts[i])
    return '_'.join(name_parts).upper()


if __name__ == '__main__':
    try:
        prompt_toolkit.shortcuts.clear()
    except NoConsoleScreenBufferError:
        sys.exit(f'[ERROR]: In Windows please type: "winpty python {__file__.split("/")[-1]}"')
    
    questions = [
        {
            'type': 'input',
            'name': 'component_name',
            'message': 'Enter C Component Name:',
        },
        {
            'type': 'input',
            'name': 'author',
            'message': 'Enter Author:',
        },
        {
            'type': 'confirm',
            'name': 'is_ut',
            'message': 'Generate files for unit tests?',
            'default': False
        },
        {
            'type': 'confirm',
            'name': 'is_mock_header',
            'message': 'Generate header for specific mocks?',
            'default': False,
            'when': lambda answers: answers['is_ut']
        },
        {
            'type': 'confirm',
            'name': 'is_ftest_gen',
            'message': 'Generate files for generic functional tests?',
            'default': False
        },
        {
            'type': 'confirm',
            'name': 'is_ftest_spec',
            'message': 'Generate files for specific functional tests?',
            'default': False,
            'when': lambda answers: not answers['is_ftest_gen']
        },
        {
            'type': 'input',
            'name': 'ftest_gen_component_name',
            'message': 'Enter generic functional test component name:',
            'when': lambda answers: not answers['is_ftest_gen'] and answers['is_ftest_spec']
        },
    ]
    answers = prompt(questions, style=IA_CLI_STYLE)
    component_name = answers['component_name']
    author = answers['author']
    is_ut = answers['is_ut']
    is_mock_header = answers['is_mock_header'] if is_ut else False
    is_ftest_gen = answers['is_ftest_gen']
    is_ftest_spec = answers['is_ftest_spec'] if not is_ftest_gen else False
    ftest_gen_component_name = answers['ftest_gen_component_name'] if is_ftest_spec else None
    
    component_dirpath = CWD / component_name
    component_dirpath.mkdir(parents=True, exist_ok=True)
     
    if is_mock_header:
        mock_header_dirpath = CWD / component_name / UNITTESTS_DIRNAME / MOCKS_DIRNAME
        mock_header_dirpath.mkdir(parents=True, exist_ok=True)
    
    generate(HEADER_TEMPLATE_NAME, 
             component_dirpath, 
             f'{component_name}.h', 
             component_name, 
             author)
    generate(SOURCE_TEMPLATE_NAME, 
             component_dirpath, 
             f'{component_name}.c',
              component_name, 
              author)
    generate(CMAKELIST_TEMPLATE_NAME, 
             component_dirpath, 
             'CMakeLists.txt',
             component_name, 
             author, 
             is_mock_header=is_mock_header)
    
    if is_ut:
        unittests_dirpath = CWD / component_name / UNITTESTS_DIRNAME
        unittests_dirpath.mkdir(parents=True, exist_ok=True)
        
        generate(UT_TEMPLATE_NAME, 
                 unittests_dirpath, 
                 f'{component_name}_ut.c', 
                 component_name, 
                 author, 
                 is_mock_header=is_mock_header)
    
        if is_mock_header:
            generate(MOCKS_HEADER_TEMPLATE_NAME, 
                     mock_header_dirpath, 
                     f'{component_name}_ut_mocks.h', 
                     component_name, 
                     author,
                     is_mock_header=is_mock_header)
        
    if is_ftest_gen:
        ftest_dirpath = CWD / component_name / FUNCTIONALTESTS_DIRNAME
        ftest_dirpath.mkdir(parents=True, exist_ok=True)
    
        generate(FTEST_HEADER_GEN_TEMPLATE_NAME, 
                 ftest_dirpath, 
                 f'{component_name}_ftest.h', 
                 component_name, 
                 author)
        generate(FTEST_SOURCE_GEN_TEMPLATE_NAME, 
                 ftest_dirpath, 
                 f'{component_name}_ftest.c', 
                 component_name, 
                 author)
        generate(FTEST_CMAKELIST_GEN_TEMPLATE_NAME,
                 ftest_dirpath,
                 'CMakeLists.txt',
                 component_name, 
                 author)
        
    if is_ftest_spec:
        ftest_dirpath = CWD / component_name / FUNCTIONALTESTS_DIRNAME
        ftest_dirpath.mkdir(parents=True, exist_ok=True)
    
        generate(FTEST_HEADER_SPEC_TEMPLATE_NAME, 
                 ftest_dirpath, 
                 f'{component_name}_ftest.h', 
                 component_name, 
                 author,
                 ftest_gen_component_name=ftest_gen_component_name)
        generate(FTEST_SOURCE_SPEC_TEMPLATE_NAME, 
                 ftest_dirpath, 
                 f'{component_name}_ftest.c', 
                 component_name, 
                 author,
                 ftest_gen_component_name=ftest_gen_component_name)
        generate(FTEST_CMAKELIST_SPEC_TEMPLATE_NAME,
                 ftest_dirpath,
                 'CMakeLists.txt',
                 component_name, 
                 author,
                 ftest_gen_component_name=ftest_gen_component_name)
