"""
This algorithm was invented and created by Lior Magen - cijalm@gmail.com in 2015 while I was working in Revuze.it

"""
from operator import itemgetter


def fixed_collocation(sentences, win_size=5, ignore_words=None, run_bigram=True, run_trigram=True):
    if not ignore_words:
        ignore_words = ['']
    if run_bigram:
        bigram_results = model_bigram_collocation(sentences, win_size, ignore_words)
    else:
        bigram_results = []
    if run_trigram:
        trigram_results = model_trigram_collocation(sentences, win_size, ignore_words)
    else:
        trigram_results = []

    return top_ngrams(bigram_results, trigram_results)


def model_bigram_collocation(sentences, win_size, ignore_words):
    bigram = {}
    for idx, sentence in enumerate(sentences):
        if len(sentence) > 0:
            w1 = sentence[0]
            if w1 not in ignore_words:
                if len(sentence) > win_size:
                    for idy in range(1, win_size):
                        w2 = sentence[idy]
                        if w2 not in ignore_words:
                            if (w1, w2) in bigram or (w2, w1) in bigram:
                                if (w1, w2) in bigram:
                                    bigram[w1, w2] += 1
                                else:
                                    bigram[w2, w1] += 1
                            elif w1 != w2:  # don't add same word to bigram or trigram:
                                bigram[w1, w2] = 1
                else:
                    for idy in range(1, len(sentence)):
                        w2 = sentence[idy]
                        if w2 not in ignore_words:
                            if (w1, w2) in bigram or (w2, w1) in bigram:
                                if (w1, w2) in bigram:
                                    bigram[w1, w2] += 1
                                else:
                                    bigram[w2, w1] += 1
                            elif w1 != w2:  # don't add same word to bigram or trigram:
                                bigram[w1, w2] = 1
    return bigram


def model_trigram_collocation(sentences, win_size, ignore_words):
    trigram = {}
    for idx, sentence in enumerate(sentences):
        if len(sentence) > 0:
            w1 = sentence[0]
            if w1 not in ignore_words:
                if len(sentence) > win_size:
                    for idy in range(1, win_size):
                        w2 = sentence[idy]
                        if w2 not in ignore_words:
                            for idz in range(idy + 1, len(sentence)):
                                w3 = sentence[idz]
                                if w3 not in ignore_words:
                                    if (w1, w2, w3) in trigram or (w1, w3, w2) in trigram:
                                        if (w1, w2, w3) in trigram:
                                            trigram[w1, w2, w3] += 1
                                        else:
                                            trigram[w1, w3, w2] += 1
                                    elif w1 != w2 and w1 != w3 and w2 != w3:  # don't add same word to bigram or trigram
                                        trigram[w1, w2, w3] = 1
                else:
                    for idy in range(1, len(sentence)):
                        w2 = sentence[idy]
                        if w2 not in ignore_words:
                            for idz in range(idy + 1, len(sentence)):
                                w3 = sentence[idz]
                                if w3 not in ignore_words:
                                    if (w1, w2, w3) in trigram or (w1, w3, w2) in trigram:
                                        if (w1, w2, w3) in trigram:
                                            trigram[w1, w2, w3] += 1
                                        else:
                                            trigram[w1, w3, w2] += 1
                                    elif w1 != w2 and w1 != w3 and w2 != w3:  # don't add same word to bigram or trigram
                                        trigram[w1, w2, w3] = 1
    return trigram


def model_quadgram_collocation(sentences):
    quadgram = {}
    for idx, sentence in enumerate(sentences):
        if len(sentence) > 3:  # if sentence has less than 4 words -> skip it
            w1 = sentence[0]
            for idy in range(1, len(sentence)):
                w2 = sentence[idy]
                for idz in range(idy + 1, len(sentence)):
                    w3 = sentence[idz]
                    for idt in range(idz + 1, len(sentence)):
                        w4 = sentence[idt]
                        if (w1, w2, w3, w4) in quadgram or (w1, w2, w4, w3) in quadgram or (w1, w3, w2, w4) \
                                in quadgram or (w1, w3, w4, w2) in quadgram or (w1, w4, w3, w2) in \
                                quadgram or (w1, w4, w2, w3) in quadgram:
                            if (w1, w2, w3, w4) in quadgram:
                                quadgram[w1, w2, w3, w4] += 1
                            elif (w1, w2, w4, w3) in quadgram:
                                quadgram[w1, w2, w4, w3] += 1
                            elif (w1, w3, w2, w4) in quadgram:
                                quadgram[w1, w3, w2, w4] += 1
                            elif (w1, w3, w4, w2) in quadgram:
                                quadgram[w1, w3, w4, w2] += 1
                            elif (w1, w4, w3, w2) in quadgram:
                                quadgram[w1, w4, w3, w2] += 1
                            elif (w1, w4, w2, w3) in quadgram:
                                quadgram[w1, w4, w2, w3] += 1
                        elif w1 != w2 and w1 != w3 and w1 != w4 and w2 != w3 and w2 != w4 and w3 != w4:
                            quadgram[w1, w2, w3, w4] = 1
    return quadgram


def top_ngrams(bigram, trigram):
    z = bigram.copy()
    z.update(trigram)
    return sorted(z.items(), key=itemgetter(1), reverse=True)

### TODO: Create some example how to extract products models.
