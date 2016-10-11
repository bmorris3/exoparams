.. doctest-skip-all

exoparams
=========

Get exoplanet parameters from `exoplanets.org <http://exoplanets.org/>`_ in
Python. All *columns* of the exoplanets.org table are stored on the
``PlanetParams`` object as *attributes*, and unitful quantities are represented
with ``astropy.unit.Quantity`` objects whenever possible. For example::

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

The exoplanets.org database is downloaded once and cached (unless you
specifically want a fresh download).

