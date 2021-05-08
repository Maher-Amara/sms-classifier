# coding: utf8
# By Maher AMARA

# importations
from copy import copy
import string


# fonction:


def smiles(ch):
    smiles = [':-)', ':)', ':-]', ':]', ':-3', ':3', ':->', ':>', '8-)', '8)', ':-}', ':}', ':o)', ':c)', ':^)', '=]',
              '=)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=D', '=3', 'B^D', ':-))', ':-(', ':(', ':-c',
              ':c', ':-<', ':<', ':-[', ':[', ':-||', '>:[', ':{', ':@', '>:(', ":'-(", ":'(", ":'-)", ":')", "D-':",
              'D:<', 'D:', 'D8', 'D;', ':-O', ':O', ':-o', ':o', ':-0', '8-0', '>:O', ':-*', ':*', ':x', ';-)', ';)',
              '*-)', '*)', ';-]', ';]', ';^)', ':-,', ';D', ':-P', ':P', 'X-P', 'x-p', ':-p', ':p', ':-Þ', ':Þ', ':-þ',
              ':þ', ':-b', ':b', '=p', '>:P', ':-/', ':-.', '>:/', '=/', ':L', '=L', ':-|', ':|', ':$', '://)', '://3',
              ':-X', ':X', ':-#', ':#', ':-&', ':&', 'O:-)', 'O:)', '0:-3', '0:3', '0:-)', '0:)', '0;^)', '>:-)', '>:)',
              '}:-)', '}:)', '3:-)', '3:)', '>;)', '>:3', '>;3', '|;-)', '|-O', ':-J', '#-)', '%-)', '%)', ':-###..',
              ':###..', '<:-|', "',:-|", "',:-l"]
    d = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k',
         'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v',
         'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}

    ch1: str = ""
    i = 0
    for smile in smiles:
        while i < len(ch):
            if smile == ch[i: i + len(smile)]:
                ch1 += " " + smile + " "  # isolate smile
                i += len(smile) - 1
            else:
                st = ch[i]
                if st in string.punctuation:  # isolate
                    ch1 += " " + st + " "
                elif st in string.ascii_uppercase:  # lowercase
                    ch1 += d[st]
                elif st in string.digits:  # remove
                    ch1 += " "
                else:
                    ch1 += st
            i += 1
    return ch1



def remove_stop_words(l):
    stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out',
                  'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such',
                  'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him',
                  'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don',
                  'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while',
                  'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them',
                  'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because',
                  'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has',
                  'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being',
                  'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
    l1 = list(l)
    for i in l:
        if i in stop_words:
            l1.remove(i)
    return l1


def deep_split(ch):
    # removing noise
    ch = smiles(ch)
    l = ch.split()
    l = remove_stop_words(l)
    return l
