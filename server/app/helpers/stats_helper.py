def model_stats(model):
    return {'all': model.all(), 'day': model.day_ago(), 'hour': model.hour_ago(), 'minute': model.minute_ago()}