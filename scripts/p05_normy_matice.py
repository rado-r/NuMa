#!/usr/bin/python
import numpy as np


def abs_sum(zoznam):
    """
    Vracia sucet absolutnych hodnot vsetkych prvkov v zozname.
    """
    return sum([abs(prvok) for prvok in zoznam])

def riadkova_norma(matica):
    #TODO pre vektory funguje inac ako pre matice neviem ci to tak ma byt
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
    temp = []
    for riadok in matica:
        temp.append(abs_sum(riadok))
    return max(temp)

def check_norms(A):
    if riadkova_norma(A) < 1:
#        print(riadkova_norma(A))
        return True
    if stlpcova_norma(A) < 1:
        return True
    if frobeniova_norma(A) < 1:
        return True

def stlpcova_norma(matica):
    #TODO pre vektory funguje inac ako pre matice neviem ci to tak ma byt
    ''' Vrati vysledok zo stlpcovej normy matice (maximum zo suctov prvkov v
        jednotlivych stlpcoch matice

    >>> m = np.array([[1,2,3],[0,1,2],[-10,2,-3]])
    >>> stlpcova_norma(m)
    11
    '''
    matica = np.array(matica).transpose()
    temp = []
    for stlpec in matica:
        temp.append(sum([abs(prvok) for prvok in stlpec]))
    return max(temp)

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

def iter_tvar(M):
    M_pom = np.array([[float(x) for x in range(len(M))] for a  in range(len(M))])
    for i in range(len(M)):
        for j in range(len(M)):
            M_pom[i][j] = float(-1) * float(M[i][j]) / float(M[i][i])
            print M_pom[i][j]
            if i == j:
                M_pom[i][j] = 0.0
   # print M_pom
    return M_pom