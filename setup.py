import os
import re
from setuptools import setup, find_packages


setup(
    name = 'online-games',
    description = ("Play online games"),
    version = '0.0.0',
    packages = find_packages(exclude=['parts']),
    author = 'Aditi',
    url = 'http://sudoku-sports.com',
    license = 'GPLv2',
    include_package_data = True,
    zip_safe = False,
    )
