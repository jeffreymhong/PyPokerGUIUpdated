from setuptools import setup, find_packages

setup(
    name = 'PyPokerGUI',
    version = '0.0.7',
    author = 'ishikota',
    author_email = 'ishikota086@gmail.com',
    description = 'GUI application for PyPokerEngine',
    license = 'MIT',
    keywords = 'python poker engine gui',
    url = 'https://github.com/ishikota/PyPokerGUI',
    packages = [pkg for pkg in find_packages() if pkg != "tests"],
    package_data={
        'pypokergui': [
            'server/static/*.css',
            'server/static/*.js',
            'server/static/images/*',
            'server/templates/*',
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        'pypokerengine',
        'tornado==6.4',
        'click==8.0',
        'PyYAML==6.0',
    ],
    entry_points={
        'console_scripts': ['pypokergui=pypokergui.__main__:cli']
    },
    )

