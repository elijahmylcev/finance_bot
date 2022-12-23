from sqlalchemy import Column, BigInteger, String, Integer, sql
from utils.db_api.db_gino import TimedBaseModel

class Costs(TimedBaseModel):
  __tablename__ = 'costs'
  cost_id = Column(BigInteger, primary_key=True)
  cost_sum = Column(Integer)
  cost_category = Column(String(50))
  
  
  query: sql.select