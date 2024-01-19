from setuptools import setup
setup(
        name='checksize',
        version='1.0.0',
        entry_points= {
            'console_scripts': [
                'checksize=checksize:checkloop'
            ]
        }
)
