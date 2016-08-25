from operator import itemgetter


# Custom collocation: Gets a list of sentences (list of lists), a window size. The method is as following:
# in each list there are two indexes, the first is fixed and the second moves along the sentence (starting from 2nd
# word and goes till the end of each list). For each found collocation it stores a collocation (starting with bigram
# and goes till quadgram). If there's a found bigrams (for example) "galaxy s3" and "s3 galaxy" the algorithm will
# identify them as same bigram and count it twice as "galaxy s3" if there are more "galaxy s3" appearances than
# "s3 galaxy" in lists. An optional addition to the algorithm will be to give weights to words in sentence based
# on the distance from the first word (the fixed index location).

# Parameters:
# Input: sentences - list of lists containing sentences. The first word in each sentence is the word we want the index
# to be fixed on.
# Output:


# example_sentence = [['galaxy', 's3', '32GB', 'white', 'beautiful', 'unlocked'], ['galaxy', '32GB', 's3',
#                                                                                  'white', 'beautiful', 'unlocked'],
#                     ['galaxy', 's3', '64GB'], ['galaxy',
#                                                's3', '32GB'], ['s3', 'galaxy', '32GB'], ['galaxy', 's3', '32GB'],
#                     ['galaxy', 's3', '32GB',
#                      'white', 'beautiful', 'unlocked'], ['galaxy', 's3', '32GB', 'white', 'beautiful', 'unlocked']]

class FixedCollocation(object):
    def __init__(self, win_size=5, ignore_words=None, run_bigram=True, run_trigram=True, collocate_numbers=True,
                 reverse=True):

        self.reverse = reverse
        self.win_size = win_size
        self.ignore_words = ignore_words
        self.run_bigram = run_bigram
        self.run_trigram = run_trigram
        self.collocate_numbers = collocate_numbers

        if win_size < 2:
            ValueError('Window size too small for bigram collocation.\nIn order to use custom collocation you '
                       'should enter a window size bigger or equal to 2.')

    def model_bigram_collocation(self, sentences):
        """
        This function returns the fixed bigram collocation.
        :param sentences: A list of strings.
        :return: A list of bigrams
        """
        bigram = {}
        for idx, sentence in enumerate(sentences):
            if len(sentence) > 0:
                w1 = sentence[0]
                if w1 not in self.ignore_words:
                    if len(sentence) > self.win_size:
                        for idy in range(1, self.win_size):
                            w2 = sentence[idy]
                            if w2 not in self.ignore_words:
                                if (w1, w2) in bigram or (w2, w1) in bigram:
                                    if (w1, w2) in bigram:
                                        bigram[w1, w2] += 1
                                    else:
                                        bigram[w2, w1] += 1
                                elif w1 != w2:
                                    bigram[w1, w2] = 1
                    else:
                        for idy in range(1, len(sentence)):
                            w2 = sentence[idy]
                            if w2 not in self.ignore_words:
                                if (w1, w2) in bigram or (w2, w1) in bigram:
                                    if (w1, w2) in bigram:
                                        bigram[w1, w2] += 1
                                    else:
                                        bigram[w2, w1] += 1
                                elif w1 != w2:
                                    bigram[w1, w2] = 1
        return bigram

    def model_trigram_collocation(self, sentences):
        """
        This function returns the fixed trigram collocation.
        :param sentences: A list of strings.
        :return: A list of trigrams.
        """
        if self.win_size < 3:
            ValueError('Window size should be bigger or equal to 3 in order to run trigram collocation.')
        else:
            trigram = {}
            for idx, sentence in enumerate(sentences):
                if len(sentence) > 0:
                    w1 = sentence[0]
                    if w1 not in self.ignore_words:
                        if len(sentence) > self.win_size:
                            for idy in range(1, self.win_size):
                                w2 = sentence[idy]
                                if w2 not in self.ignore_words:
                                    for idz in range(idy + 1, len(sentence)):
                                        w3 = sentence[idz]
                                        if w3 not in self.ignore_words:
                                            if (w1, w2, w3) in trigram or (w1, w3, w2) in trigram:
                                                if (w1, w2, w3) in trigram:
                                                    trigram[w1, w2, w3] += 1
                                                else:
                                                    trigram[w1, w3, w2] += 1
                                            elif w1 != w2 and w1 != w3 and w2 != w3:
                                                trigram[w1, w2, w3] = 1
                        else:
                            for idy in range(1, len(sentence)):
                                w2 = sentence[idy]
                                if w2 not in self.ignore_words:
                                    for idz in range(idy + 1, len(sentence)):
                                        w3 = sentence[idz]
                                        if w3 not in self.ignore_words:
                                            if (w1, w2, w3) in trigram or (w1, w3, w2) in trigram:
                                                if (w1, w2, w3) in trigram:
                                                    trigram[w1, w2, w3] += 1
                                                else:
                                                    trigram[w1, w3, w2] += 1
                                            elif w1 != w2 and w1 != w3 and w2 != w3:
                                                trigram[w1, w2, w3] = 1
            return trigram

    def model_quadgram_collocation(self, sentences):
        """
        This function returns the fixed quadgram collocation.
        :param sentences: A list of strings.
        :return: A list of quadgrams.
        """
        if self.win_size < 4:
            ValueError('Window size should be bigger or equal to 4 in order too run quadgram collocation.')
        quadgram = {}
        for idx, sentence in enumerate(sentences):
            if len(sentence) > 3:
                w1 = sentence[0]
                if w1 not in self.ignore_words:
                    for idy in range(1, len(sentence)):
                        w2 = sentence[idy]
                        if w2 not in self.ignore_words:
                            for idz in range(idy + 1, len(sentence)):
                                w3 = sentence[idz]
                                if w3 not in self.ignore_words:
                                    for idt in range(idz + 1, len(sentence)):
                                        w4 = sentence[idt]
                                        if w4 not in self.ignore_words:
                                            if (w1, w2, w3, w4) in quadgram or (w1, w2, w4, w3) in quadgram or \
                                                            (w1, w3, w2, w4) \
                                                            in quadgram or (w1, w3, w4, w2) in quadgram or (
                                                    w1, w4, w3, w2) in \
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
                                            elif w1 != w2 and w1 != w3 and w1 != w4 and w2 != w3 and w2 != w4 \
                                                    and w3 != w4:
                                                quadgram[w1, w2, w3, w4] = 1
        return quadgram

    def top_ngrams(self, bigram=None, trigram=None):
        if not bigram:
            bigram = {}
        z = bigram.copy()
        z.update(trigram)
        # add quadgram collocation
        return sorted(z.items(), key=itemgetter(1), reverse=self.reverse)

# TODO: 1. Add quadgram collocation to "top_ngrams". 2. Add a windows size check to "model quadgram collocation".
# TODO: 3. Add an explanation of the algorithm (by a simple example) to the beginning of the file.
# TODO: 4. Add an option to select at what index the collocation begins: e.g. sentence = "this watch is really nice",
# TODO: I want to use collocation only for "watch is really nice", so the user will choose custom_collocation(sentence,
# TODO: start_idx=1)
# TODO: 5. To do what Ofer suggested, instead of using many nested if's, use if and continue, that way theres no need
# TODO: for so many nested ifs:
#               if w1 in self.ignore_words:
#                   continue
#                 for idy in range(1, len(sentence)):
#                     w2 = sentence[idy]
#                 if w2 in self.ignore_words:
#                     continue
#                 for idy in range(1, len...)...
#
#         instead of:
#                 if w1 not in self.ignore_words:
#                     for idy in range(1, len(sentence)):
#                         w2 = sentence[idy]
#                         if w2 not in self.ignore_words:

