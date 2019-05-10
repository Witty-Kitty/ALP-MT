import bible_dictionaries
import click

@click.command()
@click.option('--language', help='language you are working with eg. swahili')
@click.option('--book', help='number of book you are aligning eg. 12')

def alignment_check(language, book):
    eng = open("datasets/preprocessed/english/"  + book + "." + bible_dictionaries.languages["english"][book] + ".txt", "r").read() 
    lang = open("datasets/preprocessed/" + language + "/"  + book + "." + bible_dictionaries.languages[language][book] + ".txt", "r").read() 
    
    eng = eng.split('\n')
    lang = lang.split('\n')
    
    if(len(eng) == len(lang)):
        print("All Good!")
    else:
        print(str(abs(len(eng) - len(lang))) + " line(s) mismatch")

if __name__ == '__main__':
    alignment_check()