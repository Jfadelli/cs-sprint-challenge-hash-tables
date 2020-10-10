#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    
    def get_src(self):
        return self.source

    def get_dest(self):
        return self.destination
    
def hash_tickets(tickets, length):
    linked_trip = {}
    for i in range(length):
        ticket = tickets[i]
        src, dest = ticket.get_src(), ticket.get_dest()   
        linked_trip[src] = dest
    return linked_trip

def reconstruct_trip(tickets, length):
    routes = hash_tickets(tickets, length)
    trip = [routes["NONE"]] * length

    for i in range(1, len(trip)):
        trip[i] = routes[trip[i - 1]]
        print(trip)
    return trip

    # return route
