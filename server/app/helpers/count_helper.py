# returns the amount of queries in the db
def all_redirects(db_query):
    return db_query.count()


# counts the occurances of db entries that the callback return true for
# ie if callback is all objects that were registered less than a minute ago,
# element_count returns the amount of db entries created less than a minute ago
def element_count(callback, db_query):
    return len(list(filter(callback, db_query())))