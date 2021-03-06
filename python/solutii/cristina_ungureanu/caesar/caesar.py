#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Pentru decriptarea cifrului Caesar."""

from __future__ import print_function


def decripteaza(mesaj):
    """In fisierul decript scrie posibilele decriptari ale mesajului."""
    newfisier = open("decript", "a")
    original = [item.lower() for item in mesaj]
    numere = [ord(item) for item in original]
    for index in range(1, 26):
        posibil = []
        for item in numere:
            if item >= 97 and item <= 122:
                if item-index >= 97:
                    posibil.append(chr(item-index))
                else:
                    amount = item - 97
                    posibil.append(chr(122-(index-amount)+1))
            else:
                posibil.append(chr(item))
        if 'ave caesar.' in ''.join(posibil):
            newfisier.write(''.join(posibil) + "\n")
            break
    newfisier.close()


def main():
    """Apeleaza metoda de decriptare pentru fiecare linie."""
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print ("Nu am putut obține mesajele.")
        return
    newfisier = open("decript", "w")
    newfisier.close()
    for mesaj in mesaje.splitlines():
        decripteaza(mesaj)


if __name__ == "__main__":
    main()
