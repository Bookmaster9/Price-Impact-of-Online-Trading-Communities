from datetime import time, timedelta

def time_to_milliseconds_one(time):
    """
    Convert a list of datetime.time objects to milliseconds since 09:30:00.
    
    Parameters:
        times (list of datetime.time): List of time objects.
    
    Returns:
        list of int: Milliseconds since 09:30:00 for each time in the input.
    """
    
    total_seconds = time.hour * 3600 + time.minute * 60 + time.second
    return total_seconds * 1000

def time_to_milliseconds_range(times: tuple):
    return time_to_milliseconds_one(times[0]), time_to_milliseconds_one(times[1])

def surrounding_times(input_time):
    """
    Calculate a tuple of two datetime.time objects:
    - The first is the maximum of (input time - 1 minute) and 09:30:00.
    - The second is the minimum of (input time + 5 minutes) and 16:00:00.
    
    Parameters:
        input_time (datetime.time): The input time.
    
    Returns:
        tuple of datetime.time: (adjusted time - 1 minute, adjusted time + 5 minutes).
    """
    # Reference boundary times
    start_time = time(9, 30, 0)  # 09:30:00
    end_time = time(16, 0, 0)   # 16:00:00

    # Convert time to seconds since midnight
    input_seconds = input_time.hour * 3600 + input_time.minute * 60 + input_time.second
    start_seconds = start_time.hour * 3600 + start_time.minute * 60 + start_time.second
    end_seconds = end_time.hour * 3600 + end_time.minute * 60 + end_time.second

    # Calculate seconds for 1 minute before and 5 minutes after
    one_minute_before = max(input_seconds - 60, start_seconds)
    five_minutes_after = min(input_seconds + 300, end_seconds)

    # Convert back to time objects
    first_time = time(one_minute_before // 3600, (one_minute_before % 3600) // 60, one_minute_before % 60)
    second_time = time(five_minutes_after // 3600, (five_minutes_after % 3600) // 60, five_minutes_after % 60)

    return first_time, second_time

def raw_to_date(month, day, year):
    """
    Convert a raw date to a string in the format 'YYYY-MM-DD'.
    
    Parameters:
        month (3 letter abbreviation): The month of the date.
        day (int): The day of the date.
        year (int): The year of the date.
    
    Returns:
        str: The date in the format 'YYYY-MM-DD'.
    """
    months = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    }
    month = months[month]
    return int(f"{year:04d}{month:02d}{day:02d}")