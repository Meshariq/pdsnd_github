#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np


# In[2]:


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# In[3]:


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # asking the user what city he wants to check(chicago, new york city, washington)
    
    city = input('ENTER THE CITY: ')
    while city not in ['chicago', 'new york city', 'washington']:
        city = input ("CHOOSE BETWEEN chicago, new york city OR washington: ").lower()


    # ask the user what month he wants to check or all months(all, january, february, march , april , may , june)
    
    month = input('ENTER MONTH: ').lower()
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input('ENTER MONTH january, february, march , april, may , june: ').lower()

    # ask the user what day of week he wants to display stats for(all, monday, tuesday, ... sunday)
    
    day = input('ENTER DAY : ').lower()

    print('-'*40)
    return city, month, day


# In[4]:


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #loading the chosen file into data frame
    
    df = pd.read_csv('{}.csv'.format(city))

    #convert columns( Start Time and End Time ) into date format
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #extract month from Start Time into new column called month
    
    df['month'] = df['Start Time'].dt.month

    #filtering by month

    if month != 'all':
        # use the index of the months list to get the corresponding int
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        
        #set indices to correspond with the months numbers by adding one to the index
        
        month = months.index(month) + 1

        # filtering by month to create the new dataframe contains months
        
        df = df[df['month'] == month]

    # extract day from Start Time into new column called month
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filtering by day of week and check if it is valid
    
    if day != 'all':
        # filtering by day of week to create the new dataframe
        
        df = df[df['day_of_week'] == day.title()]
        
    return df


# In[5]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # displaying the most common month
    print("The most common month is: ", df['month'].value_counts().idxmax())

    # displaying the most common day of week
    print("The most common day is: ", df['day_of_week'].value_counts().idxmax())

    # displaying the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common hour is: ", df['hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[6]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # displaying most commonly used start station
    print("The most common start station is: ", df ['Start Station'].value_counts().idxmax())

    # displaying most commonly used end station
    print("The most common end station is: ", df['End Station'].value_counts().idxmax())

    # displaying most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip")
    most_common_start_and_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(most_common_start_and_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # displaying total travel time
    total_duration = df['Trip Duration'].sum() / 3600.0
    print("total travel time in hours is: ", total_duration)

    # displaying mean travel time
    
    mean_duration = df['Trip Duration'].mean() / 3600.0
    print("mean travel time in hours is: ", mean_duration)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[10]:


#generating the user's info to analyze it

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # displaying counts of user types
    
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    # displaying counts of gender
    
    user_gender = df['Gender'].value_counts()
    print(user_gender)
    
    # displaying earliest, most recent, and most common year of birth

    earliest_year_of_birth = int(df['Birth Year'].min())
    most_recent_year_of_birth = int(df['Birth Year'].max())
    most_common_year_of_birth = int(df['Birth Year'].value_counts().idxmax())
    print("The earliest year of birth is:",earliest_year_of_birth,
          ", most recent one is:",most_recent_year_of_birth,
           "and the most common one is: ",most_common_year_of_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[11]:


def raw_data (df):
    """Displays the data due filteration.
    5 rows will added in each press"""
    print('press enter to see row data, press no to skip')
    
    x = 0
    while (input()!= 'no'):
        x = x+5
        print(df.head(x))


# In[14]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__ == "__main__":
	main()


# In[ ]:




