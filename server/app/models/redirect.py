from .. import db
import datetime
from ..helpers import count_helper
from ..helpers import time_helper


# is used for the registration of redirects
# can add redirects, and fetch the number of redirects in total, and the number of redirects
# from up to one day ago, one hour ago and one minute ago
class Redirect(db.Model):
    __tablename__ = 'redirects'
    id = db.Column(db.Integer, primary_key=True)
    registered_at = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow())

    @staticmethod
    def add_redirect():
        redirect = Redirect(registered_at=datetime.datetime.utcnow())
        db.session.add(redirect)
        db.session.commit()
        return redirect

    @staticmethod
    def all():
        return count_helper.all_redirects(db.session.query(Redirect))

    @staticmethod
    def day_ago():
        return count_helper.element_count(time_helper.less_than_day, db.session.query(Redirect).all)

    @staticmethod
    def hour_ago():
        return count_helper.element_count(time_helper.less_than_hour, db.session.query(Redirect).all)

    @staticmethod
    def minute_ago():
        return count_helper.element_count(time_helper.less_than_minute, db.session.query(Redirect).all)
