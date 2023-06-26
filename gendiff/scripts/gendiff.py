#!/usr/bin/env python3
import argparse


parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', type=str, help='First file')
parser.add_argument('second_file', type=str, help='Second_file')
args = parser.parse_args()
print(args.indir)


def main():
    print('Hi! This is gendiff.py!')



if __name__ == '__main__':
    main()



