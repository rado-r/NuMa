#!/usr/bin/python
import numpy as np

def riadkova_norma(matica):
    ''' Vrati vysledok z riadkovej normy matice (maximum zo suctov prvkov v
        riadkoch matice)

    >>> m = np.array([[1,2,3],[0,1,2],[-10,2,-3]])
    >>> riadkova_norma(m)
    15
    '''
    temp = []
    for riadok in matica:
        temp.append(sum([abs(prvok) for prvok in riadok]))
    return max(temp)

def stlpcova_norma(matica):
    ''' Vrati vysledok zo stlpcovej normy matice (maximum zo suctov prvkov v
        jednotlivych stlpcoch matice

    >>> m = np.array([[1,2,3],[0,1,2],[-10,2,-3]])
    >>> stlpcova_norma(m)
    11
    '''

    matica = np.array(matica)
    temp = []
    for stlpec in matica.transpose():
        temp.append(sum([abs(prvok) for prvok in stlpec]))
    return max(temp)

def frobeniova_norma(matica):
    '''
    >>> m = np.array([[1,2,3],[0,1,2],[-10,2,-3]])
    >>> round(frobeniova_norma(m), 4)
    11.4891
    '''

    temp = []
    for riadok in matica:
        temp.append(sum([pow(prvok, 2) for prvok in riadok]))
    return np.sqrt(sum(temp))