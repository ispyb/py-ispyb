def get_token(app, permissions, user="test"):
    client = app.test_client()
    api_root = app.config["API_ROOT"]

    response = client.get(
        api_root + "/auth/login", headers={
            "module": "dummy",
            "username": user,
            "password": ",".join(permissions)
        }
    )
    return response.json["token"]


def get_all_permissions_token(app, user="test"):
    return get_token(app, [
        'own_proposals',
        'all_proposals',
        'own_sessions',
        'all_sessions',
        'write_proposals',
        "write_sessions",
        'administrate',
    ], user=user)


def clean_db(db_module):
    tables = db_module.engine.execute(
        "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = (SELECT DATABASE()) AND TABLE_TYPE = 'BASE TABLE';")
    for table in tables:
        db_module.engine.execute('SET FOREIGN_KEY_CHECKS=0; TRUNCATE TABLE ' +
                                 table[0]+';')
