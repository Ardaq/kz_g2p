import unittest
from kzphoneme import Phoneme

arab_text = 'ءبىلىم بۇلاعى'
cyril_text = 'білім бұлағы'


class PhonemeTestCase(unittest.TestCase):
    pho = Phoneme()

    def test_phoneme_arab(self):
        arab_res = self.pho(arab_text, 'arab')
        self.assertEqual(arab_res, ['B', 'IH', 'L', 'IH', 'M', ' ', 'B', 'U', 'L', 'A', 'C', 'I'])

    def test_phoneme_cyril(self):
        cyril_res = self.pho(cyril_text, 'cyril')
        self.assertEqual(cyril_res, ['B', 'IH', 'L', 'IH', 'M', ' ', 'B', 'U', 'L', 'A', 'C', 'I'])

    def test_spead(self):
        for i in range(10000):
            arab_res = self.pho(arab_text, 'arab')
            cyril_res = self.pho(cyril_text, 'cyril')


if __name__ == '__main__':
    unittest.main()
