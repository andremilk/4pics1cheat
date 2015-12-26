import argparse

parser = argparse.ArgumentParser(description='Cheat on 4pics1word using brutefoce.')

parser.add_argument('-l', metavar='en, pt', type=str, nargs=1, default='pt',
                   help='a string to indicate the language')

parser.add_argument('-s', type=int, nargs=1, help='size of the word to be matched')
parser.add_argument('chars', metavar='string of chars', type=str, nargs='+',
                   help='characters to be used')

args = parser.parse_args()
print(args)
