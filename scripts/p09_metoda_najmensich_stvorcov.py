#!/usr/bin/python
from __future__ import division
import argparse
from p07_gauss_seidelova_metoda import gauss_seidel

def stvorce(x, fx, verbose=False):
    A = [[len(x), sum(x)]]

    A.append([sum(x), sum([prvok**2 for prvok in x])])
    b = [sum(fx), sum([(p[0] * p[1]) for p in zip(x, fx)])]
    x = [0 for i in range(len(x))]

    #print(A)
    #print b
    vysl = gauss_seidel(A, b, x, 5)
    if verbose:
        print("Vysledkom je priamka: r(x) = {}{:+}x".format(vysl[0], vysl[1]))
    return vysl

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
            stvorce(x, fx, args.verbose)
        else:
            parser.print_help()