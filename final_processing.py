import bible_dictionaries
import click
import re

@click.command()
@click.option('--language', help='language you are working with eg. swahili')
@click.option('--book', help='number of book you are aligning eg. 12')

def final_processing(language, book):
    lang = open("datasets/preprocessed/" + language + "_nwt_preprocessed/" + book + "." + bible_dictionaries.languages[language][book] + ".txt", "r").read() 
    
    lang = lang.split('\n')
    
    f = open("datasets/aligned/" + language + "_nwt_aligned/" + book + "." + bible_dictionaries.languages[language][book] + ".txt", "w")
    for i in range(0,len(lang)):
        lang[i] = re.sub("^\d+\s", '', lang[i])
        f.write(lang[i].lstrip())
        f.write("\n")
    f.close()

if __name__ == '__main__':
    final_processing()