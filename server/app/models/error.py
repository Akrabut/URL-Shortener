from .. import db
import datetime
from ..helpers import count_helper
from ..helpers import time_helper


# is used for the registration of bad requests
# can add errors, and fetch the number of errors in total, and the number of errors
# from up to one day ago, one hour ago and one minute ago
class Error(db.Model):
    __tablename__ = 'errors'
    id = db.Column(db.Integer, primary_key=True)
    registered_at = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow())

    @staticmethod
    def add_error():
        error = Error(registered_at=datetime.datetime.utcnow())
        db.session.add(error)
        db.session.commit()
        return error

    @staticmethod
    def all():
        return count_helper.all_redirects(db.session.query(Error))

    @staticmethod
    def day_ago():
        return count_helper.element_count(time_helper.less_than_day, db.session.query(Error).all)

    @staticmethod
    def hour_ago():
        return count_helper.element_count(time_helper.less_than_hour, db.session.query(Error).all)

    @staticmethod
    def minute_ago():
        return count_helper.element_count(time_helper.less_than_minute, db.session.query(Error).all)
