## About
reads a given pdf file and creates a txt file with list of tokens.

Sample usage:
```bash
python parse.py --file smp.pdf
```

## Run locally
1. Make sure java 8+ is installed. [This worked for me](https://stackoverflow.com/a/44309078/9205400) in WSL - Ubuntu 18.04
2. Create virtualenv and install requirements with `pip install -r requirements.txt`
4. Download nltk resources with `python download_nltk_resources.py`
3. Run the function with `python parse.py --file /path/to/file`
4. Optional arguments: 
    - `--language`: File language, defaults to `english`
    - `--outfile`: Output file name, defaults to `parsed.txt`
