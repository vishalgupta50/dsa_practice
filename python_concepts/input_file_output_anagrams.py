
input_word = "tini"

# def check_anagram(word1, word2):



def find_anagrams(iword):
    with open("file1.txt", "r+") as words:
        # texts_read = words.read()
        texts_readline = words.readlines()

    anagrams = dict()
    with open("file1.txt", "r+") as words:
        # texts_read = words.read()
        texts_readline1 = words.read().split()

    # print(texts_read, "\n", type(texts_read), "\n")
    print(texts_readline1, "\n", type(texts_readline), "\n")

    # texts_readline = [elem.rstrip("\n") for elem in texts_readline]
    # print(texts_readline)
    #

    # print(anagrams)
    #
    for word in texts_readline1:
        word = ''.join(sorted(word))
        if word in anagrams.keys():
            print(word)
            anagrams[word] += 1
        else:
            anagrams[word] = 1

    iword = ''.join(sorted(iword))



    print(anagrams[iword])


    #
    #
    #
    print(anagrams)

    from collections import Counter

    anagrams1 = Counter(texts_readline1)
    print(anagrams1, "\n", type(anagrams1))
    print(dict(anagrams1))



    #
    # str1 = "hello\\n"
    # print(str1)
    # print(str1.rstrip("\\n"))


def find_anagrams1(iword):
    with open("file1.txt", "r+") as words:
        texts_readline1 = words.read().split()

    anagrams = dict()
    for word in texts_readline1:
        word = ''.join(sorted(word))
        if word in anagrams.keys():
            anagrams[word] += 1
        else:
            anagrams[word] = 1

    iword = ''.join(sorted(iword))

    print(anagrams)
    print(anagrams[iword])

# print(find_anagrams(input_word))

# find_anagrams(input_word)

find_anagrams1(input_word)




