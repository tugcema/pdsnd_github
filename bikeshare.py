import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities= {'chicago', 'new york city', 'washington'}

months=['january', 'february', 'march', 'april', 'may', 'june', 'all'] 
#july, august, september, october, november, december is not allowed. Because no data available. 

days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
  
    
    while True:
        city=input("Enter the city name you want to analyze out of chicago, new york city, washington?  \n ").lower()
        if city in cities:
            break
        else:
            print("please enter a city out of given three cities")
          
                 
    
     
    while True:
        month=input("If you  want to filter by month, please Enter a month. You can enter january, february, march, april, may and june. If you do not want to filter by month, enter 'all'. \n ").lower()
        if month in months:
            break
        else:
            print ("please correct your input month.")
        

  
    
    while True:
        day=input("If you  want to filter by day of week, please Enter. If not, enter 'all'. \n ").lower()
        if day in days:
            break
        else:
            print ("please correct your input day.")
            

    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        # months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]

    print('Most Popular Month:', most_common_month)
   
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_day_of_week = df['day_of_week'].mode()[0]
    
    print('Most Common Day of Week:', common_day_of_week)
    
    
    
    df['hour'] = df['Start Time'].dt.hour

    common_start_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station :", most_common_start_station)



    most_common_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station :", most_common_end_station)

   
    
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_station, most_common_end_station))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
   
    total_travel_time=df['Trip Duration'].sum()
    print("Total travel time is {}".format(total_travel_time))
       
    mean_travel_time=df['Trip Duration'].mean()
    print("Mean travel time is {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    user_types = df['User Type'].value_counts()
    print("Count of  user types is \n{}".format(user_types)) 
      

    if('Gender' not in df):
        print("Gender data is not available for the city you choose.")
    else:
        Gender = df['Gender'].value_counts()
        print("Count of gender is \n{}".format(Gender)) 

   
    if('Birth Year' not in df):
        print("Birth Year data is not available for the city you choose.")
    else:
        max_birth_year = df['Birth Year'].max()
        min_birth_year = df['Birth Year'].min()
        most_common_birth_year= df['Birth Year'].mode()[0]
        print("Earliest year of birth is {}".format(min_birth_year))
        print("Most recent year of birth is {}".format(max_birth_year))
        print("Most common year of birth is {}".format(most_common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#display_data function will provide the functionality of showing the raw data. 
def display_data(df):
    user_choice = input('Do you want to see raw data? Enter yes or no.\n')
    row_num = 0
    #user_choices=['yes','no']

    while True:    
        if user_choice.lower() == 'yes':
            print(df.iloc[row_num : row_num + 5])
            row_num += 5
            user_choice  = input('\nDo you want to see more raw data? Enter yes or no.\n')     
        elif user_choice.lower() == 'no':
            break 
        else:
            print("You did not enter an expected choice. \n")
            break
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
