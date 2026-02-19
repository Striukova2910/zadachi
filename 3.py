#авдання 2. Середній чек кожного клієнта
#Для кожного клієнта обчислити середню суму замовлення.
clients = [
        (1, "Іван", "ivan@gmail.com"),
        (2, "Марія", "maria@gmail.com"),
        (3, "Олег", "oleg@gmail.com"),
        (4, "Софія", "sofia@gmail.com")
    ]

orders = [
        (1, 1200),
        (2, 800),
        (1, 600),
        (3, 1500),
        (2, 400),
        (1, 300)
    ]

for client in clients:
    expense = 0
    client_expense_count = 0

    for order in orders:
        if client[0] == order[0]:
            expense += order[1]
            client_expense_count += 1

    if client_expense_count > 0:
        average = expense / client_expense_count
        print(f'{client[1]}, average expense: {average}')
    else:
        print(f"{client[1]}, has no expenses")
