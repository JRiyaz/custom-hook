from setuptools import setup, find_packages

setup(
    name='custom-hooks',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'check-hello = custom_hooks.check_hello:main',
            'check-print-statement = custom_hooks.check_print_statement:main'
        ]
    },
    install_requires=[],
    extras_require={}
)
