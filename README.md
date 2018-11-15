# make-list-of-cool-words

Take a plain text file and make a new file with words containing special characters. Context:

[@alvaroefe on Twitter](https://twitter.com/alvaroefe/status/1063018922222460928):
> Code help: There is a huge list of Portuguese words I want to filter to produce a smaller list of a maximum 20k words for Word-O-Mat. Filter should prioritize words with Portuguese diacritics ➽ á à ã â é ê ç í ó ô õ ú ü.

## Usage

Check if you have Python 3 by opening a command line and running `python3 --version`. If you get an error message, [here's how to install Python 3](https://wsvincent.com/install-python3-mac/). 

Once you have Python 3:

1. Download the zip of this repo, then open the folder in a text editor like VS Code or Sublime Text
2. Replace the `source-text.txt` with whatever source text you have
3. In `make-set-of-cool-words.py`, update the top two variables as necessary

```Python
# words with letters here will be saved
coolLetters = "á à ã â é ê ç í ó ô õ ú ü"

# be sure to use backslash to escape from quotes
removePunctuation= ", . ? : ; \" \' \' --"
```

4. Run the python file in the command line, by running `python3 FILE/PATH/HERE/make-set-of-cool-words.py`

There you have it! `cool-words.txt` will be updated with a line-break separated list of unique words, containing special characters.

--- 

If the directions above are missing something or you have any questions, please ask me on Twitter: [@thundernixon](https://twitter.com/ThunderNixon)
