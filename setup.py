from setuptools import setup, find_packages

setup(
	name='NEMO',
	version='3.9.0',
	python_requires='>=3.6',
	packages=find_packages(exclude=['NEMO.tests','NEMO.tests.*']),
	include_package_data=True,
	url='https://github.com/usnistgov/NEMO',
	license='Public domain',
	author='Center for Nanoscale Science and Technology',
	author_email='CNSTapplications@nist.gov',
	description='NEMO is a laboratory logistics web application. Use it to schedule reservations, control tool access, track maintenance issues, and more.',
	long_description='Find out more about NEMO on the GitHub project page https://github.com/usnistgov/NEMO',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Web Environment',
		'Framework :: Django',
		'Intended Audience :: Science/Research',
		'Intended Audience :: System Administrators',
		'License :: Public Domain',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3.6',
	],
	install_requires=[
		'cryptography==3.4.6',
		'Django==2.2.19',
		'django-filter==2.4.0',
		'djangorestframework==3.12.2',
		'ldap3==2.9',
		'python-dateutil==2.8.1',
		'requests==2.25.1',
		'Pillow==8.1.2',
		'django-mptt==0.12.0',
	],
	entry_points={
		'console_scripts': ['nemo=NEMO.provisioning:entry_point'],
	},
)
