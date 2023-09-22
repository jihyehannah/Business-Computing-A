# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:35:40 2023

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:09:07 2023

@author: admin
"""

#1.
import pandas as pd

df = pd.read_csv('C:/Users/admin/Desktop/코딩공부/비즈니스 컴퓨팅/results.csv')

#find out data type of 'date'
df.info() #data type of 'date' is object

#change data type of 'date' as to_datetime to compare dates
df['date'] = pd.to_datetime(df['date']) 


print(df.head())

print('\n')
print(df.info())
# result: index of date = datetime
print('\n')
print(type(df['date'][0])) 
#result: <class 'pandas._libs.tslibs.timestamps.Timestamp'>


new_df = df[(df['date']>=pd.to_datetime('2011-01-01'))&(df['date']<=pd.to_datetime('2020-12-31'))]

print(new_df)

#%%
#Q1.-a

df_year = df['date'].dt.year
new_df.insert( 1,'year', df_year)

#%%
#the number of winning of hong kong, south korea, france, usa, argentina

hk = new_df[(new_df['home_team'] == 'Hong Kong')| (new_df['away_team'] == 'Hong Kong')]
hk_win = new_df[(new_df['home_score'] > new_df['away_score']) & (new_df['home_team'] == 'Hong Kong') |
                    (new_df['away_score'] > new_df['home_score']) & (new_df['away_team'] == 'Hong Kong')]
hk_win_pct = (hk_win.groupby('year')['home_score'].count()/hk.groupby('year')['home_score'].size()).reset_index(name = 'Hong Kong').set_index('year')


sk = new_df[(new_df['home_team'] == 'South Korea')| (new_df['away_team'] == 'South Korea')]
sk_win = new_df[(new_df['home_score'] > new_df['away_score']) & (new_df['home_team'] == 'South Korea') |
                    (new_df['away_score'] > new_df['home_score']) & (new_df['away_team'] == 'South Korea')]
sk_win_pct = (sk_win.groupby('year')['home_score'].count()/sk.groupby('year')['home_score'].size()).reset_index(name = 'South Korea').set_index('year')



fr = new_df[(new_df['home_team'] == 'France')| (new_df['away_team'] == 'France')]
fr_win = new_df[(new_df['home_score'] > new_df['away_score']) & (new_df['home_team'] == 'France') |
                    (new_df['away_score'] > new_df['home_score']) & (new_df['away_team'] == 'France')]
fr_win_pct = (fr_win.groupby('year')['home_score'].count()/fr.groupby('year')['home_score'].size()).reset_index(name = 'France').set_index('year')


us = new_df[(new_df['home_team'] == 'United States')| (new_df['away_team'] == 'United States')]
us_win = new_df[(new_df['home_score'] > new_df['away_score']) & (new_df['home_team'] == 'United States') |
                    (new_df['away_score'] > new_df['home_score']) & (new_df['away_team'] == 'United States')]
us_win_pct = (us_win.groupby('year')['home_score'].count()/us.groupby('year')['home_score'].size()).reset_index(name = 'United States').set_index('year')


ar = new_df[(new_df['home_team'] == 'Argentina')| (new_df['away_team'] == 'Argentina')]
ar_win = new_df[(new_df['home_score'] > new_df['away_score']) & (new_df['home_team'] == 'Argentina') |
                    (new_df['away_score'] > new_df['home_score']) & (new_df['away_team'] == 'Argentina')]
ar_win_pct = (ar_win.groupby('year')['home_score'].count()/ar.groupby('year')['home_score'].size()).reset_index(name = 'Argentina').set_index('year')

teams = ['Hong Kong', 'South Korea', 'France', 'United States', 'Argentina']
hk_win_team = len(hk_win)/len(hk)
sk_win_team = len(sk_win)/len(sk)
fr_win_team = len(fr_win)/len(fr)
us_win_team = len(us_win)/len(us)
ar_win_team = len(ar_win)/len(ar)

win_teams = [hk_win_team, sk_win_team, fr_win_team, us_win_team, ar_win_team]


total_win_team = pd.DataFrame(win_teams, index=[teams])
total_win_team.columns = ['percentages']
print('(Table 1a) The winning percentages of each team in total:')
print(total_win_team)


#%%
#2 Q1-b.

hk_sk = pd.merge(hk_win_pct, sk_win_pct, on='year', how = 'outer')
fr_us = pd.merge(fr_win_pct, us_win_pct, on='year', how = 'outer')
ar_fr_us = pd.merge(fr_us, ar_win_pct, on = 'year', how = 'outer')
countries = pd.merge(hk_sk, ar_fr_us, on = 'year', how = 'outer')

#countries_pivot = pd.pivot_table(countries, index= ['year'], values=['Hong Kong', 'South Korea', 'France', 'United States', 'Argentina'])

#%%

#2 Q1-c.
import matplotlib.pyplot as plt
import numpy as np

# size, width of bar
fig, ax = plt.subplots(figsize=(20,6))
bar_width = 0.15

index = np.arange(10)

# countries' winning pct by year. 0.4 alpha
plt.bar
b1 = plt.bar(index, countries['Hong Kong'], bar_width, alpha=0.4, color='red', label='Hong Kong')
b2 = plt.bar(index + bar_width, countries['South Korea'], bar_width, alpha=0.4, color='blue', label='South Korea')
b3 = plt.bar(index + 2 * bar_width, countries['France'], bar_width, alpha=0.4, color='green', label='France')
b3 = plt.bar(index + 3 * bar_width, countries['United States'], bar_width, alpha=0.4, color='yellow', label='United States')
b3 = plt.bar(index + 4 * bar_width, countries['Argentina'], bar_width, alpha=0.4, color='grey', label='Argentina')

# Adjust the x-axis position to center and match text on the x-axis with year information
plt.xticks(np.arange(0, 10, 1), labels=([2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]))
    
# set xlabel, ylabel and legend
plt.xlabel('year', size = 13)
plt.ylabel('winning percentage', size = 13)
plt.legend()
plt.show()


#%%

# Q1-d.

"""
Among the five countries, Hong Kong's winning percentage was the lowest from 2011 to 2020, except for 2015 and 2018. 
Among the five countries, France ranked first in the winning percentage, and the winning percentage was the highest from 2016 to 2020.

Hong Kong's winning percentage was the lowest in 2011, followed by United States, Argentina and France.
In 2011, South Korea recorded the highest winning percentage of 0.59.

In 2012, Hong Kong's winning percentage was the lowest, followed by South Korea, France, and United States. 
Argentina's winning percentage was the highest at about 0.73.

In 2013, Hong Kong's winning percentage was the lowest, followed by South Korea, France, and Argentina.
United States' winning percentage was the highest at 0.68.

In 2014, Hong Kong's winning percentage was the lowest, followed by South Korea and United States,
and France and Argentina's winning percentage were same. 

Argentina's winning percentage was the lowest in 2015, followed by United States, Hong Kong and France.
South Korea's winning percentage was the highest at 0.8.

In 2016, Hong Kong's winning percentage was the lowest, followed by United States, Argentina, and South Korea.
France recorded a high winning percentage of 0.76.

In 2017, Hong Kong's winning percentage was the lowest, followed by South Korea, United States, and Argentina.
France recorded a high winning percentage of 0.64.US and Argentina recorded the same winning percentage of 0.5.

In 2018, United States had the lowest winning percentage, followed by Hong Kong, South Korea and Argentina.
Meanwhile, France recorded a high winning percentage for the third consecutive year at 0.67.

In 2019, Hong Kong's winning percentage was the lowest, followed by Argentina, United States, and South Korea.
Meanwhile, France recorded a high winning percentage of 0.8 for the fourth consecutive year.

There is no data from Hong Kong in 2020, and South Korea's winning percentage was the highest among the remaining four countries. 
The rest of the countries (United States, Argentina and France) recorded the same winning percentage of 0.75.
"""

#%%

#2 Q2-a.

hkhome = new_df[(new_df['home_team'] == 'Hong Kong')]
hkaway = new_df[(new_df['away_team'] == 'Hong Kong')]
hkmatch = (hkhome.groupby('year')['home_team'].size()) | (hkaway.groupby('year')['away_team'].size())
hkgoal = (hkhome.groupby('year')['home_score'].sum())+(hkaway.groupby('year')['away_score'].sum())
hkavegoal = hkgoal/hkmatch
print(hkavegoal)

skhome = new_df[(new_df['home_team'] == 'South Korea')]
skaway = new_df[(new_df['away_team'] == 'South Korea')]
skmatch = (skhome.groupby('year')['home_team'].size()) | (skaway.groupby('year')['away_team'].size())
skgoal = (skhome.groupby('year')['home_score'].sum())+(skaway.groupby('year')['away_score'].sum())
skavegoal = skgoal/skmatch
print(skavegoal)

frhome = new_df[(new_df['home_team'] == 'France')]
fraway = new_df[(new_df['away_team'] == 'France')]
frmatch = (frhome.groupby('year')['home_team'].size()) | (fraway.groupby('year')['away_team'].size())
frgoal = (frhome.groupby('year')['home_score'].sum())+(fraway.groupby('year')['away_score'].sum())
fravegoal = frgoal/frmatch
print(fravegoal)

ushome = new_df[(new_df['home_team'] == 'United States')]
usaway = new_df[(new_df['away_team'] == 'United States')]
usmatch = (ushome.groupby('year')['home_team'].size()) | (usaway.groupby('year')['away_team'].size())
usgoal = (ushome.groupby('year')['home_score'].sum())+(usaway.groupby('year')['away_score'].sum())
usavegoal = usgoal/usmatch
print(usavegoal)


arghome = new_df[(new_df['home_team'] == 'Argentina')]
argaway = new_df[(new_df['away_team'] == 'Argentina')]
argmatch = (arghome.groupby('year')['home_team'].size()) | (argaway.groupby('year')['away_team'].size())
arggoal = (arghome.groupby('year')['home_score'].sum())+(argaway.groupby('year')['away_score'].sum())
argavegoal = arggoal/argmatch
print(argavegoal)



#%%
table2 = pd.concat([hkavegoal, skavegoal, fravegoal, usavegoal, argavegoal], axis=1)
table2new = table2.set_axis(['Hong Kong', 'South Korea', 'France', 'United States', 'Argentina'], axis=1, inplace=False) 
print(table2new)






#%%
#2 Q2-b.

import matplotlib.pyplot as plt

plt.title('Hong Kong Win Rate to Goals')
plt.xlabel('Win Rate')
plt.ylabel('Goals')
plt.grid()
plt.scatter(hk_win_pct,hkavegoal, c ="r",linewidths = 2, marker ="D", edgecolor ="b", s = 70, alpha=0.5)
plt.show()

plt.title('South Korea Win Rate to Goals')
plt.xlabel('Win Rate')
plt.ylabel('Goals')
plt.grid()
plt.scatter(sk_win_pct,skavegoal, c ="r",linewidths = 2, marker ="D", edgecolor ="k", s = 70, alpha=0.5)
plt.show()

plt.title('France Win Rate to Goals')
plt.xlabel('Win Rate')
plt.ylabel('Goals')
plt.grid()
plt.scatter(fr_win_pct,fravegoal, c ="r",linewidths = 2, marker ="D", edgecolor ="y", s = 70, alpha=0.5)
plt.show()

plt.title('United States Win Rate to Goals')
plt.xlabel('Win Rate')
plt.ylabel('Goals')
plt.grid()
plt.scatter(us_win_pct,usavegoal, c ="r",linewidths = 2, marker ="D", edgecolor ="r", s = 70, alpha=0.5)
plt.show()
    
plt.title('Argentina Win Rate to Goals')
plt.xlabel('Win Rate')
plt.ylabel('Goals')
plt.grid()
plt.scatter(ar_win_pct,argavegoal, c ="r",linewidths = 2, marker ="D", edgecolor ="g", s = 70, alpha=0.5)
plt.show()

#%%

#Q2-c

""" By the results of Question 2a and 2b, it is shown that there is a positive relationship between the average number of goals per match 
and its winning percentage in general. With these five selected teams, when the y-axis of the scatter diagram is higher, the x-axis follows 
and distributes mostly on the right side of the graph. Comparing the results above, teams with higher average goals often have a bigger 
chance to win the match. More specifically, Team Hong Kong and Team United States have shown a more significant positive linear 
correlation, as the scatter plots are mainly distributed on an upward-sloping straight regression line. Yet, the other three teams have 
been found with different results, on those scatter diagrams it is difficult to discover the correlation relationship between the goals and 
win rate of teams as the plots are distributed in a non-linear shape. There is still a relationship between variables but in a non-linear
shape. Therefore, it can be grouped as a non-linear relationship between Team France, South Korea, and Argentina. Overall, it shows the 
significance of goals in every match, the number of goals per match mainly impacts the winning percentages of each team in every match."""


#%%
#Q2-d

"""One of the primary reasons is the disparity in talent produced by each national team. Some European countries may allocate 
comparatively more resources to train and provide more opportunities for young talents, resulting in an increase in overall strength 
and competitiveness of national teams in it.  France, for example, has a well-known professional football league known as Ligue 1. 
Paris Saint-Germain Football Club (PSG), one of its teams, discovered and developed a young talented football player, Kylian Mbappe.
Mbappe is thus a member of the France national team, which helped France winning the FIFA World Cup in 2016. However, when compared to 
European teams, Hong Kong would be a weaker team due to a lack of talent. Yet, when compared to European teams, Hong Kong would be a weaker 
team due to a lack of talent, resulting in a lower overall winning percentage.

Furthermore, the regional football communities vary, which cause different winning results of national teams. It is known that 
football has become a significant component in several countries’ culture. For example, it is highly uncommon to meet someone who has
not played soccer at least once in their life in Argentina. Most guys play with friends on a regular basis, and during their formative 
years. They also have fantastic role models to imitate, such as Diego Maradona, and Lionel Messi, who inspire them to feel that we can be
as good as they were or are in the globe and in soccer history. Football is all around in the country, adolescents are mostly inspired to 
pursue their dream which continuously motivate the development of football in those countries. However, the public promotion of football 
may be lacking in the Asian Area. Only a small number of professional football players are allowed to play in developed leagues, and there 
are not enough football fields in these nations to facilitate professional players' training. Son Heung Min and Kim Min Jae are two examples 
of the few South Korean players who could play in European Leagues. As a result, given how football is promoted in each country, the correlation 
results are easy to see."""

#%%
#Q3. 
# index in order from 0

#hk.reset_index(inplace=True)
#sk.reset_index(inplace=True)
#fr.reset_index(inplace=True)
#us.reset_index(inplace=True)
#ar.reset_index(inplace=True)


#Hong Kong

conditions_hk = [
    (hk['home_team'] == 'Hong Kong') & (hk['home_score']>hk['away_score']),
    (hk['away_team'] == 'Hong Kong') & (hk['home_score']<hk['away_score']),
    (hk['home_team'] == 'Hong Kong') & (hk['home_score']<hk['away_score']),
    (hk['away_team'] == 'Hong Kong') & (hk['home_score']>hk['away_score']),
    (hk['home_team'] == 'Hong Kong') & (hk['home_score']==hk['away_score']),
    (hk['away_team'] == 'Hong Kong') & (hk['home_score']==hk['away_score']),]

vals = ['Win', 'Win', 'Lose', 'Lose', 'Neutral', 'Neutral']

hk['result'] = np.select(conditions_hk, vals)


result_hk=[0]*6 # 0:승승승  1:승승패  2:승패승/패승승 3:승패패/패승패 4:패패승 5:패패패 승:win / 패:lose

prev=0  # 이전겜 결과
preprev=0  # 전전겜 결과
for index, row in hk.iterrows():    #hk데이터프레임의 열 수만큼 포문 돌리기
    if(hk['result'][index] == 'Neutral'):
        preprev = prev
        prev = 0
    elif(hk['result'][index]=='Win'):  #현재판의 결과
        if (preprev == 0 or prev == 0):
            pass
        elif(preprev==1 and prev==1): # win win win holyshit
            result_hk[0]+=1
        elif((preprev==2 and prev==1) or (preprev==1 and prev==2)): # lost/win win/lost win
            result_hk[2]+=1
        else: #lost lost win
            result_hk[4]+=1
        preprev=prev #전판의 결과는 이제 전전판의 결과가 됨
        prev=1 #현재판의 결과는 이제 전판의 결과가 됨
    else:  # lost
        if (preprev == 0 or prev == 0):
            pass
        elif(preprev==1 and prev==1): # win win lost
            result_hk[1]+=1
        elif((preprev==2 and prev==1) or (preprev==1 and prev==2)): # lost/win win/lost lost
            result_hk[3]+=1
        else: #lost lost lost
            result_hk[5]+=1    
        preprev=prev
        prev=2    

# South Korea
conditions_sk = [
    (sk['home_team'] == 'South Korea') & (sk['home_score']>sk['away_score']),
    (sk['away_team'] == 'South Korea') & (sk['home_score']<sk['away_score']),
    (sk['home_team'] == 'South Korea') & (sk['home_score']<sk['away_score']),
    (sk['away_team'] == 'South Korea') & (sk['home_score']>sk['away_score']),
    (sk['home_team'] == 'South Korea') & (sk['home_score']==sk['away_score']),
    (sk['away_team'] == 'South Korea') & (sk['home_score']==sk['away_score']),]

vals = ['Win', 'Win', 'Lose', 'Lose', 'Neutral', 'Neutral']



sk['result'] = np.select(conditions_sk, vals)


result_sk=[0]*6 # 0:승승승  1:승승패  2:승패승/패승승 3:승패패/패승패 4:패패승 5:패패패 승:win / 패:lose

prev=0  # 이전겜 결과
preprev=0  # 전전겜 결과
for index, row in sk.iterrows():    #hk데이터프레임의 열 수만큼 포문 돌리기
    if(sk['result'][index] == 'Neutral'):
        preprev = prev
        prev = 0
    elif(sk['result'][index]=='Win'):  #현재판의 결과
        if (preprev == 0 or prev == 0):
            pass
        elif(preprev==1 and prev==1): # win win win holyshit
            result_sk[0]+=1
        elif((preprev==2 and prev==1) or (preprev==1 and prev==2)): # lost/win win/lost win
            result_sk[2]+=1
        else: #lost lost win
            result_sk[4]+=1
        preprev=prev #전판의 결과는 이제 전전판의 결과가 됨
        prev=1 #현재판의 결과는 이제 전판의 결과가 됨
    else:  # lost
        if (preprev == 0 or prev == 0):
            pass
        elif(preprev==1 and prev==1): # win win lost
            result_sk[1]+=1
        elif((preprev==2 and prev==1) or (preprev==1 and prev==2)): # lost/win win/lost lost
            result_sk[3]+=1
        else: #lost lost lost
            result_sk[5]+=1    
        preprev=prev
        prev=2    

# United States
conditions_us = [
    (us['home_team'] == 'United States') & (us['home_score']>us['away_score']),
    (us['away_team'] == 'United States') & (us['home_score']<us['away_score']),
    (us['home_team'] == 'United States') & (us['home_score']<us['away_score']),
    (us['away_team'] == 'United States') & (us['home_score']>us['away_score']),
    (us['home_team'] == 'United States') & (us['home_score']==us['away_score']),
    (us['away_team'] == 'United States') & (us['home_score']==us['away_score']),]

vals = ['Win', 'Win', 'Lose', 'Lose', 'Neutral', 'Neutral']


us['result'] = np.select(conditions_us, vals)


result_us=[0]*6 # 0:승승승  1:승승패  2:승패승/패승승 3:승패패/패승패 4:패패승 5:패패패 승:win / 패:lose

prev=0  # 이전겜 결과
preprev=0  # 전전겜 결과
for index, row in us.iterrows():    #hk데이터프레임의 열 수만큼 포문 돌리기
    if(us['result'][index] == 'Neutral'):
        preprev = prev
        prev = 0
    elif(us['result'][index]=='Win'):  #현재판의 결과
        if (preprev == 0 or prev == 0):
            pass
        elif(preprev==1 and prev==1): # win win win holyshit
            result_us[0]+=1
        elif((preprev==2 and prev==1) or (preprev==1 and prev==2)): # lost/win win/lost win
            result_us[2]+=1
        else: #lost lost win
            result_us[4]+=1
        preprev=prev #전판의 결과는 이제 전전판의 결과가 됨
        prev=1 #현재판의 결과는 이제 전판의 결과가 됨
    else:  # lost
        if (preprev == 0 or prev == 0):
            pass
        elif(preprev==1 and prev==1): # win win lost
            result_us[1]+=1
        elif((preprev==2 and prev==1) or (preprev==1 and prev==2)): # lost/win win/lost lost
            result_us[3]+=1
        else: #lost lost lost
            result_us[5]+=1    
        preprev=prev
        prev=2    
        

conditions_fr = [
    (fr['home_team'] == 'France') & (fr['home_score']>fr['away_score']),
    (fr['away_team'] == 'France') & (fr['home_score']<fr['away_score']),
    (fr['home_team'] == 'France') & (fr['home_score']<fr['away_score']),
    (fr['away_team'] == 'France') & (fr['home_score']>fr['away_score']),
    (fr['home_team'] == 'France') & (fr['home_score']==fr['away_score']),
    (fr['away_team'] == 'France') & (fr['home_score']==fr['away_score']),]
fr['result'] = np.select(conditions_fr, vals)
result_fr=[0]*6 # 0:승승승  1:승승패  2:승패승/패승승 3:승패패/패승패 4:패패승 5:패패패 승:win / 패:lose

prev=0  # 이전겜 결과
preprev=0  # 전전겜 결과
for index, row in fr.iterrows():    #hk데이터프레임의 열 수만큼 포문 돌리기
    if(fr['result'][index] == 'Neutral'):
        preprev = prev
        prev = 0
    elif(fr['result'][index]=='Win'):  #현재판의 결과
        if (preprev == 0 or prev == 0):
            pass
        elif(preprev==1 and prev==1): # win win win holyshit
            result_fr[0]+=1
        elif((preprev==2 and prev==1) or (preprev==1 and prev==2)): # lost/win win/lost win
            result_fr[2]+=1
        else: #lost lost win
            result_fr[4]+=1
        preprev=prev #전판의 결과는 이제 전전판의 결과가 됨
        prev=1 #현재판의 결과는 이제 전판의 결과가 됨
    else:  # lost
        if (preprev == 0 or prev == 0):
            pass
        elif(preprev==1 and prev==1): # win win lost
            result_fr[1]+=1
        elif((preprev==2 and prev==1) or (preprev==1 and prev==2)): # lost/win win/lost lost
            result_fr[3]+=1
        else: #lost lost lost
            result_fr[5]+=1
        preprev=prev
        prev=2

#Argentina
conditions_ar = [
    (ar['home_team'] == 'Argentina') & (ar['home_score']>ar['away_score']),
    (ar['away_team'] == 'Argentina') & (ar['home_score']<ar['away_score']),
    (ar['home_team'] == 'Argentina') & (ar['home_score']<ar['away_score']),
    (ar['away_team'] == 'Argentina') & (ar['home_score']>ar['away_score']),
    (ar['home_team'] == 'Argentina') & (ar['home_score']==ar['away_score']),
    (ar['away_team'] == 'Argentina') & (ar['home_score']==ar['away_score']),]

ar['result'] = np.select(conditions_ar, vals)

result_ar=[0]*6 # 0:승승승  1:승승패  2:승패승/패승승 3:승패패/패승패 4:패패승 5:패패패 승:win / 패:lose

prev=0  # 이전겜 결과
preprev=0  # 전전겜 결과
for index, row in ar.iterrows():    #hk데이터프레임의 열 수만큼 포문 돌리기
    if(ar['result'][index] == 'Neutral'):
        preprev = prev
        prev = 0
    elif(ar['result'][index]=='Win'):  #현재판의 결과
        if (preprev == 0 or prev == 0):
            pass
        elif(preprev==1 and prev==1): # win win win holyshit
            result_ar[0]+=1
        elif((preprev==2 and prev==1) or (preprev==1 and prev==2)): # lost/win win/lost win
            result_ar[2]+=1
        else: #lost lost win
            result_ar[4]+=1
        preprev=prev #전판의 결과는 이제 전전판의 결과가 됨
        prev=1 #현재판의 결과는 이제 전판의 결과가 됨
    else:  # lost
        if (preprev == 0 or prev == 0):
            pass
        elif(preprev==1 and prev==1): # win win lost
            result_ar[1]+=1
        elif((preprev==2 and prev==1) or (preprev==1 and prev==2)): # lost/win win/lost lost
            result_ar[3]+=1
        else: #lost lost lost
            result_ar[5]+=1
        preprev=prev
        prev=2


all = [[result_hk],[result_sk],[result_us],[result_fr]]

result_all = pd.DataFrame([x for x in zip(result_hk, result_sk, result_us, result_fr, result_ar )])
result_all.insert(0, 'result', ['www', 'wwl', 'wlw/lww', 'wll/lwl', 'llw', 'lll'])
result_all.columns = ['result', 'Hong Kong', 'South Korea', 'United States', 'France','Argentina']
result_all['Total'] = result_all['Hong Kong'] + result_all['South Korea'] + result_all['United States'] + result_all['France'] + result_all['Argentina']



#a P(www | www+wwl)
awinning = result_all['Total'][0] / (result_all['Total'][0]+result_all['Total'][1])
print(awinning) #0.7461538461538462

#b P(wlw+lww | wlw+lww+wll+lwl)
bwinning = result_all['Total'][2] / (result_all['Total'][2]+result_all['Total'][3])
print(bwinning) #0.6666666666666666

#c P(llw | llw+lll)
cwinning = result_all['Total'][4] / (result_all['Total'][4]+result_all['Total'][5])
print(cwinning) #0.6129032258064516

#d.

"""
If one team wins the previous two matches, the winning percentage for the next match becomes 0.74. 
If one team won one of the previous two matches, the winning percentage for the next match becomes 0.67.
If one team lost the previous two matches, the winning percentage for the next match becomes 0.61.

In conclusion, the winning percentage for the next match is affected by the previous two games, 
and the probability of winning the next match decrease when they lost for the last two previous matches. 
"""


#%%
#Q4. 
#Finding the number of wins by a large margin(>=3) of selected teams using the ten years data.

hkbigwin1 = hkhome[hkhome['home_score'] - hkhome['away_score'] >= 3]
hkbigwin2 = hkaway[hkaway['away_score'] - hkaway['home_score'] >= 3]
hktotalbigwin1 = hkbigwin1.groupby('year')['home_team'].size() 
hktotalbigwin2 = hkbigwin2.groupby('year')['away_team'].size()
hktotalbigwin = pd.concat([hktotalbigwin1,hktotalbigwin2],axis=1)



skbigwin1 = skhome[hkhome['home_score'] - skhome['away_score'] >= 3]
skbigwin2 = skaway[skaway['away_score'] - skaway['home_score'] >= 3]
sktotalbigwin1 = skbigwin1.groupby('year')['home_team'].size() 
sktotalbigwin2 = skbigwin2.groupby('year')['away_team'].size()
sktotalbigwin = pd.concat([sktotalbigwin1,sktotalbigwin2],axis=1)

usbigwin1 = ushome[ushome['home_score'] - ushome['away_score'] >= 3]
usbigwin2 = usaway[usaway['away_score'] - usaway['home_score'] >= 3]
ustotalbigwin1 = usbigwin1.groupby('year')['home_team'].size() 
ustotalbigwin2 = usbigwin2.groupby('year')['away_team'].size()
ustotalbigwin = pd.concat([ustotalbigwin1,ustotalbigwin2],axis=1)


frbigwin1 = frhome[frhome['home_score'] - frhome['away_score'] >= 3]
frbigwin2 = fraway[fraway['away_score'] - fraway['home_score'] >= 3]
frtotalbigwin1 = frbigwin1.groupby('year')['home_team'].size() 
frtotalbigwin2 = frbigwin2.groupby('year')['away_team'].size()
frtotalbigwin = pd.concat([frtotalbigwin1,frtotalbigwin2],axis=1)

argbigwin1 = arghome[arghome['home_score'] - arghome['away_score'] >= 3]
argbigwin2 = argaway[argaway['away_score'] - argaway['home_score'] >= 3]
argtotalbigwin1 = argbigwin1.groupby('year')['home_team'].size() 
argtotalbigwin2 = argbigwin2.groupby('year')['away_team'].size()
argtotalbigwin = pd.concat([argtotalbigwin1,argtotalbigwin2],axis=1)




hktotalbigwin3 = hktotalbigwin.fillna(0)
sktotalbigwin3 = sktotalbigwin.fillna(0)
ustotalbigwin3 = ustotalbigwin.fillna(0)
frtotalbigwin3 = frtotalbigwin.fillna(0)
argtotalbigwin3 = argtotalbigwin.fillna(0)

hktotalbigwin3['sum'] = hktotalbigwin3['home_team'] + hktotalbigwin3['away_team']
sktotalbigwin3['sum'] = sktotalbigwin3['home_team'] + sktotalbigwin3['away_team']
ustotalbigwin3['sum'] = ustotalbigwin3['home_team'] + ustotalbigwin3['away_team']
frtotalbigwin3['sum'] = frtotalbigwin3['home_team'] + frtotalbigwin3['away_team']
argtotalbigwin3['sum'] = argtotalbigwin3['home_team'] + argtotalbigwin3['away_team']



hksum = hktotalbigwin3['sum'].values.tolist()
sksum = sktotalbigwin3['sum'].values.tolist()
ussum = ustotalbigwin3['sum'].values.tolist()
frsum = frtotalbigwin3['sum'].values.tolist()
argsum = argtotalbigwin3['sum'].values.tolist()


# giving the item to be inserted
insertItem = "0"
insertItem2 = "1"
# giving the index value at which the item to be inserted
indexValue0 = 0
indexValue1 = 1
indexValue2 = 2
indexValue3 = 3
indexValue4 = 4
indexValue5 = 5
indexValue6 = 6
indexValue7 = 7
indexValue8 = 8
indexValue9 = 9 
# inserting the given list item at the specified index(here 2)
hksum.insert(indexValue2, insertItem)
hksum.insert(indexValue3, insertItem)
hksum.insert(indexValue5, insertItem)
hksum.insert(indexValue8, insertItem)
hksum.insert(indexValue9, insertItem)

sksum.insert(indexValue0, insertItem)
sksum.insert(indexValue2, insertItem)
sksum.insert(indexValue3, insertItem)
sksum.insert(indexValue5, insertItem)
sksum.insert(indexValue7, insertItem)
sksum.insert(indexValue8, insertItem)
sksum.insert(indexValue9, insertItem)

ussum.insert(indexValue0, insertItem)
ussum.insert(indexValue3, insertItem)

frsum.insert(indexValue7, insertItem)

del argsum[8]
argsum.insert(indexValue6, insertItem2)
argsum.insert(indexValue9, insertItem)


plotdata = pd.DataFrame({"Hong Kong": hksum,"South Korea": sksum,"United States":ussum,"France":frsum,"Argentina":argsum},index=["2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"])
plotdata['Hong Kong']= plotdata['Hong Kong'].astype(float)
plotdata['South Korea']= plotdata['South Korea'].astype(float)
plotdata['France']= plotdata['France'].astype(float)
plotdata['United States']= plotdata['United States'].astype(float)
plotdata['Argentina']= plotdata['Argentina'].astype(float)
plotdata.plot(kind="bar")
plt.title("Matches Win By a Large Margin (>=3)")
plt.xlabel("Year")
plt.ylabel("Number of Matches")



#%%
#Q5.

# comparing the winning percentage if the team plays in their home country (==home team) 
# and if they plays in other country


#hk home
hkhomematch = hkhome.groupby('year')['home_team'].size()
hkhomewin = hkhome[hkhome['home_score'] > hkhome['away_score']]
hkhomewinyear = hkhomewin.groupby('year')['home_team'].size()
hkhome_pct = hkhomewinyear / hkhomematch
hkhome_pct = hkhome_pct.fillna(0)
#hk away
hkawaymatch = hkaway.groupby('year')['away_team'].size()
hkawaywin = hkaway[hkaway['away_score'] > hkaway['home_score']]
hkawaywinyear = hkawaywin.groupby('year')['away_team'].size()
hkaway_pct = hkawaywinyear / hkawaymatch
hkaway_pct = hkaway_pct.fillna(0)

#sk home
skhomematch = skhome.groupby('year')['home_team'].size()
skhomewin = skhome[skhome['home_score'] > skhome['away_score']]
skhomewinyear = skhomewin.groupby('year')['home_team'].size()
skhome_pct = skhomewinyear / skhomematch
skhome_pct = skhome_pct.fillna(0)
#sk away
skawaymatch = skaway.groupby('year')['away_team'].size()
skawaywin = skaway[skaway['away_score'] > skaway['home_score']]
skawaywinyear = skawaywin.groupby('year')['away_team'].size()
skaway_pct = skawaywinyear / skawaymatch
skaway_pct = skaway_pct.fillna(0)

#fr home
frhomematch = frhome.groupby('year')['home_team'].size()
frhomewin = frhome[frhome['home_score'] > frhome['away_score']]
frhomewinyear = frhomewin.groupby('year')['home_team'].size()
frhome_pct = frhomewinyear / frhomematch
frhome_pct = frhome_pct.fillna(0)
#fr away
frawaymatch = fraway.groupby('year')['away_team'].size()
frawaywin = fraway[fraway['away_score'] > fraway['home_score']]
frawaywinyear = frawaywin.groupby('year')['away_team'].size()
fraway_pct = frawaywinyear / frawaymatch
fraway_pct = fraway_pct.fillna(0)

#us home
ushomematch = ushome.groupby('year')['home_team'].size()
ushomewin = ushome[ushome['home_score'] > ushome['away_score']]
ushomewinyear = ushomewin.groupby('year')['home_team'].size()
ushome_pct = ushomewinyear / ushomematch
ushome_pct = ushome_pct.fillna(0)
#us away
usawaymatch = usaway.groupby('year')['away_team'].size()
usawaywin = usaway[usaway['away_score'] > usaway['home_score']]
usawaywinyear = usawaywin.groupby('year')['away_team'].size()
usaway_pct = usawaywinyear / usawaymatch
usaway_pct = usaway_pct.fillna(0)

#ar home
arhomematch = arghome.groupby('year')['home_team'].size()
arhomewin = arghome[arghome['home_score'] > arghome['away_score']]
arhomewinyear = arhomewin.groupby('year')['home_team'].size()
arhome_pct = arhomewinyear / arhomematch
arhome_pct = arhome_pct.fillna(0)
#ar away
arawaymatch = argaway.groupby('year')['away_team'].size()
arawaywin = argaway[argaway['away_score'] > argaway['home_score']]
arawaywinyear = arawaywin.groupby('year')['away_team'].size()
araway_pct = arawaywinyear / arawaymatch
araway_pct = araway_pct.fillna(0)

#comparing percentages between when team plays in their home country and other country by year

plothk = pd.merge(hkhome_pct, hkaway_pct, on = 'year', how = 'outer')
plothk.columns = ['playing in home country', 'playing in other country']
plothk.plot(kind = 'bar')
plt.xlabel('year')
plt.ylabel('winning pct')
plt.title('comparing winning pct by venue_Hong Kong')


plotsk = pd.merge(skhome_pct, skaway_pct, on = 'year', how = 'outer')
plotsk.columns = ['playing in home country', 'playing in other country']
plotsk.plot(kind = 'bar')
plt.xlabel('year')
plt.ylabel('winning pct')
plt.title('comparing winning pct by venue_South Korea')

plotus = pd.merge(ushome_pct, usaway_pct, on = 'year', how = 'outer')
plotus.columns = ['playing in home country', 'playing in other country']
plotus.plot(kind = 'bar')
plt.xlabel('year')
plt.ylabel('winning pct')
plt.title('comparing winning pct by venue_United States')

plotfr = pd.merge(frhome_pct, fraway_pct, on = 'year', how = 'outer')
plotfr.columns = ['playing in home country', 'playing in other country']
plotfr.plot(kind = 'bar')
plt.xlabel('year')
plt.ylabel('winning pct')
plt.title('comparing winning pct by venue_France')

plotar = pd.merge(arhome_pct, araway_pct, on = 'year', how = 'outer')
plotar.columns = ['playing in home country', 'playing in other country']
plotar.plot(kind = 'bar')
plt.xlabel('year')
plt.ylabel('winning pct')
plt.title('comparing winning pct by venue_Argentina')


"""For Hong Kong and US, playing in home country increases the winning percentage in the whole years.
For South Korea, playing in home country increases the probability to win in whole years excpet for 2014.
For France, winning percentage usually increases when they play game in home country, but in 2011, 2020 winning percentage when the playing in other country is higher.
For Argentina, winning percentage usually increases when they play game in home country, but in 2017, 2019, 2020 winning percentage when the playing in other country is higher."""


