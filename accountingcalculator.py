class Factors():
    def __init__(self):
        self.pv_table = {1: [0.9901,0.9803,0.9706,0.9610,0.9515,0.9420,0.9327,0.9235,0.9143,0.9053,0.8963,0.8874,0.8787,0.8700,0.8613,0.8195,0.7798,0.7419,0.7059,0.6717,0.6391],
                    2: [0.9804,0.9612,0.9423,0.9238,0.9057,0.8880,0.8706,0.8535,0.8368,0.8203,0.8043,0.7885,0.7730,0.7579,0.7430,0.673,0.6095,0.5521,0.5,0.4529,0.4102],
                    3: [0.9709,0.9426,0.9151,0.8885,0.8626,0.8375,0.8131,0.7894,0.7664,0.7441,0.7224,0.7014,0.6810,0.6611,0.6419,0.5537,0.4776,0.412,0.3554,0.3066,0.2644],
                    4: [0.9615,0.9246,0.8890,0.8548,0.8219,0.7903,0.7599,0.7307,0.7026,0.6756,0.6496,0.6246,0.6006,0.5775,0.5553,0.4564,0.3751,0.3083,0.2534,0.2083,0.1712],
                    5: [0.9524,0.9070,0.8638,0.8227,0.7835,0.7462,0.7107,0.6768,0.6446,0.6139,0.5847,0.5568,0.5303,0.5051,0.4810,0.3769,0.2953,0.2314,0.1813,0.142,0.1113],
                    6: [0.9434,0.8900,0.8396,0.7921,0.7473,0.7050,0.6651,0.6274,0.5919,0.5584,0.5268,0.4970,0.4688,0.4423,0.4173,0.3118,0.233,0.1741,0.1301,0.0972,0.0727],
                    7: [0.9346,0.8734,0.8163,0.7629,0.7130,0.6663,0.6227,0.5820,0.5439,0.5083,0.4751,0.4440,0.4150,0.3878,0.3624,0.2584,0.1842,0.1314,0.0937,0.0668,0.0476],
                    8: [0.9259,0.8573,0.7938,0.7350,0.6806,0.6302,0.5835,0.5403,0.5002,0.4632,0.4289,0.3971,0.3677,0.3405,0.3152,0.2145,0.146,0.0994,0.0676,0.046,0.0313],
                    9: [0.9174,0.8417,0.7722,0.7084,0.6499,0.5963,0.5470,0.5019,0.4604,0.4224,0.3875,0.3555,0.3262,0.2992,0.2745,0.1784,0.116,0.0754,0.049,0.0318,0.0207],
                    10:[0.9091,0.8264,0.7513,0.6830,0.6209,0.5645,0.5132,0.4665,0.4241,0.3855,0.3505,0.3186,0.2897,0.2633,0.2394,0.1486,0.0923,0.0573,0.0356,0.0221,0.0137]}
        self.fv_table = {1: [1.01,1.0201,1.0303,1.0406,1.051,1.0615,1.0721,1.0829,1.0937,1.1046,1.1157,1.1268,1.1381,1.1495,1.161,1.2202,1.2824,1.3478,1.4166,1.4889,1.5648],
                    2: [1.02,1.0404,1.0612,1.0824,1.1041,1.1262,1.1487,1.1717,1.1951,1.219,1.2434,1.2682,1.2936,1.3195,1.3459,1.4859,1.6406,1.8114,1.9999,2.208,2.4379],
                    3: [1.03,1.0609,1.0927,1.1255,1.1593,1.1941,1.2299,1.2668,1.3048,1.3439,1.3842,1.4258,1.4685,1.5126,1.558,1.8061,2.0938,2.4273,2.8139,3.262,3.7816],
                    4: [1.04,1.0816,1.1249,1.1699,1.2167,1.2653,1.3159,1.3686,1.4233,1.4802,1.5395,1.601,1.6651,1.7317,1.8009,2.1911,2.6658,3.2434,3.9461,4.801,5.8412],
                    5: [1.05,1.1025,1.1576,1.2155,1.2763,1.3401,1.4071,1.4775,1.5513,1.6289,1.7103,1.7959,1.8856,1.9799,2.0789,2.6533,3.3864,4.3219,5.516,7.04,8.985],
                    6: [1.06,1.1236,1.191,1.2625,1.3382,1.4185,1.5036,1.5938,1.6895,1.7908,1.8983,2.0122,2.1329,2.2609,2.3966,3.2071,4.2919,5.7435,7.6861,10.2857,13.7646],
                    7: [1.07,1.1449,1.225,1.3108,1.4026,1.5007,1.6058,1.7182,1.8385,1.9672,2.1049,2.2522,2.4098,2.5785,2.759,3.8697,5.4274,7.6123,10.6766,14.9745,21.0025],
                    8: [1.08,1.1664,1.2597,1.3605,1.4693,1.5869,1.7138,1.8509,1.999,2.1589,2.3316,2.5182,2.7196,2.9372,3.1722,4.661,6.8485,10.0627,14.7853,21.7245,31.9204],
                    9: [1.09,1.1881,1.295,1.4116,1.5386,1.6771,1.828,1.9926,2.1719,2.3674,2.5804,2.8127,3.0658,3.3417,3.6425,5.6044,8.6231,13.2677,20.414,31.4094,48.3273],
                    10: [1.1,1.21,1.331,1.4641,1.6105,1.7716,1.9487,2.1436,2.3579,2.5937,2.8531,3.1384,3.4523,3.7975,4.1772,6.7275,10.8347,17.4494,28.1024,45.2593,72.8905]}
        self.pva_table = {1: [0.9901,1.9704,2.941,3.902,4.8534,5.7955,6.7282,7.6517,8.566,9.4713,10.3676,11.2551,12.1337,13.0037,13.8651,18.0456,22.0232,25.8077,29.4086,32.8347,36.0945], 																																													 								
                     2: [0.9804,1.9416,2.8839,3.8077,4.7135,5.6014,6.472,7.3255,8.1622,8.9826,9.7868,10.5753,11.3484,12.1062,12.8493,16.3514,19.5235,22.3965,24.9986,27.3555,29.4902],
                     3: [0.9709,1.9135,2.8286,3.7171,4.5797,5.4172,6.2303,7.0197,7.7861,8.5302,9.2526,9.954,10.635,11.2961,11.9379,14.8775,17.4131,19.6004,21.4872,23.1148,24.5187],
                     4: [0.9615,1.8861,2.7751,3.6299,4.4518,5.2421,6.0021,6.7327,7.4353,8.1109,8.7605,9.3851,9.9856,10.5631,11.1184,13.5903,15.6221,17.292,18.6646,19.7928,20.72],
                     5: [0.9524,1.8594,2.7232,3.546,4.3295,5.0757,5.7864,6.4632,7.1078,7.7217,8.3064,8.8633,9.3936,9.8986,10.3797,12.4622,14.0939,15.3725,16.3742,17.1591,17.7741],
                     6: [0.9434,1.8334,2.673,3.4651,4.2124,4.9173,5.5824,6.2098,6.8017,7.3601,7.8869,8.3838,8.8527,9.295,9.7122,11.4699,12.7834,13.7648,14.4982,15.0463,15.4558],
                     7: [0.9346,1.808,2.6243,3.3872,4.1002,4.7665,5.3893,5.9713,6.5152,7.0236,7.4987,7.9427,8.3577,8.7455,9.1079,10.594,11.6536,12.409,12.9477,13.3317,13.6055],
                     8: [0.9259,1.7833,2.5771,3.3121,3.9927,4.6229,5.2064,5.7466,6.2469,6.7101,7.139,7.5361,7.9038,8.2442,8.5595,9.8181,10.6748,11.2578,11.6546,11.9246,12.1084],
                     9: [0.9174,1.7591,2.5313,3.2397,3.8897,4.4859,5.033,5.5348,5.9952,6.4177,6.8052,7.1607,7.4869,7.7862,8.0607,9.1285,9.8226,10.2737,10.5668,10.7574,10.8812],
                     10:[0.9091,1.7355,2.4869,3.1699,3.7908,4.3553,4.8684,5.3349,5.759,6.1446,6.4951,6.8137,7.1034,7.3667,7.6061,8.5136,9.077,9.4269,9.6442,9.7791,9.8628]}
        self.fva_table = {1: [1,2.01,3.0301,4.0604,5.101,6.152,7.2135,8.2857,9.3685,10.4622,11.5668,12.6825,13.8093,14.9474,16.0969,22.019,28.2432,34.7849,41.6603,48.8864,56.4811],
                     2: [1,2.02,3.0604,4.1216,5.204,6.3081,7.4343,8.583,9.7546,10.9497,12.1687,13.4121,14.6803,15.9739,17.2934,24.2974,32.0303,40.5681,49.9945,60.402,71.8927],
                     3: [1,2.03,3.0909,4.1836,5.3091,6.4684,7.6625,8.8923,10.1591,11.4639,12.8078,14.192,15.6178,17.0863,18.5989,26.8704,36.4593,47.5754,60.4621,75.4013,92.7199], 																																									
                     4: [1,2.04,3.1216,4.2465,5.4163,6.633,7.8983,9.2142,10.5828,12.0061,13.4864,15.0258,16.6268,18.2919,20.0236,29.7781,41.6459,56.0849,73.6522,95.0255,121.0294],
                     5: [1,2.05,3.1525,4.3101,5.5256,6.8019,8.142,9.5491,11.0266,12.5779,14.2068,15.9171,17.713,19.5986,21.5786,33.066,47.7271,66.4388,90.3203,120.7998,159.7002],
                     6: [1,2.06,3.1836,4.3746,5.6371,6.9753,8.3938,9.8975,11.4913,13.1808,14.9716,16.8699,18.8821,21.0151,23.276,36.7856,54.8645,79.0582,111.4348,154.762,212.7435],
                     7: [1,2.07,3.2149,4.4399,5.7507,7.1533,8.654,10.2598,11.978,13.8164,15.7836,17.8885,20.1406,22.5505,25.129,40.9955,63.249,94.4608,138.2369,199.6351,285.7493],
                     8: [1,2.08,3.2464,4.5061,5.8666,7.3359,8.9228,10.6366,12.4876,14.4866,16.6455,18.9771,21.4953,24.2149,27.1521,45.762,73.1059,113.2832,172.3168,259.0565,386.5056],
                     9: [1,2.09,3.2781,4.5731,5.9847,7.5233,9.2004,11.0285,13.021,15.1929,17.5603,20.1407,22.9534,26.0192,29.3609,51.1601,84.7009,136.3075,215.7108,337.8824,525.8587],
                     10: [1,2.1,3.31,4.641,6.1051,7.7156,9.4872,11.4359,13.5795,15.9374,18.5312,21.3843,24.5227,27.975,31.7725,57.275,98.3471,164.494,271.0244,442.5926,718.9048]}
                     
def exam2calc():
    print("Choose calculator:")
    print("1. Cash payback")
    print("2. NPV")
    print("3. PV")
    print("4. FV")
    print("5. PVa")
    print("6. FVa ")
    print("7. Find Factor")
    print("8. Cost Variance\n")
    option = int(input())
    
    if option == 1:
        cash_payback()
    if option == 2:
        npv()
    if option == 3:
        pv()
    if option == 4:
        fv()
    if option == 5:
        pva()
    if option == 6:
        fva()  
    if option == 7:
        find_factor()
    if option == 8:
        cost_variance()
    
def cash_payback():
    flow = []
    cash_flow = 0
    year_count = 0
    leftover = 0
    
    print("You've chosen the Cash Payback calculator!")
    print("Enter amount to pay back:", end = " ")
    payback_amt = int(input())
    print("Enter number of years to pay back:", end = " ")
    years = int(input())
    
    for i in range(years):
        print("Enter cash flow for year" + str(i+1) + ":", end = " ")
        flow.append(int(input()))
    
    while (cash_flow <= payback_amt) and (year_count <= years):
        if cash_flow == payback_amt:
            print(str(year_count))
        cash_flow += flow[year_count]
        year_count += 1 
    
    result = (year_count - 1) + (1 - (cash_flow - payback_amt) / flow[year_count - 1])
    print("\n Your cash payback period is: " + str(result))
    
def npv():
    flow = []
    npv = 0
    pv_table = Factors().pv_table
    print("You've chosen the NPV calculator!")
    print("Enter interest rate %:", end = " ")
    interest = int(input())
    print("Enter project cost (the negative amount you begin with):", end = " ")
    npv = int(input())
    #print("Enter any down payment (put 0 if none):", end = " ")
    #down_payment = int(input())
    print("Enter number of years of cash inflow:", end = " ")
    years = int(input())

    for i in range(years):
        print("Enter cash flow for year " + str(i+1) + ":", end = " ")
        npv = npv - float(int(input()) * pv_table[interest][i])

    print("\n Your NPV is " + str(-npv))
        
def pv():
    pv_table = Factors().pv_table
    print("You've chosen the PV calculator!")
    print("Enter your Future Value:", end = " ")
    fv = int(input())
    print("Enter interest rate %:", end = " ")
    interest = int(input())
    print("Enter number of years:", end = " ")
    years = convert_year(int(input()))
    print("\n Your PV is " + str(float(fv * pv_table[interest][years - 1])))
    
def fv():
    fv_table = Factors().fv_table
    print("You've chosen the FV calculator!")
    print("Enter your Present Value:", end = " ")
    pv = int(input())
    print("Enter interest rate %:", end = " ")
    interest = int(input())
    print("Enter number of years:", end = " ")
    years = convert_year(int(input()))
    print("\n Your FV is " + str(float(pv * fv_table[interest][years - 1])))
    
def pva():
    pva_table = Factors().pva_table
    print("You've chosen the PVa calculator!")
    print("Which value is given?")
    print("1. Present Value annuity")
    print("2. Annuity Amount")
    option = int(input())
    if option == 1:
        print("Enter your Present Value annuity:", end = " ")
        pva = int(input())
    if option == 2:
        print("Enter your Annuity Amount:", end = " ")
        aa = int(input())
    print("Enter interest rate %:", end = " ")
    interest = int(input())
    print("Enter number of years:", end = " ")
    years = convert_year(int(input()))
        
    if option == 1:
        print("\n Your Annuity Amount is " + str(float(pva / pva_table[interest][years - 1])))
    if option == 2:
        print("\n Your Present Value annuity is " + str(float(aa * pva_table[interest][years - 1])))
    
def fva():
    fva_table = Factors().fva_table
    print("You've chosen the FVa calculator!")
    print("Which value is given?")
    print("1. Future Value annuity")
    print("2. Annuity Amount")
    option = int(input())
    if option == 1:
        print("Enter your Future Value annuity:", end = " ")
        fva = int(input())
    if option == 2:
        print("Enter your Annuity Amount:", end = " ")
        aa = int(input())
    print("Enter interest rate %:", end = " ")
    interest = int(input())
    print("Enter number of years:", end = " ")
    years = convert_year(int(input()))
    
    if option == 1:
        print("\n Your Annuity Amount is " + str(float(fva / fva_table[interest][years - 1])))
    if option == 2:
        print("\n Your Future Value annuity is " + str(float(aa * fva_table[interest][years - 1])))
    
def find_factor():
    pv_table = Factors().pv_table
    fv_table = Factors().fv_table
    pva_table = Factors().pva_table
    fva_table = Factors().fva_table
    
    print("What factor do you want to find?")
    print("1.PV \n2.FV \n3.PVa \n4.FVa")
    option = int(input())
    print("\nWhat's your interest rate %?", end = " ")
    interest = int(input())
    print("How many years?", end = " ")
    original_year = int(input())
    years = convert_year(original_year)
    if option == 1:
        print("\nThe Factor for PV %" + str(interest) + " n=" + str(original_year) + " is " + str(pv_table[interest][years - 1]))
    if option == 2:
        print("\nThe Factor for FV %" + str(interest) + " n=" + str(original_year) + " is " + str(fv_table[interest][years - 1]))
    if option == 3:
        print("\nThe Factor for PVa %" + str(interest) + " n=" + str(original_year) + " is " + str(pva_table[interest][years - 1]))
    if option == 4:
        print("\nThe Factor for FVa %" + str(interest) + " n=" + str(original_year) + " is " + str(fva_table[interest][years - 1]))

def convert_year(year):
    if year == 20:
        return 16
    if year == 25:
        return 17
    if year == 30:
        return 18
    if year == 35:
        return 19
    if year == 40:
        return 20
    if year == 45:
        return 21
    else:
        return year
        
def cost_variance():
    print("You've chosen the Cost Variance calculator!\n Which cost would you like to calculate?\n1.DM\n2.DL")
    option = int(input())
    
    if option == 1:
        print("\nYou want to calculate for Direct Materials.\nPlease enter the standards in this format: \n N M where N is the lbs and M is the price per lb.")
    if option == 2:
        print("\nYou want to calculate for Direct Labor.\nPlease enter the standards in this format: \n N M where N is the hour and M is the price per hour.")
    
    standard_quantity, standard_price = map(float,input().split())
    
    print("Great! Now let's define the actual amount.\n Enter actual production (units):", end = " ")
    actual_prod = int(input())
    
    if option == 1:
        print("Enter actual quantity (lbs) used in production:", end = " ")
        actual_quantity = float(input())
        print("Enter actual price per pound:", end = " ")
        input_string = str(input())
        if "/" in input_string:
            a, b = map(float, input_string.split("/"))
            actual_price = float(a / b)
        else: 
            actual_price = float(input_string)
    if option == 2:
        print("Enter actual quantity (hours) used in production:", end = " ")
        actual_quantity = float(input())
        print("Enter actual price per hour:", end = " ")
        input_string = str(input())
        if "/" in input_string:
            a, b = map(float, input_string.split("/"))
            actual_price = float(a / b)
        else: 
            actual_price = float(input_string)
        
    actual_result = float(actual_quantity * actual_price)
    standard_result = float(actual_prod * standard_quantity * standard_price)
    middle = float(actual_quantity * standard_price)
    cost_variance = float(middle - actual_result)
    quantity_variance = float(standard_result - middle )
    total = float(cost_variance + quantity_variance)
    
    print("\nActual Result: " + str(actual_result))
    print("Standard Result: " + str(standard_result))
    print("Middle: " + str(middle))
    print("Cost Variance: " + str(cost_variance))
    print("Quantity Variance: " + str(quantity_variance))
    print("Total: " + str(total))
    
if __name__ == '__main__':
    exam2calc()