#!/usr/bin/env python3

import argparse

def caesar_cipher(text, shift, decrypt=False):
    result = ""
    shift_value = shift if decrypt else -shift
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) + shift_value - ord('a')) % 26 + ord('a'))
            else:
                result += chr((ord(char) + shift_value - ord('A')) % 26 + ord('A'))
        else:
            result += char
    return result

def caesar_cipher_crack(text):
    for shift in range(1, 26):
        decrypted_text = caesar_cipher(text, shift, decrypt=True)
        print(f"ROT {shift}: {decrypted_text}")

def main():
    parser = argparse.ArgumentParser(description='Caesar Cipher Tool')
    parser = argparse.ArgumentParser(description='github: https://github.com/osga24/linux-Caesar-cipher-command')
    parser.add_argument('text', help='Text to process')
    parser.add_argument('shift', type=int, nargs='?', default=0, help='Shift value for encryption/decryption (default: 0)')
    parser.add_argument('-c', action='store_true', help='Encrypt the text')
    parser.add_argument('-d', action='store_true', help='Decrypt the text')
    parser.add_argument('-a', action='store_true', help='List all possible decryptions for shift 1 to 25')

    args = parser.parse_args()

    if args.c and args.d:
        print("Error: -c and -d options cannot be used together.")
        return

    if args.c:
        result = caesar_cipher(args.text, args.shift)
        print(result)
    elif args.d:
        if args.a:
            caesar_cipher_crack(args.text)
        else:
            result = caesar_cipher(args.text, args.shift, decrypt=True)
            print(result)
    elif args.a:
        caesar_cipher_crack(args.text)
    else:
        print("Please use either -c for encryption, -d for decryption, or -a to list all possible decryptions.")

if __name__ == "__main__":
    main()
