# Corona data, model and forecast for South Tyrol

Mathematical approximation and data for the second wave of COVID-19 in South Tyrol with data starting on 6 October 2020. Exponential growth and a serial interval of four days are assumed.

### Second wave:

<img src="main/fig/CaseIncidenceSouthTyrol.svg">

<p align=left><img width="100%" src="https://github.com/e-dub/CoronaSouthTyrol/fig/ModelDailyFatalitiesSouthTyrol.svg"></p>

<p align=left><img width="100%" src="https://github.com/e-dub/CoronaSouthTyrol/fig/numberHospitalizedPeopleSouthTyrol.svg"></p>

<p align=left><img width="100%" src="https://github.com/e-dub/CoronaSouthTyrol/fig/numberIntensiveTherapySouthTyrol.svg"></p>

<p align=left><img width="100%" src="https://github.com/e-dub/CoronaSouthTyrol/ig/newNumberTestedPeopleSouthTyrol.svg"></p>


### WHO indicators:

<p align=left><img width="100%" src="https://github.com/e-dub/CoronaSouthTyrol/fig/TestPositivitySouthTyrol.svg"></p>

<p align=left><img width="100%" src="https://github.com/e-dub/CoronaSouthTyrol/fig/TestingResponseWHOSouthTyrol.svg"></p>

<p align=left><img width="100%" src="https://github.com/e-dub/CoronaSouthTyrol/fig/CaseIncidenceSouthTyrol.svg"></p>

<p align=left><img width="100%" src="https://github.com/e-dub/CoronaSouthTyrol/fig/MortalityWHOSouthTyrol.svg"></p>

### All data:
<embed type="text/html" src="/http/currentlyPositiveTestedSouthTyrolAll.html" width="100%"></embed>

<embed type="text/html" src="http/currentlyPositiveTestedSouthTyrolAll.html" width="100%"></embed>

<iframe src="/http/newPositiveTestedSouthTyrolAll.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

<iframe src="https://github.com/e-dub/CoronaSouthTyrol/http/positiveTestedSouthTyrolAll.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

<iframe src="https://github.com/e-dub/CoronaSouthTyrol/http/deceasedSouthTyrolAll.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

<iframe src="https://github.com/e-dub/CoronaSouthTyrol/http/newDeceasedSouthTyrolAll.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

<iframe src="https://github.com/e-dub/CoronaSouthTyrol/http/FatalityRateSouthTyrolAll.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

<iframe src="https://github.com/e-dub/CoronaSouthTyrol/http/ICULoadSouthTyrolAll.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

<iframe src="https://github.com/e-dub/CoronaSouthTyrol/http/newNumberTestedPeopleSouthTyrolAll.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>


### Basis data:
Number of ICU beds = 90 [[4]](#4).

Population = 533439 [[2]](#2).

Corona values in South Tyrol [[1]](#1),[[5]](#5).


### Assumptions:
Exponential growth.

Serial interval = 4 days [[3]](#3).

Fatality interval (between test and fatality) = 4 weeks.

Calculation of R4 and R7, see [[3]](#3).

Assumptions for community spreading ([[6]](#6)).:\
Testing positivity:\
 <2%: low incidence of community spreading,\
 <5%: moderate incidence of community spreading,\
 <20%: high incidence of community spreading,\
 \>20%: very high incidence of community spreading.\
Hospitalization rate:\
 <5%: low incidence of community spreading,\
 <10%: moderate incidence of community spreading,\
 <30%: high incidence of community spreading,\
 \>30%: very high incidence of community spreading.

## Sources
<a id="1">[1]</a>
http://www.provinz.bz.it/sicherheit-zivilschutz/zivilschutz/aktuelle-daten-zum-coronavirus.asp

<a id="2">[2]</a>
https://astat.provinz.bz.it/de/bevoelkerung.asp

<a id="3">[3]</a>
https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Projekte_RKI/R-Wert-Erlaeuterung.pdf?__blob=publicationFile

<a id="4">[4]</a>
https://www.stol.it/artikel/chronik/die-angst-vor-der-naechsten-corona-welle

<a id="5">[5]</a>
http://api.corona-bz.simedia.cloud/

<a id="6">[6]</a>
https://www.who.int/publications/i/item/considerations-in-adjusting-public-health-and-social-measures-in-the-context-of-covid-19-interim-guidance


