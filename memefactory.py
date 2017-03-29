import json
import random


# Constants.
PHRASES_JSON = "phrases.json"
KEY_PHRASES = "phrases"
KEY_DESCRIPTION = "description"


def _load_phrases(filepath):
    """Load dictionary from json file at `filepath`."""
    with open(filepath) as f:
        return json.load(f)


def _phrases(category, phrases):
    """Get all the phrases from a category."""
    return phrases[category][KEY_PHRASES]


def _random_phrase(category, phrases):
    """Get a randomly chosen phrase from a category.

    Parameters
    ----------
    category: str
        Category name.
    phrases: dict
        Dictionary mapping categories to phrase lists.

    Returns
    -------
    phrases: list
        List of phrases from `category`.
    """
    phrases = _phrases(category, phrases)
    return random.choice(phrases)


def random_phrases(categories, phrases):
    """Get a randomly chosen phrases from categories. Phrases are returned in
    the order of `categories`.

    Parameters
    ----------
    categories: list
        Category names.
    phrases: dict
        Dictionary mapping categories to phrase lists.

    Returns
    -------
    phrases: list
        List of one phrase from each of `categories`.
    """
    return [_random_phrase(category, phrases)
            for category in categories]


def meme(phrases, deep=1):
    #TODO: add later  "broad", "callout", "defensive"
    meme_cat = [
        "when",
        "when",
        "while",
        "opinionated"
    ]
    meme_cat_select = random.choice(meme_cat)

    if meme_cat_select == "when":
        if deep == '1':
            categories = ['when_situation',
                          'singular_noun',
                          'singular_action']
            meme = "::  {}{}{}".format(*random_phrases(categories, phrases))
            print(meme)
        elif deep == '2':
            categories = ['when_situation',
                          'singular_noun',
                          'singular_action',
                          'singular_action']
            meme = "::  {}{}{} and {}".format(*random_phrases(categories, phrases))
            print(meme)
        elif deep == '3':
            categories = ['when_situation',
                          'singular_noun',
                          'singular_action',
                          'singular_action',
                          'singular_action']
            meme = "::  {}{}{} and {} and {}".format(
                *random_phrases(categories, phrases))
            print(meme)

    elif meme_cat_select == "while":
        if deep == '1':
            categories = ['opinion',
                          'swimmy',
                          'potential',
                          'thing2be',
                          'self_aggrandizing',
                          'thing2do',
                          'howso']
            meme = "::  {}{}{}{}, {}{}{}".format(
                *random_phrases(categories, phrases))
            print(meme)
        elif deep == '2':
            categories = ['opinion',
                          'swimmy',
                          'potential',
                          'thing2be',
                          'self_aggrandizing',
                          'thing2do',
                          'thing2do',
                          'howso']
            meme = "::  {}{}{}{}, {}{},and {}{}".format(
                *random_phrases(categories, phrases))
            print(meme)
        elif deep == '3':
            categories = ['opinion',
                          'swimmy',
                          'potential',
                          'thing2be',
                          'self_aggrandizing',
                          'thing2do',
                          'thing2do',
                          'thing2do',
                          'howso']
            meme = "::  {}{}{}{}{}{}, and {}, and {}{}".format(
                *random_phrases(categories, phrases))
            print(meme)

    elif meme_cat_select == "opinionated":
        if deep == '1':
            categories = ['opinion',
                          'singular_noun',
                          'singular_action',
                          'self_aggrandizing',
                          'thing2do',
                          'howso']
            meme = "::  {}{}{}... {}{}{}".format(
                *random_phrases(categories, phrases))
            print(meme)
        elif deep == '2':
            categories = ['opinion',
                          'singular_noun',
                          'singular_action',
                          'singular_action',
                          'self_aggrandizing',
                          'thing2do',
                          'howso']
            meme = "::  {}{}{}, and {}... {}{}{}".format(
                *random_phrases(categories, phrases))
            print(meme)
        elif deep == '3':
            categories = ['opinion',
                          'singular_noun',
                          'singular_action',
                          'singular_action',
                          'self_aggrandizing',
                          'thing2do',
                          'thing2do',
                          'howso']
            meme = "::  {}{}{}, and {}... {}{}, and {}{}".format(
                *random_phrases(categories, phrases))
            print(meme)


def wowe(phrases):

    print()
    print("""
¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯
#--                           Meme Research Lab                            --#
#--                                                                        --#""")
    mememake = input("#--                          Generate Meme? [y/n]                          --#\n[ayy@lmao~/] $ ")
    if mememake == 'y':
        manymeme = int(input("#--                         How many you want fam?                        --#\n[ayy@lmao~/] $ "))
        deep = input("#--                     How many layers you want? [1-3]                    --#\n[ayy@lmao~/] $ ")
        print("""
¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯¯\_(ツ)_/¯
#--                              k here u go                               --#
##############################################################################
""")
        print()
        for _ in range(manymeme):
            meme(phrases, deep=deep)
        wowe(phrases)
    elif mememake == 'n':
        print('ok')
        exit
    else:
        wowe(phrases)

if __name__ == "__main__":
    phrases = _load_phrases(PHRASES_JSON)
    wowe(phrases)


