from setuptools import find_packages, setup

setup(

    # name='djangocraft',
    # packages=find_packages(),
    package_data={
        'djangocraft': ['data/*.txt','*pyproject.toml','*setup.py'],
        },
    # zip_safe= False,
    # install_requires = ['distribute'],    

    
    # tar -xzvf packagename.tar.gz
    # packages=['djangocraft'],
    # package_dir={'djangocraft':'src/djangoauth'},
    
)
