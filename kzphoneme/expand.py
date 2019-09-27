import re

unit = ["", "bihr", "ekih", "uhsh", "tohrt", "bes", "alti", "jetih", "segihz", "toghiz"]
ten = [
    "",
    "on",
    "jyirma",
    "otiz",
    "qiriq",
    "elw",
    "alpis",
    "jetpihs",
    "seksen",
    "toqsan",
]
inshi = {
    0: 'inshi',
    1: 'ihnshih',
    2: 'ihnshih',
    3: 'ihnshih',
    4: 'ihnshih',
    5: 'ihnshih',
    6: 'inshi',
    7: 'ihnshih',
    8: 'ihnshih',
    9: 'inshi',
}
mill = [
    " ",
    " ming",
    " myllyon",
    " myllyard",
    " tryllyon",
    " kvadryllyon",
    " kvantyllyon",
    " sextyllyon",
    " septyllyon",
    " oktyllyon",
    " nonyllyon",
    " desyllyon",
]


def _remove_commas(m):
    return m.group(1).replace(',', '')


class Number(object):
    def __init__(self, comma=",", zero="nohl", one="bihr", decimal="buhtihn", *args, **kwargs):
        super(Number, self).__init__(*args, **kwargs)
        self._mill_count = 0
        self._number_args = dict(zero=zero, one=one)
        self._comma = comma
        self._decimal = decimal
        self._comma_number_re = re.compile(r'([0-9][0-9,]+[0-9])')
        self._decimal_number_re = re.compile(r'([0-9]+\.[0-9]+)')
        self._pounds_re = re.compile(r'£([0-9,]*[0-9]+)')
        self._yuan_re = re.compile(r'([0-9.,]*[0-9]+)￥')
        self._tenge_re = re.compile(r'([0-9.,]*[0-9]+)₸')
        self._tenge2_re = re.compile(r'₸([0-9.,]*[0-9]+)')
        self._dollars_re = re.compile(r'\$([0-9.,]*[0-9]+)')
        self._ordinal_re = re.compile(r'([0-9]+)\s*?([-])')
        self._number_re = re.compile(r'[0-9]+')

    def _group_sub(self, mo):
        units = int(mo.group(1))
        if units:
            return "{}, ".format(unit[units])
        else:
            return " {}, ".format(self._number_args["zero"])

    def _enword(self, num, group):
        # import pdb
        # pdb.set_trace()

        if group == 1:
            num = re.sub(r"(\d)", self._group_sub, num)
        elif int(num) == 0:
            num = self._number_args["zero"]
        elif int(num) == 1:
            num = self._number_args["one"]
        else:
            num = num.lstrip().lstrip("0")
            self._mill_count = 0
            mo = re.search(r"(\d)(\d)(\d)(?=\D*\Z)", num)
            while mo:
                num = re.sub(r"(\d)(\d)(\d)(?=\D*\Z)", self._hundred_sub, num, 1)
                mo = re.search(r"(\d)(\d)(\d)(?=\D*\Z)", num)
            num = re.sub(r"(\d)(\d)(?=\D*\Z)", self._ten_sub, num, 1)
            num = re.sub(r"(\d)(?=\D*\Z)", self._unit_sub, num, 1)
        return num

    @staticmethod
    def _mill_fn(ind=0):
        if ind > len(mill) - 1:
            raise Exception
        return mill[ind]

    def _unit_fn(self, units, m_index=0):
        return "{}{}".format(unit[units], self._mill_fn(m_index))

    def _ten_fn(self, tens, units, m_index=0):
        return "{} {}{}".format(
            ten[tens],
            unit[units],
            self._mill_fn(m_index),
        )

    def _hundred_fn(self, hundreds, tens, units, m_index):
        if hundreds:
            return "{} juz {} {}, ".format(
                unit[hundreds],  # use unit not unitfn as simpler
                self._ten_fn(tens, units),
                self._mill_fn(m_index),
            )
        if tens or units:
            return "{}{}, ".format(self._ten_fn(tens, units), self._mill_fn(m_index))
        return ""

    def _hundred_sub(self, mo):
        ret = self._hundred_fn(
            int(mo.group(1)), int(mo.group(2)), int(mo.group(3)), self._mill_count
        )
        self._mill_count += 1
        return ret

    def _ten_sub(self, mo):
        return "%s, " % self._ten_fn(int(mo.group(1)), int(mo.group(2)), self._mill_count)

    def _unit_sub(self, mo):
        return "%s, " % self._unit_fn(int(mo.group(1)), self._mill_count)

    def number_to_words(self, num):
        num = "%s" % num
        nonwhite = num.lstrip()
        if nonwhite[0] == "+":
            sign = "pylos"
        elif nonwhite[0] == "-":
            sign = "mynos"
        else:
            sign = ""

        final_point = False
        if self._decimal:
            chunks = num.split(".", 1)
            if chunks[-1] == "":  # remove blank string if nothing after decimal
                chunks = chunks[:-1]
                final_point = True  # add 'point' to end of output
        else:
            chunks = [num]

        first = 1
        loop_start = 0

        if chunks[0] == "":
            first = 0
            if len(chunks) > 1:
                loop_start = 1

        for i in range(loop_start, len(chunks)):
            chunk = chunks[i]
            # remove all non numeric \D
            chunk = re.sub(r"\D", '', chunk)
            if chunk == "":
                chunk = "0"

            if first == 0 or first == "":
                chunk = self._enword(chunk, 1)
            else:
                chunk = self._enword(chunk, 0)

            if chunk[-2:] == ", ":
                chunk = chunk[:-2]
            chunk = re.sub(r"\s+,", ',', chunk)

            if first:
                chunk = re.sub(r", (\S+)\s+\Z", " \\1", chunk)
            chunk = re.sub(r"\s+", ' ', chunk)
            chunk = chunk.strip()
            if first:
                first = ""
            chunks[i] = chunk

        num_chunks = []
        if first != 0:
            num_chunks = chunks[0].split("%s " % self._comma)

        for chunk in chunks[1:]:
            num_chunks.append(self._decimal)
            num_chunks.extend(chunk.split("%s " % self._comma))

        if final_point:
            num_chunks.append(self._decimal)

        sign_out = "%s " % sign if sign else ""
        num = "{}{}".format(sign_out, num_chunks.pop(0))
        if self._decimal is None:
            first = True
        else:
            first = not num.endswith(self._decimal)
        for nc in num_chunks:
            if nc == self._decimal:
                num += " %s" % nc
                first = 0
            elif first:
                num += "{} {}".format(self._comma, nc)
            else:
                num += " %s" % nc
        return num

    def _expand_decimal_point(self, m):
        return m.group(1).replace('.', ' {} '.format(self._decimal))

    @staticmethod
    def _expand_dollars(m):
        match = m.group(1)
        parts = match.split('.')
        dollar_unit = 'dollar'
        cent_unit = 'tiyin'
        if len(parts) > 2:
            return match + ' dollar'  # Unexpected format
        dollars = int(parts[0]) if parts[0] else 0
        cents = int(parts[1]) if len(parts) > 1 and parts[1] else 0
        if dollars and cents:
            return '{} {}, {} {}'.format(dollars, dollar_unit, cents, cent_unit)
        elif dollars:
            return '{} {}'.format(dollars, dollar_unit)
        elif cents:
            return '{} {}'.format(cents, cent_unit)
        else:
            return 'noel dollar'

    @staticmethod
    def _expand_tenge(m):
        match = m.group(1)
        parts = match.split('.')
        dollar_unit = 'tenhge'
        cent_unit = 'tiyin'
        if len(parts) > 2:
            return match + ' tenhge'  # Unexpected format
        dollars = int(parts[0]) if parts[0] else 0
        cents = int(parts[1]) if len(parts) > 1 and parts[1] else 0
        if dollars and cents:
            return '{} {}, {} {}'.format(dollars, dollar_unit, cents, cent_unit)
        elif dollars:
            return '{} {}'.format(dollars, dollar_unit)
        elif cents:
            return '{} {}'.format(cents, cent_unit)
        else:
            return 'noel tenhge'

    @staticmethod
    def _expand_ordinal(m):
        num = m.group(1)
        if num == 0:
            return 'nohlihnshih'
        else:
            num = "%s" % num
            last = int(num[-1])
            return '{}{} '.format(num, inshi[last])

    def _expand_number(self, m):
        return self.number_to_words(int(m.group(0)))

    def normalize_numbers(self, text):
        text = re.sub(self._comma_number_re, _remove_commas, text)
        text = re.sub(self._pounds_re, r'\1 fwnt', text)
        text = re.sub(self._dollars_re, self._expand_dollars, text)
        text = re.sub(self._yuan_re, r'\1 yuan', text)
        text = re.sub(self._tenge_re, self._expand_tenge, text)
        text = re.sub(self._tenge2_re, self._expand_tenge, text)
        text = re.sub(self._decimal_number_re, self._expand_decimal_point, text)
        text = re.sub(self._ordinal_re, self._expand_ordinal, text)
        text = re.sub(self._number_re, self._expand_number, text)
        return text
