from next_biggest_number import next_biggest_number
def test_simple_cases():
    assert(next_biggest_number(12,2) == 21)
    assert(next_biggest_number(123,3) == 132)
    assert(next_biggest_number(67809,5) == 67890)


def test_simple_cases_no_solution():
    assert(next_biggest_number(21,2) == -1)
    assert(next_biggest_number(54321,5) == -1)


def test_52210():
    assert(next_biggest_number(52210,5) == -1)


def test_95701():
    assert(next_biggest_number(95701,5) == 95710)


def test_71305():
    assert(next_biggest_number(71305,5) == 71350)


def test_6358():
    assert(next_biggest_number(6358,4) == 6385)


def test_25437():
    assert(next_biggest_number(25437,5) == 25473)


def test_49893():
    assert(next_biggest_number(49893,5) == 49938)


def test_76778():
    assert(next_biggest_number(76778,5) == 76787)


def test_2372():
    assert(next_biggest_number(2372,4) == 2723)


def test_45071():
    assert(next_biggest_number(45071,5) == 45107)


def test_31233():
    assert(next_biggest_number(31233,5) == 31323)


def test_50401():
    assert(next_biggest_number(50401,5) == 50410)


def test_57067():
    assert(next_biggest_number(57067,5) == 57076)


def test_40272():
    assert(next_biggest_number(40272,5) == 40722)


def test_54998():
    assert(next_biggest_number(54998,5) == 58499)


def test_22437():
    assert(next_biggest_number(22437,5) == 22473)


def test_53510():
    assert(next_biggest_number(53510,5) == 55013)


def test_78263():
    assert(next_biggest_number(78263,5) == 78326)


def test_42661():
    assert(next_biggest_number(42661,5) == 46126)


def test_45118():
    assert(next_biggest_number(45118,5) == 45181)


def test_26075():
    assert(next_biggest_number(26075,5) == 26507)


def test_93932():
    assert(next_biggest_number(93932,5) == 99233)


def test_84252():
    assert(next_biggest_number(84252,5) == 84522)


def test_33203():
    assert(next_biggest_number(33203,5) == 33230)


def test_98037():
    assert(next_biggest_number(98037,5) == 98073)


def test_74041():
    assert(next_biggest_number(74041,5) == 74104)


def test_11856():
    assert(next_biggest_number(11856,5) == 11865)


def test_47998():
    assert(next_biggest_number(47998,5) == 48799)


def test_36708():
    assert(next_biggest_number(36708,5) == 36780)


def test_93802():
    assert(next_biggest_number(93802,5) == 93820)


def test_2902():
    assert(next_biggest_number(2902,4) == 2920)


def test_71116():
    assert(next_biggest_number(71116,5) == 71161)


def test_76532():
    assert(next_biggest_number(76532,5) == -1)


def test_81848():
    assert(next_biggest_number(81848,5) == 81884)


def test_93493():
    assert(next_biggest_number(93493,5) == 93934)


def test_16332():
    assert(next_biggest_number(16332,5) == 21336)


def test_97939():
    assert(next_biggest_number(97939,5) == 97993)


def test_4386():
    assert(next_biggest_number(4386,4) == 4638)


def test_6950():
    assert(next_biggest_number(6950,4) == 9056)


def test_92232():
    assert(next_biggest_number(92232,5) == 92322)


def test_39527():
    assert(next_biggest_number(39527,5) == 39572)


def test_41766():
    assert(next_biggest_number(41766,5) == 46167)


def test_3399():
    assert(next_biggest_number(3399,4) == 3939)


def test_77957():
    assert(next_biggest_number(77957,5) == 77975)


def test_81899():
    assert(next_biggest_number(81899,5) == 81989)


def test_2403():
    assert(next_biggest_number(2403,4) == 2430)


def test_23817():
    assert(next_biggest_number(23817,5) == 23871)


def test_85520():
    assert(next_biggest_number(85520,5) == -1)


def test_42882():
    assert(next_biggest_number(42882,5) == 48228)


def test_56072():
    assert(next_biggest_number(56072,5) == 56207)


def test_89101():
    assert(next_biggest_number(89101,5) == 89110)


def test_25384():
    assert(next_biggest_number(25384,5) == 25438)


def test_54443():
    assert(next_biggest_number(54443,5) == -1)


def test_49459():
    assert(next_biggest_number(49459,5) == 49495)


def test_84803():
    assert(next_biggest_number(84803,5) == 84830)


def test_50766():
    assert(next_biggest_number(50766,5) == 56067)


def test_43770():
    assert(next_biggest_number(43770,5) == 47037)


def test_33285():
    assert(next_biggest_number(33285,5) == 33528)


def test_42083():
    assert(next_biggest_number(42083,5) == 42308)


def test_47482():
    assert(next_biggest_number(47482,5) == 47824)


def test_45634():
    assert(next_biggest_number(45634,5) == 45643)


def test_73784():
    assert(next_biggest_number(73784,5) == 73847)


def test_97071():
    assert(next_biggest_number(97071,5) == 97107)


def test_81003():
    assert(next_biggest_number(81003,5) == 81030)


def test_32619():
    assert(next_biggest_number(32619,5) == 32691)


def test_36448():
    assert(next_biggest_number(36448,5) == 36484)


def test_22368():
    assert(next_biggest_number(22368,5) == 22386)


def test_22794():
    assert(next_biggest_number(22794,5) == 22947)


def test_58927():
    assert(next_biggest_number(58927,5) == 58972)


def test_73399():
    assert(next_biggest_number(73399,5) == 73939)


def test_81830():
    assert(next_biggest_number(81830,5) == 83018)


def test_49685():
    assert(next_biggest_number(49685,5) == 49856)


def test_73251():
    assert(next_biggest_number(73251,5) == 73512)


def test_44595():
    assert(next_biggest_number(44595,5) == 44955)


def test_81165():
    assert(next_biggest_number(81165,5) == 81516)


def test_85034():
    assert(next_biggest_number(85034,5) == 85043)


def test_31814():
    assert(next_biggest_number(31814,5) == 31841)


def test_79768():
    assert(next_biggest_number(79768,5) == 79786)


def test_88439():
    assert(next_biggest_number(88439,5) == 88493)


def test_44697():
    assert(next_biggest_number(44697,5) == 44769)


def test_52821():
    assert(next_biggest_number(52821,5) == 58122)


def test_80263():
    assert(next_biggest_number(80263,5) == 80326)


def test_71049():
    assert(next_biggest_number(71049,5) == 71094)


def test_91362():
    assert(next_biggest_number(91362,5) == 91623)


def test_17056():
    assert(next_biggest_number(17056,5) == 17065)


def test_26130():
    assert(next_biggest_number(26130,5) == 26301)


def test_83800():
    assert(next_biggest_number(83800,5) == 88003)


def test_52246():
    assert(next_biggest_number(52246,5) == 52264)


def test_56996():
    assert(next_biggest_number(56996,5) == 59669)


def test_30281():
    assert(next_biggest_number(30281,5) == 30812)


def test_51428():
    assert(next_biggest_number(51428,5) == 51482)


def test_7654():
    assert(next_biggest_number(7654,4) == -1)


def test_33095():
    assert(next_biggest_number(33095,5) == 33509)


def test_50933():
    assert(next_biggest_number(50933,5) == 53039)


def test_7558():
    assert(next_biggest_number(7558,4) == 7585)


def test_75659():
    assert(next_biggest_number(75659,5) == 75695)


def test_36639():
    assert(next_biggest_number(36639,5) == 36693)


def test_75517():
    assert(next_biggest_number(75517,5) == 75571)


def test_64149():
    assert(next_biggest_number(64149,5) == 64194)


def test_44926():
    assert(next_biggest_number(44926,5) == 44962)


def test_16230():
    assert(next_biggest_number(16230,5) == 16302)


def test_36166():
    assert(next_biggest_number(36166,5) == 36616)


def test_14134():
    assert(next_biggest_number(14134,5) == 14143)


def test_66848():
    assert(next_biggest_number(66848,5) == 66884)


def test_85420():
    assert(next_biggest_number(85420,5) == -1)


def test_6447():
    assert(next_biggest_number(6447,4) == 6474)


def test_70690():
    assert(next_biggest_number(70690,5) == 70906)


def test_55511():
    assert(next_biggest_number(55511,5) == -1)


def test_55224():
    assert(next_biggest_number(55224,5) == 55242)


def test_73239():
    assert(next_biggest_number(73239,5) == 73293)


def test_21166():
    assert(next_biggest_number(21166,5) == 21616)


def test_69958():
    assert(next_biggest_number(69958,5) == 69985)


def test_59609():
    assert(next_biggest_number(59609,5) == 59690)


def test_28850():
    assert(next_biggest_number(28850,5) == 50288)


def test_34085():
    assert(next_biggest_number(34085,5) == 34508)


def test_68686():
    assert(next_biggest_number(68686,5) == 68866)


def test_30015():
    assert(next_biggest_number(30015,5) == 30051)


def test_95116():
    assert(next_biggest_number(95116,5) == 95161)


def test_68150():
    assert(next_biggest_number(68150,5) == 68501)


def test_80403():
    assert(next_biggest_number(80403,5) == 80430)


def test_32154():
    assert(next_biggest_number(32154,5) == 32415)


def test_34731():
    assert(next_biggest_number(34731,5) == 37134)


def test_18099():
    assert(next_biggest_number(18099,5) == 18909)


def test_13447():
    assert(next_biggest_number(13447.5) == 13474)


def test_56296():
    assert(next_biggest_number(56296,5) == 56629)


def test_1276():
    assert(next_biggest_number(1276,4) == 1627)


def test_44944():
    assert(next_biggest_number(44944,5) == 49444)


def test_75519():
    assert(next_biggest_number(75519,5) == 75591)


def test_45632():
    assert(next_biggest_number(45632,5) == 46235)


def test_27590():
    assert(next_biggest_number(27590,5) == 27905)


def test_7251():
    assert(next_biggest_number(7251,4) == 7512)


def test_90251():
    assert(next_biggest_number(90251,5) == 90512)


def test_98728():
    assert(next_biggest_number(98728,5) == 98782)


def test_51811():
    assert(next_biggest_number(51811,5) == 58111)


def test_59358():
    assert(next_biggest_number(59358,5) == 59385)


def test_24098():
    assert(next_biggest_number(24098,5) == 24809)


def test_59176():
    assert(next_biggest_number(59176,5) == 59617)


def test_54917():
    assert(next_biggest_number(54917,5) == 54971)


def test_8165():
    assert(next_biggest_number(8165,4) == 8516)


def test_34178():
    assert(next_biggest_number(34178,5) == 34187)


def test_71652():
    assert(next_biggest_number(71652,5) == 72156)


def test_26168():
    assert(next_biggest_number(26168,5) == 26186)


def test_49396():
    assert(next_biggest_number(49396,5) == 49639)


def test_78946():
    assert(next_biggest_number(78946,5) == 78964)


def test_33316():
    assert(next_biggest_number(33316,5) == 33361)


def test_15484():
    assert(next_biggest_number(15484,5) == 15844)


def test_2211():
    assert(next_biggest_number(2211,4) == -1)


def test_97203():
    assert(next_biggest_number(97203,5) == 97230)


def test_70956():
    assert(next_biggest_number(70956,5) == 70965)


