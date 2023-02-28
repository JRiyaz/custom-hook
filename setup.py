from setuptools import setup, find_packages

setup(
    name='custom-hooks',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'check-hello = custom_hooks.check-hello',
            'check-print-statement = custom_hooks.check-print-statement'
        ]
    },
    install_requires=[],
    extras_require={}
)
