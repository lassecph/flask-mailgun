from setuptools import setup


setup(
    name='Flask-Mailgun',
    version='0.5',
    url='https://github.com/lassecph/flask-mailgun',
    license='BSD',
    author='LKT',
    description='Adds Mailgun support to Flask applications',
    long_description=__doc__,
    py_modules=['flask_mailgun'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'requests'
        ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)
