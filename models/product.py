
from sqlalchemy import Column, String, BigInteger, Numeric, Boolean, ForeignKey, Integer
from sqlalchemy.schema import Sequence
from sqlalchemy.orm import relationship, backref
from base import Base

from stark.models.category import Category


class Product(Base):
    __tablename__ = 'product'
    id = Column(BigInteger,
                Sequence('seq_product_id', start=1, increment=1),
                primary_key=True)
    # customer relationship
    customer_id = Column(BigInteger, ForeignKey('customer.id'))
    customer = relationship("Customer", backref="products")
    #category relationship
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category, backref="products")
    # fields
    token = Column(String(200), nullable=False)
    name = Column(String(255), nullable=False)
    is_affiliate_ready = Column(Boolean, default=False)
    affiliate_percentage = Column(Numeric(3, 2))
    affiliate_fee = Column(Numeric(12, 2), default=0.00)
    affiliate_fee_type = Column(String(1))
    price = Column(Numeric(12, 2))
    image = Column(String(1024))
    description = Column(String(1024))
    headline = Column(String(1024))
    product_page = Column(String(1024))