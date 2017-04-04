import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import triple_exponential_moving_average


class TestTripleExponentialMovingAverage(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.tema_period_6_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, 798.76868511742964, 791.31445543619179, 777.79446854131652,
        774.12964798538781, 764.49177561595423, 760.854469009887,
        769.29345723051767, 783.50202832652883, 788.3973969667926,
        785.67697103872615, 783.55727190438392, 785.8549703871065,
        785.49544515085847, 778.14524225807384, 782.40423979599086,
        780.75436379909752, 776.75637242708922, 759.32256404774444,
        764.6745663288475, 774.50690897656239, 796.34862781176616,
        811.22826194014112, 810.34480579901378, 795.04870256480649,
        785.96965369360237, 785.44389424248527, 796.02258297005164,
        804.5940390247888, 816.40556621467067, 821.36414224331998,
        825.63932535639117, 830.51909429529326, 835.68997538166514,
        829.02016142305467, 823.20339287806291, 824.71271592358164,
        821.54590374253257, 809.79900781506421, 802.9402152981437,
        801.17332611150755, 806.63461082987612, 807.87793098575219,
        812.37747940310965, 805.95863998447714, 804.28258982740761,
        802.08465340763314, 801.65912292790279, 800.14522397751875,
        801.93152502750149, 802.92704790862672, 808.29550555473429,
        811.22974074633476, 806.45575030361363, 812.65925500080129,
        815.77624656944022, 809.41280759847837, 802.05074389489641,
        795.77476149223776, 795.65785912075398, 797.57937568979071,
        791.52796649348943, 788.67399843930491, 795.03282870198143,
        791.1679571229505, 799.11345484807657, 806.16484998042438,
        809.81283824645243, 803.08209554857933, 794.87100819820637,
        790.64536066635981, 789.36958361421875, 791.8036983438202,
        791.79926483811221, 791.57154811312489, 793.41053040916677,
        796.33790467690346, 797.54932805268072, 799.47674017464044,
        802.50921773320329, 805.63761781778851, 803.63315025497354,
        805.5476836164919, 807.04600048900102, 808.19770046996052,
        808.62438098826908, 807.90337376195635, 806.2522559108794,
        806.31085020503963, 799.62897995058154, 797.80027607201953,
        798.17123114144829, 799.35140637542281, 793.59175170087269,
        773.15031796065477, 762.07472268636297, 754.78761483485539,
        752.51878547054207, 753.97413385862592, 752.96086516572097,
        756.4582962452572, 755.5746165034484, 754.91671147251043,
        741.98375675230659, 735.86128747083899, 729.37965931720271,
        728.97538531070745, 726.11841775538778, 718.83630386118614,
        709.7801879908933, 707.11789689461955, 704.04654889030201,
        706.64506392899125]

        self.tema_period_8_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        765.2007636014539, 777.18974413800697, 783.23515875617795,
        783.48510595954929, 783.48568670766292, 786.33130416873587,
        788.13885500275558, 783.2458941497249, 785.21126759997969,
        781.7265329124649, 777.22833229262528, 762.21724845708593,
        764.94768766575487, 771.73425926058565, 791.01465379344222,
        806.37189529655063, 808.00643311098906, 796.16532519593284,
        789.60052011261746, 790.39320212211157, 799.25870599593782,
        806.18712164416695, 814.0975048387761, 816.96798967223708,
        821.87241142591608, 829.2930685086535, 836.8324335548233,
        833.0072341527333, 827.59200302694376, 827.18179366035145,
        822.99238683728379, 812.22546121923858, 804.7835433825984,
        800.5623474465167, 803.18557748585886, 805.00859480248926,
        809.37191584079039, 803.88584325641023, 802.71878259328332,
        802.03223860289756, 802.63291298231525, 801.49487619144486,
        802.47464182692045, 802.43361931419611, 806.56116579577781,
        810.14736835177405, 807.00366788193014, 812.35062693153316,
        815.69947146117158, 811.02959153512791, 804.72130042392121,
        798.55849609288498, 796.24769492384564, 797.23832472811284,
        792.33187698441384, 788.03850634797698, 792.04825048225553,
        789.4265792291153, 796.88703837847231, 804.48903007208867,
        808.41657099386225, 803.50755334371888, 797.79604372681206,
        793.38769607500262, 791.36742645351308, 793.31494606917897,
        792.11584113256458, 790.2921112469196, 790.97513181893225,
        794.0973296752818, 796.46526756714456, 799.35877712455056,
        802.46468877424377, 805.34604938379357, 804.37644659830914,
        806.39732384579565, 807.73792040462638, 808.75608997938264,
        809.30441396168681, 808.69630193759929, 806.7376899569947,
        806.45383463598205, 800.91788397078074, 798.52865608837135,
        798.08227510871473, 798.54610028385798, 793.42157877320847,
        775.80598480320577, 764.07616771350342, 755.58397615001684,
        752.31153991673136, 752.35035633619168, 750.36200854241702,
        751.58016055733367, 751.40475650650308, 753.06003207957576,
        743.75521271658772, 738.66309455472822, 732.12862524029777,
        730.32807271953664, 726.85263573815382, 719.49880983350363,
        709.82060199910518, 705.99893671214124, 703.24349045475844,
        705.31824752411217]

        self.tema_period_10_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, 786.53726959981645, 783.43102751223853,
        786.97250500775499, 785.62765584075214, 781.23353412363406,
        766.36920334979027, 766.61442697651023, 771.7445376479925,
        788.15532010876018, 801.60927191026963, 804.9726971551969,
        796.53389429985623, 790.64169054019703, 790.2087940853819,
        798.6962034434049, 807.27558102230159, 815.99272425065851,
        819.46248992931112, 822.23361390867967, 826.73108016737206,
        833.60601854870106, 832.80012496741051, 830.23728849004283,
        830.42317203997311, 826.39661301407352, 816.092070490438,
        807.93736375770845, 802.97787049426086, 803.89980778136601,
        803.5662691582213, 805.87475536408681, 801.77666401225292,
        800.86166548738845, 799.40494941920326, 799.93229856726725,
        800.08598580228625, 802.17626338422792, 802.79012290815831,
        806.4582423607236, 809.25164663106295, 806.57162599008564,
        811.75068763126444, 815.22951458003513, 811.74721034271624,
        806.4847807191228, 800.89896342116481, 798.42279674418319,
        798.7118994707655, 793.18150391264112, 788.97914196787201,
        792.17952274404695, 788.60840431538327, 793.92189073853115,
        800.8811988333008, 805.67559026940523, 803.15316943813082,
        798.34316559547619, 794.15605054131208, 793.09240631882449,
        794.4103796152823, 793.34656942308993, 792.28961826068416,
        791.95296586132372, 793.15939681832526, 794.34772955252834,
        797.2542172315832, 800.94753363356483, 804.57291423887955,
        804.40268251713303, 806.26641124217372, 807.95949071805819,
        809.50318384390198, 810.22664468246899, 809.75623795444142,
        808.09584074879922, 807.62205528751645, 802.20936865863644,
        799.50054599600185, 798.77948585015429, 798.62784213064037,
        793.81859472213398, 777.98591545281261, 766.2608147117528,
        757.28572356722668, 752.41680754085564, 750.97515669309519,
        748.97538430095346, 749.64244348336013, 748.80836635183869,
        748.70896136684155, 740.77839482150773, 737.51815298690246,
        732.57282818616386, 731.33190959585613, 728.03248870181892,
        721.24957816560448, 712.14534599323895, 707.41893772160972,
        703.0652526505728, 703.54743710223204]

    def test_triple_exponential_moving_average_period_6(self):
        period = 6
        tema = triple_exponential_moving_average.triple_exponential_moving_average(self.data, period)
        np.testing.assert_array_equal(tema, self.tema_period_6_expected)

    def test_triple_exponential_moving_average_period_8(self):
        period = 8
        tema = triple_exponential_moving_average.triple_exponential_moving_average(self.data, period)
        np.testing.assert_array_equal(tema, self.tema_period_8_expected)

    def test_triple_exponential_moving_average_period_10(self):
        period = 10
        tema = triple_exponential_moving_average.triple_exponential_moving_average(self.data, period)
        np.testing.assert_array_equal(tema, self.tema_period_10_expected)

    def test_triple_exponential_moving_average_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            triple_exponential_moving_average.triple_exponential_moving_average(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)
