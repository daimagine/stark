from sqlalchemy import Column, String, BigInteger
from sqlalchemy.schema import Sequence
from base import Base

from marshmallow import Schema, fields, pprint

class CustomerSocmedAccount(Base):
	__tablename__ = 'customer_socmed_account'
	id = Column(BigInteger, Sequence('seq_customer_socmed_account_id', start=1, increment=1), primary_key=True)
	token = Column(String(255), nullable=False)
	secret = Column(String(255), nullable=False)

	# social_media relationship
	social_media_id = Column(Integer, ForeignKey('social_media.id'))
	social_media = relationship("SocialMedia", backref="socmed_accounts")
    # customer relationship
	customer_id = Column(BigInteger, ForeignKey('customer.id'))
	customer = relationship("Customer", backref="socmed_accounts")

class CustomerSocmedAccountSchema(Schema):
	class Meta:
		fields = ('id', 'name', 'customer', 'social_media')
