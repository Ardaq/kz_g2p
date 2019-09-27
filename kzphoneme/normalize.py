import re


class Normalize(object):
    def __init__(self, *args, **kwargs):
        super(Normalize, self).__init__(*args, **kwargs)

    @staticmethod
    def _arab_norm(string):
        string = re.sub(r'[ٴ]', 'ء', string)
        string = re.sub(r'[ﺎﺍ]', 'ا', string)
        string = re.sub(r'[ٵ]', 'ءا', string)
        string = re.sub(r'[ﺩﺪ]', 'د', string)
        string = re.sub(r'[ﺭﺮ]', 'ر', string)
        string = re.sub(r'[ﺯﺰ]', 'ز', string)
        string = re.sub(r'[ﺏﺐﺑﺒ]', 'ب', string)
        string = re.sub(r'[ﺕﺖﺗﺘ]', 'ت', string)
        string = re.sub(r'[ﺝﺞﺟﺠ]', 'ج', string)
        string = re.sub(r'[ﺡﺢﺣﺤ]', 'ح', string)
        string = re.sub(r'[ﺱﺲﺳﺴ]', 'س', string)
        string = re.sub(r'[ﺵﺶﺷﺸ]', 'ش', string)
        string = re.sub(r'[ﻉﻊﻋﻌ]', 'ع', string)
        string = re.sub(r'[ﻑﻒﻓﻔ]', 'ف', string)
        string = re.sub(r'[ﻕﻖﻗﻘ]', 'ق', string)
        string = re.sub(r'[ﻙﻚﻛﻜ]', 'ك', string)
        string = re.sub(r'[ﻝﻞﻟﻠ]', 'ل', string)
        string = re.sub(r'[ﻡﻢﻣﻤ]', 'م', string)
        string = re.sub(r'[ﻥﻦﻧﻨ]', 'ن', string)
        string = re.sub(r'[ﻯﻰﯨﯩ]', 'ى', string)
        string = re.sub(r'[ﻱﻲﻳﻴ]', 'ي', string)
        string = re.sub(r'[ﭖﭗﭘﭙ]', 'پ', string)
        string = re.sub(r'[ﭺﭻﭼﭽ]', 'چ', string)
        string = re.sub(r'[ﯓﯔﯕﯖ]', 'ڭ', string)
        string = re.sub(r'[ﮒﮓﮔﮕ]', 'گ', string)
        string = re.sub(r'[ﮪﮫﮬﮭ]', 'ھ', string)
        string = re.sub(r'[ﻭﻮ]', 'و', string)
        string = re.sub(r'[ﯙﯚ]', 'ۆ', string)
        string = re.sub(r'[ﯗﯘ]', 'ۇ', string)
        string = re.sub(r'[ﯞﯟ]', 'ۋ', string)
        string = re.sub(r'[ﻩﻪ]', 'ه', string)
        string = re.sub(r'[ٶ]', 'ءو', string)
        string = re.sub(r'[ٷ]', 'ءۇ', string)
        string = re.sub(r'[ٸ]', 'ءى', string)
        return string

    @staticmethod
    def _cyril_norm(string):
        return string.lower()

    def norm(self, string: str, script='arab'):
        if script == 'arab':
            return self._arab_norm(string)
        if script == 'cyril':
            return self._cyril_norm(string)
        return string
