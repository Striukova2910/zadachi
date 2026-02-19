# клієнти без замовлень
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
def no_expense():
        buyer_0 = []
        for i in clients:
                expense = 0
                client_expense_count = 0
                for order in orders:
                        if i[0] == order[0]:
                                expense += order[1]
                                client_expense_count += 1
                if client_expense_count == 0:
                        print(f'client without expense: {i}')

no_expense()
