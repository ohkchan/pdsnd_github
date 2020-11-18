import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    #list city month day
    cities = ["chicago", "new york city", "washington"]

    months = ["january", "february", "march", "april", "may", "june", "all"]

    day_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for chicago, new york city, or washington? ").lower()
        if city in cities:
            print("Alright")
            break
        else:
            print("Please select from the following: chicago, new york city, or washington. ")


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month - january, february, march, april, may, june or all? ").lower()
        if month in months:
            print("Alright")
            break
        else:
            print("Please select from: all or one month from january, february, march, april, may, june. ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("Which day - monday, tuesday, wednesday, thursday, friday, saturday, sunday or all? ").lower()
        if day in day_of_week:
            print("Alright")
            break
        else:
            print("Please select from: all or monday, tuesday, wednesday, thursday, friday, saturday, sunday. ")

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


    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]

    print("Most Common Month:", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]

    print("Most Common Day of Week:", most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]

    print("Most Common Hour:", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]

    print("Most Common Start Station Used:", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]

    print("Most Common End Station Used:", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_combo = df['Start Station'] + df['End Station']

    print("Most Combination of start and end station:", most_combo.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print("Total travel time:", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print("Mean travel time:", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_types = df['User Type'].value_counts()
        print("Counts of user types:", user_types)
    else:
        print("User type data is not available")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        genders = df['Gender'].value_counts()
        print("Counts of genders:", genders)
    else:
        print("Gender data is not available")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print("The earliest birth year is:", int(earliest_year))
        most_recent_year = df['Birth Year'].max()
        print("The most recent birth year is:", int(most_recent_year))
        most_common_year = df['Birth Year'].mode()[0]
        print("The most common birth year is:", int(most_common_year))
    else:
        print("Birth year data is not available")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # ask for raw data 5 rows at a time
        n = 0
        data = input('\nWould you like to see first 5 rows of data? Type yes or no.\n').lower()

        while True:
            if data == 'no':
                break
            print(df[n:n+5])
            data = input('\nWould you like to see next 5 rows of data? Type yes or no.\n').lower()
            n += 5


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
