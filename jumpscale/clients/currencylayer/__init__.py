from jumpscale.core.base import StoredFactory

from .currencylayer import CurrencyLayerClient


export_module_as = StoredFactory(CurrencyLayerClient)

"""
JS-NG> fake = j.clients.currencylayer.new('fake')                                                                      
JS-NG> fake.cur2id_print()                                                                                             
{'aed': 1,
 'afn': 2,
 'all': 3,
 'amd': 4,
 'ang': 5,
 'aoa': 6,
 'ars': 7,
 'aud': 8,
 'awg': 9,
 'azn': 10,
 'bam': 11,
 'bbd': 12,
 'bdt': 13,
 'bgn': 14,
 'bhd': 15,
 'bif': 16,
 'bmd': 17,
 'bnd': 18,
 'bob': 19,
 'brl': 20,
 'bsd': 21,
 'btc': 22,
 'btn': 23,
 'bwp': 24,
 'byn': 25,
 'byr': 26,
 'bzd': 27,
 'cad': 28,
 'cdf': 29,
 'chf': 30,
 'clf': 31,
 'clp': 32,
 'cny': 33,
 'cop': 34,
 'crc': 35,
 'cuc': 36,
 'cup': 37,
 'cve': 38,
 'czk': 39,
 'djf': 40,
 'dkk': 41,
 'dop': 42,
 'dzd': 43,
 'egp': 44,
 'ern': 45,
 'etb': 46,
 'eth': 47,
 'eur': 48,
 'fjd': 49,
 'fkp': 50,
 'gbp': 51,
 'gel': 52,
 'ggp': 53,
 'ghs': 54,
 'gip': 55,
 'gmd': 56,
 'gnf': 57,
 'gtq': 58,
 'gyd': 59,
 'hkd': 60,
 'hnl': 61,
 'hrk': 62,
 'htg': 63,
 'huf': 64,
 'idr': 65,
 'ils': 66,
 'imp': 67,
 'inr': 68,
 'iqd': 69,
 'irr': 70,
 'isk': 71,
 'jep': 72,
 'jmd': 73,
 'jod': 74,
 'jpy': 75,
 'kes': 76,
 'kgs': 77,
 'khr': 78,
 'kmf': 79,
 'kpw': 80,
 'krw': 81,
 'kwd': 82,
 'kyd': 83,
 'kzt': 84,
 'lak': 85,
 'lbp': 86,
 'lkr': 87,
 'lrd': 88,
 'lsl': 89,
 'ltl': 90,
 'lvl': 91,
 'lyd': 92,
 'mad': 93,
 'mdl': 94,
 'mga': 95,
 'mkd': 96,
 'mmk': 97,
 'mnt': 98,
 'mop': 99,
 'mro': 100,
 'mur': 101,
 'mvr': 102,
 'mwk': 103,
 'mxn': 104,
 'myr': 105,
 'mzn': 106,
 'nad': 107,
 'ngn': 108,
 'nio': 109,
 'nok': 110,
 'npr': 111,
 'nzd': 112,
 'omr': 113,
 'pab': 114,
 'pen': 115,
 'pgk': 116,
 'php': 117,
 'pkr': 118,
 'pln': 119,
 'pyg': 120,
 'qar': 121,
 'ron': 122,
 'rsd': 123,
 'rub': 124,
 'rwf': 125,
 'sar': 126,
 'sbd': 127,
 'scr': 128,
 'sdg': 129,
 'sek': 130,
 'sgd': 131,
 'shp': 132,
 'sll': 133,
 'sos': 134,
 'srd': 135,
 'std': 136,
 'svc': 137,
 'syp': 138,
 'szl': 139,
 'thb': 140,
 'tjs': 141,
 'tmt': 142,
 'tnd': 143,
 'top': 144,
 'try': 145,
 'ttd': 146,
 'twd': 147,
 'tzs': 148,
 'uah': 149,
 'ugx': 150,
 'usd': 151,
 'uyu': 152,
 'uzs': 153,
 'vef': 154,
 'vnd': 155,
 'vuv': 156,
 'wst': 157,
 'xaf': 158,
 'xag': 159,
 'xau': 160,
 'xcd': 161,
 'xdr': 162,
 'xof': 163,
 'xpf': 164,
 'xrp': 165,
 'yer': 166,
 'zar': 167,
 'zmk': 168,
 'zmw': 169,
 'zwl': 170}
JS-NG> fake.id2cur_print()                                                                                             
{1: 'aed',
 2: 'afn',
 3: 'all',
 4: 'amd',
 5: 'ang',
 6: 'aoa',
 7: 'ars',
 8: 'aud',
 9: 'awg',
 10: 'azn',
 11: 'bam',
 12: 'bbd',
 13: 'bdt',
 14: 'bgn',
 15: 'bhd',
 16: 'bif',
 17: 'bmd',
 18: 'bnd',
 19: 'bob',
 20: 'brl',
 21: 'bsd',
 22: 'btc',
 23: 'btn',
 24: 'bwp',
 25: 'byn',
 26: 'byr',
 27: 'bzd',
 28: 'cad',
 29: 'cdf',
 30: 'chf',
 31: 'clf',
 32: 'clp',
 33: 'cny',
 34: 'cop',
 35: 'crc',
 36: 'cuc',
 37: 'cup',
 38: 'cve',
 39: 'czk',
 40: 'djf',
 41: 'dkk',
 42: 'dop',
 43: 'dzd',
 44: 'egp',
 45: 'ern',
 46: 'etb',
 47: 'eth',
 48: 'eur',
 49: 'fjd',
 50: 'fkp',
 51: 'gbp',
 52: 'gel',
 53: 'ggp',
 54: 'ghs',
 55: 'gip',
 56: 'gmd',
 57: 'gnf',
 58: 'gtq',
 59: 'gyd',
 60: 'hkd',
 61: 'hnl',
 62: 'hrk',
 63: 'htg',
 64: 'huf',
 65: 'idr',
 66: 'ils',
 67: 'imp',
 68: 'inr',
 69: 'iqd',
 70: 'irr',
 71: 'isk',
 72: 'jep',
 73: 'jmd',
 74: 'jod',
 75: 'jpy',
 76: 'kes',
 77: 'kgs',
 78: 'khr',
 79: 'kmf',
 80: 'kpw',
 81: 'krw',
 82: 'kwd',
 83: 'kyd',
 84: 'kzt',
 85: 'lak',
 86: 'lbp',
 87: 'lkr',
 88: 'lrd',
 89: 'lsl',
 90: 'ltl',
 91: 'lvl',
 92: 'lyd',
 93: 'mad',
 94: 'mdl',
 95: 'mga',
 96: 'mkd',
 97: 'mmk',
 98: 'mnt',
 99: 'mop',
 100: 'mro',
 101: 'mur',
 102: 'mvr',
 103: 'mwk',
 104: 'mxn',
 105: 'myr',
 106: 'mzn',
 107: 'nad',
 108: 'ngn',
 109: 'nio',
 110: 'nok',
 111: 'npr',
 112: 'nzd',
 113: 'omr',
 114: 'pab',
 115: 'pen',
 116: 'pgk',
 117: 'php',
 118: 'pkr',
 119: 'pln',
 120: 'pyg',
 121: 'qar',
 122: 'ron',
 123: 'rsd',
 124: 'rub',
 125: 'rwf',
 126: 'sar',
 127: 'sbd',
 128: 'scr',
 129: 'sdg',
 130: 'sek',
 131: 'sgd',
 132: 'shp',
 133: 'sll',
 134: 'sos',
 135: 'srd',
 136: 'std',
 137: 'svc',
 138: 'syp',
 139: 'szl',
 140: 'thb',
 141: 'tjs',
 142: 'tmt',
 143: 'tnd',
 144: 'top',
 145: 'try',
 146: 'ttd',
 147: 'twd',
 148: 'tzs',
 149: 'uah',
 150: 'ugx',
 151: 'usd',
 152: 'uyu',
 153: 'uzs',
 154: 'vef',
 155: 'vnd',
 156: 'vuv',
 157: 'wst',
 158: 'xaf',
 159: 'xag',
 160: 'xau',
 161: 'xcd',
 162: 'xdr',
 163: 'xof',
 164: 'xpf',
 165: 'xrp',
 166: 'yer',
 167: 'zar',
 168: 'zmk',
 169: 'zmw',
 170: 'zwl'}
JS-NG> fake.id2cur                                                                                                     
{1: 'aed', 2: 'afn', 3: 'all', 4: 'amd', 5: 'ang', 6: 'aoa', 7: 'ars', 8: 'aud', 9: 'awg', 10: 'azn', 11: 'bam', 12: 'b
bd', 13: 'bdt', 14: 'bgn', 15: 'bhd', 16: 'bif', 17: 'bmd', 18: 'bnd', 19: 'bob', 20: 'brl', 21: 'bsd', 22: 'btc', 23: 
'btn', 24: 'bwp', 25: 'byn', 26: 'byr', 27: 'bzd', 28: 'cad', 29: 'cdf', 30: 'chf', 31: 'clf', 32: 'clp', 33: 'cny', 34
: 'cop', 35: 'crc', 36: 'cuc', 37: 'cup', 38: 'cve', 39: 'czk', 40: 'djf', 41: 'dkk', 42: 'dop', 43: 'dzd', 44: 'egp', 
45: 'ern', 46: 'etb', 47: 'eth', 48: 'eur', 49: 'fjd', 50: 'fkp', 51: 'gbp', 52: 'gel', 53: 'ggp', 54: 'ghs', 55: 'gip'
, 56: 'gmd', 57: 'gnf', 58: 'gtq', 59: 'gyd', 60: 'hkd', 61: 'hnl', 62: 'hrk', 63: 'htg', 64: 'huf', 65: 'idr', 66: 'ils', 67: 'imp', 68: 'inr', 69: 'iqd', 70: 'irr', 71: 'isk', 72: 'jep', 73: 'jmd', 74: 'jod', 75: 'jpy', 76: 'kes', 77: 'kgs', 78: 'khr', 79: 'kmf', 80: 'kpw', 81: 'krw', 82: 'kwd', 83: 'kyd', 84: 'kzt', 85: 'lak', 86: 'lbp', 87: 'lkr', 88: 'lrd', 89: 'lsl', 90: 'ltl', 91: 'lvl', 92: 'lyd', 93: 'mad', 94: 'mdl', 95: 'mga', 96: 'mkd', 97: 'mmk', 98: 'mnt', 99: 'mop', 100: 'mro', 101: 'mur', 102: 'mvr', 103: 'mwk', 104: 'mxn', 105: 'myr', 106: 'mzn', 107: 'nad', 108: 'ngn', 109: 'nio', 110: 'nok', 111: 'npr', 112: 'nzd', 113: 'omr', 114: 'pab', 115: 'pen', 116: 'pgk', 117: 'php', 118: 'pkr', 119: 'pln', 120: 'pyg', 121: 'qar', 122: 'ron', 123: 'rsd', 124: 'rub', 125: 'rwf', 126: 'sar', 127: 'sbd', 128: 'scr', 129: 'sdg', 130: 'sek', 131: 'sgd', 132: 'shp', 133: 'sll', 134: 'sos', 135: 'srd', 136: 'std', 137: 'svc', 138: 'syp', 139: 'szl', 140: 'thb', 141: 'tjs', 142: 'tmt', 143: 'tnd', 144: 'top', 145: 'try', 146: 'ttd', 147: 'twd', 148: 'tzs', 149: 'uah', 150: 'ugx', 151: 'usd', 152: 'uyu', 153: 'uzs', 154: 'vef', 155: 'vnd', 156: 'vuv', 157: 'wst', 158: 'xaf', 159: 'xag', 160: 'xau', 161: 'xcd', 162: 'xdr', 163: 'xof', 164: 'xpf', 165: 'xrp', 166: 'yer', 167: 'zar', 168: 'zmk', 169: 'zmw', 170: 'zwl'}

JS-NG> fake.cur2id                                                                                                     
{'aed': 1, 'afn': 2, 'all': 3, 'amd': 4, 'ang': 5, 'aoa': 6, 'ars': 7, 'aud': 8, 'awg': 9, 'azn': 10, 'bam': 11, 'bbd':
 12, 'bdt': 13, 'bgn': 14, 'bhd': 15, 'bif': 16, 'bmd': 17, 'bnd': 18, 'bob': 19, 'brl': 20, 'bsd': 21, 'btc': 22, 'btn
': 23, 'bwp': 24, 'byn': 25, 'byr': 26, 'bzd': 27, 'cad': 28, 'cdf': 29, 'chf': 30, 'clf': 31, 'clp': 32, 'cny': 33, 'c
op': 34, 'crc': 35, 'cuc': 36, 'cup': 37, 'cve': 38, 'czk': 39, 'djf': 40, 'dkk': 41, 'dop': 42, 'dzd': 43, 'egp': 44, 
'ern': 45, 'etb': 46, 'eth': 47, 'eur': 48, 'fjd': 49, 'fkp': 50, 'gbp': 51, 'gel': 52, 'ggp': 53, 'ghs': 54, 'gip': 55
, 'gmd': 56, 'gnf': 57, 'gtq': 58, 'gyd': 59, 'hkd': 60, 'hnl': 61, 'hrk': 62, 'htg': 63, 'huf': 64, 'idr': 65, 'ils': 66, 'imp': 67, 'inr': 68, 'iqd': 69, 'irr': 70, 'isk': 71, 'jep': 72, 'jmd': 73, 'jod': 74, 'jpy': 75, 'kes': 76, 'kgs': 77, 'khr': 78, 'kmf': 79, 'kpw': 80, 'krw': 81, 'kwd': 82, 'kyd': 83, 'kzt': 84, 'lak': 85, 'lbp': 86, 'lkr': 87, 'lrd': 88, 'lsl': 89, 'ltl': 90, 'lvl': 91, 'lyd': 92, 'mad': 93, 'mdl': 94, 'mga': 95, 'mkd': 96, 'mmk': 97, 'mnt': 98, 'mop': 99, 'mro': 100, 'mur': 101, 'mvr': 102, 'mwk': 103, 'mxn': 104, 'myr': 105, 'mzn': 106, 'nad': 107, 'ngn': 108, 'nio': 109, 'nok': 110, 'npr': 111, 'nzd': 112, 'omr': 113, 'pab': 114, 'pen': 115, 'pgk': 116, 'php': 117, 'pkr': 118, 'pln': 119, 'pyg': 120, 'qar': 121, 'ron': 122, 'rsd': 123, 'rub': 124, 'rwf': 125, 'sar': 126, 'sbd': 127, 'scr': 128, 'sdg': 129, 'sek': 130, 'sgd': 131, 'shp': 132, 'sll': 133, 'sos': 134, 'srd': 135, 'std': 136, 'svc': 137, 'syp': 138, 'szl': 139, 'thb': 140, 'tjs': 141, 'tmt': 142, 'tnd': 143, 'top': 144, 'try': 145, 'ttd': 146, 'twd': 147, 'tzs': 148, 'uah': 149, 'ugx': 150, 'usd': 151, 'uyu': 152, 'uzs': 153, 'vef': 154, 'vnd': 155, 'vuv': 156, 'wst': 157, 'xaf': 158, 'xag': 159, 'xau': 160, 'xcd': 161, 'xdr': 162, 'xof': 163, 'xpf': 164, 'xrp': 165, 'yer': 166, 'zar': 167, 'zmk': 168, 'zmw': 169, 'zwl': 170}

JS-NG>                                                                                                                 
JS-NG> fake.api_key="VALID KEY"                                                                 
JS-NG> j.clients.currencylayer.fake.load()                                                                             
JS-NG> j.clients.currencylayer.fake.id2cur_print()                                                                     
{1: 'aed',
 2: 'afn',
 3: 'all',
 4: 'amd',
 5: 'ang',
 6: 'aoa',
 7: 'ars',
 8: 'aud',
 9: 'awg',
 10: 'azn',
 11: 'bam',
 12: 'bbd',
 13: 'bdt',
 14: 'bgn',
 15: 'bhd',
 16: 'bif',
 17: 'bmd',
 18: 'bnd',
 19: 'bob',
 20: 'brl',
 21: 'bsd',
 22: 'btc',
 23: 'btn',
 24: 'bwp',
 25: 'byn',
 26: 'byr',
 27: 'bzd',
 28: 'cad',
 29: 'cdf',
 30: 'chf',
 31: 'clf',
 32: 'clp',
 33: 'cny',
 34: 'cop',
 35: 'crc',
 36: 'cuc',
 37: 'cup',
 38: 'cve',
 39: 'czk',
 40: 'djf',
 41: 'dkk',
 42: 'dop',
 43: 'dzd',
 44: 'egp',
 45: 'ern',
 46: 'etb',
 47: 'eth',
 48: 'eur',
 49: 'fjd',
 50: 'fkp',
 51: 'gbp',
 52: 'gel',
 53: 'ggp',
 54: 'ghs',
 55: 'gip',
 56: 'gmd',
 57: 'gnf',
 58: 'gtq',
 59: 'gyd',
 60: 'hkd',
 61: 'hnl',
 62: 'hrk',
 63: 'htg',
 64: 'huf',
 65: 'idr',
 66: 'ils',
 67: 'imp',
 68: 'inr',
 69: 'iqd',
 70: 'irr',
 71: 'isk',
 72: 'jep',
 73: 'jmd',
 74: 'jod',
 75: 'jpy',
 76: 'kes',
 77: 'kgs',
 78: 'khr',
 79: 'kmf',
 80: 'kpw',
 81: 'krw',
 82: 'kwd',
 83: 'kyd',
 84: 'kzt',
 85: 'lak',
 86: 'lbp',
 87: 'lkr',
 88: 'lrd',
 89: 'lsl',
 90: 'ltl',
 91: 'lvl',
 92: 'lyd',
 93: 'mad',
 94: 'mdl',
 95: 'mga',
 96: 'mkd',
 97: 'mmk',
 98: 'mnt',
 99: 'mop',
 100: 'mro',
 101: 'mur',
 102: 'mvr',
 103: 'mwk',
 104: 'mxn',
 105: 'myr',
 106: 'mzn',
 107: 'nad',
 108: 'ngn',
 109: 'nio',
 110: 'nok',
 111: 'npr',
 112: 'nzd',
 113: 'omr',
 114: 'pab',
 115: 'pen',
 116: 'pgk',
 117: 'php',
 118: 'pkr',
 119: 'pln',
 120: 'pyg',
 121: 'qar',
 122: 'ron',
 123: 'rsd',
 124: 'rub',
 125: 'rwf',
 126: 'sar',
 127: 'sbd',
 128: 'scr',
 129: 'sdg',
 130: 'sek',
 131: 'sgd',
 132: 'shp',
 133: 'sll',
 134: 'sos',
 135: 'srd',
 136: 'std',
 137: 'svc',
 138: 'syp',
 139: 'szl',
 140: 'thb',
 141: 'tjs',
 142: 'tmt',
 143: 'tnd',
 144: 'top',
 145: 'try',
 146: 'ttd',
 147: 'twd',
 148: 'tzs',
 149: 'uah',
 150: 'ugx',
 151: 'usd',
 152: 'uyu',
 153: 'uzs',
 154: 'vef',
 155: 'vnd',
 156: 'vuv',
 157: 'wst',
 158: 'xaf',
 159: 'xag',
 160: 'xau',
 161: 'xcd',
 162: 'xdr',
 163: 'xof',
 164: 'xpf',
 165: 'xrp',
 166: 'yer',
 167: 'zar',
 168: 'zmk',
 169: 'zmw',
 170: 'zwl'}
JS-NG> j.clients.currencylayer.fake.cur2usd_print()                                                                    
{'': 1,
 'aed': 3.672979,
 'afn': 78.296617,
 'ah': 24.914996,
 'all': 109.150047,
 'amd': 476.210221,
 'ang': 1.78525,
 'aoa': 362.0025,
 'ar': 3.75045,
 'ars': 55.394992,
 'aud': 1.474703,
 'awg': 1.8,
 'azn': 1.704964,
 'bam': 1.758993,
 'bbd': 2.0194,
 'bd': 8.221403,
 'bdt': 83.745499,
 'bgn': 1.760801,
 'bhd': 0.375961,
 'bif': 1855,
 'bmd': 1,
 'bnd': 1.350696,
 'bob': 6.86065,
 'brl': 4.152695,
 'bsd': 0.99205,
 'btc': 9.948852946999476e-05,
 'btn': 71.884502,
 'bwp': 10.961999,
 'byn': 2.060501,
 'byr': 19600,
 'bzd': 2.01595,
 'cad': 1.32733,
 'cdf': 1659.99946,
 'chf': 0.978545,
 'clf': 0.026094,
 'clp': 720.00501,
 'cny': 7.151304,
 'cop': 3431.55,
 'cr': 13.669974,
 'crc': 567.080062,
 'cuc': 1,
 'cup': 26.5,
 'cve': 98.749501,
 'czk': 23.208988,
 'egp': 16.53602,
 'ek': 9.67235,
 'ern': 14.999484,
 'etb': 29.000284,
 'eth': 0.005395489370885939,
 'eur': 0.900035,
 'fjd': 2.17495,
 'fkp': 0.81691,
 'g': 45.119039,
 'gbp': 0.81752,
 'gd': 1.38792,
 'gel': 2.925034,
 'ggp': 0.81764,
 'ghs': 5.402501,
 'gip': 0.81691,
 'gmd': 50.415037,
 'gnf': 9239.999966,
 'gtq': 7.680957,
 'gx': 3685.496424,
 'gyd': 209.244968,
 'hkd': 7.84595,
 'hnl': 24.674984,
 'hp': 1.320898,
 'hrk': 6.653399,
 'htg': 95.361503,
 'huf': 296.280997,
 'idr': 14258.25,
 'ils': 3.52095,
 'imp': 0.81764,
 'inr': 71.792403,
 'iqd': 1190,
 'irr': 42104.999481,
 'isk': 124.829491,
 'jep': 0.81764,
 'jf': 177.720165,
 'jmd': 134.559965,
 'jod': 0.7084,
 'jpy': 106.015996,
 'kes': 103.389937,
 'kgs': 69.8159,
 'khr': 4140.000279,
 'kk': 6.71151,
 'kmf': 443.249767,
 'kpw': 900.052015,
 'krw': 1214.824979,
 'kwd': 0.303901,
 'kyd': 0.83355,
 'kzt': 383.110385,
 'lak': 8735.000017,
 'lbp': 1507.949729,
 'lkr': 179.605474,
 'll': 9299.999946,
 'lrd': 205.000232,
 'lsl': 15.250149,
 'ltl': 2.95274,
 'lvl': 0.60489,
 'lyd': 1.40503,
 'mad': 9.5685,
 'mdl': 17.887498,
 'mga': 3674.999563,
 'mkd': 55.324023,
 'mmk': 1516.702673,
 'mnt': 2669.391245,
 'mop': 8.080496,
 'mro': 357.000024,
 'mur': 36.043506,
 'mvr': 15.410297,
 'mwk': 731.210149,
 'mxn': 19.92145,
 'myr': 4.198897,
 'mzn': 61.020166,
 'nad': 15.270055,
 'ngn': 362.000148,
 'nio': 33.602406,
 'nok': 8.988065,
 'npr': 115.010199,
 'nzd': 1.56365,
 'omr': 0.384976,
 'op': 51.294983,
 'os': 579.999893,
 'pab': 0.99205,
 'pen': 3.37635,
 'pgk': 3.397801,
 'php': 52.438012,
 'pkr': 157.249855,
 'pln': 3.92254,
 'pyg': 6217.103241,
 'qar': 3.64175,
 'rd': 7.457963,
 'ron': 4.256202,
 'rsd': 106.069758,
 'rub': 66.06102,
 'rwf': 910,
 'td': 21560.79,
 'thb': 30.589849,
 'tjs': 9.696302,
 'tmt': 3.5,
 'tnd': 2.857701,
 'top': 2.320597,
 'try': 5.81132,
 'ttd': 6.71695,
 'twd': 31.400972,
 'tzs': 2298.149889,
 'vc': 8.75195,
 'vef': 9.987501,
 'vnd': 23199,
 'vuv': 117.90362,
 'wst': 2.675215,
 'xaf': 589.959986,
 'xag': 0.056555,
 'xau': 0.000653,
 'xcd': 2.70245,
 'xdr': 0.729108,
 'xof': 584.499865,
 'xpf': 106.950279,
 'xrp': 3.771,
 'yer': 250.349819,
 'yp': 515.000236,
 'yu': 36.34003,
 'zar': 15.26498,
 'zd': 119.879946,
 'zl': 15.269489,
 'zmk': 9001.202171,
 'zmw': 13.112024,
 'zs': 9376.306597,
 'zwl': 322.000001}


"""