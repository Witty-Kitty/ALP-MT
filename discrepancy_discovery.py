import bible_dictionaries
import click
import re

@click.command()
@click.option('--language', help='language you are working with eg. swahili')
@click.option('--book', help='number of book you are aligning eg. 12')

def discrepancy_discovery(language, book):
    eng = open("datasets/preprocessed/english/" + book + "." + bible_dictionaries.languages["english"][book] + ".txt", "r").read() 
    lang = open("datasets/preprocessed/" + language + "/" + book + "." + bible_dictionaries.languages[language][book] + ".txt", "r").read() 
    
    eng = eng.split('\n')
    lang = lang.split('\n')
    
    line = []
    length = len(lang)
    for i in range(0,length):
        if (eng[i][0].isdigit()):  
            if (not lang[i][0].isdigit()):
                print(i)
                break
            else:
                if (re.search("^\d+\s", eng[i]).group(0) != re.search("^\d+\s", lang[i]).group(0)):
                    print(i)
                    break

if __name__ == '__main__':
    discrepancy_discovery()