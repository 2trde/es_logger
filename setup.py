from setuptools import setup

setup(name='es_logger',
      version='0.1',
      description='Log events and errors to elasticsearch',
      url='http://github.com/2trde/amqp_dsl',
      author='Daniel Kirch',
      author_email='daniel.kirch@2trde.com',
      packages=['es_logger'],
      install_requires=['requests'])
