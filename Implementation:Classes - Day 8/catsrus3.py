class Store():
    def __init__(self):
        self.breed_to_price = {}
        self.breed_to_bulk = {}
        self.breed_inventory = {}
        self.revenue = 0
        self.costs = 0

    def add_cat_breed(self, breed, bulk, bulk_price):
        self.breed_to_bulk[breed] = (bulk, bulk_price)
        self.breed_inventory[breed] = 0

    def add_cat_price(self, breed, selling_price):
        self.breed_to_price[breed] = selling_price

    def sell(self, breed, amount):
        while self.breed_inventory[breed] < amount:
            print("BUY: "+str(breed))
            self.breed_inventory[breed] += self.breed_to_bulk[breed][0]
            self.costs += self.breed_to_bulk[breed][1]
        self.breed_inventory[breed] -= amount
        self.revenue += amount * self.breed_to_price[breed]

    def profit(self):
        return self.revenue - self.costs


if __name__ == '__main__':
    n, m = map(int, input().split())
    store = Store()
    for i in range(n):
        breed, bulk, bulk_price, selling_price = input().split()
        store.add_cat_breed(breed, int(bulk), int(bulk_price))
        store.add_cat_price(breed, int(selling_price))
    for i in range(m):
        breed, amount = input().split()
        store.sell(breed, int(amount))
    print("PROFIT: "+str(store.profit()))
