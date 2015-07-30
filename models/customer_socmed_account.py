from sqlalchemy import Column, String, BigInteger, Integer, ForeignKey
from sqlalchemy.schema import Sequence
from sqlalchemy.orm import relationship, backref
from base import Base

from marshmallow import Schema, fields, pprint

from stark.models.social_media import SocialMedia


class CustomerSocmedAccount(Base):
	__tablename__ = 'customer_socmed_account'
	id = Column(BigInteger, Sequence('seq_customer_socmed_account_id', start=1, increment=1), primary_key=True)
	# customer relationship
	customer_id = Column(BigInteger, ForeignKey('customer.id'))
	customer = relationship("Customer", backref="socmed_accounts")
	# social_media relationship
	social_media_id = Column(Integer, ForeignKey('social_media.id'))
	social_media = relationship(SocialMedia, backref="socmed_accounts")
	#fields
	token = Column(String(1024), nullable=False)
	secret = Column(String(1024), nullable=False)
	social_id = Column(String(200))
	social_name = Column(String(500))
	image = Column(String(1024))
	type = Column(String(1))
