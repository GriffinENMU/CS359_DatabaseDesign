def recordExists(conn, table, column, value):
    curse = conn.cursor()
    curse.execute(f"SELECT 1 FROM {table} WHERE {column} = ?", (value,))
    return curse.fetchone() is not None


def isPositiveInteger(value):
    try:
        return int(value) > 0
    except (ValueError, TypeError):
        return False

def isValidPhone(value):
    """
    Returns True if `value` is 10–15 digits, False otherwise.
    """
    digits = ''.join(filter(str.isdigit, value))
    return 10 <= len(digits) <= 15