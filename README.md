# Kazakh Language grapheme to phoneme

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This g2p convert kazakh language scripts to phonemes.

  - kazakh(arabic) script to phoneme
  - kazakh(cyrillic) script to phoneme
  - Numbers to word

### Usage

Dillinger requires [Python](https://python.org/) v3+ to run.

Install the dependencies and devDependencies and start the server.

```sh
from kzphoneme import Phoneme
arab_text = 'ءبىلىم بۇلاعى'
cyril_text = 'білім бұлағы'

pho = Phoneme()

arab_res = pho(arab_text, 'arab') #output:   ['B', 'IH', 'L', 'IH', 'M', ' ', 'B', 'U', 'L', 'A', 'C', 'I']

cyril_res = pho(cyril_text, 'cyril') #output:   ['B', 'IH', 'L', 'IH', 'M', ' ', 'B', 'U', 'L', 'A', 'C', 'I']
```

### Todos

 - Write MORE Tests

License
----

MIT


**Free Software, Hell Yeah!**
