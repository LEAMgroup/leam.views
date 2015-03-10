from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='leam.views',
      version=version,
      description="A bridge product to provide some views of LEAM AT content types.",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Jeff Terstriep',
      author_email='jefft@leamgroup.com',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['leam'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.wtf',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
