#!/usr/bin/python
import argparse
from numpy.lib.polynomial import poly1d

def lagrange(x, w, verbose=False):
    M = len(x)
    p = poly1d(0.0)
    for j in xrange(M):
        pt = poly1d(w[j])
        for k in xrange(M):
            if k == j: continue
            fac = x[j]-x[k]
            pt *= poly1d([1.0,-x[k]])/fac
        p += pt

    if verbose:
        print("Lagrangerov interpolacny polynom je:\n{}".format(p))
    else:
        print(p)
    return p

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", default=False,
        help="Zapina rozsireny vypis.")
    parser.add_argument("x", help="Zoznam hodnot x. [-2,-1,0,2]]")
    parser.add_argument("fx", help="Zoznam vysledkov funkcie f(x)")

    args = parser.parse_args()

    try:
        x = eval(args.x)
        fx = eval(args.fx)
    except SyntaxError as err:
        print("Nespravne zadany vstup.")
        parser.print_help()
    else:
        if (len(x) == len(fx)):
            lagrange(x, fx, args.verbose)
        else:
            parser.print_help()