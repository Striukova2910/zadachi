# клієнти без замовлень
clients = [
        (1, "Іван", "ivan@gmail.com"),
        (2, "Марія", "maria@gmail.com"),
        (3, "Олег", "oleg@gmail.com"),
        (4, "Софія", "sofia@gmail.com")
    ]

orders = [
        (3, 1200),
        (2, 800),
        (4, 600),
        (1, 1500),
        (2, 400),
        (1, 300)
    ]
def no_expense():
        find_no_expence = False

        for i in clients:
                expense = 0
                client_expense_count = 0
                for order in orders:
                        if i[0] == order[0]:
                                expense += order[1]
                                client_expense_count += 1
                if client_expense_count == 0:
                    find_no_expence = True
                    print(f'client without expense: {i}')


        if not find_no_expence:
                        print(f'no client with expense 0')

no_expense()
