print("\n~~~~~~~~ GENSHIN AR EXP CALCULATOR ~~~~~~~~")
my_ar = int(input("Enter your current AR Level: "))
if my_ar < 12:
    print("Please enter level 12 or above AR..")
else:
    my_xp = int(input("Enter your current AR Exp amount: "))
    reqd_ar = int(input("Enter your desired AR Level: "))
    ar_table = {
        12:	10525,
        13:	12175,
        14:	13950,
        15:	15825,
        16:	17825,
        17:	20200,
        18:	22700,
        19:	25325,
        20:	28100,
        21:	30925,
        22:	34350,
        23:	38075,
        24:	42075,
        25:	46375,
        26:	50950,
        27:	55825,
        28:	60975,
        29:	66425,
        30:	72150,
        31:	78175,
        32:	84475,
        33:	91075,
        34:	97975,
        35:	105150,
        36:	112625,
        37:	120375,
        38:	128425,
        39:	136750,
        40: 145375,
        41: 155925,
        42: 167450,
        43: 179925,
        44: 193375,
        45: 207775,
        46: 223125,
        47: 239450,
        48: 256725,
        49: 274975,
        50: 294175,
        51: 320575,
        52: 349375,
        53: 380575,
        54: 414175,
        55: 450175,
        56: 682525,
    }
    
    resin_usage_per_day = 180
    xp_per_20_resin = 100
    
    resin_xp_per_day = resin_usage_per_day / 20 * xp_per_20_resin
    daily_comm_xp = 500 + (4*250)
    
    xp_gain_per_day = daily_comm_xp + resin_xp_per_day
    total_reqd = ar_table[reqd_ar] - ar_table[my_ar] - my_xp
    
    print("Total AR Exp required to reach level ",reqd_ar, ": ", total_reqd)
    print("Estimated days required to reach goal AR: ",total_reqd / xp_gain_per_day)

input("Press any key to continue...")