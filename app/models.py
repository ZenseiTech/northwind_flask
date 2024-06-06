"""Contains the model to the database."""
from . import db


class Category(db.Model):
    """Category model."""

    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(64), nullable=False, unique=True, index=True)
    description = db.Column(db.Text())
    picture = db.Column(db.LargeBinary)

    products = db.relationship("Product", backref="role", lazy="dynamic")

    def __repr__(self):
        """Representation."""
        return "<Categories %r>" % self.category_name


class Supplier(db.Model):
    """Supplier model."""

    __tablename__ = "suppliers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(64), nullable=False, unique=True, index=True)
    contact_name = db.Column(db.String(64))
    contact_title = db.Column(db.String(64))
    address = db.Column(db.String(64))
    city = db.Column(db.String(64))
    region = db.Column(db.String(64))
    postal_code = db.Column(db.String(64))
    country = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    fax = db.Column(db.String(64))
    home_page = db.Column(db.String(64))

    products = db.relationship("Product", backref="role", lazy="dynamic")

    def __repr__(self):
        """Representation."""
        return "<Companies %r>" % self.company_name


class Product(db.Model):
    """Product model."""

    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(64), nullable=False, unique=True, index=True)
    quantity_per_unit = db.Column(db.Integer)
    unit_price = db.Column(db.Float)
    units_in_stock = db.Column(db.Integer)
    units_on_order = db.Column(db.Integer)
    reorder_level = db.Column(db.Integer)
    discontinued = db.Column(db.String(64))
    supplier_id = db.Column(db.Integer, db.ForeignKey("suppliers.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    def __repr__(self):
        """Representation."""
        return "<Products %r>" % self.product_name


class Employee(db.Model):
    """Employee model."""

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    last_name = db.Column(db.String(64), nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    title = db.Column(db.String(64), nullable=False)
    title_of_courtesy = db.Column(db.String(64))
    birthdate = db.Column(db.String(64), nullable=False)
    hire_date = db.Column(db.DateTime(), nullable=False)
    address = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    region = db.Column(db.String(64), nullable=False)
    postal_code = db.Column(db.String(64), nullable=False)
    country = db.Column(db.String(64), nullable=False)
    home_phone = db.Column(db.String(64), nullable=False)
    extension = db.Column(db.String(64))
    photo = db.Column(db.LargeBinary)
    notes = db.Column(db.String(64))
    reports_to = db.Column(db.Integer, db.ForeignKey("employees.id"))
    photo_path = db.Column(db.String(64))

    def __repr__(self):
        """Representation."""
        return f"<Employees {self.first_name} {self.last_name}>"

    class Customer(db.Model):
        """Customer model."""

        __tablename__ = "customers"

        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        customer_id = db.Column(db.String(64), nullable=False, unique=True, index=True)
        company_name = db.Column(db.String(64), nullable=False)
        contact_name = db.Column(db.String(64), nullable=False)
        contact_title = db.Column(db.String(64), nullable=False)
        address = db.Column(db.String(64), nullable=True)
        city = db.Column(db.String(64), nullable=True)
        region = db.Column(db.String(64), nullable=True)
        postal_code = db.Column(db.String(64), nullable=True)
        country = db.Column(db.String(64), nullable=True)
        phone = db.Column(db.String(64), nullable=True)
        fax = db.Column(db.String(64), nullable=True)

        def __repr__(self):
            """Representation."""
            return f"<Customers {self.company_name} {self.customer_id}>"

    class Shipper(db.Model):
        """Shipper model."""

        __tablename__ = "shippers"

        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        company_name = db.Column(db.String(64), nullable=False)
        phone = db.Column(db.String(64), nullable=False)

        def __repr__(self):
            """Representation."""
            return f"<Shippers {self.company_name} {self.phone}>"

    class Order(db.Model):
        """Order model."""

        __tablename__ = "orders"

        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        order_date = db.Column(db.DateTime(), nullable=False)
        required_date = db.Column(db.DateTime(), nullable=False)
        shipped_date = db.Column(db.DateTime(), nullable=True)
        freight = db.Column(db.Integer, default=0)
        ship_name = db.Column(db.String(64), nullable=False)
        ship_address = db.Column(db.String(64), nullable=False)
        ship_city = db.Column(db.String(64), nullable=False)
        ship_region = db.Column(db.String(64), nullable=False)
        ship_postal_code = db.Column(db.String(64), nullable=True)
        ship_country = db.Column(db.String(64), nullable=False)

        customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
        employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"))
        ship_via = db.Column(db.Integer, db.ForeignKey("shippers.id"))

        def __repr__(self):
            """Representation."""
            return f"<Orders {self.order_id} {self.customer_id}>"
