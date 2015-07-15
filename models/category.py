from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.schema import Sequence
from base import Base


class Category(Base):
	__tablename__ = 'category'
	id = Column(Integer, Sequence('seq_category_id', start=1, increment=1), primary_key=True)
	name = Column(String(255), nullable=False)
	description = Column(String(255))
	need_logistic = Column(Boolean, default=False)
	downloadable = Column(Boolean, default=False)
	stock_related = Column(Boolean, default=False)
	have_expiry_date = Column(Boolean, default=False)