from setuptools import setup, find_packages
import os

VERSION = '0.0.5'
DESCRIPTION = 'Easily cut the video by moviepy'

setup(
    name="my_project",
    version="1.0",
    author="guoguogewangzi",
    author_email="87986359@qq.com",
    long_description_content_type = "text/markdown",
    long_description = open('README.MD',encoding="UTF8").read(),
    packages=find_packages(),
    install_requires = ['moviepy'],
    keywords=['python','moviepy','cut video'],
    data_files=[ ( 'cut_video', [ 'cut_video/clip_to_erase.json '])],
    entry_points ={
    'console_scripts':['cut_video = cut_video.main:main']
    },
    license="MIT",
    url="http://iswbm.com/", 
    scripts=[ 'cut_video/cut_video.py'],
    classifiers= [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ]
)