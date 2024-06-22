def bank(x, y):
  total = x  

  for year in range(1, y + 1):
    interest = total * 0.1
    total = total * 1.1
    total += interest

  return total

вклад = 10000 
срок = 5  

сумма_на_счете = bank(вклад, срок)
print(f"Сумма на счету через {срок} лет: {сумма_на_счете:.2f} рублей")