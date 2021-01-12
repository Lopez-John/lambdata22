"""lambdata_new - A collection of Data Science Functions"""

import setuptools

REQUIRED = ['numpy',
            'pandas',
            ]

with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='NewLambdata',
    version='0.0.4',
    author='Lopez-John',
    description=LONG_DESCRIPTION,
    url="https://github.com/Lopez-John/lambdata22.git",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=REQUIRED,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ]
)
