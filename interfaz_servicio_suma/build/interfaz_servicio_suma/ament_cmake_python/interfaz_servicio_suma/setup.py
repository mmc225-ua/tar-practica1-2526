from setuptools import find_packages
from setuptools import setup

setup(
    name='interfaz_servicio_suma',
    version='0.0.0',
    packages=find_packages(
        include=('interfaz_servicio_suma', 'interfaz_servicio_suma.*')),
)
