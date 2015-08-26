
from sqlalchemy import Column, String, BigInteger, Numeric, Boolean, ForeignKey, Integer
from sqlalchemy.schema import Sequence
from sqlalchemy.orm import relationship, backref
from base import Base


class Transactions(Base):
    __tablename__ = 'transactions'
    id = Column(BigInteger,
                Sequence('seq_transactions_id', start=1, increment=1),
                primary_key=True)
    # customer relationship
    customer_id = Column(BigInteger, ForeignKey('customer.id'))
    customer = relationship("Customer", backref="transactions")
    # product relationship
    product_id = Column(BigInteger, ForeignKey('product.id'))
    product = relationship("Product", backref="transactions")
    # affiliate relationship
    affiliate_id = Column(Integer, ForeignKey('affiliate.id'))
    affiliate = relationship("Affiliate", backref="transactions")
    # fields
    type = Column(String(1))
    status = Column(String(1))
    state = Column(String(1))
    quantity = Column(Integer)
    amount = Column(Numeric(12, 2))
    total_amount = Column(Numeric(12, 2))
    fee = Column(Numeric(12, 2))

    affiliator_received = Column(Numeric(12, 2), default=0)