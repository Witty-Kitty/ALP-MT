# ALP-MT
This project is aimed at aligning translations of the Bible for the task of Machine Translation. 
We consider the English version to be our point of reference so all other efforts at adding datasets for other languages work towards aligning them with the English version, hence by extension, with each other.
NEVER EDIT THE ENGLISH TEXTS AS THEY ARE THE 'SOURCE OF TRUTH'.

##Requirements:
* python3
* click

The folder named 'datasets' contains raw, preprocessed and aligned folders where different versions of the files we are working on will live.

This folder contains 4 scripts that we will use:
* text_preprocessing.py
* alignment_check.py
* discrepancy_discovery.py
* final_processing.py
Running each of the above with the flag --help will give you a quick reminder of the options the script requires to run.
eg. python3 text_preprocessing.py --help or python text_preprocessing.py --help (depending on whether you have both python2 and python3 installed)

Usage: text_preprocessing.py [OPTIONS]

Options:
  --language TEXT  language you are working with eg. swahili
  --book TEXT      number of book you are aligning eg. 12
  --help           Show this message and exit.

##How to:
1. the text_preprocessing function is to do some preprocessin on the text. It requires the options 'language' that you are working with, and 'book' of the bible that you are aligning. It removes most punctuation and breaks sentences up at full-stop so that each is on a new line. 

example usage: 
```sh
$ python3 text_preprocessing.py --language swahili --book 4
```

2. the alignment_check.py function will check to see if the text you are working on has the same number of sentences as its English equivalent. Should it not, you will see the difference in the number of lines. 

example usage:
```sh
$ python3 alignment_check.py --language swahili --book 4
```

If you have run this script on a book for the first time and it is aligned, please also run the third script for good measure. Sometimes the number of sentences may be equal but they have not been split correctly.
Also, as this process is iterative, as you continually work on a book, sometimes the difference in the number of sentences will rise as opposed to fall. Do not be discouraged, keep going, eventually it shall get to alignment.

3. the discrepancy_discovery.py function will let you know where exactly sentences are not aligned, if the alignment check has failed. It returns an integer.

example usage:
```sh
$ python3 discrepancy_discovery.py --language swahili --book 4
```

It returns an integer, which is the line with the problem. 
Note that when there is no discrepancy, you will instead get an 'IndexError: string index out of range' error.
At this point, open the preprocessed version of the book you have been working on in a text editor that shows line numbers.
Navigate to the line indicated as being the problem. 
If this line begins with a number, copy a small part of it. If does not begin with a number(a verse), instead navigate to the closest sentence before it that begins with a number and copy a small part of that instead.
Proceed to the raw version of the book of the Bible you are working on and search for the snippet you copied from the other text file. Note that this file has punctuation whereas the other does not so you may need to alter the snippet copied, make it shorter, before it matches to the equivalent here because of the differences in punctuation.
Identify the line that number that has the issue on the raw text of your language and then open the English equivalent text and navigate to the same sentence. Examine the differences in the two looking out particularly for differences in punctuation. 

One sentence may have more fullstops than the other, hence they are split into a different number of sentences. More often than not, all you have to do is change the punctuation in the version that you are working with to MATCH THE ENGLISH PUNCUATION.
Remember, NEVER EDIT THE ENGLISH TEXTS AS THEY ARE THE 'SOURCE OF TRUTH'.
More rare is having to add a short sentence or phrase for the two texts to match. 

Once the change is made, save the raw text of the file you are working on and then proceed to repeat the process from step 1, the text_preprocessing script, again. Repeat this process until the alignment_check is all good and the discrepancy_discovery gives you the 'IndexError: string index out of range' error.

4. the final_processing.py removes all punctutation and saves, does further processing and saves the output in the 'aligned' folder.

example usage:
```sh
$ python3 final_processing.py --language swahili --book 4
```


