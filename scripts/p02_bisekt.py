#!/usr/bin/python
'''
Created on 06.11.2012

@author: rado

Metoda bisekcie alebo Metoda polenia intervalu.

'''
import argparse
import math

def funkcia(x):
    #return x + math.sin(x) - 2
    return 10 * math.cos(x-1) - (x**2) + 2 * x - 1
    #math.log(x) je ln ak chceme naozaj log musime pouzit math.log10(x)
    #return x**2 - x - (6.0/7.0)*math.log(x)

def bisekt(a, b, presnost, verbose=False):
    """
        Hladanie korenov funkcie pomocou metody bisekt (delenim intervalu
        na polovicu).
    """
    presnost = 10**(-presnost)
    k = 0
    a0 = a
    b0 = b
    while True:
        k += 1
        x = (a + b) / 2.0

        if funkcia(x) == 0: 
            # ak trafime presny vysledok skonci
            break
        elif funkcia(a) * funkcia(x) < 0:
            # zaciatok intervalu ostava rovnaky a konice intervalu 
            # nastavyme na polovicu teda na x
            b = x
        else:
            # zaciatok intervalu nastavim na stred teda x
            # a koniec zostava b
            a = x
        if b - a <= presnost:
            break
        if verbose:
            print("{}, {}, {}".format(a, b, presnost))
    if verbose:
        print("Vysledok je: {} a bolo pouzitych {} opakovani.".format(
               x, k))
    else:
        print(x)
    return x
                     
  
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", 
                        help="Zapina rozsireny vypis.")
    parser.add_argument("a", type=float, help="Zaciatok intervalu." \
                        "(Musi byt mensie ako koniec intervalu)")
    parser.add_argument("b", type=float, help="Koniec intervalu." \
                        "(Musi byt vacsi ako zaciatok intervalu)")
    parser.add_argument("presnost", type=int, help="Na kolko desatinych miest."\
                        "(Musi byt vacsie ako 0)", default=2)
    #parser.add_argument("funkcia", default="", help="Funkcia ktorej koren chceme" \
    #                    "vypocitat. Nemusi byt zadana.")
    args = parser.parse_args()
        
    if args.a >= args.b or args.presnost <= 0:
        parser.print_help()
    else:
        bisekt(args.a, args.b, args.presnost, args.verbose)


