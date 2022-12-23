from utils.db_api.schemas.costs import Costs

async def add_cost(cost_id: int, cost_sum: int, cost_category: str):
  try:
    cost = Costs(cost_id, cost_sum, cost_category)
    await cost.create()
    
  except:
    print('Запись не сохранилась')
    
async def select_all_costs():
  costs = await Costs.query.gino.all()
  return  costs

