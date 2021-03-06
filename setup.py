from setuptools import setup, find_packages
import os

version = '1.0.4.dev0'

tests_require = [
    'ftw.lawgiver [tests]',
    'plone.app.testing',
    'Products.PloneFormGen'
    ]

setup(name='onegov.edu',
      version=version,
      description="Policy package for OneGov.edu pages",
      long_description=open("README.txt").read() + "\n" + \
          open(os.path.join("docs", "HISTORY.txt")).read(),

      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.2',
        'Programming Language :: Python',
        ],

      keywords='onegov edu plone',
      author='Verein OneGov',
      author_email='mailto:info@4teamwork.ch',
      url='http://github.com/onegov/onegov.edu',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['onegov', ],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'Plone',
        'Products.CMFPlacefulWorkflow',
        'Products.PloneFormGen < 1.8.0.a',
        'ftw.calendar',
        'ftw.contentpage >= 1.11.0',
        'ftw.inflator',
        'ftw.lawgiver',
        'ftw.slider',
        'ftw.subsite',
        'ftw.upgrade >= 1.11.0',
        'plonetheme.onegov',
        'setuptools',
        'simplelayout.types.flowplayerblock',
        'simplelayout.ui.base >= 3.0.3',
        ],

      tests_require=tests_require,
      extras_require=dict(tests=tests_require),

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
