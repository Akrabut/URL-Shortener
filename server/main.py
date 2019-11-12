from app import app


# custom errors
# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404

# @app.errorhandler(404)
# def not_found(error):
#     resp = make_response(render_template('error.html'), 404)
#     resp.headers['X-Something'] = 'A value'
#     return resp
