import pulp

# ініціалізуємо модель і створюємо задачу лінійного програмування на максимізацію
model = pulp.LpProblem("Maximize_Drink_Production", pulp.LpMaximize)

# визначаємо змінні
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# додаємо цільову функцію до моделі
model += lemonade + fruit_juice, "Total_Production"

# додаємо обмеження ресурсів
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"

# обмеження на цукор
model += 1 * lemonade <= 50, "Sugar_Constraint"

# обмеження на лимонний сік
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"

# обмеження на фруктове пюре
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# розв'язання моделі
model.solve()

print(f"Статус розв'язку: {pulp.LpStatus[model.status]}")
print("-" * 30)
print(f"Кількість 'Лимонаду': {lemonade.varValue}")
print(f"Кількість 'Фруктового соку': {fruit_juice.varValue}")
print("-" * 30)
print(f"Загальна кількість продуктів: {pulp.value(model.objective)}")

