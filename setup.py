from setuptools import setup,  find_packages

setup(
	name = 'sc2gym',
	packages = find_packages(),
	version = '1.0',
	description = 'make pysc2 easy',
	author = 'lizhihao6',
	author_email = 'lizhihao6@outlook.com',
	install_requires=['PySC2==1.2', 'numpy>=1.14.0', 'logging', 'absl-py']
)