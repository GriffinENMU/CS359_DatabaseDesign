def recordExists(conn, table, column, value):
    curse = conn.cursor()
    curse.execute(f"SELECT 1 FROM {table} WHERE {column} = ?", (value,))
    return curse.fetchone() is not None


def isPositiveInteger(value):
    try:
        return int(value) > 0
    except (ValueError, TypeError):
        return False
