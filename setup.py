from setuptools import setup

setup(
    name='inst_loader',  # প্যাকেজের নাম
    version='0.1',
    py_modules=['inst_loader'],
    install_requires=[
        'requests',  # আপনার অন্য ডিপেনডেন্সি
        'Flask',
    ],
)
