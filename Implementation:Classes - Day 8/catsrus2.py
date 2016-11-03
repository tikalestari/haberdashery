class Cat():
    def __init__(self, br, bn, b, p, i):
        bulk_to_cost = {}
        breed_price = {}
        breed_bulk = {}
        profit = 0
        total_cost = 0
        self.bn = bn
        self.b = b
        self.p = p

    def bulk_cost(self):
        return self.b

    def bulk(self):
        return self.bn

    def price(self):
        return self.p

    def inventory(self):
        return self.i

    def transact(self, n):
        if self.inventory() < n:
            while self.inventory() < n:
                self.i += self.bulk()
                total_cost += self.bulk_cost()
                print("BUY: " + b)
        if self.inventory() >= n:
            profit += self.price() * n
            self.i -= n 

def catsrus():
    cats = {}
    profit = 0
    total_cost = 0
    n,m = map(int,input().split())
    for i in range(n):
        breed, bulk, bulk_price, price = input().split()
        cats[breed] = Cat(breed, bulk, bulk_price, price, 0)
    for i in range(m):
        b, n = input().split()
        '''if cats[b][1] < int(n):
            while cats[b][1] < int(n):
                cats[b][1] += int(cats[b][0].bulk())
                total_cost += int(cats[b][0].bulk_cost())
                print("BUY: " + b)
        if cats[b][1] >= int(n):
            profit += int(cats[b][0].price()) * int(n)
            cats[b][1] -= int(n)'''
        cats[b].transact(n)
    print("PROFIT: " + str(profit - total_cost))

if __name__ == "__main__":
    catsrus()
