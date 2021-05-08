# coding: utf8
from optimisation import deep_split


# By Maher AMARA


def all_words():
    return size_tot


def card(feature):
    return len(feature)


def Prob_word(word, feature):
    if word in feature.keys():
        p = (int(feature[word]) + 1) / (len(feature) + all_words())
    else:
        p = 1 / (len(feature) + all_words())
    return p


def Prob_SMS(feature, words):
    # this is the naive part
    # assuming that every word in a sentence is independent
    p = 1
    for word in words:
        p *= Prob_word(word, feature)
    return p


def Prob(feature, words):
    # donne la probabilité que ce SMS est de cette caracteristique
    # la partie BAYES
    p = Prob_SMS(feature, words) / len(feature)
    return p


def comparateur(words):
    # camprer les probabilité
    return Prob(d_ham, words) >= Prob(d_spam, words)


def classifier(SMS):
    # takes sms and reterns  spam or ham
    words = deep_split(SMS)
    if comparateur(words):
        return "Ham"
    else:
        return "Spam"


# main
with open("ham_d1.txt", 'r') as ham:
    lines = ham.readlines()
l1 = []
for line in lines:
    l1 += [line.split()]
d_ham = dict(l1)

with open("spam_d1.txt", 'r') as spam:
    lines = spam.readlines()
l1 = []
for line in lines:
    l1 += [line.split()]
d_spam = dict(l1)

with open("sheet.txt", "r") as sheet:
    ch = sheet.readline()

l = ch.split()
size_ham = int(l[0])
size_spam = int(l[1])
size_tot = int(l[2])
