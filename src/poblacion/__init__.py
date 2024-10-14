# Oscar AG - 2024

try: from typing import List, Tuple, NamedTuple # For static type checking
except: pass

import csv

from collections import namedtuple
from itertools import chain 
from pathlib import Path

from datetime import datetime

import matplotlib.pyplot as plt

DEF_PATH = '{}/data/population.csv'.format(Path.cwd())

RegistroPoblacion = namedtuple('RegistroPoblacion', 'country, code, year, population')

class Registros(list):
    def read(path: str):
        with open(path, encoding="utf-8") as f:
            _parsed = csv.reader(f)
            entries = []
            for l in _parsed: entries.append(RegistroPoblacion(l[0], l[1], datetime.strptime(l[2], '%Y').year, int(l[3])))
            return Registros(entries)

    def countries(self) -> List[str]:
        _countries = set()
        for data in self: _countries.add(data.country)
        return sorted(_countries)

    def show_population_evolution(self, country: str):
        entries = self.filter_by_country(country)
        _, ax = plt.subplots()
        x_axis = list(map(lambda x: x.year, entries))
        y_axis = list(map(lambda x: x.population, entries))
        ax.plot(x_axis, y_axis)
        ax.set(xlabel='year', ylabel='population')
        plt.show()

    def show_comparison(self, countries: list[str], year: int):
        entries = self.filter_by_countries_year(countries, year)
        print(entries)
        _, ax = plt.subplots()
        x_axis = list(map(lambda x: x.country, entries))
        y_axis = list(map(lambda x: x.population, entries))
        ax.bar(x_axis, y_axis)
        ax.set(xlabel='countries', ylabel='population')
        plt.show()
        
    def filter_by_country(self, country: str) -> List[RegistroPoblacion]: # The data will be sorted by year
        # Check whether we have to check for country code or country name, to avoid
        # doing that check in the loop
        entries = None
        if len(c_code := country.lower()) == 3: entries = list(filter(lambda x: x.code.lower() == c_code, self))
        else: entries = list(filter(lambda x: x.country.lower() == country.lower(), self))
        if entries == None or len(entries) == 0: raise Exception('Invalid country name or code')
        entries = sorted(entries, key=lambda x: x.year) # Make sure data is sorted
        return Registros(entries)
    
    def filter_by_countries_year(self, countries: list[str], year: int) -> List[RegistroPoblacion]:
        # Check whether we have to check for country code or country name, to avoid
        # doing that check in the loop
        countries_entries = []
        for country in countries:
            if len(c_code := country.lower()) == 3: countries_entries.append((list(filter(lambda x: x.code.lower() == c_code, self))))
            else: countries_entries.append(list(filter(lambda x: x.country.lower() == country.lower(), self)))
        if len(countries_entries) == 0: raise Exception('All countries were invalid')
        countries_entries = chain.from_iterable(countries_entries)
        countries_entries = sorted(countries_entries, key=lambda x: x.country) # Make sure data is sorted
        print(countries_entries)
        return Registros(countries_entries)
