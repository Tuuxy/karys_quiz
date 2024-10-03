from setuptools import setup, find_packages

setup(
    name='karys_quiz',
    version='0.1.0',
    description='Karys trivia quiz library using Open Trivia DB.',
    author='Karys Hautmont',
    author_email='hautmont.karys@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'karys_quiz=package.main:main',
        ],
    },
)

