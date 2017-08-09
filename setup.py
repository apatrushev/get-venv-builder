from setuptools import setup, find_packages

setup(
    name='get-venv-builder',
    version='0.1',
    author='Anton Patrushev',
    author_email='apatrushev@gmail.com',
    description='Tool to create virtualenv bootstrap scripts.',
    zip_safe=False,
    packages=[
        'get_venv_builder',
    ],
    package_data={
        'get_venv_builder': [
            'resources/*'
        ]
    },
    install_requires=[
        'click',
    ]
)
