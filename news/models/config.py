from orator import DatabaseManager, Model

config = {
    'mysql': {
        'driver': 'mysql',
        'host': '62.109.17.19',
        'database': 'scr',
        'user': 'root',
        'password': 'psGxfQ6jEMpx5s64',
        'prefix': ''
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)

