"""Load data from sql files."""
from sqlalchemy import text


def __load_data__(db, filename):
    with open(filename, "r") as f:
        insert_data_sql = f.read()

    if "categories" in insert_data_sql:
        # this is necessary to propery set image data ...
        print()
        print("===========> Adding categories images ...")
        insert_data_sql = (
            insert_data_sql.replace("0x", "x'")
            .replace("),", "'),")
            .replace(");", "');")
        )
    elif "employees" in insert_data_sql:
        print()
        print("===========> Adding employees images ...")

        insert_data_sql = insert_data_sql.replace("0x", "x'").replace("D900,", "D900',")

    with db.get_engine().begin() as conn:
        try:
            conn.execute(text(insert_data_sql))
        except Exception as e:
            print(e)
    print("\n\n")


def load(db):
    """Load datas."""
    __load_data__(db, "./db_backup/categories.sql")
    __load_data__(db, "./db_backup/products.sql")
    __load_data__(db, "./db_backup/suppliers.sql")
    __load_data__(db, "./db_backup/employees.sql")
    __load_data__(db, "./db_backup/customers.sql")
    __load_data__(db, "./db_backup/shippers.sql")
    __load_data__(db, "./db_backup/orders.sql")
