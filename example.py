def get_yearly_revenue(monthly_revenue):
#monthly_revenue (월간 매출)를 인수로 받고, revenue for a year (연간 매출)를 리턴.
  return monthly_revenue * 12

def get_yearly_expenses(monthly_expenses):
#monthly_expenses (월간 비용)를 인수로 받고, expenses for a year (연간 비용)를 리턴.
  return monthly_expenses * 12
def get_tax_amount (profit):
#profit (이익) 를 인수로 받고, tax_amount (세금 금액) 를 리턴.
  if profit > 100000:
    return profit * 0.25
  else:
    return profit * 0.15
def apply_tax_credits (tax_amount, tax_credits):
#tax_amount (세금 금액), tax_credits (세액 공제율)를 인수로 받고, amount to discount (할인할 금액)를 리턴.
  return tax_amount - (tax_amount * tax_credits)