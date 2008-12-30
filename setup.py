from setuptools import setup, find_packages
from os.path import join

name = 'flint.menu'
version = "0.1"
readme = open("README.txt").read()
history = ""

setup(name = name,
      version = version,
      description = 'Plone menu for flint',
      long_description = readme[readme.find('\n\n'):] + '\n' + history,
      keywords = 'plone CMS zope',
      author = 'Souheil Chelfouh',
      author_email = 'trollfot@gmail.com',
      url = 'http://tracker.trollfot.org',
      download_url = '',
      license = 'GPL',
      packages = find_packages(),
      namespace_packages = ['flint'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      install_requires=[
          'setuptools',
          'five.grok',
          'flint.content'
      ],
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Grok',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
      ],
)
