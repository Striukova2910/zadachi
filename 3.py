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
max_expense = 0
    winner = ""
    for client in clients:
        expense = 0
        for order in orders:
            if client[0] == order[0]:
                expense += order[1]
        print(f'user id: {client[0]}, total expenses: {expense}, name: {client[1]}')
        if expense > max_expense:
            winner = client[1]
            max_expense = expense
    print(f'max expenses: {max_expense}, name: {winner}')