# exoparams

Get exoplanet parameters from [exoplanets.org](http://exoplanets.org/) in Python. All _columns_ of the exoplanets.org table are stored on the `PlanetParams` object as _attributes_, and unitful quantities are represented with `astropy.unit.Quantity`s whenever possible. For example: 

```python
In [1]: from exoparams import PlanetParams

In [2]: p = PlanetParams('HAT-P-11 b')

In [3]: p.per  # orbital period
Out[3]: <Quantity 4.8878162 d>

In [4]: p.tt  # mid-transit time
Out[4]: <Time object: scale='utc' format='jd' value=2454605.89132>

In [5]: p.transit  # is planet transiting?
Out[5]: True
```

The exoplanets.org database is downloaded once and cached (unless you specifically want a fresh download).

Comments and contributions welcome!
