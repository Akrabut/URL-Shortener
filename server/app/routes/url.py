from flask import request, render_template, redirect
from .. import app
from ..models.url import URL
from ..models.redirect import Redirect
from ..models.error import Error


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


# make sure the input is an actual URL
# this is a hand made regexp and is surely not perfect, but the python validators lib
# seems to only validate for URLs starting with http, and your examples should input without it
def check_url(url):
    import re
    url_regex = re.compile(r'(http(s)?:\/\/)?(\w*\.)?\w+\.[a-zA-Z]+(\/.*)*')
    return re.match(url_regex, url)


# avoid cases where both https://www.abc.com, http://www.abc.com and www.abc.com are different DB entries
def pad_url(url):
    if not url.startswith('http'):
        return (f'http://{url}')
    if url.startswith('https'):
        return url.replace('https', 'http')
    return url


def invalid_url(url):
    if not url or len(url) > 400 or not check_url(url):
        return True
    return False


# handles url shortening requests
@app.route('/api/url', methods=['POST'])
def handle_url():
    url_param = request.get_json().get('url_param')
    if invalid_url(url_param):
        # when no parameter was given in the form,
        # or the given parameter is an invalid url
        Error.add_error()
        # return render_template('invalid_url.html', url=url_param), 400
        return (f'{url_param} is not a valid URL'), 400
    short_url = URL.setup_url(URL(long_url=pad_url(url_param)))
    return (f'http://{request.host}/{short_url}')


# handles redirections when user enters domain/some_short_url
@app.route('/<shortened_url>', methods=['GET'])
def handle_redirect(shortened_url):
    fetched_url = URL.fetch_by_short_url(shortened_url)
    if not fetched_url:
        # case when short url is not in the database
        Error.add_error()
        return (f'http://{request.host}/{shortened_url} is an unknown URL'), 404
    Redirect.add_redirect()
    return redirect(fetched_url.long_url)
