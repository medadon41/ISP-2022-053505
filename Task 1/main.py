import statistics

SYMBS = ",.?!-"


class TextAnal:

    @classmethod
    def clear_and_split(cls, text):
        for i in SYMBS:
            text = text.replace(i, "")
        return text.split(' ')

    @staticmethod
    def count(spltd):
        repeats = {}
        for element in spltd:
            if repeats.get(element, None):
                repeats[element] += 1
            else:
                repeats[element] = 1
        return dict(repeats)

    @classmethod
    def words_per_sentences(cls, spltd: list):
        counts = []
        for element in spltd:
            cnt = len(element.split())
            if (cnt != 0):
                counts.append(len(element.split()))
        return counts

    @staticmethod
    def average(text):
        return statistics.mean(TextAnal.words_per_sentences(text.split('.')))

    @staticmethod
    def median(text):
        return statistics.median(TextAnal.words_per_sentences(text.split('.')))

    @staticmethod
    def ngram(text, n=4):
        spltd = TextAnal.clear_and_split(text)
        for word in spltd:
            if len(word) < n:
                spltd[spltd.index(word)] = ""
        spltd = " ".join(spltd)
        spltd = spltd.split()
        for i in spltd:
            spltd[spltd.index(i)] = i[:n]
        out_dict = {i: 1 for i in spltd}
        outage = []
        for word in spltd:
            if word not in outage:
                outage.append(i)
            if out_dict.get(word, None):
                out_dict[word] += 1
        return out_dict
