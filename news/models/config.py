from orator import DatabaseManager, Model

config = {
    'mysql': {
        'driver': 'mysql',
        'host': '',
        'database': '',
        'user': '',
        'password': '',
        'prefix': ''
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)

