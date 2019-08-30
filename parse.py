from tika import parser
from nltk.corpus import stopwords
from nltk import word_tokenize
from argparse import ArgumentParser

PUNCTUATIONS = [
    '.', ',', '(', ')', '/', '?', ';', ':', '[', ']', '{', '}', '¿', '*', '--',
    '_', '%', '&', '$'
]
DEFAULT_LANG = 'english'
DEFAULT_OUTFILE = 'parsed.txt'


def main():
    """ Main function """
    parser = _build_parser()
    options = parser.parse_args()
    filepath = options.filepath
    language = options.language
    outpath = options.outpath

    tokens = pdf_tokens(filepath, language)
    print(tokens)
    with open(outpath, 'w') as outfile:
        for item in tokens:
            outfile.write(f'{item}\n')


def _build_parser():
    parser = ArgumentParser()
    parser.add_argument('--file',
                        type=str,
                        dest='filepath',
                        help='File to parse',
                        required=True)
    parser.add_argument('--language',
                        type=str,
                        dest='language',
                        help='Language of file. Default: English',
                        required=False,
                        default=DEFAULT_LANG)
    parser.add_argument('--outpath',
                        type=str,
                        dest='outpath',
                        help='Name of output file',
                        required=False,
                        default=DEFAULT_OUTFILE)
    return parser


def pdf_tokens(filepath, lan='english'):
    '''
    Input: PDF file, language of stopwords
    Output: list with all words apart from stopwords and punctuation marks
    '''
    #
    stopwds = stopwords.words(lan)
    # PDF to dictionary
    rawText = parser.from_file(filepath)
    # Dictionary to string
    rawText = rawText['content']
    # Tokenizing
    tokens = word_tokenize(rawText)
    # Cleaning Stopwords and Punctuation marks
    tokens = [w for w in tokens if w not in stopwds]
    tokens = [w for w in tokens if w not in PUNCTUATIONS]
    tokens = [w.lower() for w in tokens]
    return tokens

if __name__ == '__main__':
    main()
