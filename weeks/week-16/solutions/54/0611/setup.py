from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [Extension("sorts_fast", ["sorts_fast.pyx"])]

setup(ext_modules=cythonize(ext_modules, compiler_directives={"binding": True}))
