#!/usr/bin/env python
# -*- coding: utf-8 -*-


from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize


Sts_Demo_ext = Extension(
    name='Sts_Demo',
    sources=['Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Demo/cython/Sts_Demo.pyx'],
    libraries=['Sts_Common', 'Sts_Stream', 'Sts_Demo'],
    library_dirs=['Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_Demo/Release', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_Common/Release', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_Assert/Release', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_Trace/Release', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_Error/Release', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_Utils/Release', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_Timer/Release', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_Set/Release', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_Mem/Release', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_Log/Release', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_Sync/Release', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_Port/Release', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_BusyDelay/Release', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_Iface/Release', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_ComStack/Sts_CS_Common/Release', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_Stream/Release', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_Time/Release'],
    include_dirs=['Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Demo', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Common', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Assert', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Trace', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Error', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Utils', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Timer', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Set', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Mem', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Log', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Sync', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/externals/cython/Sts_Framework_Port', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Port', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_BusyDelay', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Iface', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_ComStack/Sts_CS_Common', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Stream', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Time']
)

setup(
    name='Sts_Demo',
    ext_modules=cythonize(
        [Sts_Demo_ext], 
        compiler_directives={'language_level' : '3'},
        include_path=['Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Demo/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Common/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Assert/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Trace/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Error/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Utils/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Timer/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Set/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Mem/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Log/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Sync/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/externals/cython/Sts_Framework_Port/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Port/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_BusyDelay/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Iface/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_ComStack/Sts_CS_Common/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Stream/cython', 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/Sts-Framework/Sts_Time/cython']
    ),
    script_args=['build'], 
    options={'build': {'build_lib': 'Q:/Repo_Workspace/Eclipse/Sts-Framework-Dev/build/cython/Sts-Framework/Sts_Demo/build'}}
)
