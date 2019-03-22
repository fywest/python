import sys
import csv
from collections import namedtuple

IncomeTaxQuickLookupItem = namedtuple('IncomeTaxQuickLookupItem',['start_point','tax_rate','quick_subtractor'])

INCOME_TAX_START_POINT = 3500

INCOME_TAX_QUICK_LOOPUP_TABLE=[
IncomeTaxQuickLookupItem(80000, 0.45, 13505),
IncomeTaxQuickLookupItem(55000, 0.35, 5505),
IncomeTaxQuickLookupItem(35000, 0.30, 2755),
IncomeTaxQuickLookupItem(9000, 0.25, 1005),
IncomeTaxQuickLookupItem(4500, 0.2, 555),
IncomeTaxQuickLookupItem(1500, 0.1, 105),
IncomeTaxQuickLookupItem(0, 0.03, 0),
]

calss Args(object):
    def __init__(self):
        self.args=sys.argv[1:]

    def _value_after_option(self,option):
        try:
            index = self.args.index(option)
            return self.args[index+1]
        except(ValueError,IndexError):
            print('Parameter Error')
            exit()

    @property
    def config_path(self):
        return slef._value_after_option('-c')

    @property
    def userdata_path(self):
        return self._value_after_option('-d')

    @property
    def export_path(self):
        return self._value_after_option('-o')

args=Args()

class Config(object):
    def __init__(self):
        self.config=self._read_config()

    def _read_config(self):
        config_path=args.config_path
        config={}
        with open(config_path) as f:
            for line in f.readlines():
