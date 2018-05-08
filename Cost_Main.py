from cvxpy import *
import numpy

std = input('Do you use the Metric system or Imperial? (M or I) ')
if(std == 'M'):
	wkg = float(input('What is you weight in kilograms? '))
	wlb = wkg*2.2046226218
	height = float(input('What is you height in meters? '))
elif(std == 'I'):
	wlb = float(input('What is you weight in pounds? '))
	wkg = wlb/2.2046226218
	print('Input your height: ')
	h_ft = int(input('Feet: '))
	h_inch = int(input('Inches: '))
	h_inch += h_ft * 12
	height = (h_inch * 2.54)/100
age = float(input('How old are you? '))
sex = input('What is your sex? (M or F) ')
if(sex == "M"):
	DCI = 864 - 9.72 * age + (14.2 * wkg + 503 * height)
elif(sex == "F"):
	DCI = 387 - 7.31 * age + (10.9 * wkg + 660.7 * height)
print('Metric weight is: ' +str(round(wkg,2)) + ' kg')
print('Metric height is: ' +str(round(height,2)) + ' m')
print('Daily Caloric intake: '+str(round(DCI,2))+' calories')

# Name, Price, Protein, Carbs, Fat, Calories 
Scb = [0.006613873261,0.2955,0,0.0772,1.95] #Skinless Chicken Breast
Grb = [0.0154103247,0.2535,0,0.1858,2.76] #Ground Beef
Rfb = [0.004679682769,0.046875,0.140625,0.01953125,0.9375] #Refried Beans
Tfu = [0.005706930206,0.069,0.024,0.027,0.62] #Tofu
Egg = [0.1231062276,0.13,0.01,0.1,1.43] #Egg
Apl = [0.002821919258,0,0.3,0,0.8] #Apple
Crt = [0.001741653292,0.01,0.1,0,0.41] #Carrots
Ptc = [40.01100107586,0.0656,0.4974,0.3747,5.47] #Potato Chips
Grp = [0.002175229428,0.01,0.05,0,0.2] #Green Pepper
Lfy = [0.006613873261,0.0294,0.0882,0,0.4706] #Light nonfat Yogurt
Pnt = [0.008796451437,0.2803,0.1526,0.525,5.99] #Peanuts
Ach = [30.01759290287,0.1894,0.0694,0.2605,3.37] #American Cheese
Tcc = [0.02641140055,0.289,0,0.0702,1.87] #Turkey Cold Cut
Hcc = [0.008796451437,0.1826,0.0228,0.0839,1.62] #Ham Cold Cut
Wwb = [0.005864300958,0.0913,0.4714,0.0411,2.59] #Whole Wheat Bread
Whr = [0.007029602437,0.0266,0.279,0.0028,1.29] #White Rice
Brr = [0.007029602437,0.0256,0.2278,0.0089,1.1] #Brown Rice
Oin = [0.001829838269,0.0092,0.1011,0,0.42] #Onion
Rpt = [0.001532213972,0.0232,0.2006,0.07,1.49] #Roasted Potato
Whm = [0.001469387755,0.0322,0.0452,0.0325,0.6] #Whole Milk
Ces = [0.01075856717,0.1184,0.74,0.059,3.69] #Cheerios
Bcn = [0.0154103247,0.37,0.0143,0.4178,5.41] #Bacon
Ban = [0.001058219722,0.0109,0.2284,0.0033,0.89] #Banana
Let = [0.005487065224,0.009,0.0297,0.0014,0.14] #Lettuce
Brc = [0.005961304432,0.0282,0.0664,0.0037,0.34] #Broccoli
Btr = [0.0154103247,0.0085,0,0.8111,7.17] #Butter

ScbV = Variable()
GrbV = Variable()
RfbV = Variable()
TfuV = Variable()
EggV = Variable()
AplV = Variable()
CrtV = Variable()
PtcV = Variable()
GrpV = Variable()
LfyV = Variable()
PntV = Variable()
AchV = Variable()
TccV = Variable()
HccV = Variable()
WwbV = Variable()
WhrV = Variable()
BrrV = Variable()
OinV = Variable()
RptV = Variable()
WhmV = Variable()
CesV = Variable()
BcnV = Variable()
BanV = Variable()
LetV = Variable()
BrcV = Variable() 
BtrV = Variable()

default = [0 <= ScbV, ScbV <= 453,
0 <= GrbV,
0 <= RfbV,
0 <= TfuV, 
0 <= EggV,
0 <= AplV,
0 <= CrtV,
0 <= PtcV,
0 <= GrpV,
0 <= LfyV,
0 <= PntV,
0 <= AchV,
0 <= TccV, TccV <= 155,
0 <= HccV, HccV <= 155,
0 <= WwbV,
0 <= WhrV,
0 <= BrrV,
0 <= OinV,
0 <= RptV,
0 <= WhmV,
0 <= CesV,
0 <= BcnV,
0 <= BanV,
0 <= LetV,
0 <= BrcV,
0 <= BtrV]

diet = input("Please select your diet (Paleo = P, Atkins = A, Keto = K, Zone = Z) ")

if(diet == "P"):
	if(sex == "M"):
		constraints = [0.7*(wlb-20) <= Scb[1]*ScbV + Grb[1]*GrbV + Rfb[1]*RfbV + Tfu[1]*TfuV + Egg[1]*EggV + Apl[1]*AplV + Crt[1]*CrtV + Ptc[1]*PtcV + Grp[1]*GrpV 
		+ Lfy[1]*LfyV + Pnt[1]*PntV + Ach[1]*AchV +Tcc[1]*TccV + Hcc[1]*HccV + Wwb[1]*WwbV + Whr[1]*WhrV + Whr[1]*WhrV + Brr[1]*BrrV + Oin[1]*OinV + Rpt[1]*RptV 
		+ Whm[1]*WhmV + Ces[1]*CesV + Bcn[1]*BcnV + Ban[1]*BanV + Let[1]*LetV + Brc[1]*BrcV + Btr[1]*BtrV,
		wlb >= Scb[1]*ScbV + Grb[1]*GrbV + Rfb[1]*RfbV + Tfu[1]*TfuV + Egg[1]*EggV + Apl[1]*AplV + Crt[1]*CrtV + Ptc[1]*PtcV + Grp[1]*GrpV
		+ Lfy[1]*LfyV + Pnt[1]*PntV + Ach[1]*AchV +Tcc[1]*TccV + Hcc[1]*HccV + Wwb[1]*WwbV + Whr[1]*WhrV + Whr[1]*WhrV + Brr[1]*BrrV + Oin[1]*OinV + Rpt[1]*RptV 
		+ Whm[1]*WhmV + Ces[1]*CesV + Bcn[1]*BcnV + Ban[1]*BanV + Let[1]*LetV + Brc[1]*BrcV + Btr[1]*BtrV,
		50 <= Scb[2]*ScbV + Grb[2]*GrbV + Rfb[2]*RfbV + Tfu[2]*TfuV + Egg[2]*EggV + Apl[2]*AplV + Crt[2]*CrtV + Ptc[2]*PtcV + Grp[2]*GrpV
		+ Lfy[2]*LfyV + Pnt[2]*PntV + Ach[2]*AchV +Tcc[2]*TccV + Hcc[2]*HccV + Wwb[2]*WwbV + Whr[2]*WhrV + Whr[2]*WhrV + Brr[2]*BrrV + Oin[2]*OinV + Rpt[2]*RptV 
		+ Whm[2]*WhmV + Ces[2]*CesV + Bcn[2]*BcnV + Ban[2]*BanV + Let[2]*LetV + Brc[2]*BrcV + Btr[2]*BtrV,
		100 >= Scb[2]*ScbV + Grb[2]*GrbV + Rfb[2]*RfbV + Tfu[2]*TfuV + Egg[2]*EggV + Apl[2]*AplV + Crt[2]*CrtV + Ptc[2]*PtcV + Grp[2]*GrpV
		+ Lfy[2]*LfyV + Pnt[2]*PntV + Ach[2]*AchV +Tcc[2]*TccV + Hcc[2]*HccV + Wwb[2]*WwbV + Whr[2]*WhrV + Whr[2]*WhrV + Brr[2]*BrrV + Oin[2]*OinV + Rpt[2]*RptV 
		+ Whm[2]*WhmV + Ces[2]*CesV + Bcn[2]*BcnV + Ban[2]*BanV + Let[2]*LetV + Brc[2]*BrcV + Btr[2]*BtrV,
		80 <= Scb[3]*ScbV + Grb[3]*GrbV + Rfb[3]*RfbV + Tfu[3]*TfuV + Egg[3]*EggV + Apl[3]*AplV + Crt[3]*CrtV + Ptc[3]*PtcV + Grp[3]*GrpV
		+ Lfy[3]*LfyV + Pnt[3]*PntV + Ach[3]*AchV +Tcc[3]*TccV + Hcc[3]*HccV + Wwb[3]*WwbV + Whr[3]*WhrV + Whr[3]*WhrV + Brr[3]*BrrV + Oin[3]*OinV + Rpt[3]*RptV 
		+ Whm[3]*WhmV + Ces[3]*CesV + Bcn[3]*BcnV + Ban[3]*BanV + Let[3]*LetV + Brc[3]*BrcV + Btr[3]*BtrV,
		120 >= Scb[3]*ScbV + Grb[3]*GrbV + Rfb[3]*RfbV + Tfu[3]*TfuV + Egg[3]*EggV + Apl[3]*AplV + Crt[3]*CrtV + Ptc[3]*PtcV + Grp[3]*GrpV
		+ Lfy[3]*LfyV + Pnt[3]*PntV + Ach[3]*AchV +Tcc[3]*TccV + Hcc[3]*HccV + Wwb[3]*WwbV + Whr[3]*WhrV + Whr[3]*WhrV + Brr[3]*BrrV + Oin[3]*OinV + Rpt[3]*RptV 
		+ Whm[3]*WhmV + Ces[3]*CesV + Bcn[3]*BcnV + Ban[3]*BanV + Let[3]*LetV + Brc[3]*BrcV + Btr[3]*BtrV] + default
	elif(sex =="F"):
		constraints = [0.7*(wlb-25) <= Scb[1]*ScbV + Grb[1]*GrbV + Rfb[1]*RfbV + Tfu[1]*TfuV + Egg[1]*EggV + Apl[1]*AplV + Crt[1]*CrtV + Ptc[1]*PtcV + Grp[1]*GrpV 
		+ Lfy[1]*LfyV + Pnt[1]*PntV + Ach[1]*AchV +Tcc[1]*TccV + Hcc[1]*HccV + Wwb[1]*WwbV + Whr[1]*WhrV + Whr[1]*WhrV + Brr[1]*BrrV + Oin[1]*OinV + Rpt[1]*RptV 
		+ Whm[1]*WhmV + Ces[1]*CesV + Bcn[1]*BcnV + Ban[1]*BanV + Let[1]*LetV + Brc[1]*BrcV + Btr[1]*BtrV,
		wlb >= Scb[1]*ScbV + Grb[1]*GrbV + Rfb[1]*RfbV + Tfu[1]*TfuV + Egg[1]*EggV + Apl[1]*AplV + Crt[1]*CrtV + Ptc[1]*PtcV + Grp[1]*GrpV
		+ Lfy[1]*LfyV + Pnt[1]*PntV + Ach[1]*AchV +Tcc[1]*TccV + Hcc[1]*HccV + Wwb[1]*WwbV + Whr[1]*WhrV + Whr[1]*WhrV + Brr[1]*BrrV + Oin[1]*OinV + Rpt[1]*RptV 
		+ Whm[1]*WhmV + Ces[1]*CesV + Bcn[1]*BcnV + Ban[1]*BanV + Let[1]*LetV + Brc[1]*BrcV + Btr[1]*BtrV,
		50 <= Scb[2]*ScbV + Grb[2]*GrbV + Rfb[2]*RfbV + Tfu[2]*TfuV + Egg[2]*EggV + Apl[2]*AplV + Crt[2]*CrtV + Ptc[2]*PtcV + Grp[2]*GrpV
		+ Lfy[2]*LfyV + Pnt[2]*PntV + Ach[2]*AchV +Tcc[2]*TccV + Hcc[2]*HccV + Wwb[2]*WwbV + Whr[2]*WhrV + Whr[2]*WhrV + Brr[2]*BrrV + Oin[2]*OinV + Rpt[2]*RptV 
		+ Whm[2]*WhmV + Ces[2]*CesV + Bcn[2]*BcnV + Ban[2]*BanV + Let[2]*LetV + Brc[2]*BrcV + Btr[2]*BtrV,
		100 >= Scb[2]*ScbV + Grb[2]*GrbV + Rfb[2]*RfbV + Tfu[2]*TfuV + Egg[2]*EggV + Apl[2]*AplV + Crt[2]*CrtV + Ptc[2]*PtcV + Grp[2]*GrpV
		+ Lfy[2]*LfyV + Pnt[2]*PntV + Ach[2]*AchV +Tcc[2]*TccV + Hcc[2]*HccV + Wwb[2]*WwbV + Whr[2]*WhrV + Whr[2]*WhrV + Brr[2]*BrrV + Oin[2]*OinV + Rpt[2]*RptV 
		+ Whm[2]*WhmV + Ces[2]*CesV + Bcn[2]*BcnV + Ban[2]*BanV + Let[2]*LetV + Brc[2]*BrcV + Btr[2]*BtrV,
		80 <= Scb[3]*ScbV + Grb[3]*GrbV + Rfb[3]*RfbV + Tfu[3]*TfuV + Egg[3]*EggV + Apl[3]*AplV + Crt[3]*CrtV + Ptc[3]*PtcV + Grp[3]*GrpV
		+ Lfy[3]*LfyV + Pnt[3]*PntV + Ach[3]*AchV +Tcc[3]*TccV + Hcc[3]*HccV + Wwb[3]*WwbV + Whr[3]*WhrV + Whr[3]*WhrV + Brr[3]*BrrV + Oin[3]*OinV + Rpt[3]*RptV 
		+ Whm[3]*WhmV + Ces[3]*CesV + Bcn[3]*BcnV + Ban[3]*BanV + Let[3]*LetV + Brc[3]*BrcV + Btr[3]*BtrV,
		120 >= Scb[3]*ScbV + Grb[3]*GrbV + Rfb[3]*RfbV + Tfu[3]*TfuV + Egg[3]*EggV + Apl[3]*AplV + Crt[3]*CrtV + Ptc[3]*PtcV + Grp[3]*GrpV
		+ Lfy[3]*LfyV + Pnt[3]*PntV + Ach[3]*AchV +Tcc[3]*TccV + Hcc[3]*HccV + Wwb[3]*WwbV + Whr[3]*WhrV + Whr[3]*WhrV + Brr[3]*BrrV + Oin[3]*OinV + Rpt[3]*RptV 
		+ Whm[3]*WhmV + Ces[3]*CesV + Bcn[3]*BcnV + Ban[3]*BanV + Let[3]*LetV + Brc[3]*BrcV + Btr[3]*BtrV] + default
elif(diet == "A"):
	constraints = [340 <= Scb[1]*ScbV + Grb[1]*GrbV + Rfb[1]*RfbV + Tfu[1]*TfuV + Egg[1]*EggV + Apl[1]*AplV + Crt[1]*CrtV + Ptc[1]*PtcV + Grp[1]*GrpV 
	+ Lfy[1]*LfyV + Pnt[1]*PntV + Ach[1]*AchV +Tcc[1]*TccV + Hcc[1]*HccV + Wwb[1]*WwbV + Whr[1]*WhrV + Whr[1]*WhrV + Brr[1]*BrrV + Oin[1]*OinV + Rpt[1]*RptV 
	+ Whm[1]*WhmV + Ces[1]*CesV + Bcn[1]*BcnV + Ban[1]*BanV + Let[1]*LetV + Brc[1]*BrcV + Btr[1]*BtrV,
	520 >= Scb[1]*ScbV + Grb[1]*GrbV + Rfb[1]*RfbV + Tfu[1]*TfuV + Egg[1]*EggV + Apl[1]*AplV + Crt[1]*CrtV + Ptc[1]*PtcV + Grp[1]*GrpV
	+ Lfy[1]*LfyV + Pnt[1]*PntV + Ach[1]*AchV +Tcc[1]*TccV + Hcc[1]*HccV + Wwb[1]*WwbV + Whr[1]*WhrV + Whr[1]*WhrV + Brr[1]*BrrV + Oin[1]*OinV + Rpt[1]*RptV 
	+ Whm[1]*WhmV + Ces[1]*CesV + Bcn[1]*BcnV + Ban[1]*BanV + Let[1]*LetV + Brc[1]*BrcV + Btr[1]*BtrV,
	18 <= Scb[2]*ScbV + Grb[2]*GrbV + Rfb[2]*RfbV + Tfu[2]*TfuV + Egg[2]*EggV + Apl[2]*AplV + Crt[2]*CrtV + Ptc[2]*PtcV + Grp[2]*GrpV
	+ Lfy[2]*LfyV + Pnt[2]*PntV + Ach[2]*AchV +Tcc[2]*TccV + Hcc[2]*HccV + Wwb[2]*WwbV + Whr[2]*WhrV + Whr[2]*WhrV + Brr[2]*BrrV + Oin[2]*OinV + Rpt[2]*RptV 
	+ Whm[2]*WhmV + Ces[2]*CesV + Bcn[2]*BcnV + Ban[2]*BanV + Let[2]*LetV + Brc[2]*BrcV + Btr[2]*BtrV,
	22 >= Scb[2]*ScbV + Grb[2]*GrbV + Rfb[2]*RfbV + Tfu[2]*TfuV + Egg[2]*EggV + Apl[2]*AplV + Crt[2]*CrtV + Ptc[2]*PtcV + Grp[2]*GrpV
	+ Lfy[2]*LfyV + Pnt[2]*PntV + Ach[2]*AchV +Tcc[2]*TccV + Hcc[2]*HccV + Wwb[2]*WwbV + Whr[2]*WhrV + Whr[2]*WhrV + Brr[2]*BrrV + Oin[2]*OinV + Rpt[2]*RptV 
	+ Whm[2]*WhmV + Ces[2]*CesV + Bcn[2]*BcnV + Ban[2]*BanV + Let[2]*LetV + Brc[2]*BrcV + Btr[2]*BtrV,
	120 <= Scb[3]*ScbV + Grb[3]*GrbV + Rfb[3]*RfbV + Tfu[3]*TfuV + Egg[3]*EggV + Apl[3]*AplV + Crt[3]*CrtV + Ptc[3]*PtcV + Grp[3]*GrpV
	+ Lfy[3]*LfyV + Pnt[3]*PntV + Ach[3]*AchV +Tcc[3]*TccV + Hcc[3]*HccV + Wwb[3]*WwbV + Whr[3]*WhrV + Whr[3]*WhrV + Brr[3]*BrrV + Oin[3]*OinV + Rpt[3]*RptV 
	+ Whm[3]*WhmV + Ces[3]*CesV + Bcn[3]*BcnV + Ban[3]*BanV + Let[3]*LetV + Brc[3]*BrcV + Btr[3]*BtrV,
	140 >= Scb[3]*ScbV + Grb[3]*GrbV + Rfb[3]*RfbV + Tfu[3]*TfuV + Egg[3]*EggV + Apl[3]*AplV + Crt[3]*CrtV + Ptc[3]*PtcV + Grp[3]*GrpV
	+ Lfy[3]*LfyV + Pnt[3]*PntV + Ach[3]*AchV +Tcc[3]*TccV + Hcc[3]*HccV + Wwb[3]*WwbV + Whr[3]*WhrV + Whr[3]*WhrV + Brr[3]*BrrV + Oin[3]*OinV + Rpt[3]*RptV 
	+ Whm[3]*WhmV + Ces[3]*CesV + Bcn[3]*BcnV + Ban[3]*BanV + Let[3]*LetV + Brc[3]*BrcV + Btr[3]*BtrV] + default
elif(diet == "K"):
	if(sex == "M"):
		constraints = [0.8*(wlb-20) <= Scb[1]*ScbV + Grb[1]*GrbV + Rfb[1]*RfbV + Tfu[1]*TfuV + Egg[1]*EggV + Apl[1]*AplV + Crt[1]*CrtV + Ptc[1]*PtcV + Grp[1]*GrpV 
		+ Lfy[1]*LfyV + Pnt[1]*PntV + Ach[1]*AchV +Tcc[1]*TccV + Hcc[1]*HccV + Wwb[1]*WwbV + Whr[1]*WhrV + Whr[1]*WhrV + Brr[1]*BrrV + Oin[1]*OinV + Rpt[1]*RptV 
		+ Whm[1]*WhmV + Ces[1]*CesV + Bcn[1]*BcnV + Ban[1]*BanV + Let[1]*LetV + Brc[1]*BrcV + Btr[1]*BtrV,
		(wlb-20) >= Scb[1]*ScbV + Grb[1]*GrbV + Rfb[1]*RfbV + Tfu[1]*TfuV + Egg[1]*EggV + Apl[1]*AplV + Crt[1]*CrtV + Ptc[1]*PtcV + Grp[1]*GrpV
		+ Lfy[1]*LfyV + Pnt[1]*PntV + Ach[1]*AchV +Tcc[1]*TccV + Hcc[1]*HccV + Wwb[1]*WwbV + Whr[1]*WhrV + Whr[1]*WhrV + Brr[1]*BrrV + Oin[1]*OinV + Rpt[1]*RptV 
		+ Whm[1]*WhmV + Ces[1]*CesV + Bcn[1]*BcnV + Ban[1]*BanV + Let[1]*LetV + Brc[1]*BrcV + Btr[1]*BtrV,
		30 <= Scb[2]*ScbV + Grb[2]*GrbV + Rfb[2]*RfbV + Tfu[2]*TfuV + Egg[2]*EggV + Apl[2]*AplV + Crt[2]*CrtV + Ptc[2]*PtcV + Grp[2]*GrpV
		+ Lfy[2]*LfyV + Pnt[2]*PntV + Ach[2]*AchV +Tcc[2]*TccV + Hcc[2]*HccV + Wwb[2]*WwbV + Whr[2]*WhrV + Whr[2]*WhrV + Brr[2]*BrrV + Oin[2]*OinV + Rpt[2]*RptV 
		+ Whm[2]*WhmV + Ces[2]*CesV + Bcn[2]*BcnV + Ban[2]*BanV + Let[2]*LetV + Brc[2]*BrcV + Btr[2]*BtrV,
		40 >= Scb[2]*ScbV + Grb[2]*GrbV + Rfb[2]*RfbV + Tfu[2]*TfuV + Egg[2]*EggV + Apl[2]*AplV + Crt[2]*CrtV + Ptc[2]*PtcV + Grp[2]*GrpV
		+ Lfy[2]*LfyV + Pnt[2]*PntV + Ach[2]*AchV +Tcc[2]*TccV + Hcc[2]*HccV + Wwb[2]*WwbV + Whr[2]*WhrV + Whr[2]*WhrV + Brr[2]*BrrV + Oin[2]*OinV + Rpt[2]*RptV 
		+ Whm[2]*WhmV + Ces[2]*CesV + Bcn[2]*BcnV + Ban[2]*BanV + Let[2]*LetV + Brc[2]*BrcV + Btr[2]*BtrV,
		60 <= Scb[3]*ScbV + Grb[3]*GrbV + Rfb[3]*RfbV + Tfu[3]*TfuV + Egg[3]*EggV + Apl[3]*AplV + Crt[3]*CrtV + Ptc[3]*PtcV + Grp[3]*GrpV
		+ Lfy[3]*LfyV + Pnt[3]*PntV + Ach[3]*AchV +Tcc[3]*TccV + Hcc[3]*HccV + Wwb[3]*WwbV + Whr[3]*WhrV + Whr[3]*WhrV + Brr[3]*BrrV + Oin[3]*OinV + Rpt[3]*RptV 
		+ Whm[3]*WhmV + Ces[3]*CesV + Bcn[3]*BcnV + Ban[3]*BanV + Let[3]*LetV + Brc[3]*BrcV + Btr[3]*BtrV,
		120 >= Scb[3]*ScbV + Grb[3]*GrbV + Rfb[3]*RfbV + Tfu[3]*TfuV + Egg[3]*EggV + Apl[3]*AplV + Crt[3]*CrtV + Ptc[3]*PtcV + Grp[3]*GrpV
		+ Lfy[3]*LfyV + Pnt[3]*PntV + Ach[3]*AchV +Tcc[3]*TccV + Hcc[3]*HccV + Wwb[3]*WwbV + Whr[3]*WhrV + Whr[3]*WhrV + Brr[3]*BrrV + Oin[3]*OinV + Rpt[3]*RptV 
		+ Whm[3]*WhmV + Ces[3]*CesV + Bcn[3]*BcnV + Ban[3]*BanV + Let[3]*LetV + Brc[3]*BrcV + Btr[3]*BtrV] + default
	elif(sex == "F"):
		constraints = [0.8*(wlb-25) <= Scb[1]*ScbV + Grb[1]*GrbV + Rfb[1]*RfbV + Tfu[1]*TfuV + Egg[1]*EggV + Apl[1]*AplV + Crt[1]*CrtV + Ptc[1]*PtcV + Grp[1]*GrpV 
		+ Lfy[1]*LfyV + Pnt[1]*PntV + Ach[1]*AchV +Tcc[1]*TccV + Hcc[1]*HccV + Wwb[1]*WwbV + Whr[1]*WhrV + Whr[1]*WhrV + Brr[1]*BrrV + Oin[1]*OinV + Rpt[1]*RptV 
		+ Whm[1]*WhmV + Ces[1]*CesV + Bcn[1]*BcnV + Ban[1]*BanV + Let[1]*LetV + Brc[1]*BrcV + Btr[1]*BtrV,
		(wlb-25) >= Scb[1]*ScbV + Grb[1]*GrbV + Rfb[1]*RfbV + Tfu[1]*TfuV + Egg[1]*EggV + Apl[1]*AplV + Crt[1]*CrtV + Ptc[1]*PtcV + Grp[1]*GrpV
		+ Lfy[1]*LfyV + Pnt[1]*PntV + Ach[1]*AchV +Tcc[1]*TccV + Hcc[1]*HccV + Wwb[1]*WwbV + Whr[1]*WhrV + Whr[1]*WhrV + Brr[1]*BrrV + Oin[1]*OinV + Rpt[1]*RptV 
		+ Whm[1]*WhmV + Ces[1]*CesV + Bcn[1]*BcnV + Ban[1]*BanV + Let[1]*LetV + Brc[1]*BrcV + Btr[1]*BtrV,
		30 <= Scb[2]*ScbV + Grb[2]*GrbV + Rfb[2]*RfbV + Tfu[2]*TfuV + Egg[2]*EggV + Apl[2]*AplV + Crt[2]*CrtV + Ptc[2]*PtcV + Grp[2]*GrpV
		+ Lfy[2]*LfyV + Pnt[2]*PntV + Ach[2]*AchV +Tcc[2]*TccV + Hcc[2]*HccV + Wwb[2]*WwbV + Whr[2]*WhrV + Whr[2]*WhrV + Brr[2]*BrrV + Oin[2]*OinV + Rpt[2]*RptV 
		+ Whm[2]*WhmV + Ces[2]*CesV + Bcn[2]*BcnV + Ban[2]*BanV + Let[2]*LetV + Brc[2]*BrcV + Btr[2]*BtrV,
		40 >= Scb[2]*ScbV + Grb[2]*GrbV + Rfb[2]*RfbV + Tfu[2]*TfuV + Egg[2]*EggV + Apl[2]*AplV + Crt[2]*CrtV + Ptc[2]*PtcV + Grp[2]*GrpV
		+ Lfy[2]*LfyV + Pnt[2]*PntV + Ach[2]*AchV +Tcc[2]*TccV + Hcc[2]*HccV + Wwb[2]*WwbV + Whr[2]*WhrV + Whr[2]*WhrV + Brr[2]*BrrV + Oin[2]*OinV + Rpt[2]*RptV 
		+ Whm[2]*WhmV + Ces[2]*CesV + Bcn[2]*BcnV + Ban[2]*BanV + Let[2]*LetV + Brc[2]*BrcV + Btr[2]*BtrV,
		60 <= Scb[3]*ScbV + Grb[3]*GrbV + Rfb[3]*RfbV + Tfu[3]*TfuV + Egg[3]*EggV + Apl[3]*AplV + Crt[3]*CrtV + Ptc[3]*PtcV + Grp[3]*GrpV
		+ Lfy[3]*LfyV + Pnt[3]*PntV + Ach[3]*AchV +Tcc[3]*TccV + Hcc[3]*HccV + Wwb[3]*WwbV + Whr[3]*WhrV + Whr[3]*WhrV + Brr[3]*BrrV + Oin[3]*OinV + Rpt[3]*RptV 
		+ Whm[3]*WhmV + Ces[3]*CesV + Bcn[3]*BcnV + Ban[3]*BanV + Let[3]*LetV + Brc[3]*BrcV + Btr[3]*BtrV,
		120 >= Scb[3]*ScbV + Grb[3]*GrbV + Rfb[3]*RfbV + Tfu[3]*TfuV + Egg[3]*EggV + Apl[3]*AplV + Crt[3]*CrtV + Ptc[3]*PtcV + Grp[3]*GrpV
		+ Lfy[3]*LfyV + Pnt[3]*PntV + Ach[3]*AchV +Tcc[3]*TccV + Hcc[3]*HccV + Wwb[3]*WwbV + Whr[3]*WhrV + Whr[3]*WhrV + Brr[3]*BrrV + Oin[3]*OinV + Rpt[3]*RptV 
		+ Whm[3]*WhmV + Ces[3]*CesV + Bcn[3]*BcnV + Ban[3]*BanV + Let[3]*LetV + Brc[3]*BrcV + Btr[3]*BtrV] + default
elif(diet == "Z"):
	if(sex == "M"):
		constraints = [105 <= Scb[1]*ScbV + Grb[1]*GrbV + Rfb[1]*RfbV + Tfu[1]*TfuV + Egg[1]*EggV + Apl[1]*AplV + Crt[1]*CrtV + Ptc[1]*PtcV + Grp[1]*GrpV 
		+ Lfy[1]*LfyV + Pnt[1]*PntV + Ach[1]*AchV +Tcc[1]*TccV + Hcc[1]*HccV + Wwb[1]*WwbV + Whr[1]*WhrV + Whr[1]*WhrV + Brr[1]*BrrV + Oin[1]*OinV + Rpt[1]*RptV 
		+ Whm[1]*WhmV + Ces[1]*CesV + Bcn[1]*BcnV + Ban[1]*BanV + Let[1]*LetV + Brc[1]*BrcV + Btr[1]*BtrV,
		115 >= Scb[1]*ScbV + Grb[1]*GrbV + Rfb[1]*RfbV + Tfu[1]*TfuV + Egg[1]*EggV + Apl[1]*AplV + Crt[1]*CrtV + Ptc[1]*PtcV + Grp[1]*GrpV
		+ Lfy[1]*LfyV + Pnt[1]*PntV + Ach[1]*AchV +Tcc[1]*TccV + Hcc[1]*HccV + Wwb[1]*WwbV + Whr[1]*WhrV + Whr[1]*WhrV + Brr[1]*BrrV + Oin[1]*OinV + Rpt[1]*RptV 
		+ Whm[1]*WhmV + Ces[1]*CesV + Bcn[1]*BcnV + Ban[1]*BanV + Let[1]*LetV + Brc[1]*BrcV + Btr[1]*BtrV,
		140 <= Scb[2]*ScbV + Grb[2]*GrbV + Rfb[2]*RfbV + Tfu[2]*TfuV + Egg[2]*EggV + Apl[2]*AplV + Crt[2]*CrtV + Ptc[2]*PtcV + Grp[2]*GrpV
		+ Lfy[2]*LfyV + Pnt[2]*PntV + Ach[2]*AchV +Tcc[2]*TccV + Hcc[2]*HccV + Wwb[2]*WwbV + Whr[2]*WhrV + Whr[2]*WhrV + Brr[2]*BrrV + Oin[2]*OinV + Rpt[2]*RptV 
		+ Whm[2]*WhmV + Ces[2]*CesV + Bcn[2]*BcnV + Ban[2]*BanV + Let[2]*LetV + Brc[2]*BrcV + Btr[2]*BtrV,
		160 >= Scb[2]*ScbV + Grb[2]*GrbV + Rfb[2]*RfbV + Tfu[2]*TfuV + Egg[2]*EggV + Apl[2]*AplV + Crt[2]*CrtV + Ptc[2]*PtcV + Grp[2]*GrpV
		+ Lfy[2]*LfyV + Pnt[2]*PntV + Ach[2]*AchV +Tcc[2]*TccV + Hcc[2]*HccV + Wwb[2]*WwbV + Whr[2]*WhrV + Whr[2]*WhrV + Brr[2]*BrrV + Oin[2]*OinV + Rpt[2]*RptV 
		+ Whm[2]*WhmV + Ces[2]*CesV + Bcn[2]*BcnV + Ban[2]*BanV + Let[2]*LetV + Brc[2]*BrcV + Btr[2]*BtrV,
		40 <= Scb[3]*ScbV + Grb[3]*GrbV + Rfb[3]*RfbV + Tfu[3]*TfuV + Egg[3]*EggV + Apl[3]*AplV + Crt[3]*CrtV + Ptc[3]*PtcV + Grp[3]*GrpV
		+ Lfy[3]*LfyV + Pnt[3]*PntV + Ach[3]*AchV +Tcc[3]*TccV + Hcc[3]*HccV + Wwb[3]*WwbV + Whr[3]*WhrV + Whr[3]*WhrV + Brr[3]*BrrV + Oin[3]*OinV + Rpt[3]*RptV 
		+ Whm[3]*WhmV + Ces[3]*CesV + Bcn[3]*BcnV + Ban[3]*BanV + Let[3]*LetV + Brc[3]*BrcV + Btr[3]*BtrV,
		50 >= Scb[3]*ScbV + Grb[3]*GrbV + Rfb[3]*RfbV + Tfu[3]*TfuV + Egg[3]*EggV + Apl[3]*AplV + Crt[3]*CrtV + Ptc[3]*PtcV + Grp[3]*GrpV
		+ Lfy[3]*LfyV + Pnt[3]*PntV + Ach[3]*AchV +Tcc[3]*TccV + Hcc[3]*HccV + Wwb[3]*WwbV + Whr[3]*WhrV + Whr[3]*WhrV + Brr[3]*BrrV + Oin[3]*OinV + Rpt[3]*RptV 
		+ Whm[3]*WhmV + Ces[3]*CesV + Bcn[3]*BcnV + Ban[3]*BanV + Let[3]*LetV + Brc[3]*BrcV + Btr[3]*BtrV, BanV <= 155] + default
	elif(sex == "F"):
		constraints = [80 <= Scb[1]*ScbV + Grb[1]*GrbV + Rfb[1]*RfbV + Tfu[1]*TfuV + Egg[1]*EggV + Apl[1]*AplV + Crt[1]*CrtV + Ptc[1]*PtcV + Grp[1]*GrpV 
		+ Lfy[1]*LfyV + Pnt[1]*PntV + Ach[1]*AchV +Tcc[1]*TccV + Hcc[1]*HccV + Wwb[1]*WwbV + Whr[1]*WhrV + Whr[1]*WhrV + Brr[1]*BrrV + Oin[1]*OinV + Rpt[1]*RptV 
		+ Whm[1]*WhmV + Ces[1]*CesV + Bcn[1]*BcnV + Ban[1]*BanV + Let[1]*LetV + Brc[1]*BrcV + Btr[1]*BtrV,
		100 >= Scb[1]*ScbV + Grb[1]*GrbV + Rfb[1]*RfbV + Tfu[1]*TfuV + Egg[1]*EggV + Apl[1]*AplV + Crt[1]*CrtV + Ptc[1]*PtcV + Grp[1]*GrpV
		+ Lfy[1]*LfyV + Pnt[1]*PntV + Ach[1]*AchV +Tcc[1]*TccV + Hcc[1]*HccV + Wwb[1]*WwbV + Whr[1]*WhrV + Whr[1]*WhrV + Brr[1]*BrrV + Oin[1]*OinV + Rpt[1]*RptV 
		+ Whm[1]*WhmV + Ces[1]*CesV + Bcn[1]*BcnV + Ban[1]*BanV + Let[1]*LetV + Brc[1]*BrcV + Btr[1]*BtrV,
		110 <= Scb[2]*ScbV + Grb[2]*GrbV + Rfb[2]*RfbV + Tfu[2]*TfuV + Egg[2]*EggV + Apl[2]*AplV + Crt[2]*CrtV + Ptc[2]*PtcV + Grp[2]*GrpV
		+ Lfy[2]*LfyV + Pnt[2]*PntV + Ach[2]*AchV +Tcc[2]*TccV + Hcc[2]*HccV + Wwb[2]*WwbV + Whr[2]*WhrV + Whr[2]*WhrV + Brr[2]*BrrV + Oin[2]*OinV + Rpt[2]*RptV 
		+ Whm[2]*WhmV + Ces[2]*CesV + Bcn[2]*BcnV + Ban[2]*BanV + Let[2]*LetV + Brc[2]*BrcV + Btr[2]*BtrV,
		130 >= Scb[2]*ScbV + Grb[2]*GrbV + Rfb[2]*RfbV + Tfu[2]*TfuV + Egg[2]*EggV + Apl[2]*AplV + Crt[2]*CrtV + Ptc[2]*PtcV + Grp[2]*GrpV
		+ Lfy[2]*LfyV + Pnt[2]*PntV + Ach[2]*AchV +Tcc[2]*TccV + Hcc[2]*HccV + Wwb[2]*WwbV + Whr[2]*WhrV + Whr[2]*WhrV + Brr[2]*BrrV + Oin[2]*OinV + Rpt[2]*RptV 
		+ Whm[2]*WhmV + Ces[2]*CesV + Bcn[2]*BcnV + Ban[2]*BanV + Let[2]*LetV + Brc[2]*BrcV + Btr[2]*BtrV,
		30 <= Scb[3]*ScbV + Grb[3]*GrbV + Rfb[3]*RfbV + Tfu[3]*TfuV + Egg[3]*EggV + Apl[3]*AplV + Crt[3]*CrtV + Ptc[3]*PtcV + Grp[3]*GrpV
		+ Lfy[3]*LfyV + Pnt[3]*PntV + Ach[3]*AchV +Tcc[3]*TccV + Hcc[3]*HccV + Wwb[3]*WwbV + Whr[3]*WhrV + Whr[3]*WhrV + Brr[3]*BrrV + Oin[3]*OinV + Rpt[3]*RptV 
		+ Whm[3]*WhmV + Ces[3]*CesV + Bcn[3]*BcnV + Ban[3]*BanV + Let[3]*LetV + Brc[3]*BrcV + Btr[3]*BtrV,
		50 >= Scb[3]*ScbV + Grb[3]*GrbV + Rfb[3]*RfbV + Tfu[3]*TfuV + Egg[3]*EggV + Apl[3]*AplV + Crt[3]*CrtV + Ptc[3]*PtcV + Grp[3]*GrpV
		+ Lfy[3]*LfyV + Pnt[3]*PntV + Ach[3]*AchV +Tcc[3]*TccV + Hcc[3]*HccV + Wwb[3]*WwbV + Whr[3]*WhrV + Whr[3]*WhrV + Brr[3]*BrrV + Oin[3]*OinV + Rpt[3]*RptV 
		+ Whm[3]*WhmV + Ces[3]*CesV + Bcn[3]*BcnV + Ban[3]*BanV + Let[3]*LetV + Brc[3]*BrcV + Btr[3]*BtrV, BanV <= 155] + default

objective = Minimize(Scb[0]*ScbV + Grb[0]*GrbV + Rfb[0]*RfbV + Tfu[0]*TfuV + Egg[0]*EggV + Apl[0]*AplV + Crt[0]*CrtV + Ptc[0]*PtcV + Grp[0]*GrpV 
	+ Lfy[0]*LfyV + Pnt[0]*PntV + Ach[0]*AchV +Tcc[0]*TccV + Hcc[0]*HccV + Wwb[0]*WwbV + Whr[0]*WhrV + Whr[0]*WhrV + Brr[0]*BrrV + Oin[0]*OinV + Rpt[0]*RptV 
	+ Whm[0]*WhmV + Ces[0]*CesV + Bcn[0]*BcnV + Ban[0]*BanV + Let[0]*LetV + Brc[0]*BrcV + Btr[0]*BtrV)

prob = Problem(objective, constraints)

# The optimal objective is returned by prob.solve().
result = prob.solve()
print('{}: ${} '.format('Cost: ', round(result,2)))
print('{}: {} grams'.format('Skinless Chicken Breast', round(ScbV.value,2)))
print('{}: {} grams'.format('Ground Beef', round(GrbV.value,2)))
print('{}: {} grams'.format('Refried Beans', round(RfbV.value,2)))
print('{}: {} grams'.format('Tofu', round(TfuV.value,2)))
print('{}: {} grams'.format('Egg', round(EggV.value,2)))
print('{}: {} grams'.format('Apple', round(AplV.value,2)))
print('{}: {} grams'.format('Carrots', round(CrtV.value,2)))
print('{}: {} grams'.format('Potato Chips', round(PtcV.value,2)))
print('{}: {} grams'.format('Green Pepper', round(GrpV.value,2)))
print('{}: {} grams'.format('Light nonfat Yogurt',round(LfyV.value,2)))
print('{}: {} grams'.format('Peanuts',round(PntV.value,2)))
print('{}: {} grams'.format('American Cheese',round(AchV.value,2)))
print('{}: {} grams'.format('Turkey Cold Cut',round(TccV.value,2)))
print('{}: {} grams'.format('Ham Cold Cut',round(HccV.value,2)))
print('{}: {} grams'.format('Whole Wheat Bread',round(WwbV.value,2)))
print('{}: {} grams'.format('White Rice',round(WhrV.value,2)))
print('{}: {} grams'.format('Brown Rice',round(BrrV.value,2)))
print('{}: {} grams'.format('Onion',round(OinV.value,2)))
print('{}: {} grams'.format('Roasted Potato',round(RptV.value,2)))
print('{}: {} grams'.format('Whole Milk',round(WhmV.value,2)))
print('{}: {} grams'.format('Cheerios',round(CesV.value,2)))
print('{}: {} grams'.format('Bacon',round(BcnV.value,2)))
print('{}: {} grams'.format('Banana',round(BanV.value,2)))
print('{}: {} grams'.format('Lettuce',round(LetV.value,2)))
print('{}: {} grams'.format('Broccoli',round(BrcV.value,2)))
print('{}: {} grams'.format('Butter',round(BtrV.value,2)))
print('\n')
print('Protein: '+str(round(Scb[1]*ScbV.value + Grb[1]*GrbV.value + Rfb[1]*RfbV.value + Tfu[1]*TfuV.value + Egg[1]*EggV.value + Apl[1]*AplV.value + Crt[1]*CrtV.value + Ptc[1]*PtcV.value + Grp[1]*GrpV.value
	+ Lfy[1]*LfyV.value + Pnt[1]*PntV.value + Ach[1]*AchV.value +Tcc[1]*TccV.value + Hcc[1]*HccV.value + Wwb[1]*WwbV.value + Whr[1]*WhrV.value + Whr[1]*WhrV.value + Brr[1]*BrrV.value
	+ Oin[1]*OinV.value + Rpt[1]*RptV.value + Whm[1]*WhmV.value + Ces[1]*CesV.value + Bcn[1]*BcnV.value + Ban[1]*BanV.value + Let[1]*LetV.value + Brc[1]*BrcV.value + Btr[1]*BtrV.value,2))+' grams')
print('Carbs: '+str(round(Scb[2]*ScbV.value + Grb[2]*GrbV.value + Rfb[2]*RfbV.value + Tfu[2]*TfuV.value + Egg[2]*EggV.value + Apl[2]*AplV.value + Crt[2]*CrtV.value + Ptc[2]*PtcV.value + Grp[2]*GrpV.value
	+ Lfy[2]*LfyV.value + Pnt[2]*PntV.value + Ach[2]*AchV.value +Tcc[2]*TccV.value + Hcc[2]*HccV.value + Wwb[2]*WwbV.value + Whr[2]*WhrV.value + Whr[2]*WhrV.value + Brr[2]*BrrV.value
	+ Oin[2]*OinV.value + Rpt[2]*RptV.value + Whm[2]*WhmV.value + Ces[2]*CesV.value + Bcn[2]*BcnV.value + Ban[2]*BanV.value + Let[2]*LetV.value + Brc[2]*BrcV.value + Btr[2]*BtrV.value,2))+' grams')
print('Fat: '+str(round(Scb[3]*ScbV.value + Grb[3]*GrbV.value + Rfb[3]*RfbV.value + Tfu[3]*TfuV.value + Egg[3]*EggV.value + Apl[3]*AplV.value + Crt[3]*CrtV.value + Ptc[3]*PtcV.value + Grp[3]*GrpV.value
	+ Lfy[3]*LfyV.value + Pnt[3]*PntV.value + Ach[3]*AchV.value +Tcc[3]*TccV.value + Hcc[3]*HccV.value + Wwb[3]*WwbV.value + Whr[3]*WhrV.value + Whr[3]*WhrV.value + Brr[3]*BrrV.value
	+ Oin[3]*OinV.value + Rpt[3]*RptV.value + Whm[3]*WhmV.value + Ces[3]*CesV.value + Bcn[3]*BcnV.value + Ban[3]*BanV.value + Let[3]*LetV.value + Brc[3]*BrcV.value + Btr[3]*BtrV.value,2))+' grams')
print('Calories: '+str(round(Scb[4]*ScbV.value + Grb[4]*GrbV.value + Rfb[4]*RfbV.value + Tfu[4]*TfuV.value + Egg[4]*EggV.value + Apl[4]*AplV.value + Crt[4]*CrtV.value + Ptc[4]*PtcV.value + Grp[4]*GrpV.value
	+ Lfy[4]*LfyV.value + Pnt[4]*PntV.value + Ach[4]*AchV.value +Tcc[4]*TccV.value + Hcc[4]*HccV.value + Wwb[4]*WwbV.value + Whr[4]*WhrV.value + Whr[4]*WhrV.value + Brr[4]*BrrV.value
	+ Oin[4]*OinV.value + Rpt[4]*RptV.value + Whm[4]*WhmV.value + Ces[4]*CesV.value + Bcn[4]*BcnV.value + Ban[4]*BanV.value + Let[4]*LetV.value + Brc[4]*BrcV.value + Btr[4]*BtrV.value,2)))