from setuptools import setup

setup(name='nix-kernel',
      version='0.1.0',
      description='A nix-repl kernel for Jupyter',
      author='Zach Collins',
      author_email='recursive.cookie.jar@gmail.com',
      license='MIT',
      url="https://github.com/corps/nix-kernel",
      install_requires=[
          'pexpect >= 4.0',
          'notebook >= 4.0'],
      packages=['nix-kernel'],
      classifiers=[
          'Framework :: IPython',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: System :: Shells',
      ]
      )
