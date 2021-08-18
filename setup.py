#!/usr/bin/env python3

import os
import setuptools

package_name = 'command-injection-tester'

f = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'),
         encoding='utf-8')
readme = f.read()
f.close()

setuptools.setup(
    name=package_name,
    version="0.0.2",
    description="Testing servers for STARTTLS command injection vulnerability",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Samson Umezulike, Fabian Ising, Damian Poddebniak, Hanno Böck",
    url='https://nostarttls.secvuln.info/',
    packages=[],
    scripts=['command-injection-tester'],
    python_requires='>=3',
    install_requires=[],
    license="MIT",
    zip_safe=True,
    keywords=['starttls', 'security'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
