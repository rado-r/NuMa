#!/usr/bin/python
'''
Created on 29.10.2012

@author: rado
'''
import argparse

def babylon(S, odhad, presnost, verbose=False):
    x0 = float(odhad)
    i = 0
    temp = 0.0
    # ak bude absolutna chyba vacsia ako vyzadovana prestnost
    while abs(float(x0) - float(temp)) >= 10**(-presnost):
        i += 1
        temp = x0
        x0 = (1.0/2.0)*(x0 + S/x0)
        if verbose:
            print("X{i} = (1/2) * ({temp} + ({S} / {temp})) = {x0}".format(**locals()))
    if verbose:
        print("Odmocnina z cisla {S} pomocou Babylonskej metody na {presnost} "\
        "desatin(ne/nych) miest(a) je {x0:.{presnost}f}".format(**locals()))
    else:
        print("{0:.{1}f}".format(x0, presnost))
    return x0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("S", type=int, help="Cislo ktore chceme odmocnit." \
                        "(Musi byt vacsie ako 0)")
    parser.add_argument("odhad", type=int, help="Priblizny odhad vysledku." \
                        "(Musi byt vacsie ako 0)")
    parser.add_argument("presnost", type=int, help="Na kolko desatinych miest."\
                        "(Musi byt vacsie ako 0)", default=2)
    args = parser.parse_args()

    if args.S <= 0 or args.odhad <= 0 or args.presnost <= 0:
        parser.print_help()
    else:
        babylon(args.S, args.odhad, args.presnost, args.verbose)
    
    
    
