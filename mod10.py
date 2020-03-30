# Ethan Martin
# Module 10

# Import packages
import numpy as np
import pandas as pd
# import ggplot
import matplotlib.pyplot as plt

# # Aquire DATA
# # This is state by state data on corona virus cases
#
# df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
#
# # Examine the data
# print(df[0:25])
#
#
# # print(df.shape)
#
# # Change the format of the date column
# df['date'] = pd.to_datetime(df.date)
# print(df.dtypes)
# print(df[0:25])
#
# # Get rid of the state information since I want to examine the data for the entire US

# df.drop(['state', 'fips'], axis=1, inplace=True)
# print(df[0:25])
#
# # Try to group the data

# date_grp = df.groupby('date')['cases'].apply(', '.join).reset_index()
# print (date_grp)

# for date, date_df in date_grp:
#     print(date)
#     print(date_df[0:2])

# # print(df2.max())
#

# # Can not get this to work the way I want it to, time to do it the simpler way.


# Create a Data Frame
covid = [ ('3/2', 62, 0),
             ('3/3', 64, 2),
             ('3/4', 108, 6),
             ('3/5', 129, 9),
             ('3/6', 148, 10),
             ('3/7', 213, 11),
             ('3/8', 213, 11),
             ('3/9', 213, 11),
             ('3/10', 472, 19),
             ('3/11', 696, 25),
             ('3/12', 987, 29),
             ('3/13', 1264, 36),
             ('3/14', 1678, 41),
             ('3/15', 1678, 41),
             ('3/16', 4567, 85),
             ('3/17', 6349, 98),
             ('3/18', 9273, 150),
             ('3/19', 13726, 201),
             ('3/20', 19393, 256),
             ('3/21', 25772, 311),
             ('3/22', 33889, 428),
             ('3/23', 43874, 558),
             ('3/24', 53794, 705),
             ('3/25', 64675, 910),
             ('3/26', 83545, 1201),
             ('3/27', 100390, 1543),
             ('3/28', 123311, 2211)
             ]

covid_df = pd.DataFrame(covid, columns = ['Date' , 'CumulativeCases', 'CumulativeDeaths'])
print(covid_df)

# # The first method I tried.

#covid_df.plot(kind='line', x='Date', y='CumulativeCases', color='green')
# plt.plot(covid_df.Date, covid_df.CumulativeCases,
#          covid_df.Date, covid_df.Deaths)
# plt.title('Cumulative Cases of COVID-19 in the US by Day')
# plt.xlabel('Date')
# plt.ylabel('Number of Cases / Deaths')
# plt.show()

# fig_1 = plt.figure(1, figsize=[20, 8])
#
# chart1 = fig_1.add_subplot(211)
# chart2 = fig_1.add_subplot(212)
#
# chart1.plot(covid_df.Date, covid_df.CumulativeCases, 'red',
#             covid_df.Date, covid_df.Deaths, 'green')
# # chart1.scatter(covid_df.Date, covid_df.CumulativeCases, 'k',
# #             covid_df.Date, covid_df.Deaths, 'k')
# plt.title('Cumulative Cases of COVID-19 in the US by Day')
# chart2.plot(covid_df.Date, covid_df.Deaths, 'green')
# plt.title('Cumulative Deaths from COVID-19 in the US by Day')
#
# plt.show()

# # The second, successful method
# Create Plots

plt.style.use("seaborn-dark")
plt.figure(2)

plt.subplot(211)
plt.plot(covid_df.Date, covid_df.CumulativeCases, label='Cumulative Cases')
plt.plot(covid_df.Date, covid_df.CumulativeDeaths, label='Cumulative Deaths', color='red')
# plt.scatter(covid_df.Date, covid_df.CumulativeCases)
# plt.scatter(covid_df.Date, covid_df.CumulativeDeaths, color='red')
plt.title("Cumulative Cases/Deaths From COVID-19 in the US")
plt.xlabel("Date")
plt.ylabel("People")
plt.legend()
plt.grid(True)


plt.subplot(212)
plt.plot(covid_df.Date, covid_df.CumulativeDeaths, label='Cumulative Deaths', color='red')
# plt.scatter(covid_df.Date, covid_df.CumulativeDeaths, color='red')
plt.title("Cumulative Deaths From COVID-19 in the US")
plt.xlabel("Date")
plt.ylabel("People")
# plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Fail to get ggplot to work.  Tried from ggplot import *, tried import ggplot, tried import ggplot as gp.
# It is definitely installed.....sigh.

# p = ggplot(data=covid_df, x=Date, y=CumulativeCases)
# p + geom_line()