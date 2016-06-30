from setuptools import setup, find_packages

setup(name='xyzpy',
      version='0.1.1',
      author='Johnnie Gray',
      license='MIT',
      packages=find_packages(exclude=['contrib', 'docs', 'test*']),
      install_requires=[
          'numpy>=1.10.0',
          'scipy>=0.16.0'
          'xarray>=0.7.0',
          'plotly>=1.9.0',
          'matplotlib>=1.5.0',
          'h5py',
          'h5netcdf',
          ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          ])
