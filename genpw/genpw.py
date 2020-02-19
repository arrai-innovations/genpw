""" GENPW - Generate pronounceable passwords """

# This program uses statistics on the frequency of three-letter sequences in
# English to generate passwords.  The statistics are generated from your
# dictionary by the program load_trigram.
#
# See www.multicians.org/thvv/gpw.html for history and info.
# Tom Van Vleck
#
# THVV 06/01/94 Coded
# THVV 04/14/96 converted to Java
# THVV 07/30/97 fixed for Netscape 4.0
# THVV 11/27/09 ported to Javascript
# CB 10/12/16 ported to Python
# python port Copyright (C) 2017 Emergence by Design Inc. - All Rights Reserved
# python port Copyright (C) 2020 Arrai Innovations Inc. - All Rights Reserved

from csv import reader
from os.path import dirname
from os.path import join as path_join

try:
    from secrets import randbelow
    from functools import partial

    random = partial(randbelow, 2)
except ImportError:
    from random import random


class TrigramLoader(object):
    """ Wrapper for loading the word frequency data. """

    trigrams = None

    @classmethod
    def is_loaded(cls):
        """ Return whether the trigrams have been loaded. """
        return cls.trigrams is not None

    @classmethod
    def load_trigrams(cls):
        """ Load the trigrams from the data files. """
        if cls.is_loaded():
            return cls.trigrams

        trigrams = []
        for char_one in [chr(x) for x in range(ord("A"), ord("Z") + 1)]:
            char_data = []
            trigram_file = open(path_join(dirname(__file__), "trigrams", "{}.csv".format(char_one)))
            trigram_reader = reader(trigram_file, delimiter="\t")
            for data_line in trigram_reader:
                if data_line:
                    char_data.append(tuple(int(x) for x in data_line))
            trigrams.append(tuple(char_data))
            trigram_file.close()
        cls.trigrams = tuple(trigrams)
        return trigrams


def first_three_chrs(_alphabet, _trigram, ranno):
    output = ""
    rotating_sum = 0
    for ch1 in range(0, 26):
        for ch2 in range(0, 26):
            for ch3 in range(0, 26):
                rotating_sum += _trigram[ch1][ch2][ch3]

                if rotating_sum > ranno:
                    output += _alphabet[ch1]
                    output += _alphabet[ch2]
                    output += _alphabet[ch3]
                    return output, rotating_sum
    return output, rotating_sum


def pronounceable_passwd(pwl):
    """ Return a password of length pwl. """
    _alphabet = "abcdefghijklmnopqrstuvwxyz"

    # letter frequencies
    _trigram = TrigramLoader.load_trigrams()

    # Pick a random starting point.
    pik = random()  # random number [0,1]
    ranno = pik * 125729.0
    output, rotating_sum = first_three_chrs(_alphabet, _trigram, ranno)

    # Now do a random walk.
    nchar = 3
    while nchar < pwl:
        ch1 = _alphabet.find(output[nchar - 2])
        ch2 = _alphabet.find(output[nchar - 1])
        rotating_sum = 0
        for ch3 in range(0, 26):
            rotating_sum += _trigram[ch1][ch2][ch3]
        if rotating_sum == 0:
            break  # exit while loop
        pik = random()
        ranno = pik * rotating_sum
        rotating_sum = 0
        for ch3 in range(0, 26):
            rotating_sum += _trigram[ch1][ch2][ch3]
            if rotating_sum > ranno:
                output += _alphabet[ch3]
                break  # break for loop
        nchar += 1

    return output
