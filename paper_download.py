# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 18:08:37 2022

@author: W. Benedikt Schmal

Purpose:
    1) Download IO Papers and the abstracts
    2) Aggregate Data
    3) Export data to .xslx & prepare export to .tex
    
"""

import os
os.chdir('C:\\Users\\DICE\\sciebo\\research\\IAD Collusion\\quant') #change directory as needed
import pandas as pd
import numpy as np
import pickle
from pybliometrics.scopus import ScopusSearch
from pybliometrics.scopus import AbstractRetrieval


hv2b = pd.DataFrame()
adfb1 = pd.DataFrame()
fulldata = pd.DataFrame()

for y in range(2002, 2022, 1):
    SPS = ScopusSearch(f'PUBYEAR IS {y} AND ISSN(1756-2171) OR ISSN(0741-6261) OR ISSN(0025-1909) OR ISSN(1526-5501) OR ISSN(0022-0531) OR ISSN(10957235) OR ISSN(1467-6451) OR ISSN(0022-1821) OR ISSN(1559-7431) OR ISSN(1559-744X) OR ISSN(1530-9134) OR ISSN(1058-6407) OR ISSN(0167-7187)')
    df = pd.DataFrame(pd.DataFrame(SPS.results))
    print(len(df))
    for i in range(len(df)):
        SPS2 = AbstractRetrieval(df.iloc[i,1], view='FULL')
        adfb1 = pd.DataFrame([SPS2.abstract], columns=['abstract'])
        df_2h = pd.DataFrame(df.iloc[i])
        df_2 = df_2h.T
        df_2 = df_2.reset_index(drop=True)
        adfb1 = adfb1.reset_index(drop=True)
        hv1 = pd.concat([df_2, adfb1], axis=1, join='inner')
        hv2b = hv2b.append(hv1)
    fulldata = fulldata.append(hv2b)    
    hv2b.to_excel(f'io_journals_{y}.xlsx') 

# additional download of JEBO
data90_mainjebo = pd.DataFrame()
for y in range(2002, 2022, 1):
    SPS2 = ScopusSearch(f'PUBYEAR IS {y} AND ISSN(01672681)')
    df2 = pd.DataFrame(pd.DataFrame(SPS2.results))
    print(len(df2))
    data90_mainjebo = data90_mainjebo.append(df2)  

    
    
fulldata2 = pd.DataFrame()
for y in range(2002, 2022, 1):
    SPS2 = ScopusSearch(f'PUBYEAR IS {y} AND ISSN(00335533) OR ISSN(15314650) OR ISSN(00223808) OR ISSN(1537534X) OR ISSN(00028282) OR ISSN(00129682) OR ISSN(14680262) OR ISSN(00346527) OR ISSN(1467937X) OR ISSN(19457782) OR ISSN(19457790) OR ISSN(00220515) OR ISSN(08953309) OR ISSN(00346535) OR ISSN(15309142) OR ISSN(15424766) OR ISSN(15424774) OR ISSN(19457669) OR ISSN(19457685) OR ISSN(00130133) OR ISSN(14680297) OR ISSN(15557561) OR ISSN(02664658) OR ISSN(14680327) OR ISSN(17597323) OR ISSN(17597331) OR ISSN(00206598) OR ISSN(14682354) OR ISSN(14657341) OR ISSN(87566222) OR ISSN(00142921)')
    df2 = pd.DataFrame(pd.DataFrame(SPS2.results))
    print(len(df2))
    fulldata2 = fulldata2.append(df2) 
fulldata2.to_excel('other_journals_full.xlsx') 
fulldata2.to_pickle('jrnl_data_general')  # where to save it, usually as a .pkl
#df.loc[:,"description"]


# Additional Journal: RIO and JLE
add_data = pd.DataFrame()
for y in range(2002, 2022, 1):
    SPS2 = ScopusSearch(f'PUBYEAR IS {y} AND ISSN(00222186) OR ISSN(15375285) OR ISSN(15737160) OR ISSN(0889938X)')
    df2_add = pd.DataFrame(pd.DataFrame(SPS2.results))
    print(len(df2_add))
    add_data = add_data.append(df2_add) 
    add_data.to_pickle('jrnl_data_add') 
    # ATTENTION: WRONG RIO added (removed later on)
    
fulldata2.to_excel('other_journals_full.xlsx') 
add_data.to_pickle('jrnl_data_general')  # where to save it, usually as a .pkl
#df.loc[:,"description"]


for i in range(len(fulldata2)):
    try:
        SPS2 = AbstractRetrieval(fulldata2.iloc[i,1], view='FULL')
        adfb1 = pd.DataFrame([SPS2.abstract], columns=['abstract'])
    except ValueError:
        adfb1 = pd.DataFrame([str('Not Found')], columns=['abstract'])
        print("Abstract missing"+" in entry " + str(i))
    df_2h = pd.DataFrame(fulldata2.iloc[i])
    df_2 = df_2h.T
    df_2 = df_2.reset_index(drop=True)
    adfb1 = adfb1.reset_index(drop=True)
    hv1 = pd.concat([df_2, adfb1], axis=1, join='inner')
    hv2b = hv2b.append(hv1)
fulldata = fulldata.append(hv2b)    
hv2b.to_excel(f'io_journals_{y}_expand.xlsx') 
fulldata.to_excel('other_journals_full_w_abstract.xlsx') 

try:
    SPS2 = AbstractRetrieval(df2.iloc[1102,1], view='FULL')
except ValueError:
    adfb1 = pd.DataFrame([str('Not Found')], columns=['abstract'])
    print("Abstract missing"+" in entry " + str(i))

######################################################
df.to_excel('io_jrnls_wo_abstract.xlsx')
######################################################



###############################################################################

###  OLDER JOURNALS
data90_1 = pd.DataFrame()

for y in range(1992, 2002, 1): #all io journals incl RIO and JLE
    SPS = ScopusSearch(f'PUBYEAR IS {y} AND ISSN(1756-2171) OR ISSN(0741-6261) OR ISSN(0025-1909) OR ISSN(1526-5501) OR ISSN(0022-0531) OR ISSN(10957235) OR ISSN(1467-6451) OR ISSN(0022-1821) OR ISSN(1530-9134) OR ISSN(00222186) OR ISSN(15375285) OR ISSN(15737160) OR ISSN(0889938X) OR ISSN(1058-6407) OR ISSN(0167-7187)')
    df = pd.DataFrame(pd.DataFrame(SPS.results))
    print(len(df))
    data90_1 = data90_1.append(df) 
    
    
data90_2 = pd.DataFrame()
for y in range(1992, 2002, 1):
    SPS2 = ScopusSearch(f'PUBYEAR IS {y} AND ISSN(00335533) OR ISSN(15314650) OR ISSN(00223808) OR ISSN(1537534X) OR ISSN(00028282) OR ISSN(00129682) OR ISSN(14680262) OR ISSN(00346527) OR ISSN(1467937X) OR ISSN(19457782) OR ISSN(19457790) OR ISSN(00220515) OR ISSN(08953309) OR ISSN(00346535) OR ISSN(15309142) OR ISSN(15424766) OR ISSN(15424774) OR ISSN(19457669) OR ISSN(19457685) OR ISSN(00130133) OR ISSN(14680297) OR ISSN(15557561) OR ISSN(02664658) OR ISSN(14680327) OR ISSN(17597323) OR ISSN(17597331) OR ISSN(00206598) OR ISSN(14682354) OR ISSN(14657341) OR ISSN(87566222) OR ISSN(00142921)')
    df2 = pd.DataFrame(pd.DataFrame(SPS2.results))
    print(len(df2))
    data90_2 = data90_2.append(df2) 
    

data90_3 = pd.DataFrame()

for y in range(1982, 1992, 1): #all io journals incl RIO and JLE
    SPS = ScopusSearch(f'PUBYEAR IS {y} AND ISSN(1756-2171) OR ISSN(0741-6261) OR ISSN(0025-1909) OR ISSN(1526-5501) OR ISSN(0022-0531) OR ISSN(10957235) OR ISSN(1467-6451) OR ISSN(0022-1821) OR ISSN(1530-9134) OR ISSN(00222186) OR ISSN(15375285) OR ISSN(15737160) OR ISSN(0889938X) OR ISSN(1058-6407) OR ISSN(0167-7187)')
    df = pd.DataFrame(pd.DataFrame(SPS.results))
    print(len(df))
    data90_3 = data90_3.append(df) 
    #hv2b.to_excel(f'io_journals_{y}.xlsx') 
    
    
data90_4 = pd.DataFrame()
for y in range(1992, 2002, 1):
    SPS2 = ScopusSearch(f'PUBYEAR IS {y} AND ISSN(00335533) OR ISSN(15314650) OR ISSN(00223808) OR ISSN(1537534X) OR ISSN(00028282) OR ISSN(00129682) OR ISSN(14680262) OR ISSN(00346527) OR ISSN(1467937X) OR ISSN(19457782) OR ISSN(19457790) OR ISSN(00220515) OR ISSN(08953309) OR ISSN(00346535) OR ISSN(15309142) OR ISSN(15424766) OR ISSN(15424774) OR ISSN(19457669) OR ISSN(19457685) OR ISSN(00130133) OR ISSN(14680297) OR ISSN(15557561) OR ISSN(02664658) OR ISSN(14680327) OR ISSN(17597323) OR ISSN(17597331) OR ISSN(00206598) OR ISSN(14682354) OR ISSN(14657341) OR ISSN(87566222) OR ISSN(00142921)')
    df2 = pd.DataFrame(pd.DataFrame(SPS2.results))
    print(len(df2))
    data90_4 = data90_4.append(df2) 

data90_5 = pd.DataFrame()

for y in range(1969, 1982, 1): #all io journals incl RIO and JLE
    SPS = ScopusSearch(f'PUBYEAR IS {y} AND ISSN(1756-2171) OR ISSN(0741-6261) OR ISSN(0025-1909) OR ISSN(1526-5501) OR ISSN(0022-0531) OR ISSN(10957235) OR ISSN(1467-6451) OR ISSN(0022-1821) OR ISSN(1530-9134) OR ISSN(00222186) OR ISSN(15375285) OR ISSN(15737160) OR ISSN(0889938X) OR ISSN(1058-6407) OR ISSN(0167-7187)')
    df = pd.DataFrame(pd.DataFrame(SPS.results))
    print(len(df))
    data90_5 = data90_5.append(df) 

    
data90_6 = pd.DataFrame()
for y in range(1969, 1982, 1):
    SPS2 = ScopusSearch(f'PUBYEAR IS {y} AND ISSN(00335533) OR ISSN(15314650) OR ISSN(00223808) OR ISSN(1537534X) OR ISSN(00028282) OR ISSN(00129682) OR ISSN(14680262) OR ISSN(00346527) OR ISSN(1467937X) OR ISSN(19457782) OR ISSN(19457790) OR ISSN(00220515) OR ISSN(08953309) OR ISSN(00346535) OR ISSN(15309142) OR ISSN(15424766) OR ISSN(15424774) OR ISSN(19457669) OR ISSN(19457685) OR ISSN(00130133) OR ISSN(14680297) OR ISSN(15557561) OR ISSN(02664658) OR ISSN(14680327) OR ISSN(17597323) OR ISSN(17597331) OR ISSN(00206598) OR ISSN(14682354) OR ISSN(14657341) OR ISSN(87566222) OR ISSN(00142921)')
    df2 = pd.DataFrame(pd.DataFrame(SPS2.results))
    print(len(df2))
    data90_6 = data90_6.append(df2) 

old_jrnls2 = [data90_1, data90_2, data90_3, data90_4, data90_5, data90_6]
old_jrnls = pd.concat(old_jrnls2)
old_jrnls.to_pickle('oldjrnls_add')
### 


# additional download of JEBO
#JEBO ISSN: 01672681
data90_5jebo = pd.DataFrame()
for y in range(1972, 1982, 1):
    SPS2 = ScopusSearch(f'PUBYEAR IS {y} AND ISSN(01672681)')
    df2 = pd.DataFrame(pd.DataFrame(SPS2.results))
    print(len(df2))
    data90_5jebo = data90_5jebo.append(df2)
data90_3jebo = pd.DataFrame()
for y in range(1982, 1992, 1):
    SPS2 = ScopusSearch(f'PUBYEAR IS {y} AND ISSN(01672681)')
    df2 = pd.DataFrame(pd.DataFrame(SPS2.results))
    print(len(df2))
    data90_3jebo = data90_3jebo.append(df2)
data90_1jebo = pd.DataFrame()
for y in range(1992, 2002, 1):
    SPS2 = ScopusSearch(f'PUBYEAR IS {y} AND ISSN(01672681)')
    df2 = pd.DataFrame(pd.DataFrame(SPS2.results))
    print(len(df2))
    data90_1jebo = data90_1jebo.append(df2)
 
jebo_comb = [data90_mainjebo, data90_1jebo, data90_3jebo, data90_5jebo]
jebo_data = pd.concat(jebo_comb)
jebo_data.to_pickle('jebo_data_add')


# Extract abstract information (easy use in R)
#add_papers = pickle.load('jrnl_data_add')

file_to_read = open("jrnl_data_add", "rb") # Knoke papers
add_papers = pickle.load(file_to_read)
file_to_read = open("oldjrnls_add", "rb") # Knoke papers
add_old = pickle.load(file_to_read)

file_to_read.close()
print(add_papers)
#add_papers.drop(['freetoread', 'freetoreadLabel'],1, inplace=True)
add_papers['abstract'] = np.nan
#

# Add jebo papers as one package
file_to_read2 = open("jebo_data_add", "rb") # Knoke papers
add_jebo = pickle.load(file_to_read2)
file_to_read2.close()
print(add_jebo)
#add_jebo.drop(['freetoread', 'freetoreadLabel'],1, inplace=True)
add_jebo['abstract'] = np.nan
#

# Combine Dataframes
io_papers = fulldata
other_papers = hv2b # insert complete provided by Leon
comb = [io_papers, add_old, fulldata2]
all_papers = pd.concat(comb)
comb2 = [all_papers, add_papers, add_jebo]
all_papers = pd.concat(comb2)
all_papers.drop(['freetoread', 'freetoreadLabel'],1, inplace=True)

all_papers.to_csv(r'all_papers.csv', index = False)


C = A.reset_index(drop=True).join(B)
year = pd.split(all_papers['coverDate'], 1)
all_papers.sort_values(by=['year'])
year = str(all_papers['coverDate'], index = False)
year_a = str.split(year, '-')
year3 = dt(all_papers['coverDate'])

date2 = datetime(all_papers['coverDate'])

from datetime import datetime



year = all_papers['coverDate'].to_string(index = False)
date1 = datetime.strptime(year, '%Y-%m-%d')
pubyear = date1.strftime("%Y")

datetime(all_papers['coverDate'])
 
test = year.dt.year

all_papers['intage'] = all_papers['coverDate'].astype(int)

ap_nonempty = all_papers.dropna(subset = ['description']) #funktioniert 10k obs lost
ap_coll1 = ap_nonempty[ap_nonempty['description'].str.contains("collusion")]
ap_coll2 = ap_nonempty[ap_nonempty['description'].str.contains("collusive")]
ap_coll3 = ap_nonempty[ap_nonempty['description'].str.contains("cartel")]
ap_coll4 = ap_nonempty[ap_nonempty['description'].str.contains("cartels")]
ap_coll5 = ap_nonempty[ap_nonempty['description'].str.contains("bidding ring")]
ap_coll6 = ap_nonempty[ap_nonempty['description'].str.contains("bidding rings")]

comb2 = [ap_coll1, ap_coll2, ap_coll3, ap_coll4, ap_coll5, ap_coll6]
ap_coll = pd.concat(comb2)
ap_coll = ap_coll.drop_duplicates(subset=['eid'])
ap_coll.drop(ap_coll[ap_coll['publicationName'] == 'Review of International Organizations'].index, inplace=True)
 #477 observations (+19%)
 
np.savetxt(r'C:\\Users\\DICE\\sciebo\\research\\IAD Collusion\\quant\\abstracts.txt', ap_coll['description'], fmt='%1000s', encoding='utf-8')
ap_coll.to_excel(r'jrnl_list.xlsx', sheet_name='sheet1', index = False)

###

# Export paper information to Latex

ap_coll.sort_values(by=['coverDate', 'publicationName'])
pd.set_option('display.max_colwidth', 40)
#print(ap_coll.to_latex(buf=None, longtable = True, columns= ['title', 'author_names', 'publicationName'], index=False, header=True))
longtable = ap_coll.to_latex(buf=None, longtable = True, columns= ['title', 'author_names', 'publicationName'], index=False, header=True)
list1 = ap_coll.publicationName.value_counts()
print(list1)




data90_2.to_excel('other_journals_full.xlsx') 
data90_2.to_pickle('jrnl_data_general90')  # where to save it, usually as a .pkl
#df.loc[:,"description"]





### END OF SCRIPT ###

