import datetime


# called in every iteration separately because the current time
# may significantly change between the first iteration and the millionth
def calc_time_ago(timedelta):
    return datetime.datetime.utcnow() - timedelta


# these take an object (Error or Redirect), and check the registration time
# against the required timedelta
def less_than_day(timestamp):
    return timestamp.registered_at > calc_time_ago(datetime.timedelta(days=1))


def less_than_hour(timestamp):
    return timestamp.registered_at > calc_time_ago(datetime.timedelta(hours=1))


def less_than_minute(timestamp):
    return timestamp.registered_at > calc_time_ago(datetime.timedelta(minutes=1))