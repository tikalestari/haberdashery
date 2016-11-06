class Store():
    def __init__(self):
        self.supply_to_bulk = {}
        self.project_to_supplies = {}
        self.project_to_price = {}
        self.inventory = {}
        self.revenue = 0
        self.total_cost = 0

    def add_project(self, project, price, supplies):
        self.project_to_price[project] = price
        self.project_to_supplies[project] = supplies

    def add_supply(self, supply, bulk, bulk_price):
        self.supply_to_bulk[supply] = (bulk, bulk_price)
        self.inventory[supply] = 0

    def sell(self, project, amount):
        for supply in self.project_to_supplies[project]:
            while self.inventory[supply] < amount:
                self.inventory[supply] += self.supply_to_bulk[supply][0]
                self.total_cost += self.supply_to_bulk[supply][1]
            self.inventory[supply] -= amount
        self.revenue += self.project_to_price[project] * amount

    def profit(self):
        return self.revenue - self.total_cost


def business():
    t = int(input())
    for i in range(t):
        n, m, o = map(int,input().split())
        store = Store()
        for i in range(n):
            project, price, = input().split()
            supplies = input().split()
            store.add_project(project, int(price), supplies)
        for i in range(m):
            supply, bulk, bulk_price = input().split()
            store.add_supply(supply, int(bulk), int(bulk_price))
        for i in range(o):
            project, amount = input().split()
            store.sell(project, int(amount))
        print(str(store.profit()))


if __name__ == '__main__':
    business()
