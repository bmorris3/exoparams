from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import json
import os

import numpy as np
from astropy.utils.data import download_file
from astropy.io import ascii
import astropy.units as u
from astropy.time import Time

__all__ = ['PlanetParams']

# Set global variables
EXOPLANETS_CSV_URL = 'http://exoplanets.org/csv-files/exoplanets.csv'
EXOPLANETS_TABLE = None
EXOPLANETS_UNITS = None
TIME_ATTRS = {'TT': 'jd', 'T0': 'jd'}
BOOL_ATTRS = ('ASTROMETRY', 'BINARY', 'EOD', 'KDE', 'MICROLENSING', 'MULT',
              'SE', 'TIMING', 'TRANSIT', 'TREND')


def exoplanets_table(cache=True):
    global EXOPLANETS_TABLE

    if EXOPLANETS_TABLE is None:
        table_path = download_file(EXOPLANETS_CSV_URL, cache=cache)
        EXOPLANETS_TABLE = ascii.read(table_path)

        # Store column of lowercase names for string matching later:
        lowercase_names = [i.lower() for i in EXOPLANETS_TABLE['NAME'].data]
        EXOPLANETS_TABLE['NAME_LOWERCASE'] = lowercase_names

    return EXOPLANETS_TABLE


def exoplanet_units():
    global EXOPLANETS_UNITS

    if EXOPLANETS_UNITS is None:
        pkg_dir = os.path.dirname(os.path.abspath(__file__))
        units_file = open(os.path.join(pkg_dir, 'data', 'param_units.json'))
        EXOPLANETS_UNITS = json.load(units_file)

    return EXOPLANETS_UNITS


class PlanetParams(object):
    def __init__(self, exoplanet_name, cache=True):
        """
        Exoplanet system parameters.

        Parameters
        ----------
        exoplanet_name : str
            Name of exoplanet
        cache : bool (optional)
            Cache exoplanet table to local astropy cache? Default is `True`.
        """
        # Load exoplanets table, corresponding units
        table = exoplanets_table()
        param_units = exoplanet_units()

        if exoplanet_name.lower() in table['NAME_LOWERCASE'].data:
            row_index = np.argwhere(table['NAME_LOWERCASE'].data ==
                                    exoplanet_name.lower())[0, 0]
        else:
            raise ValueError('Planet "{0}" not found in exoplanets.org catalog')

        for column in table.keys():
            value = table[column][row_index]

            # If param is unitful quantity, make it a `astropy.units.Quantity`
            if column in param_units:
                parameter = u.Quantity(value, unit=param_units[column])

            # If param describes a time, make it a `astropy.time.Time`
            elif column in TIME_ATTRS:
                parameter = Time(value, format=TIME_ATTRS[column])

            elif column in BOOL_ATTRS:
                parameter = bool(value)

            # Otherwise, simply set the parameter to its raw value
            else:
                parameter = table[column][row_index]

            # Attributes should be all lowercase:
            setattr(self, column.lower(), parameter)

    def __repr__(self):
        return '<{0}: name="{1}">'.format(self.__class__.__name__, self.name)
