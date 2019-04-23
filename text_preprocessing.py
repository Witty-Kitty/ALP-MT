import click
import bible_dictionaries

@click.command()
@click.option('--language', help='language you are working with eg. swahili')
@click.option('--book', help='number of book you are aligning eg. 12')

def text_preprocessing(language, book):
    #   read in the file
    file = open("datasets/raw/" + language + "_nwt/" + book + "." + bible_dictionaries.languages[language][book] + ".txt", "r").read()
    # remove space characters from text 
    text = file.replace(u'\xa0', u' ')
    # split at newline character
    text = text.split('\n')
    # split at full stops, for sentence alignment
    new_text = []
    for line in text: 
        new_text.append(line.split('.'))
    # flatten the nested sublists that result from the previous step
    flat_text = [item for sublist in new_text for item in sublist]
    flat_text = list(filter(None, flat_text))
    # [''.join(c for c in s if c not in string.punctuation) for s in flat_list]
    # remove punctuation using this code
    new_text2 = []
    import re
    for line in flat_text:
        new_text2.append(re.sub(r'[^\w\s]','',line.lower()))
    # remove any empty sensences in the list
    new_text2 = list(filter(None, new_text2))
    f = open("datasets/preprocessed/" + language + "_nwt_preprocessed/" + book + "." + bible_dictionaries.languages[language][book] + ".txt", "w")
    for line in new_text2: 
        # strip sentences of space either at the beginning or end
        f.write(line.lstrip())
        # write line to output file  
        f.write("\n")
    f.close()

if __name__ == '__main__':
    text_preprocessing()
