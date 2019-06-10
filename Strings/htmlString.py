#Write a Python function to create the HTML string with tags around the word(s).


def add_tag(word, tag):
    new_string = '<' + tag + '>' + word + '</' + tag + '>'
    return new_string
    # return '<%s>%s</%s>' %(tag, word, tag)


def main():
    word = 'Python'
    tag = 'i'
    print(add_tag(word, tag))


main()