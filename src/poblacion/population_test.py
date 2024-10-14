# Oscar AG - 2024

from poblacion import *

def test_read(path: str) -> Registros:
    entries = Registros.read(path)
    print('First 3 entries: {}\nLast 3 entries: {}\n'.format(entries[:3], entries[-3::]))
    return entries

def test_countries(entries: Registros):
    _countries = entries.countries()
    print('Countries: {}\n'.format(_countries))

def test_filter_name(entries: Registros):
    _entries = entries.filter_by_country('Spain')
    print('{}\n'.format(_entries))

def test_filter_name_year(entries: Registros):
    _entries = entries.filter_by_countries_year(['Spain', 'Germany'], 2015)
    print('{}\n'.format(_entries))

def test_population_evolution(entries: Registros):
    entries.show_population_evolution('Spain')

def test_population_comparison(entries: Registros):
    entries.show_comparison(['Spain', 'Germany'], 2000)

if __name__ == '__main__':
    entries = test_read(DEF_PATH)
    test_countries(entries)
    test_filter_name(entries)
    test_filter_name_year(entries)
    test_population_evolution(entries)
    test_population_comparison(entries)
