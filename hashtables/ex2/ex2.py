#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # Create `route`
    for ticket in range(length):
        if ticket == 0:
            start = hash_table_retrieve(hashtable, "NONE")
            route[ticket] = start
        else:
            # Get destination (value) of previous route
            route[ticket] = hash_table_retrieve(hashtable, route[ticket - 1])

    print(route)
    return route
