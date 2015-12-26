from word_matching import MatchingDB
import sys

def main():
    mdb = MatchingDB.MatchingDB('172.17.0.2', 'root', 'root', 'word', 'word', 'word')
    # TODO: select matcher 
    try:
        while True:
            number_of_chars, pattern = input("Number of characters and pattern :").split(' ')
            possible_solutions = []
            results = set()
            for word in mdb.get_words(int(number_of_chars)):
                new_pattern = pattern
                for c in word[1]:
                    if c not in new_pattern: 
                        break
                    else:
                        new_pattern = new_pattern.replace(c, "", 1)
                else:
                    results.add(word[1])

            print(sorted(results))
    except KeyboardInterrupt:
        print('')
        sys.exit(0)



if __name__ == '__main__':
    main()
