from .. import db


# long_url is recieved in a post request from a user, short_url is generated from the
# generated id by encoding it in base64
# also has timestamps because who knows? maybe one day when we scale to oblivion we'll need it
class URL(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    # 10 characters because who knows,
    # maybe one day this URL shortener will dominate the world?
    short_url = db.Column(db.String(10), index=True, unique=True)
    long_url = db.Column(db.String(400), index=True, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())

    # flush the URL object with a long url parameter, generate an id and
    # convert it to base 64 to be used as a short_url
    @staticmethod
    def setup_url(url):
        existing_url = URL.fetch_by_long_url(url.long_url)
        if existing_url:
            return existing_url.short_url
        db.session.add(url)
        # generate an id to be converted to base 64 as a short url
        db.session.flush()
        # the == at the end of the string doesn't help the uniqueness
        # but it needlessly lengthens the string
        from base64 import urlsafe_b64encode
        # this encoding and decoding back and forth is absurd but it
        # just doesn't work otherwise
        short_url = urlsafe_b64encode(str(url.id).encode())
        url.short_url = short_url.decode().replace('=', '')
        db.session.commit()
        return url.short_url

    @staticmethod
    def fetch_by_long_url(url):
        return db.session.query(URL).filter_by(long_url=url).first()

    @staticmethod
    def fetch_by_short_url(url):
        return db.session.query(URL).filter_by(short_url=url).first()

    # def __repr__(self):
    #     # return (f'{self.id} = {self.long_url} -> {self.short_url}')
    #     return self.long_url
