# Kazakh Language grapheme to phoneme

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This g2p convert kazakh language scripts to phonemes.

- kazakh(arabic) script to phoneme
- kazakh(cyrillic) script to phoneme
- Numbers to word

## Installations

```shell script
pip install g2p-kz
```

## Usage

requires [Python](https://python.org/) v3+ to run.

```python
from kzphoneme import Phoneme
arab_text = 'ءبىلىم بۇلاعى'
cyril_text = 'білім бұлағы'

pho = Phoneme()

arab_res = pho(arab_text, 'arab') #output:   ['B', 'IH', 'L', 'IH', 'M', ' ', 'B', 'U', 'L', 'A', 'C', 'I']

cyril_res = pho(cyril_text, 'cyril') #output:   ['B', 'IH', 'L', 'IH', 'M', ' ', 'B', 'U', 'L', 'A', 'C', 'I']
```

## Table

**Cyrillic**| |**Arabic**| | | | | |**Phoneme**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
 |  | |Name|Normal|Isolated|Final|Initial|Medial|
-| |  Arabic Letter High Hamza| ٴ | | | | | |-
 | | | |0x0674| | | | |
-| |Arabic Letter Hamza|ء|ﺀ| | | |-
 | | | |0x0621|0xFE80| | |
А|а|Arabic Letter Alef|ا‎|ﺍ|ﺎ| | |A
 | | | |0x0627|0xFE8D|0xFE8E| |
Ә|ә|Hamza + Alef|ءا‎| | | | |AH
 | | |Arabic Letter High Hamza Alef|ٵ| | | | |
 | | | |0x0675| | | | |
Б|б|Arabic Letter Beh|ب|ﺏ|ﺐ|ﺑ|ﺒ|B
 | | | |0x0628|0xFE8F|0xFE90|0xFE91|0xFE92|
В|в|Arabic Letter Oe|ۆ|ﯙ|ﯚ| | |V
 | | | |0x06C6|0xFBD9|0xFBDA| | |
Г|г|Arabic Letter Gaf|گ|ﮒ|ﮓ|ﮔ|ﮕ|G
 | | |0x06AF|0xFB92|0xFB93|0xFB94|0xFB95|
Ғ|ғ|Arabic Letter Ain|ع|ﻉ|ﻊ|ﻋ|ﻌ|C
 | | | |0x0639|0xFEC9|0xFECA|0xFECB|0xFECC|
Д|д|Arabic Letter Dal|د|ﺩ|ﺪ| | |D
 | | | |0x062F|0xFEA9|0xFEAA| | |
Е|е|Arabic Letter Heh|ه|ﻩ|ﻪ| | |E
 | | | |0x0647|0xFEE9|0xFEEA| | |
Ж|ж|Arabic Letter Jeem|ج|ﺝ|ﺞ|ﺟ|ﺠ|J
 | | | |0x062C|0xFE9D|0xFE9E|0xFE9F|0xFEA0|
З|з|Arabic Letter Zain|ز|ﺯ|ﺰ| | |Z
 | | | |0x0632|0xFEAF|0xFEB0| | |
И|и|Arabic Letter Yeh|ي|ﻱ|ﻲ|ﻳ|ﻴ|Y
 | | | |0x064A|0xFEF1|0xFEF2|0xFEF3|0xFEF4|
К|к|Arabic Letter Kaf|ك|ﻙ|ﻚ|ﻛ|ﻜ|K
 | | | |0x0643|0xFED9|0xFEDA|0xFEDB|0xFEDC|
Қ|қ|Arabic Letter Qaf|ق| ﻕ|ﻖ|ﻗ|ﻘ|Q
 | | | |0xFED5|0xFED5|0xFED6|0xFED7|0xFED8|
Л|л|Arabic Letter Lam|ل|ﻝ|ﻞ|ﻟ|ﻠ|L
 | | | |0x0644|0xFEDD|0xFEDE|0xFEDF|0xFEE0|
М|м|Arabic Letter Meem|م|ﻡ|ﻢ|ﻣ|ﻤ|M
 | | | |0x0645|0xFEE1|0xFEE2|0xFEE3|0xFEE4|
Н|н|Arabic Letter Noon|ن|ﻥ|ﻦ|ﻧ|ﻨ|N
 | | | |0x0646|0xFEE5|0xFEE6|0xFEE7|0xFEE8|
Ң|ң|Arabic Letter Ng|ڭ|ﯓ|ﯔ|ﯕ|ﯖ|NH
 | | | |0x06AD|0xFBD3|0xFBD4|0xFBD5|0xFBD6|
О|о|Arabic Letter Waw|و|ﻭ|ﻮ| | |O
 | | | |0x0648|0xFEED|0xFEEE| | |
Ө|ө|Hamza + Waw|ءو| | | | |OH
 | | |Arabic Letter High Hamza Waw|ٶ| | | | |
 | | | |0x0676| | | | |
П|п|Arabic Letter Peh|پ|ﭖ|ﭗ|ﭘ|ﭙ|P
 | | | |0x067E|0xFB56|0xFB57|0xFB58|0xFB59|
Р|р|Arabic Letter Reh|ر|ﺭ|ﺮ| | |R
 | | | |0x0631|0xFEAD|0xFEAE| | |
С|с|Arabic Letter Seen|س|ﺱ|ﺲ|ﺳ|ﺴ|S
 | | | |0x0633|0xFEB1|0xFEB2|0xFEB3|0xFEB4|
Т|т|Arabic Letter Teh|ت|ﺕ|ﺖ|ﺗ|ﺘ|T
 | | | |0x062A|0xFE95|0xFE96|0xFE97|0xFE98|
У|у|Arabic Letter Ve|ۋ|ﯞ|ﯟ| | |W
 | | | |0x06CB|0xFBDE|0xFBDF| | |
Ұ|ұ|Arabic Letter U|ۇ|ﯗ|ﯘ| | |U
 | | | |0x06C7|0xFBD7|0xFBD8| | |
Ү|ү|Hamza + U|ءۇ| | | | |UH
 | | |Arabic Letter U with Hamza Above|ٷ| | | | |
 | | | |0x0677| | | | |
Ф|ф|Arabic Letter Feh|ف|ﻑ|ﻒ|ﻓ|ﻔ|F
 | | | |0x0641|0xFED1|0xFED2|0xFED3|0xFED4|
Х|х|Arabic Letter Hah|ح|ﺡ|ﺢ|ﺣ|ﺤ|X
 | | | |0x062D|0xFEA1|0xFEA2|0xFEA3|0xFEA4|
Һ|һ|Arabic Letter Heh Doachashmee|ھ|ﮪ|ﮫ|ﮬ|ﮭ|XH
 | | | |0x06BE|0xFBAA|0xFBAB|0xFBAC|0xFBAD|
Ч|ч|Arabic Letter Tcheh|چ|ﭺ|ﭻ|ﭼ|ﭽ|CH
 | | | |0x0686|0xFB7A|0xFB7B|0xFB7C|0xFB7D|
Ш|ш|Arabic Letter Sheen|ش|ﺵ|ﺶ|ﺷ|ﺸ|SH
 | | | |0x0634|0xFEB5|0xFEB6|0xFEB7|0xFEB8|
Щ|щ|Sheen + Sheen|شش| | | | |
Ы|ы|Arabic Letter Alef Maksura|ى|ﻯ|ﻰ|ﯨ|ﯩ|I
 | | | |0x0649|0xFEEF|0xFEF0|0xFBE8|0xFBE9|
І|і|Hamza + Alef Maksura|ءى| | | | |IH
 | | |Arabic Letter High Hamza Yeh|ٸ| | | | |
 | | | |0x0678| | | | |
-| |Arabic Ligature Lam with Alef|ﻻ|ﻻ|ﻼ| | |-
 | | | |0xFEFB|0xFEFB|0xFEFC| | |
Э|э|Heh|ه| | | | |-
Ю|ю|Yeh + Ve|يۋ| | | | |-
Ц|ц|Teh + Seen|تس| | | | |-
Ё|ё|Yeh + Waw|يو| | | | |
Я|я|Yeh + Alef|يا‎| | | | |-
Ия| | |يا‎| | | | |-
АƏ| | |ا‎| | | | |-
ЬЕ|ЪЕ| |يە| | | | |-
ИЕВ|ЕВ| |يەۆ| | | | |-
Ъ|ъ| | | | | | |-
Ь|ь| | | | | | |

## Todos

- Write MORE Tests

## License

MIT

**Free Software, Hell Yeah!**
