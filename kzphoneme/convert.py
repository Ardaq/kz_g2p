import os
import re

dirname = os.path.dirname(__file__)


class Convert(object):
    def __init__(self, *args, **kwargs):
        super(Convert, self).__init__(*args, **kwargs)
        data = {}
        with open(os.path.join(dirname, 'data/rightreading.kz'), 'r', encoding='utf8') as file:
            for line in file:
                line = line.strip()
                if line.startswith('#') or len(line) < 1:
                    continue
                k, v = line.split('|')
                data[k] = v
        self._spacial_words = data
        self._spacial_words_keys = tuple(data.keys())
        self._siziq_re = re.compile(r'[^_.-]+')
        self._special_suffix = ["men", "pen", "ben", "menen", "penen", "benen", "niki", "diki",
                                "tiki", "ker", "ger", "qor", "paz", "qoy", "kes", "simaq", "ant",
                                "tay", "tal", "dar", "eke", "tar", "kesh", "xana", "cal", "kent",
                                "uli", "yev", "ova", "ov", "qizi", "tucin", "kunem"]
        self._name_suffix = ["jan", "bek", "bay", "gul"]
        self._un_suffix = ["by", "bey", "esh", "key", "qay"]
        self._vh = re.compile("[auio]")
        self._ve = re.compile("[ekg]")

    def _arab2latin(self, word: str):
        word = word.strip().rstrip()
        if len(word) < 1:
            return word
        if ('-' in word or '.' in word) and len(word) > 1:
            s_iter = self._siziq_re.finditer(word)
            ss = []
            pos = 0
            for xt in s_iter:
                st, end = xt.span()
                a_w = word[pos:st]
                b_w = word[st: end]
                ss.append(a_w)
                ss.append(self._arab2latin(b_w))
                pos = end
            if pos < len(word):
                ss.append(word[pos:])
            return ''.join(ss)
        word = re.sub(r'ا', 'a', word)
        word = re.sub(r"ب", "b", word)
        word = re.sub(r"پ", "p", word)
        word = re.sub(r"ت", "t", word)
        word = re.sub(r"د", "d", word)
        word = re.sub(r"ح", "x", word)
        word = re.sub(r"ع", "c", word)
        word = re.sub(r"ھ", "xh", word)
        word = re.sub(r"ق", "q", word)
        word = re.sub(r"ف", "f", word)
        word = re.sub(r"ج", "j", word)
        word = re.sub(r"ز", "z", word)
        word = re.sub(r"ر", "r", word)
        word = re.sub(r"س", "s", word)
        word = re.sub(r"ش", "sh", word)
        word = re.sub(r"چ", "ch", word)
        word = re.sub(r"ك", "k", word)
        word = re.sub(r"گ", "g", word)
        word = re.sub(r"ل", "l", word)
        word = re.sub(r"م", "m", word)
        word = re.sub(r"ن", "n", word)
        word = re.sub(r"ڭ", "nh", word)
        word = re.sub(r"ە", "e", word)
        word = re.sub(r"و", "o", word)
        word = re.sub(r"ۇ", "u", word)
        word = re.sub(r"ۋ", "w", word)
        word = re.sub(r"ۆ", "v", word)
        word = re.sub(r"ي", "y", word)
        word = re.sub(r"ى", "i", word)

        word = re.sub("[،]", ",", word)
        word = re.sub("[؟]", "?", word)
        word = re.sub("[؛]", ";", word)
        word = re.sub("[»«]", "\"", word)
        if 'ء' in word:
            n_word = word[1:]
        else:
            n_word = word
        exists = self._word_startswith(n_word, self._spacial_words_keys)
        if any(exists):
            a_w = self._spacial_words[exists[0]]
            rest_w = n_word[len(exists[0]):]
            vv = re.compile(r'[auoie]h?').findall(a_w)
            last_one = vv[-1] if len(vv) > 0 else None
            if last_one and ('h' in last_one or 'e' in last_one):
                rest_w = re.sub(r'([aoui])', r'\1h', rest_w)
            word = a_w + rest_w
        else:
            word = self._spacial_rules(word)
        return word

    @staticmethod
    def _word_startswith(word, word_list):
        return [w for w in word_list if word.startswith(w)]

    @staticmethod
    def _word_contains(word, word_list):
        return [w for w in word_list if w in word]

    def _spacial_rules(self, word):
        exists = self._word_startswith(word, self._un_suffix)
        if any(exists):
            word = exists[0] + self._spacial_rules(word[len(exists[0])])
        exists = self._word_contains(word, self._name_suffix)
        if any(exists):
            suffix = exists[0]
            index = word.index(suffix)
            root = word[:index]
            rest = word[index + len(suffix):]
            word = self._spacial_rules(root) + suffix + self._spacial_rules(rest)
        for suff in self._special_suffix:
            if not word.startswith(suff) and suff in word:
                index = word.index(suff)
                root = word[:index]
                rest = word[index + len(suff):]
                if not any(re.findall(r'[auioe]', root)):
                    continue
                if suff in ["niki", "diki", "tiki"]:
                    suff = suff.replace('i', 'ih')
                if suff == 'kunem':
                    suff = suff.replace('u', 'uh')
                if 'h' in suff or 'e' in suff:
                    if 'i' in rest and 'ih' not in rest:
                        rest = rest.replace('i', 'ih')
                word = self._spacial_rules(root) + suff + rest
                break
        return self._hamza_normalize(word)

    def _hamza_normalize(self, word):
        if 'ء' in word:
            word = word.replace('ء', '')
            word = re.sub(r'([auio])', r'\1h', word)
        if self._vh.search(word) and self._ve.search(word):
            word = re.sub(r'([auio])', r'\1h', word)
        if word.startswith(('q', 'c')):
            word = re.sub(r'([qc][auio])h', r'\1', word)
        word = re.sub(r'h+', 'h', word)
        return word

    @staticmethod
    def _cyril2latin(word: str):
        word = word.strip().rstrip()
        word = word.replace("ИЕВ", "yev")
        word = word.replace("иев", "yev")
        word = word.replace("ЕВ", "yev")
        word = word.replace("ев", "yev")
        word = word.replace("ЪЕ", "ye")
        word = word.replace("ЬЕ", "ye")
        word = word.replace("ье", "ye")
        word = word.replace("ъе", "ye")
        word = word.replace("ә", "ah")
        word = word.replace("Ә", "ah")
        word = word.replace("аə", "a")
        word = word.replace("АƏ", "a")
        word = word.replace("а", "a")
        word = word.replace("А", "a")
        word = word.replace("б", "b")
        word = word.replace("Б", "b")
        word = word.replace("в", "v")
        word = word.replace("В", "v")
        word = word.replace("г", "g")
        word = word.replace("Г", "g")
        word = word.replace("ғ", "c")
        word = word.replace("Ғ", "c")
        word = word.replace("д", "d")
        word = word.replace("Д", "d")
        word = word.replace("Е", "e")
        word = word.replace("Э", "e")
        word = word.replace("е", "e")
        word = word.replace("э", "e")
        word = word.replace("ж", "j")
        word = word.replace("Ж", "j")
        word = word.replace("з", "z")
        word = word.replace("З", "z")
        word = word.replace("ИЯ", "ya")
        word = word.replace("Ия", "ya")
        word = word.replace("ия", "ya")
        word = word.replace("И", "y")
        word = word.replace("и", "y")
        word = word.replace("Й", "y")
        word = word.replace("й", "y")
        word = word.replace("к", "k")
        word = word.replace("К", "k")
        word = word.replace("қ", "q")
        word = word.replace("Қ", "q")
        word = word.replace("л", "l")
        word = word.replace("Л", "l")
        word = word.replace("м", "m")
        word = word.replace("М", "m")
        word = word.replace("н", "n")
        word = word.replace("Н", "n")
        word = word.replace("ң", "nh")
        word = word.replace("Ң", "nh")
        word = word.replace("ө", "oh")
        word = word.replace("Ө", "oh")
        word = word.replace("о", "o")
        word = word.replace("О", "o")
        word = word.replace("п", "p")
        word = word.replace("П", "p")
        word = word.replace("р", "r")
        word = word.replace("Р", "r")
        word = word.replace("с", "s")
        word = word.replace("С", "s")
        word = word.replace("т", "t")
        word = word.replace("Т", "t")
        word = word.replace("у", "w")
        word = word.replace("У", "w")
        word = word.replace("ү", "uh")
        word = word.replace("Ү", "uh")
        word = word.replace("ұ", "u")
        word = word.replace("Ұ", "u")
        word = word.replace("Ф", "f")
        word = word.replace("ф", "f")
        word = word.replace("х", "x")
        word = word.replace("Х", "x")
        word = word.replace("һ", "xh")
        word = word.replace("Һ", "xh")
        word = word.replace("ц", "ts")
        word = word.replace("Ц", "ts")
        word = word.replace("ч", "ch")
        word = word.replace("Ч", "ch")
        word = word.replace("ш", "sh")
        word = word.replace("Ш", "sh")
        word = word.replace("ы", "i")
        word = word.replace("Ы", "i")
        word = word.replace("і", "ih")
        word = word.replace("І", "ih")
        word = word.replace("ё", "yo")
        word = word.replace("Ё", "yo")
        word = word.replace("ю", "yw")
        word = word.replace("Ю", "yw")
        word = word.replace("я", "ya")
        word = word.replace("Я", "ya")
        word = word.replace("щ", "shsh")
        word = word.replace("Щ", "shsh")
        word = word.replace("Ъ", "")
        word = word.replace("Ь", "")
        word = word.replace("ъ", "")
        word = word.replace("ь", "")
        return word

    def convert(self, sentence: str, script='arab'):
        words = sentence.split()
        if script == 'arab':
            words = [self._arab2latin(w) for w in words]
        if script == 'cyril':
            words = [self._cyril2latin(w) for w in words]
        return ' '.join(words)
