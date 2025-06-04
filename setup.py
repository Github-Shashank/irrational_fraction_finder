from setuptools import setup, find_packages

setup(
    name='irrational_fraction_finder',
    version='0.1.0',
    author='Shashank Singh Patel',
    description='Approximate irrational numbers with rational fractions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Github-Shashank/irrational_fraction_finder',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
