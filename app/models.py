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
