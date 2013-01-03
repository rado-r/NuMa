#!/usr/bin/python
'''
Created on 06.11.2012

@author: rado
'''
import argparse
import math

def funkcia(x):
    return x + math.sin(x) - 2
    #return 10 * math.cos(x-1) - (x**2) + 2 * x - 1
    #return x**2 - x - (6.0/7.0)*math.log(x)    // log je v skutocnosti ln ( klasicky log je log10)
    #return x + math.log(x) - 2

def prva_derivacia(x):
    return 1 + math.cos(x)

def druha_derivacia(x):
    return -math.sin(x)

def newtonova_metoda(a, b, presnost, verbose):
    """
        Hladanie korenov funkcie pomocou newtonovej metody
    """
    presnost = 10**(-presnost)
    k = 0
    # urcujeme prve x
    if funkcia(a) * druha_derivacia(a):
        x = a
    else:
        x = b

    while k < 20:
        k += 1
        # vypocita nasledujuce x
        x1 = x - (funkcia(x) / prva_derivacia(x))
        if abs(x1 - x) <= presnost:
            break
        if verbose:
            print("x{} = {}".format(k, x1))
        x = x1

    if verbose:
        print("Korenom rovnice je cislo x = {} +-{}.".format(x1, presnost))
        print("Vysledok sme dostali po {} iteraciach.".format(k))
    else:
        print(x1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", 
                        help="Zapina rozsireny vypis.")
    parser.add_argument("a", type=float, help="Zaciatok intervalu." \
                        "(Musi byt mensie ako koniec intervalu)")
    parser.add_argument("b", type=float, help="Koniec intervalu." \
                        "(Musi byt vacsi ako zaciatok intervalu)")
    parser.add_argument("presnost", type=int, help="Na kolko desatinych " \
                        "miest. (Musi byt vacsie ako 0)", default=2)
    #parser.add_argument("funkcia", default="", help="Funkcia ktorej koren chceme" \
    #                    "vypocitat. Nemusi byt zadana.")
    args = parser.parse_args()
        
    if args.a >= args.b or args.presnost <= 0:
        parser.print_help()
    else:
       newtonova_metoda(args.a, args.b, args.presnost, args.verbose)

