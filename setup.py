from setuptools import setup, find_packages

setup(
    name='math_quiz',  # name of project
    version='1',  # version of project
    packages=find_packages(),  # included packages
    install_requires=[ 'unittest', 'random'],
        # what i need to install


    # data of project
    author='Haotian Li',
    author_email='erwinli3579@gmail.com',
    description='A math_quiz project',
    long_description='A Python package for solving math quizzes.',
    url='https://github.com/Codierungskatz/dsss_homework_2.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)