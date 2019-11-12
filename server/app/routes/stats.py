from .. import app
from ..models.redirect import Redirect
from ..models.error import Error
from flask import jsonify
from ..helpers import stats_helper


@app.route('/stats')
def display_statistics():
    reds = stats_helper.model_stats(Redirect)
    errs = stats_helper.model_stats(Error)
    return jsonify({
        'all_reds': reds['all'],
        'day_reds': reds['day'],
        'hour_reds': reds['hour'],
        'minute_reds': reds['minute'],
        'all_errs': errs['all'],
        'day_errs': errs['day'],
        'hour_errs': errs['hour'],
        'minute_errs': errs['minute']
    })
