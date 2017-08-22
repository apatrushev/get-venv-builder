from setuptools import setup

setup(
    name='get-venv-builder',
    version='0.1',
    url='https://github.com/apatrushev/get-venv-builder',
    description='Tool to create scripts for virtualenv bootstrap.',
    license='MIT',

    author='Anton Patrushev',
    author_email='apatrushev@gmail.com',

    packages=[
        'get_venv_builder',
    ],
    package_data={
        'get_venv_builder': [
            'resources/*'
        ]
    },
    zip_safe=False,
    platforms='any',

    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': ['gvb=get_venv_builder.build:main'],
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ]
)
