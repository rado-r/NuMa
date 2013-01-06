#!/usr/bin/python
import argparse
import numpy as np

import p05_normy_matice as normy

def gauss_seidel(A, b, x, presnost=2, verbose=False):
    k = 0
    x_tmp = x[:]
    presnost = 10**(-presnost)

    if verbose:
        print("A: {}".format(A))
        print("b: {}".format(b))
        print("x: {}".format(x))
        print("#"*10 + " Zaciatok vypoctu " + "#"*10)

    while True:
        k += 1
        for i in range(len(A[0])):  # pocet riadkov
            sum_1 = sum_2 = 0
            for j in range(i):
                sum_1 += A[i][j] * x_tmp[j]
            for j in range(i+1, len(A[0])):
                sum_2 += A[i][j] * x[j]
            x_tmp[i] = 1.0/A[i][i] * float(b[i] - sum_1 - sum_2)

        if verbose:
            print("Momentalna presnost: {}".format(
                abs(normy.riadkova_norma(np.array(x_tmp)) -
                    normy.riadkova_norma(np.array(x)))))
            print("k{}\nx = {}".format(k, x))

        if abs(normy.riadkova_norma(np.array(x_tmp)) -
               normy.riadkova_norma(np.array(x))) <= presnost and k > 2:
            print('-'*20)
            print("Vysledok je: {}".format(x_tmp))
            print("Pouzitych bolo {} iteracii a presnost "\
                  "vysledku je +-{}".format(k, presnost))
            break

        x = x_tmp[:]

'''
A = [[11, 2,  1],
     [1, 10,  2],
     [2,  3, -8]]
b = [15, 16, 1]
x = [0, 0, 0]
jacoby(A, b, x, 5, True)'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", default=False,
        help="Zapina rozsireny vypis.")
    parser.add_argument("A", help="Matica A napr. [[1,2],[3,4]]")
    parser.add_argument("b", help="Vektor pravej strany [3, 4, 5]")
    parser.add_argument("x", help="Pociatocna aproximacia [0, 0, 0]")
    parser.add_argument("presnost", type=int, help="Na kolko desatinych "\
                                                   "miest. (Musi byt vacsie ako 0)", default=2)

    args = parser.parse_args()

    try:
        A = eval(args.A)
        b = eval(args.b)
        x = eval(args.x)
    except SyntaxError as err:
        print("Nespravne zadany vstup.")
        parser.print_help()
    else:
        if (args.presnost > 0):
            gauss_seidel(A, b, x, int(args.presnost), args.verbose)
        else:
            parser.print_help()