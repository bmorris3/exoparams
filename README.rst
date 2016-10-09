exoparams
=========

Grab exoplanet parameters, fast!

.. image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat
    :target: http://www.astropy.org/
   
Get exoplanet parameters from `exoplanets.org <http://exoplanets.org/>`_ in 
Python. All *columns* of the exoplanets.org table are stored on the 
``PlanetParams`` object as *attributes*, and unitful quantities are represented
with ``astropy.unit.Quantity`` objects whenever possible.

.. code-block:: python
    In [1]: from exoparams import PlanetParams
    
    In [2]: p = PlanetParams('HAT-P-11 b')
    
    In [3]: p.per  # orbital period
    Out[3]: <Quantity 4.8878162 d>
    
    In [4]: p.tt  # mid-transit time
    Out[4]: <Time object: scale='utc' format='jd' value=2454605.89132>
    
    In [5]: p.transit  # is planet transiting?
    Out[5]: True
    
    In [6]: p.r  # planet radius
    Out[6]: <Quantity 0.422 jupiterRad>
    
    In [7]: p.mass  # planet mass
    Out[7]: <Quantity 0.0825354 jupiterMass>
    
    In [8]: (p.mass / (4./3 * 3.1415 * p.r**3)).decompose()  # computer your own planet density
    Out[8]: <Quantity 1362.4203351174147 kg / m3>
    
    In [9]: p.orbref  # Show reference for planet's orbit
    Out[9]: 'Bakos 2010'

The exoplanets.org database is downloaded once and cached (unless you
specifically want a fresh download).

Comments and contributions welcome!
    
Status shields
++++++++++++++

.. image:: http://img.shields.io/travis/bmorris3/exoparams.svg?branch=master
    :target: https://travis-ci.org/bmorris3/exoparams
    :alt: Travis Status

.. image:: https://readthedocs.org/projects/exoparams/badge/?version=latest
    :target: http://exoparams.readthedocs.io/en/latest/
    :alt: Latest Documentation Status
