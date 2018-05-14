from distutils.core import setup

setup(
    name='shangyin',
    version='1.0',
    description='Coffee addiction tracker',
    author='Marian Hlavac',
    author_email='hlavac95@gmail.com',
    url='https://github.com/mmajko/shangyin',
    packages=['shangyin', 'shangyin.interface', 'shangyin.server'],
)