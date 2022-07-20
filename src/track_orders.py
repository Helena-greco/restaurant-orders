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

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
