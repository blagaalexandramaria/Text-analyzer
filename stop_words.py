# Common stop words in Romanian and English
# These words are ignored in the analysis because they are too frequent
STOP_WORDS = {
    "si", "și", "de", "la", "cu", "pe", "din", "in", "în",
    "un", "o", "a", "ai", "ale", "al", "este", "sunt",
    "să", "mai", "care", "că", "sau", "pentru", "după",

    # Modal verbs & auxiliaries
    "may","might","must","can","could","shall","should","will","would",

    # Pronouns
    "i","you","he","she","it","we","they","me","him","her","them",
    "my","your","his","their","our","its","ours","yours","theirs",
    "which",

    # Articles & determiners
    "a","an","the","this","that","these","those",

    # Prepositions
    "in","on","at","by","for","with","about","against","between","into",
    "through","during","before","after","above","below","from","up","down",
    "out","off","over","under","again","further","within","without",

    # Conjunctions
    "and","or","but","so","because","although","if","while","where","when",

    # Common verbs
    "is","are","was","were","be","been","being",
    "have","has","had",
    "do","does","did",

    # Very common useless words
    "not","no","yes","very","just","more","most","such","only","own","same",
    "too","than","then","also","even","still","yet",

    # Extra
    "one","two","first","second","new","many","much"
}
