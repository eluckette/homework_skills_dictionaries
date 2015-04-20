# To work on the advanced problems, set to True
ADVANCED = False


def count_unique(string1):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    # dictionary will hold unique items
    dict_of_items = {}

    # take input string and split items (words/numbers) into list
    # dictionary keys -> unique items
    # dictionary values -> number of times item appears 
    for item in string1.split():
        if item not in dict_of_items:
            dict_of_items[item] = 1
        else:
            dict_of_items[item] += 1

    return dict_of_items


def common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in both lists, return it each
    time:

        >>> sorted(common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """
    # list to contain items in both lists
    in_both_lists = []

    # nested for loops to iterate through both given lists
    # if the items are the same add to new defined list 
    for item_list1 in list1:
        for item_list2 in list2:
            if item_list1 == item_list2:
                in_both_lists.append(item_list2)

    return in_both_lists

def unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `common_items`, this should find [1, 2]:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """
    # take two given sets -> make sets and use set addition
    # new set holding unique items -> create list 
    unique_common_list = list(set(list1) & set(list2))
    
    return unique_common_list


def sum_zero(list1):
    """Return list of x,y number pair lists from a list where x+y==0

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 0, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    # dicitionary to contain opposite pairs 
    dictionary_with_opposites = {}

    # make dictionary with number pair in list as key 
    # check to make sure that reverse is not in dictionary to avoid duplicates
    for num in list1:
        for num_compare in list1:
            if num + num_compare == 0 and (num_compare, num) not in dictionary_with_opposites:
                dictionary_with_opposites[(num, num_compare)] = "sum zero pair"
    return dictionary_with_opposites


def find_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(find_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(find_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """
    # list with duplicate words removed
    duplicates_removed = []

    # iterate through words in given list
    for word in words:
        if word in duplicates_removed:
            continue
        else:
            duplicates_removed.append(word)

    return duplicates_removed


def word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    # dicitionary 
    # key -> length of word(s)
    # value -> list of words matching number in key
    length_of_words_dict = {}

    # iterate through list of words
    # use set default to see if key already exists
    # if not -> create key with length of word and empty list as value --> then append word
    # if already created --> word appended to exisiting list 
    for word in words:
        length_of_words_dict.setdefault(len(word), []).append(word)
   
    return length_of_words_dict.items()


def pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """
    # dictionary of pirate language
    # key -> English
    # value -> Pirate
    pirate_dictionary = {
                        'sir':'matey',
                        'hotel':'fleebag inn',
                        'student':'swabbie',
                        'boy':'matey',
                        'madam' :'proud beauty',
                        'professor':'foul blaggart',
                        'restaurant':'galley',
                        'your':'yer',
                        'excuse':'arr',
                        'students':'swabbies',
                        'are':'be',
                        'lawyer':'foul blaggart',
                        'the':"th'",
                        'restroom':'head',
                        'my':'me',
                        'hello':'avast',
                        'is':'be',
                        'man':'matey'
                        }

    # list holding words in new phrase 
    translated_phrase = []

    # for given phrase iterate through word by word
    # change word if needed, and return string -> each word in list separated by space
    for item in phrase.split():
        if item in pirate_dictionary:
            translated_phrase.append(pirate_dictionary[item])
        else:
            translated_phrase.append(item)
 
    return " ".join(translated_phrase)

def adv_word_length_sorted_words(words):
    """Given list of words, return list of ascending [(len, [sorted-words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length. The list of words
    for that length should be sorted alphabetically.

    For example:

        >>> adv_word_length_sorted_words(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    # same as word_length
    length_of_words_dict = {}
    for word in words:
        length_of_words_dict.setdefault(len(word), []).append(word)
   
    # create sorted list 
    # iterate through dictionary and sort key values
    sorted_list = []
    for key, value in length_of_words_dict.items():
        sorted_list.append((key, sorted(value)))

    return sorted_list

##############################################################################
# You can ignore everything after here

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
