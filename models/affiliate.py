from sqlalchemy import Column, String, BigInteger, ForeignKey
from sqlalchemy.schema import Sequence, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from base import Base


class Affiliate(Base):
	__tablename__ = 'affiliate'
	id = Column(BigInteger, Sequence('seq_affiliate_id', start=1, increment=1), primary_key=True)
	# product relationship
	product_id = Column(BigInteger, ForeignKey('product.id'))
	product = relationship("Product", backref="affiliates")
    # customer relationship
	customer_id = Column(BigInteger, ForeignKey('customer.id'))
	customer = relationship("Customer", backref="affiliates")
	headline = Column(String(1024))
	product_page = Column(String(1024))

	UniqueConstraint('product_id', 'customer_id', name='product_customer_affiliate_unique_constraint')