from distutils.core import setup
with open("README.md", "r") as f:
      long_description = f.read()

setup(name='wwexercise',
    version='v0.4',
    description='Weight Watchers coding exercise in python',
    url='https://github.com/birdman0030/wwexercise',
    download_url=[
        'https://github.com/birdman0030/wwexercise/archive/v0.4.tar.gz',
        'https://github.com/birdman0030/wwexercise/archive/v0.4.zip'
        ],
    author='Kurt Bird',
    author_email='kurtbird1@gmail.com',
    license='GNU',
    packages=["wwexercise"],
    install_requires=["selenium==3.141.0",
                      "pytest==5.4.1",
                      ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
        ],
)