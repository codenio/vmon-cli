from setuptools import setup, find_packages

setup(
    name = 'vmon',
    version = '0.2.0',
    packages = find_packages(exclude=[]),
    install_requires=[
        "click==7.1.2",
        "cycler==0.10.0",
        "DateTime==4.3",
        "kiwisolver==1.3.1",
        "matplotlib==3.3.3",
        "numpy==1.19.4",
        "pandas==1.1.5",
        "Pillow==8.0.1",
        "pyparsing==2.4.7",
        "python-dateutil==2.8.1",
        "pytz==2020.4",
        "scipy==1.5.4",
        "six==1.15.0",
        "zope.interface==5.2.0",
    ],
    entry_points = {
        'console_scripts': [
            'vmon = vmon.main:cli'
        ]
    })
