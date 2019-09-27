import os
import re

dirname = os.path.dirname(__file__)


class Convert(object):
    def __init__(self, *args, **kwargs):
        super(Convert, self).__init__(*args, **kwargs)
        data = {}
        with open(os.path.join(dirname, 'rightreading.kz'), 'r', encoding='utf8') as file:
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


