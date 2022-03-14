import argparse
from main import TextAnal


class Entry:

    parser = argparse.ArgumentParser()
    parser.add_argument('-k', nargs='?', default=10)
    parser.add_argument('-n', nargs='?', default=4)
    args = parser.parse_args()

    def print_ngram(out_dict: dict, k=int(args.k)):
        list_d = list(out_dict.items())
        list_d.sort(key=lambda l: l[1])
        list_d.reverse()

        print(*[f'{i} {j}' for i, j in enumerate(list_d[:k])], sep='\n')

    @staticmethod
    def main():
        f = open("text.txt", "r")
        text = f.read()
        f.close()
        print(f"Words repeats: {TextAnal.count(TextAnal.clear_and_split(text))}")
        print(f"Average number of words per sentence: {TextAnal.average(text)}")
        print(f"Median number of words per sentence: {TextAnal.median(text)}")
        Entry.print_ngram(TextAnal.ngram((text), int(Entry.args.n)))


Entry.main()

