from setuptools import setup, find_packages
from os.path import join

name = 'spear.menu'
version = "0.1a"
readme = open("README.txt").read()
history = ""

setup(name = name,
      version = version,
      description = 'Plone menu for spear',
      long_description = readme[readme.find('\n\n'):] + '\n' + history,
      keywords = 'plone CMS zope',
      author = 'Souheil Chelfouh',
      author_email = 'trollfot@gmail.com',
      url = 'http://tracker.trollfot.org',
      download_url = '',
      license = 'GPL',
      packages = find_packages(),
      namespace_packages = ['spear'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      install_requires=[
          'setuptools',
          'five.grok',
          'spear.content'
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
