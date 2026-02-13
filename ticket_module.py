import random
NUMBER_LIST = list(range(1000, 9999))

def generate_tickets(count):
    tickets = []
    
    for _ in range(count):
        ticket = random.choice(NUMBER_LIST)
        tickets.append(ticket)
    return