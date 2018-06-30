from setuptools import setup
from insta_meter import version as v


description = open('README.rst').read()

version = v.__version__

setup(
    name='insta_meter',
    packages=['insta_meter'],
    include_package_data=True,
    version=version,
    description='library for gathering any instagram account statistic',
    long_description=description,
    author='Aleksej Krichevsky',
    author_email='krich.al.vl@gmail.com',
    url='https://github.com/kricha/insta_meter',
    download_url='https://github.com/kricha/insta_meter/archive/{}.tar.gz'.format(version),
    keywords=['instagram', 'statistic', 'analytic'],
    license='MIT',
    classifiers=[  # look here https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
    ],
    install_requires=[
        'tqdm',
        'requests'
    ],
)
