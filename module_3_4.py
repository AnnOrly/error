def single_root_words(root_word, *other_words): # root_word - строка, *other_words - кортеж
    same_words = [] # - список

    list_other_words = list(other_words) # список
    str_other_words = str(other_words)  # строка


    if root_word in str_other_words:

        same_words.append(str_other_words)

    print(same_words)

single_root_words('five',
                  'five', 'six', 'seven', 'fifteen', 'sixteen', 'seventeen', 'fifty', 'sixty', 'seventy')
