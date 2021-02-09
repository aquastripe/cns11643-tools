from pathlib import Path

import pandas as pd

from definitions import ROOT_DIR


class LookupComponent(object):

    def __init__(self, data_root=ROOT_DIR / 'downloads/Open_Data', plane_1=True):
        self._init_word2unicode()
        self._init_cns2unicode_unicode2cns(data_root, plane_1)
        self._init_cns2component(data_root, plane_1)
        self._unicode2component = {}

        for word in self._word2unicode.keys():
            pass

    def _init_cns2component(self, data_root, plane_1):
        self._cns2component = {}
        cns_component_file = data_root / 'Properties/CNS_component.txt'
        with open(cns_component_file, 'r') as f:
            lines = f.readlines()
        end = 5401 if plane_1 else None
        for line in lines[:end]:
            cns_code, components = line.split()
            components = components.split(';')[0]  # consider the first components only, `;` as separator
            components = components.split(',')  # list of str
            components = list(map(lambda x: int(x), components))  # list of int
            self._cns2component[cns_code] = components

    def _init_cns2unicode_unicode2cns(self, data_root, plane_1):
        self._cns2unicode = {}
        self._unicode2cns = {}
        cns2unicode_file = data_root / 'MapingTables/Unicode/CNS2UNICODE_Unicode BMP.txt'
        with open(cns2unicode_file, 'r') as f:
            cns2unicode_lines = f.readlines()

        end = 6330 if plane_1 else None
        for line in cns2unicode_lines[:end]:
            cns_code, unicode = line.strip().split()
            unicode = int(unicode, 16)
            self._cns2unicode[cns_code] = unicode
            self._unicode2cns[unicode] = cns_code

    def _init_word2unicode(self):
        self._word2unicode = {}
        common_words_dataframe = pd.read_csv('../traditional_Chinese_4808_common_words.csv')
        for row in common_words_dataframe.values:
            # serial_id = row[0]
            unicode = row[1]
            unicode = int(unicode, 16)
            word = row[2]
            self._word2unicode[word] = unicode

    def __call__(self, word: str = None):
        unicode = self._word2unicode[word]
        cns_code = self._unicode2cns[unicode]
        components = self._cns2component[cns_code]
        return components
