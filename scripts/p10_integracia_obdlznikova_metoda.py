#!/usr/bin/python
import argparse
import math

def funkcia(x):
    #return x + math.sin(x) - 2
    #return 10 * math.cos(x-1) - (x**2) + 2 * x - 1
    #return x**2 - x - (6.0/7.0)*math.log(x)    // log je v skutocnosti ln ( klasicky log je log10)
    #return x + math.log(x) - 2
    return math.e**x
    #return math.cos(x**2)

def obdlzniky(a, b, m, presnost, verbose):
    presnost = 10**(-presnost)
    h = (b - a) / m
    J = 0
    I = []
    for i in xrange(m):
        J += funkcia(((a + (h*i)) + (a + h * (i + 1))) / 2)
    I.append(h * J)

    if verbose:
        print("m: {0}\th: {1}\tIh: {2}\todchylka: {3}".format(m, h, I[0],
            "neznama"))

    k = 0
    while True:
        J = 0
        m *= 2
        h = h/2
        for i in xrange(m):
            J += funkcia(((a + (h*i)) + (a + h * (i + 1))) / 2)
        I.append(h * J)

        if verbose:
            print("m: {0}\th: {1}\tIh: {2}\todchylka: {3}".format(m, h, I[k+1],
                  abs(I[k] - I[k+1])))

        if (abs(I[k] - I[k+1])) <= presnost:
            k += 1
            break
        k += 1

    if verbose:
        print("Vysledok je: {}".format(I[k]))
    return I[k]



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true",
        help="Zapina rozsireny vypis.")
    parser.add_argument("a", type=float, help="Zaciatok intervalu. (Musi byt " \
                                              "mensie ako koniec intervalu)")
    parser.add_argument("b", type=float, help="Koniec intervalu. (Musi byt " \
                                              "vacsi ako zaciatok intervalu)")
    parser.add_argument("m", type=int, help="Pociatocny pocet delenia " \
                                            "intervalu m.")
    parser.add_argument("presnost", type=int, help="Na kolko desatinych " \
                                                   "miest. (Musi byt vacsie " \
                                                   "ako 0)", default=2)
    args = parser.parse_args()

    if args.a >= args.b or args.presnost <= 0 or args.m < 0:
        parser.print_help()
    else:
        obdlzniky(args.a, args.b, args.m, args.presnost, args.verbose)