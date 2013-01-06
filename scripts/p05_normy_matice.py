#!/usr/bin/python

import numpy as np

def abs_sum(zoznam):
    """
    Vracia sucet absolutnych hodnot vsetkych prvkov v zozname.
    """
    return sum([abs(prvok) for prvok in zoznam])

def riadkova_norma(matica):
    ''' Vrati vysledok z riadkovej normy matice (maximum zo suctov prvkov v
        riadkoch matice)

    >>> m = np.array([[1,2,3],[0,1,2],[-10,2,-3]])
    >>> riadkova_norma(m)
    15
    >>> b = [15, 16, 1]
    >>> riadkova_norma(b)
    32
    '''
    matica = np.array(matica)
    if type(matica[0]) == list:
        temp = []
        for riadok in matica:
            temp.append(abs_sum(riadok))
        return max(temp)
    else:
        return abs_sum(matica)

def stlpcova_norma(matica):
    #TODO pre vektory funguje rovnako ako riadkova neviem ako to ma byt
    ''' Vrati vysledok zo stlpcovej normy matice (maximum zo suctov prvkov v
        jednotlivych stlpcoch matice

    >>> m = np.array([[1,2,3],[0,1,2],[-10,2,-3]])
    >>> stlpcova_norma(m)
    11
    '''
    matica = np.array(matica).transpose()
    if type(matica[0]) == list:
        temp = []
        for stlpec in matica:
            temp.append(sum([abs(prvok) for prvok in stlpec]))
        return max(temp)
    else:
        return abs_sum(matica)

def frobeniova_norma(matica):
    #TODO nefunguje na vektory
    '''
    >>> m = np.array([[1,2,3],[0,1,2],[-10,2,-3]])
    >>> round(frobeniova_norma(m), 4)
    11.4891
    '''
    matica = np.array(matica)
    temp = []
    for riadok in matica:
        temp.append(sum([pow(prvok, 2) for prvok in riadok]))
    return np.sqrt(sum(temp))