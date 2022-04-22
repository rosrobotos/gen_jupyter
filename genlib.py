"""
Generator for genetic algoritms

functions for creating creatures and generations.
create_creature() return creature (pandas Series)
create_generation return generation (pandas DataFrame)
create_many_generations will return many generations some day (pandas DataFrame)
"""

__version__ = 0.14
__author__ = 'github.com/rosrobotos'

import random as rnd
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.plotting.register_matplotlib_converters()


def create_creature(gen_length=10,
                    creature_name='one'):
    creature = pd.Series(data=[rnd.randint(0, 1) for i in range(gen_length)],
                         name=creature_name)
    return creature


def create_generation(generation_size=50,
                      gen_length=10):
    generation = pd.DataFrame(data=[create_creature(creature_name=(str(i + 1)) + 'th',
                                                    gen_length=gen_length) for i in range(generation_size)])
    generation['quality'] = generation.sum(axis=1)
    return generation


def __indexes_of_quality(generation):
    """
    :rtype: pd.Series
    """
    for i in generation.quality.unique():
        print('quality = ', i, ': ',
              generation.loc[generation.quality == i, 'quality'].index.values,
              '\n',
              '__')

def one_generation_pyplot(generation):
    """
    paint pyplot!!!!
    """
    sns.barplot(x=generation.index,
                y=generation.sort_values('quality').quality)
    plt.show()


def many_generations_pyplot(list_of_generations):
    qualities = [sum(generation.quality) for generation in list_of_generations]
    sns.lineplot(data=qualities)
    plt.show()


def __mutation(creature: pd.Series) -> pd.Series:
    point = rnd.randint(0, len(creature))
    creature[point] = int(not creature[point].values)
    creature['quality'] = 0
    creature['quality'] = creature.sum(axis=1)
    return creature


def almost_generation(generation, chance=0.1):
    
    sample = generation.sample()
    sample = __mutation(sample)
    generation.loc[sample.index] = sample[generation.columns].values
    return generation
