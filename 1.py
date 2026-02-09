# Підготувати звіт для керівника. Знайти клієнта, який витратив найбільше грошей за весь час.
def calculate_max_expenses():
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
    for client in clients:
        expense = 0
        client_id = client[0]
        for order in orders:
            if client_id == order[0]:
                expense += order[1]
calculate_max_expenses()

