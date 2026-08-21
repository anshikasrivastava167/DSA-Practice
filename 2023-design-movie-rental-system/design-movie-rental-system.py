from sortedcontainers import SortedList

class MovieRentingSystem:

    def __init__(self, n, entries):
        self.price = {}
        self.available = {}
        self.rented = SortedList()

        for shop, movie, price in entries:
            self.price[(shop, movie)] = price

            if movie not in self.available:
                self.available[movie] = SortedList()

            self.available[movie].add((price, shop))

    def search(self, movie):
        if movie not in self.available:
            return []

        return [shop for price, shop in self.available[movie][:5]]

    def rent(self, shop, movie):
        price = self.price[(shop, movie)]

        self.available[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop, movie):
        price = self.price[(shop, movie)]

        self.rented.remove((price, shop, movie))
        self.available[movie].add((price, shop))

    def report(self):
        return [
            [shop, movie]
            for price, shop, movie in self.rented[:5]
        ]