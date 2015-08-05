from sqlalchemy import Column, String, BigInteger, Integer, Boolean, ForeignKey
from sqlalchemy.schema import Sequence
from sqlalchemy.orm import relationship, backref
from base import Base


class ProductImage(Base):
	__tablename__ = 'images'
	id = Column(Integer, Sequence('seq_images_id', start=1, increment=1), primary_key=True)
	# product relationship
	product_id = Column(BigInteger, ForeignKey('product.id'))
	product = relationship("Product", backref="product_images")
	# fields
	link = Column(String(1024))
	is_primary = Column(Boolean, default=False)