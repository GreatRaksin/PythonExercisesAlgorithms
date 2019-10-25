amount = int(input("Сколько хотите взять денег: "))
pct = float(input("Под какой процент вам их дают: "))
years = float(input("Насколько лет берете: "))


pct = pct / 100
monthPay = (amount * pct * (1 + pct) ** years) / (12 * ((1 + pct) ** years - 1))
print("Ваш месячный платеж составит: %.2f" % monthPay)

sum = monthPay * years * 12
print("За весь период вы заплатите: %.2f" % sum)
print("Это составит %.2f%% от первоначальной суммы" % ((sum / amount) * 100))