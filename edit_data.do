

clear all
set more off

cd "C:\Users\DICE\sciebo\research\IAD Collusion\quant"

import delimited "all_papers.csv", clear

split coverdate, parse("-")
ren coverdate1 year
drop coverdate*

destring year, replace
drop if year==1969 // start from the 70s
drop if description=="" // drop papers w/ missing abstracts

gen coll_present =  strpos(lower(description), "collusion") > 0
replace coll_present = 1 if strpos(lower(description), "collusive") > 0
replace coll_present = 1 if strpos(lower(description), "cartel") > 0
replace coll_present = 1 if strpos(lower(description), "bidding ring") > 0
tab coll_present //845 papers in total

gen journal = lower(publicationname)
tab journal
drop if journal == "review of international organizations"
replace journal = "journal of economics and management strategy" if strpos(journal, "journal of economics &amp;") > 0
replace journal = "econometrica" if strpos(journal, "econometrica : journal") > 0
replace journal = "management science" if strpos(journal, "manage. sci") > 0
replace journal = "management science" if strpos(journal, "manage sci") > 0
replace journal = "rand journal of economics" if strpos(journal, "the rand journal of economics") > 0

gen top5 = 0
replace top5 = 1 if journal == "american economic review" |journal ==  "econometrica" | journal == "journal of political economy" | journal == "review of economic studies" | journal == "quarterly journal of economics"
tab top5 // works 
tab top5 if coll_present == 1
gen genint = 0
replace genint = 1 if top5 == 1
replace genint = 1 if journal == "economic journal"  |journal ==  "international economic review" |journal == "european economic review" |journal == "american economic journal: applied economics" |journal == "journal of economic literature" |journal == "journal of economic perspectives" |journal == "journal of the european economic association" |journal == "review of economics and statistics"
replace genint = 1 if journal == "economic policy"
tab genint
tab genint if coll_present == 1

gen jtype = "" 
replace jtype = "genint" if genint == 1
replace jtype = "io" if journal == "rand journal of economics" | journal == "international journal of industrial organization" | journal == "review of industrial organization" | journal == "journal of industrial economics"
replace jtype = "field" if jtype==""
tab jtype
tab jtype if coll_present==1

gen jtype2 = "" 
replace jtype2 = "genint" if journal == "economic journal"  |journal ==  "international economic review" |journal == "european economic review" |journal == "american economic journal: applied economics" |journal == "journal of economic literature" |journal == "journal of economic perspectives" |journal == "journal of the european economic association" |journal == "review of economics and statistics" | journal == "economic policy"
replace jtype2 = "top5" if top5 == 1
replace jtype2 = "io" if journal == "rand journal of economics" | journal == "international journal of industrial organization" | journal == "review of industrial organization" | journal == "journal of industrial economics"
replace jtype2 = "field" if jtype2==""
tab jtype2
tab jtype2 if coll_present==1

// drop duplicates
bys eid: gen hv1 = _n
tab hv1
drop if hv1 > 1
drop hv*

tab journal, sort // 43,074
tab journal if coll_present==1, sort //786
tab journal if coll_present==1 & year>2001, sort //532

encode journal, gen(jrnl)
latab jrnl if coll_present==1, dec(2) col

export delimited "all_papers_edit.csv", replace





********************************************************************************
