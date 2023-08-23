settings = dict(
    sqlite=dict(provider='sqlite', filename='ponytasker.db', create_db=True),
    mysql=dict(provider='mysql', user='pony', password='pony', host='localhost',
        database='ponytasker')
)
secret_key = 'CHANGE_ME_FOR_PRODUCTION'