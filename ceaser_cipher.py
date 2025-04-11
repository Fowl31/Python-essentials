#!/usr/bin/env python3

import sys


def decompose():
    if len(sys.argv)<4:
        print("Missing <encrypt/decrypt> <plaintext/ciphertext> <shift value>")
        sys.exit(1)

    sys.argv[1].lower()
    if sys.argv[1] == "encrypt":
        inp = sys.argv[2]
        try:
            shift = int(sys.argv[3])
        except ValueError:
            print("Shift value must be integer")
            sys.exit(1)
        encrypt(inp,shift)

    elif sys.argv[1] == "decrypt":
        inp = sys.argv[2]
        try:
            shift = int(sys.argv[3])
        except ValueError:
            print("Shift value must be integer")
            sys.exit(1)
        decrypt(inp,shift)
    else:
        print(f" {sys.argv[1]} is neither encrypt/decrypt")
        sys.exit(1)



def encrypt(inp,shift):
    string = ('')
    for i in inp:
        if i.isalpha():
            if i.isupper():
                ascii_rep = ord(i) - ord('A')
                ascii_rep += shift
                ascii_rep = ascii_rep % 26
                final = chr(ascii_rep + ord('A'))
                string += final

            else:
                ascii_rep = ord(i) - ord('a')
                ascii_rep += shift
                ascii_rep = ascii_rep%26
                final = chr(ascii_rep + ord('a'))
                string += final

        else:
            string += i


    print(f"Cipher text: {string}")


def decrypt(inp,shift):
    string = ('')
    for i in inp:
        if i.isalpha():
            if i.isupper():
                ord_rep = ord(i)
                ord_rep -= ord('A')
                ord_rep -= shift
                ord_rep = ord_rep%26
                final = chr(ord_rep + ord('A'))
                string += final
            else:
                ord_rep = ord(i) 
                ord_rep -= ord('a')
                ord_rep -= shift
                ord_rep = ord_rep%26
                final = chr(ord_rep + ord('a'))
                string += final
        else:
            string += i

    print(f"Plain text: {string}")



decompose()
