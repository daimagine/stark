from sqlalchemy import Column, String, BigInteger, DateTime
from sqlalchemy.schema import Sequence
from base import Base


class Customer(Base):
	__tablename__ = 'customer'
	id = Column(BigInteger, Sequence('seq_customer_id', start=1, increment=1), primary_key=True)
	#fields
	name = Column(String(255), nullable=False)
	email = Column(String(255), nullable=False)
	password_1 = Column(String(1024))
	client_token = Column(String(1024))
	client_token_valid_time = Column(DateTime(timezone=False))
	address = Column(String(200))
	mobile_no = Column(String(200))
	phone_1 = Column(String(200))
	phone_2 = Column(String(200))
	phone_3 = Column(String(200))
	bank_account_no = Column(String(200))
	bank_account_name = Column(String(200))
	bank_name = Column(String(200))
	email_verified = Column(String(1), default='V')
	phone_verified = Column(String(1), default='U')