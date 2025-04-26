import sys

def marketing():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    if len(sys.argv) != 2:
        raise ValueError("Invalid number of arguments")

    goal = sys.argv[1]
    if goal == "call_center":
        print(list(set(clients) - set(recipients)))
    elif goal == "potential_clients":
        print(list(set(participants) - set(clients)))
    elif goal == "loyalty_program":
        print(list(set(clients) - set(participants)))
    else:
        raise ValueError("Invalid task name")

if __name__ == '__main__':
    marketing()