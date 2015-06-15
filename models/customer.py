from sqlalchemy import Column, String, BigInteger
from sqlalchemy.schema import Sequence
from base import Base

from marshmallow import Schema, fields, pprint

class Customer(Base):
	__tablename__ = 'customer'
	id = Column(BigInteger, Sequence('seq_customer_id', start=1, increment=1), primary_key=True)
	name = Column(String(255), nullable=False)
	email = Column(String(255), nullable=False)


class CustomerSchema(Schema):
	class Meta:
		fields = ('id', 'name', 'email')
