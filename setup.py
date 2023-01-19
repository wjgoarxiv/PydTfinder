from setuptools import setup

setup(
	  name='PydTfinder', 
	  version='1.1.0',  
	  description='::A tool to find the phase eq temperature at a given pressure with a given ΔT value::',
	  long_description= 'Added useful features for the user.', 
	  author='wjgoarxiv',
	  author_email='woo_go@yahoo.com',
	  url='https://pypi.org/project/PydTfinder/',
	  license='MIT',
	  py_modules=['PydTfinder'],
	  python_requires='>=3.8', #python version required
	  install_requires = [
	  'matplotlib',
	  'numpy',
	  'scikit-learn',
	  'scipy',
	  'pandas',
	  'seaborn',
	  'argparse',
    'pyfiglet',
    'tabulate',
	  ],
	  packages=['PydTfinder'],
		entry_points={
			'console_scripts': [
				'pydtfinder = PydTfinder.__main__:main'
			]
		}
	)
