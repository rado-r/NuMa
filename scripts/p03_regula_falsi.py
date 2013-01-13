#!/usr/bin/python
'''
Created on 06.11.2012

@author: rado

Metoda regula falsi alebo tie Metoda secnic.

'''
import argparse
import math

def funkcia(x):
    #return x + math.sin(x) - 2
    #return 10 * math.cos(x-1) - (x**2) + 2 * x - 1
    #return x**2 - x - (6.0/7.0)*math.log(x)    // log je v skutocnosti ln ( klasicky log je log10)
    return x + math.log(x) - 2
                     
def regula_falsi(a, b, presnost, verbose=False):
    """
        Hladanie korenov funkcie pomocou metody regula falsi (metoda secnic).
    """
    presnost = 10**(-presnost)
    k = 0
    a0 = a
    b0 = b
    x = a
    while True:
        k += 1
        x1 = a - ((b - a) / (funkcia(b) - funkcia(a)) * funkcia(a)) 

        if funkcia(x1) == 0: 
            # ak trafime presny vysledok vypocet konci
            break
        elif funkcia(a) * funkcia(x1) < 0:
            b = x1
        else:
            a = x1
        if abs(x1 - x) <= presnost:
            break
        x = x1
        if verbose:
            print("a={}, b={}".format(a, b))
    if verbose:
        print("Vysledok je: {} +-{} a bolo pouzitych {} opakovani.".format(
               x, presnost, k))
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
       regula_falsi(args.a, args.b, args.presnost, args.verbose)

