import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='better-pywhois',
    version='0.0.1',
    description='a WHOIS library for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=setuptools.find_packages(),
    author='Cynthia Revstrom',
    author_email='me@cynthia.re',
    keywords=['whois'],
    url='https://github.com/bitcynth/better-pywhois',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)