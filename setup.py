#!/usr/bin/env python
import os
from distutils.core import setup, Extension
from numpy.distutils.misc_util import get_numpy_include_dirs

# Begin config.
cppad_include_dir = []
cppad_lib_dir = []
boost_python_include_dir = ['/usr/local/include']
boost_python_lib_dir = ['/usr/local/lib']
libbost_python_name = 'boost_python-mt'
# End config.

cppad_extension_name          = os.path.join('pycppad', 'cppad_')
cppad_extension_include_dirs  = get_numpy_include_dirs()
cppad_extension_include_dirs += cppad_include_dir
cppad_extension_include_dirs += boost_python_include_dir
cppad_extension_library_dirs  = cppad_lib_dir
cppad_extension_library_dirs += boost_python_lib_dir
cppad_extension_libraries    = [libbost_python_name]

cppad_source_files = ['adfun.cpp', 'pycppad.cpp', 'vec2array.cpp', 'vector.cpp']
cppad_extension_sources = map(lambda p: os.path.join('pycppad', p),
                              cppad_source_files)

extension_modules = [ Extension(
  cppad_extension_name                        ,
  cppad_extension_sources                     ,
  include_dirs = cppad_extension_include_dirs ,
  library_dirs = cppad_extension_library_dirs ,
  libraries    = cppad_extension_libraries    ,
) ]

brad_email             = 'bradbell @ seanet dot com'
sebastian_email        = 'sebastian dot walter @ gmail dot com'
package_author_email   = sebastian_email + ' , ' + brad_email

setup(
  name         = 'pycppad',
  version      = '20111018',
  license      = 'BSD',
  description  = 'Python Algorihtmic Differentiation Using CppAD',
  author       = 'Bradley M. Bell and Sebastian F. Walter',
  author_email = package_author_email,
  url          = 'http://github.com/b45ch1/pycppad/tree/master',
  ext_modules  = extension_modules,
  packages     = [ 'pycppad' , 'pycppad' ],
  package_dir  = { 'pycppad' : 'pycppad' },
)
