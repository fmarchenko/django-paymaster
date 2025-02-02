#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from distutils.core import setup

for cmd in ('egg_info', 'develop'):
    if cmd in sys.argv:
        from setuptools import setup

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")

setup(
    name='django-paymaster',
    version='0.2.0',
    author='Dmitriy Vlasov',
    author_email='scailer@lwr.pw',

    include_package_data=True,
    packages=['paymaster'],
    package_data={
        'paymaster': ['migrations/*.py', 'templates/paymaster/*.html']
    },

    url='https://github.com/scailer/django-paymaster/',
    license='MIT license',
    description='Application for integration PayMaster payment system in Django projects.',
    long_description=(
        'Приложение для интеграции платежной системы PayMaster '
        '(http://paymaster.ru/) в проекты на Django. Реализовано '
        'только основное API PayMaster, согласно спецификации'
        'http://paymaster.ru/Partners/ru/docs/protocol/\n\n'
        'С ознакомиться документацией, а так же сообщить об '
        'ошибках можно на странице проекта '
        'http://github.com/scailer/django-paymaster/'
    ),

    requires=['django (>= 1.5)', 'pytz', 'simple_crypt'],

    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)
