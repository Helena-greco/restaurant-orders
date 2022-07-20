class TrackOrders:
    def __init__(self):
        self.data = list()

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.data)

    def add_new_order(self, customer, order, day):
        self.data.append({"customer": customer, "order": order, "day": day})

# Ref: https://pythonguides.com/python-find-max-value-in-a-dictionary/
    def get_most_ordered_dish_per_customer(self, customer):
        most_ordered = dict()
        order_list = list()

        for order in self.data:
            if order["customer"] == customer:
                order_list.append(order)

        for costumer in order_list:
            if costumer["order"] not in most_ordered:
                most_ordered[costumer["order"]] = 1
            else:
                most_ordered[costumer["order"]] += 1

        return max(most_ordered, key=most_ordered.get)

# Ref: https://www.geeksforgeeks.org/python-set-difference/
    def get_never_ordered_per_customer(self, customer):
        order_list = set()
        order_by_customer = set()

        for order in self.data:
            order_list.add(order["order"])
            if order["customer"] == customer:
                order_by_customer.add(order["order"])

        return order_list.difference(order_by_customer)

    def get_days_never_visited_per_customer(self, customer):
        day_list = set()
        day_by_customer = set()

        for day in self.data:
            day_list.add(day["day"])
            if day["customer"] == customer:
                day_by_customer.add(day["day"])

        return day_list.difference(day_by_customer)

    def get_busiest_day(self):
        busiest_day = dict()

        for day in self.data:
            if day["day"] not in busiest_day:
                busiest_day[day["day"]] = 1
            else:
                busiest_day[day["day"]] += 1

        return max(busiest_day, key=busiest_day.get)

    def get_least_busy_day(self):
        pass
