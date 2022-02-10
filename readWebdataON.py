"""
source munich?:
    https://public.fusionbase.com/explore/covid19-germany/data

source germany
https://static.dwcdn.net/data/HG0nw.csv
add other indicators from WHO!
"""


import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
import seaborn as sns
from Model_COVID19_new import covid
import os
import locale

Upload=0
locale.setlocale(locale.LC_ALL, 'en_US.utf8')

# dataJSON = pd.read_json("https://data.cdc.gov/resource/kn79-hsxy.json")


# """
# New York Times GitHub repository
# """
# dataCSV = pd.read_csv(
#     'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
# )
# dataNY = dataCSV[dataCSV['state'] == 'New York']
# dataON = dataNY[dataNY['county'] == 'Onondaga']
# DeathsTotal = dataON['deaths']
# CasesTotal = dataON['cases']


# os.sys(
#     'curl https://data.cdc.gov/api/views/9mfq-cb36/rows.csv?accessType=DOWNLOAD -o dataCDC.csv'
# )


# data = pd.read_json("https://datawrapper.dwcdn.net/I4IZD/184/&format=json")

# data = pd.read_json("https://static.dwcdn.net/I4IZD/184/&format=json")


a = 0
val = [322, 331, 308, 62, 224, 67]
#[306, 315, 292, 46, 207, 51]
#[301, 310, 287, 41, 202, 46]
while a == 0:
    #https://datawrapper.dwcdn.net/5Voa2/298/dataset.csv
    url = 'https://datawrapper.dwcdn.net/5Voa2/'+str(val[0])+'/dataset.csv'
    a = os.system("wget -O datasetNewCases.csv " + url)
    if a != 0:
        url = 'https://datawrapper.dwcdn.net/5Voa2/'+str(val[0]-1)+'/dataset.csv'
        os.system("wget -O datasetNewCases.csv " + url)
        dataNewCases = pd.read_csv("datasetNewCases.csv",sep='\t')
    val[0] += 1
a = 0
while a == 0:
    url = 'https://datawrapper.dwcdn.net/z3IKX/'+str(val[1])+'/dataset.csv'
    a = os.system("wget -O datasetCurrent.csv " + url)
    if a != 0:
        url = 'https://datawrapper.dwcdn.net/z3IKX/'+str(val[1]-1)+'/dataset.csv'
        os.system("wget -O datasetCurrent.csv " + url)
        dataCurrentCases = pd.read_csv("datasetCurrent.csv") #= pd.read_csv(url)
    val[1] += 1
a = 0
while a == 0:
    url = 'https://datawrapper.dwcdn.net/HG0nw/'+str(val[2])+'/dataset.csv'
    a = os.system("wget -O datasetHospitalizations.csv " + url)
    if a != 0:
        url = 'https://datawrapper.dwcdn.net/HG0nw/'+str(val[2]-1)+'/dataset.csv'
        os.system("wget -O datasetHospitalizations.csv " + url)
        dataHospitalizations = pd.read_csv("datasetHospitalizations.csv")
    val[2] += 1
a = 0
while a == 0:
    # hospitalizations: https://www.datawrapper.de/_/I4IZD
    url = 'https://datawrapper.dwcdn.net/I4IZD/'+str(val[3])+'/dataset.csv'
    a = os.system("wget -O datasetHospitalizations2.csv " + url)
    if a != 0:
        url = 'https://datawrapper.dwcdn.net/I4IZD/'+str(val[3]-1)+'/dataset.csv'
        os.system("wget -O datasetHospitalizations2.csv " + url)
        dataHospitalizations2 = pd.read_csv("dataset.csv")
    val[3] += 1
a = 0
while a == 0:
    # hospiti
    url = 'https://datawrapper.dwcdn.net/NZw22/'+str(val[4])+'/dataset.csv'
    a = os.system("wget -O datasetDeaths.csv " + url)
    if a != 0:
        url = 'https://datawrapper.dwcdn.net/NZw22/'+str(val[4]-1)+'/dataset.csv'
        os.system("wget -O datasetDeaths.csv " + url)
        dataDeaths = pd.read_csv("datasetDeaths.csv")
    val[4] += 1
a = 0
while a == 0:
    url = 'https://datawrapper.dwcdn.net/WYgOL/'+str(val[5])+'/dataset.csv'
    a = os.system("wget -O datasetActive.csv " + url)
    if a != 0:
        url = 'https://datawrapper.dwcdn.net/WYgOL/'+str(val[5]-1)+'/dataset.csv'
        os.system("wget -O datasetActive.csv " + url)
        dataActive = pd.read_csv("datasetActive.csv", header=None,sep='\t')
    val[5] += 1


####code testing
# url = 'https://datawrapper.dwcdn.net/F9ZcO/53/dataset.csv'



# url = 'https://datawrapper.dwcdn.net/mDbeO/79/dataset.csv'
# os.system("wget -O dataset.csv " + url)
# data = pd.read_csv("dataset.csv")

# #age
# url = 'https://datawrapper.dwcdn.net/mDbeO/79/dataset.csv'
# os.system("wget -O dataset.csv " + url)
# data = pd.read_csv("dataset.csv")

# #vac current
# url = 'https://datawrapper.dwcdn.net/Pnfcb/47/dataset.csv'
# os.system("wget -O dataset.csv " + url)
# data = pd.read_csv("dataset.csv")


###########

# # These are NYS
# # https://www.syracuse.com/coronavirus-ny/
# # cumulative tests
# file = 'aTHYq.csv'
# os.system('wget ' + source + file)
# data = pd.read_csv(file)





# # testing
# file = '9ACNX.csv'
# os.system('wget ' + source + file)
# data = pd.read_csv(file)

# # new deaths and cumulative
# file = 'KC606.csv'
# os.system('wget ' + source + file)
# data = pd.read_csv(file)

# # hospitalizations
# file = 'XRnvb.csv'
# os.system('wget ' + source + file)
# data = pd.read_csv(file)


# Upload = True
# Upload = False

nICU = 254
nTotHospitalBeds = 1457 + 170 + 130

# TestPositivity = data.newPositiveTested/data.newNumberTestedPeople*100
data = pd.DataFrame()


data["numberIntensiveTherapy"] = dataHospitalizations["Total ICU"]
# ICULoad = data.numberIntensiveTherapy/nICU
# FatalityRate = data.deceased/(data.deceased+data.cured)*100
data["date"] =  pd.to_datetime(dataDeaths["Date"], infer_datetime_format=True)
data["newDeceased"] = dataHospitalizations["Deaths"]
data["deceased"] = np.cumsum(data["newDeceased"])
data["numberHospitalizedPeople"] = dataHospitalizations["Total Hospitalized"]

data["newPositiveTested"] = dataCurrentCases["New Positives"]
data["positiveTested"] = dataCurrentCases["Cumulative Positives"]

data = data.dropna()
#not correct!!!!
data["currentlyPositiveTested"] = dataCurrentCases["Cumulative Positives"]
#data.currentlyPositiveTested

data["cured"] = data.positiveTested - data["deceased"] - data["numberHospitalizedPeople"] #- np.array(dataActive[1])[0]

StartDate = dt.date(2021, 6, 21)
mask = (data['date'] >= str(StartDate)) & (
    data['date'] <= data.iloc[-1]['date']
)
data2wave = data.loc[mask]

mask28 = (data['date'] >= str(StartDate + dt.timedelta(weeks=4))) & (
    data['date'] <= data.iloc[-1]['date']
)
data2wave28 = data.loc[mask28]


# second wave
ST = covid()

ST.pop = 476516
ST.tMax = 28
ST.nBedsICU = nICU
ST.data = data2wave
ST.FigSave = True
ST.where = 'Onondaga County (Syracuse, New York)'
ST.nf100k = np.array(ST.data.deceased)[-1] / ST.pop * 100000
ST.startDate = StartDate
# ST.data['TestPositivity'] = (
#     ST.data.newPositiveTested / ST.data.newNumberTestedPeople * 100
# )
ST.data['ICULoad'] = ST.data.numberIntensiveTherapy / nICU * 100
ST.data['FatalityRate'] = (
    ST.data.deceased / (ST.data.deceased + ST.data.cured) * 100
)
ST.data['HospitalizationRate'] = (
    ST.data.numberHospitalizedPeople / ST.pop * 100000
)
# ST.data['NewHospitalizationRate'] = np.concatenate((np.array(ST.data.newNumberHospitalizedPeople)[:6],
#                                           np.convolve(np.array(ST.data.newPositiveTested/ST.pop*100000),
#                                                       np.ones(7, dtype=int), 'valid')))
ST.data['CaseIncidence'] = np.concatenate(
    (
        np.array(ST.data.newPositiveTested)[:6],
        np.convolve(
            np.array(ST.data.newPositiveTested / ST.pop * 100000),
            np.ones(7, dtype=int),
            'valid',
        ),
    )
)
ST.data['MortalityWHO'] = np.concatenate(
    (
        np.array(ST.data.newDeceased)[:6],
        np.convolve(
            np.array(ST.data.newDeceased / ST.pop * 100000),
            np.ones(7, dtype=int),
            'valid',
        ),
    )
)

# ST.data['TestingResponseWHO'] = (
#     np.concatenate(
#         (
#             np.array(ST.data.newNumberTestedPeople / ST.pop * 1000)[:6],
#             np.convolve(
#                 np.array(ST.data.newNumberTestedPeople),
#                 np.ones(7, dtype=int),
#                 'valid',
#             ),
#         )
#     )
#     / ST.pop
#     * 1000
# )
ST.y0 = np.array(data2wave.newPositiveTested)
ST.f = np.array(data2wave.newDeceased)
ST.active = np.array(data.currentlyPositiveTested)[-1]
ST.fatality = np.array(ST.data.FatalityRate)[-1]
ST.yICU = np.array(data.numberIntensiveTherapy)[-1]
#ST.nTests = np.array(data.newNumberTestedPeople)[-1]

ST.CaseLines = True
ST.calc()
ST.ApproxPlot(FirstModel=False)
ST.FatalityPlot()


#ST.GeneralPlot('TestPositivity', 'daily test positivity')
# ST.GeneralPlot("numberIntensiveTherapy", "number of ICU patients")
# ST.GeneralPlot("ICULoad", "percent of COVID patients in ICU")
# ST.GeneralBarPlot(
#     'TestPositivity',
#     'daily test positivity',
#     AddLine=[2, 5, 20],
#     AddLineLabel=[
#         'low incidence of community transmission',
#         'moderate incidence of community transmission',
#         'high incidence of community transmission',
#     ],
#     AddLineColor=['yellow', 'orange', 'red'],
# )
ST.GeneralBarPlot('numberIntensiveTherapy', 'ICU patients')
ST.GeneralBarPlot('numberHospitalizedPeople', 'hospitalized corona patients')
ST.GeneralBarPlot('ICULoad', 'ICU COVID load [\\%]')

#ST.GeneralBarPlot('newNumberTestedPeople', 'daily tested persons')
# ST.GeneralBarPlot("NewHospitalizationRate", "newly hospitalized rate per 100000",
#                   AddLine=[5, 10, 30],
#                   AddLineLabel=["Low incidence of community transmission",
#                                 "Moderate incidence of community transmission",
#                                 "High incidence of community transmission"],
#                   AddLineColor=["yellow","orange", "red"])
ST.GeneralBarPlot(
    'CaseIncidence',
    'case incidence (WHO)\nnew cases over 7 days per 100000',
    AddLine=[20, 50, 150],
    AddLineLabel=[
        'low incidence of community transmission',
        'moderate incidence of community transmission',
        'high incidence of community transmission',
    ],
    AddLineColor=['yellow', 'orange', 'red'],
    startDateShift=6,
)
ST.GeneralBarPlot(
    'MortalityWHO',
    'mortality (WHO)\nfatalities over 7 days per 100000',
    AddLine=[1, 2, 5],
    AddLineLabel=[
        'low incidence of community transmission',
        'moderate incidence of community transmission',
        'high incidence of community transmission',
    ],
    AddLineColor=['yellow', 'orange', 'red'],
    startDateShift=6,
)
# ST.GeneralBarPlot(
#     'TestingResponseWHO',
#     'testing indicator (WHO)\npersons tested over 7 days per 1000',
#     AddLine=[2, 1],
#     AddLineLabel=[
#         'moderate capacity to respond',
#         'limited capacity to respond',
#     ],
#     AddLineColor=['orange', 'red'],
#     startDateShift=6,
# )

ST.FigSave = False
ST.data = data
ST.data['CaseIncidence'] = np.concatenate(
    (
        np.array(ST.data.newPositiveTested)[:6],
        np.convolve(
            np.array(ST.data.newPositiveTested / ST.pop * 100000),
            np.ones(7, dtype=int),
            'valid',
        ),
    )
)
ST.data['MortalityWHO'] = np.concatenate(
    (
        np.array(ST.data.newDeceased)[:6],
        np.convolve(
            np.array(ST.data.newDeceased / ST.pop * 100000),
            np.ones(7, dtype=int),
            'valid',
        ),
    )
)

# ST.data['TestingResponseWHO'] = (
#     np.concatenate(
#         (
#             np.array(ST.data.newNumberTestedPeople / ST.pop * 1000)[:6],
#             np.convolve(
#                 np.array(ST.data.newNumberTestedPeople),
#                 np.ones(7, dtype=int),
#                 'valid',
#             ),
#         )
#     )
#     / ST.pop
#     * 1000
# )
# ST.data['TestPositivity'] = (
#     ST.data.newPositiveTested / ST.data.newNumberTestedPeople * 100
# )
ST.data['ICULoad'] = ST.data.numberIntensiveTherapy / nICU * 100
ST.data['FatalityRate'] = (
    ST.data.deceased / (ST.data.deceased + ST.data.cured) * 100
)
ST.GeneralBarPlot('positiveTested', 'cumulative corona cases')
ST.GeneralBarPlot('currentlyPositiveTested', 'active corona cases')

ST.FigSave = True
ST.GeneralBarPlot(
    'FatalityRate',
    'case fatality rate [\\%]',
    FileNameAdd='All',
    PrintText=False,
)
ST.GeneralBarPlot(
    'positiveTested',
    'cumulative corona cases',
    PrintText=False,
    FileNameAdd='All',
)
ST.GeneralBarPlot(
    'newPositiveTested',
    'daily new corona cases',
    PrintText=False,
    FileNameAdd='All',
)
ST.GeneralBarPlot(
    'deceased',
    'cumulative corona fatalities',
    PrintText=False,
    FileNameAdd='All',
)
ST.GeneralBarPlot(
    'currentlyPositiveTested',
    'active corona cases',
    PrintText=False,
    FileNameAdd='All',
)
ST.GeneralBarPlot(
    'newDeceased',
    'daily corona fatalities',
    PrintText=False,
    FileNameAdd='All',
)
ST.GeneralBarPlot(
    'ICULoad', 'ICU corona load [\\%]', PrintText=False, FileNameAdd='All'
)
# ST.GeneralBarPlot(
#     'newNumberTestedPeople',
#     'daily tested persons',
#     PrintText=False,
#     FileNameAdd='All',
# )
ST.GeneralBarPlot(
    'newPositiveTested',
    'daily new corona cases',
    PrintText=False,
    FileNameAdd='All',
)
# ST.GeneralBarPlot(
#     'TestPositivity',
#     'daily test positivity [\\%]',
#     AddLine=[2, 5, 20],
#     AddLineLabel=[
#         'Low incidence of community transmission',
#         'Moderate incidence of community transmission',
#         'High incidence of community transmission',
#     ],
#     AddLineColor=['yellow', 'orange', 'red'],
#     PrintText=False,
#     FileNameAdd='All',
# )

from BokehPlotting import BokehPlot

BokehPlot(
    ST.data,
    dataSet='FatalityRate',
    name='case fatality rate [%]',
    FileNameAdd='All',
    where='Onondaga County (Syracuse, New York)',
    PrintText=False,
)
BokehPlot(
    ST.data,
    dataSet='positiveTested',
    name='cumulative corona cases',
    where='Onondaga County (Syracuse, New York)',
    PrintText=False,
    FileNameAdd='All',
)
BokehPlot(
    ST.data,
    dataSet='newPositiveTested',
    name='daily new corona cases',
    where='Onondaga County (Syracuse, New York)',
    PrintText=False,
    FileNameAdd='All',
)
BokehPlot(
    ST.data,
    dataSet='deceased',
    name='cumulative corona fatalities',
    where='Onondaga County (Syracuse, New York)',
    PrintText=False,
    FileNameAdd='All',
)
BokehPlot(
    ST.data,
    dataSet='currentlyPositiveTested',
    name='active corona cases',
    where='Onondaga County (Syracuse, New York)',
    PrintText=False,
    FileNameAdd='All',
)
BokehPlot(
    ST.data,
    dataSet='newDeceased',
    name='daily corona fatalities',
    where='Onondaga County (Syracuse, New York)',
    PrintText=False,
    FileNameAdd='All',
)
BokehPlot(
    ST.data,
    dataSet='ICULoad',
    name='ICU corona load [%]',
    where='Onondaga County (Syracuse, New York)',
    PrintText=False,
    FileNameAdd='All',
)
BokehPlot(
    ST.data,
    dataSet='numberIntensiveTherapy',
    name='ICU corona patients',
    where='Onondaga County (Syracuse, New York)',
    PrintText=False,
    FileNameAdd='All',
)
# BokehPlot(
#     ST.data,
#     dataSet='newNumberTestedPeople',
#     name='daily persons tested',
#     where='Onondaga County (Syracuse, New York)',
#     PrintText=False,
#     FileNameAdd='All',
# )

BokehPlot(
    ST.data,
    dataSet='newPositiveTested',
    name='daily new corona cases',
    where='Onondaga County (Syracuse, New York)',
    FileNameAdd='All',
)
BokehPlot(
    ST.data,
    dataSet='numberHospitalizedPeople',
    name='hospitalized corona patients',
    where='Onondaga County (Syracuse, New York)',
    FileNameAdd='All',
)
# BokehPlot(
#     ST.data,
#     dataSet='TestPositivity',
#     name='daily test positivity [%]',
#     where='Onondaga County (Syracuse, New York)',
#     AddLine=[2, 5, 20],
#     AddLineLabel=[
#         'low incidence of community transmission',
#         'moderate incidence of community transmission',
#         'high incidence of community transmission',
#     ],
#     AddLineColor=['yellow', 'orange', 'red'],
#     PrintText=False,
#     FileNameAdd='All',
# )

# BokehPlot(
#     ST.data,
#     dataSet='TestingResponseWHO',
#     name='testing indicator (WHO): persons tested over 7 days per 1000',
#     where='Onondaga County (Syracuse, New York)',
#     AddLine=[2, 1],
#     AddLineLabel=[
#         'moderate capacity to respond',
#         'limited capacity to respond',
#     ],
#     AddLineColor=['orange', 'red'],
#     PrintText=False,
#     FileNameAdd='All',
# )

BokehPlot(
    ST.data,
    dataSet='CaseIncidence',
    name='case incidence (WHO): new cases over 7 days per 100000',
    where='Onondaga County (Syracuse, New York)',
    AddLine=[20, 50, 150],
    AddLineLabel=[
        'low incidence of community transmission',
        'moderate incidence of community transmission',
        'high incidence of community transmission',
    ],
    AddLineColor=['yellow', 'orange', 'red'],
    PrintText=False,
    FileNameAdd='All',
)


BokehPlot(
    ST.data,
    dataSet='MortalityWHO',
    name='mortality (WHO): fatalities over 7 days per 100000',
    where='Onondaga County (Syracuse, New York)',
    AddLine=[1, 2, 5],
    AddLineLabel=[
        'low incidence of community transmission',
        'moderate incidence of community transmission',
        'high incidence of community transmission',
    ],
    AddLineColor=['yellow', 'orange', 'red'],
    PrintText=False,
    FileNameAdd='All',
)
# https://towardsdatascience.com/interactive-bar-charts-with-bokeh-7230e5653ba3

import covid_daily
import numpy as np


STfat1M = round(np.array(ST.data['deceased'])[-1] / ST.pop * 1e6)
data = covid_daily.overview(as_json=False)
data = data[['Country,Other', 'Deaths/1M pop']]
data = data.rename(columns={'Country,Other': 'country'})
data = data.rename(columns={'Deaths/1M pop': 'Corona deaths per 1M'})
STdata = {'country': 'Onondaga County', 'Corona deaths per 1M': STfat1M}
data = data.append(STdata, ignore_index=True)
data = data[data['country'] != 'Gibraltar']
data = data[data['country'] != 'San Marino']
data = data[data['country'] != 'Liechtenstein']
data = data[data['country'] != 'Andorra']
data = data[data['country'] != 'Aruba']
data = data[data['country'] != 'Sint Maarten']
dataSorted = data.sort_values(by=['Corona deaths per 1M'], ascending=False)
dataSorted.reset_index(drop=True, inplace=True)
dataSorted.index = np.arange(1, len(dataSorted) + 1)
print(dataSorted[:60])

nST = dataSorted[dataSorted['country'] == 'Onondaga County'].index[0]
nI = dataSorted[dataSorted['country'] == 'Italy'].index[0]
nC = max(25, nST)


locale.setlocale(locale.LC_ALL, 'en_US.utf8')
fig, ax = plt.subplots()
# plt.rcParams['xtick.major.pad']='0'
x = (
    dataSorted.groupby('country')['Corona deaths per 1M']
    .mean()
    .sort_values()
    .tail(nC)
)
ax = x.plot(kind='barh', figsize=(8, 6), width=0.8)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
# ax.tick_params(bottom="off", top="off",
#               labelbottom="on", left="off", right="off", labelleft="off")
vals = ax.get_xticks()
for tick in vals:
    ax.axvline(x=tick, linestyle='solid', alpha=0.4, color='white')
for tick in ax.get_xaxis().get_major_ticks():
    tick.set_pad(-5)
ax.xaxis.tick_top()
ax.xaxis.set_label_position('top')
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
ax.set_ylabel(None)
ax.set_xlabel('corona fatalities per one million inhabitants', labelpad=10)
# ax[0].set_color('r')
ax.get_children()[nC - nST].set_color('tab:red')
plt.gca().get_yticklabels()[nC - nST].set_color('tab:red')
ax.text(
    3500,
    0,
    'worst '
    + str(nC - 1)
    + ' countries\nand Onondaga County\n'
    + dt.datetime.today().strftime('%A, %-d %B %Y'),
)

valueName = 'FatalityComparison'
FileNameAdd = ''
plt.savefig(
    ST.FigFolder
    + os.sep
    + valueName
    + ST.where.replace(' ', '')
    + FileNameAdd
    + '.png',
    bbox_inches='tight',
    metadata={'Date': None},
)
plt.savefig(
    ST.FigFolder
    + os.sep
    + valueName
    + ST.where.replace(' ', '')
    + FileNameAdd
    + '.svg',
    bbox_inches='tight',
    metadata={'Date': None},
)

print(val)
