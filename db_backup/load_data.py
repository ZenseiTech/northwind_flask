"""Load data from sql files."""
from sqlalchemy import text


def __load_data__(db, filename):
    with open(filename, "r") as f:
        insert_data_sql = f.read()

    if "categories" in insert_data_sql:
        # this is necessary to propery set image data ...
        insert_data_sql = (
            insert_data_sql.replace("0x", "x'")
            .replace("),", "'),")
            .replace(");", "');")
        )

    with db.get_engine().begin() as conn:
        conn.execute(text(insert_data_sql))


def load(db):
    """Load datas."""
    __load_data__(db, "./db_backup/categories.sql")
