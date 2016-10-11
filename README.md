exoparams
=========
![](http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat)

Grab exoplanet parameters, fast!

```python
>>> from exoparams import PlanetParams

>>> p = PlanetParams('HAT-P-11 b')

>>> p.per  # orbital period
<Quantity 4.8878162 d>

>>> p.tt  # mid-transit time
<Time object: scale='utc' format='jd' value=2454605.89132>

>>> p.transit  # is planet transiting?
True

>>> p.r  # planet radius
<Quantity 0.422 jupiterRad>

>>> p.mass  # planet mass
<Quantity 0.0825354 jupiterMass>

>>> (p.mass / (4./3 * 3.1415 * p.r**3)).decompose()  # computer your own planet density
<Quantity 1362.4203351174147 kg / m3>

>>> p.orbref  # Show reference for planet's orbit
'Bakos 2010'
```

Comments and contributions welcome!
    
## Status shields

![https://travis-ci.org/bmorris3/exoparams](http://img.shields.io/travis/bmorris3/exoparams.svg?branch=master)

![http://exoparams.readthedocs.io/en/latest/](https://readthedocs.org/projects/exoparams/badge/?version=latest)
