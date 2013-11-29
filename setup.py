from setuptools import setup
from setuptools import Command

__version__ = '0.1.1'
long_description = file('README.rst').read()

class tag(Command):
    """Tag git release."""

    description = __doc__
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        ret = subprocess.call(['git', 'tag', '-a', __version__, '-m', __version__])
        if ret:
            raise SystemExit("git tag failed")
        ret = subprocess.call(['git', 'push', '--tags'])
        if ret:
            raise SystemExit("git push --tags failed")

setup(name='cloudily',
      version=__version__,
      description='Command line tool to visualize your EC2 infrastructure',
      long_description=long_description,
      license='MIT',
      author='Barnaby Gray',
      author_email='barnaby@pickle.me.uk',
      url='http://loads.pickle.me.uk/cloudily/',
      install_requires=['boto', 'paramiko'],
      scripts=['scripts/cloudily'],
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        ],
      cmdclass={
          'tag': tag,
      },
      )
