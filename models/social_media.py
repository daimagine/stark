from sqlalchemy import Column, String, BigInteger, Integer
from sqlalchemy.schema import Sequence
from base import Base

from marshmallow import Schema, fields, pprint

class SocialMedia(Base):
	__tablename__ = 'social_media'
	id = Column(Integer, Sequence('seq_social_media_id', start=1, increment=1), primary_key=True)
	name = Column(String(255), nullable=False)
	consumer_key = Column(String(255), nullable=False)
	consumer_secret = Column(String(255), nullable=False)
	interface = Column(String(200), nullable=False)
	interface_package = Column(String(200), nullable=False)