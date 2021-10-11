"""Modul with all restaurant classes"""
class Restaurant:
    """Class Restaurant keeps data about busy and free tables"""

    def __init__(self, us_seats):
        """Keeps id of all taken seats per year and presently"""
        self.add_idtable_when_servicing = us_seats
        self.id_table_free_or_not = {1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True}
        self.tables = [1, 2, 3, 4, 5, 6, 7]

    def add_client(self, id_table):
        """Add new table to busy ones"""
        if id_table in self.tables:
            self.add_idtable_when_servicing.append(id_table)
            self.id_table_free_or_not[id_table] = False
        else:
            print("Sory, we have no seats.")

    def client_payoff(self, id_tabl):
        """If client leave, table must be free again"""
        self.id_table_free_or_not[id_tabl] = True


class Client:
    """Name, payment status and id table of client"""

    def __init__(self, cl_name: str, table: int):
        """Client introduce himself and choose a table"""
        self.name = cl_name
        self.payoff = False
        self.table = table

    @staticmethod
    def watch_menu(menu_list):
        """Client can see, what in menu today"""
        for next_dish in menu_list.keys():
            print(next_dish, menu_list[next_dish])

    @staticmethod
    def make_order():
        """Client enumerates id of dish one by one"""
        client_make_order = []
        while True:
            add_order = input("Enter the id dish to order it.    "
                              "1, 2, 3 or 4    Enter 0 to confirm the order"
                              "   Enter 00 start over ")
            if add_order in ("1", "2", "3", "4"):
                client_make_order.append(int(add_order))
                continue
            elif add_order == "0":
                break
            elif add_order == "00":
                client_make_order = []
                continue
            print("Wrong choose, please try again")
        return client_make_order

    def payoff_change(self):
        """Client payoff and change payoff status"""
        self.payoff = True

    @staticmethod
    def watch_sum_of_payment(sum_pay):
        """Client can find out his payment sum"""
        print()
        print(f"Whole sum is: {sum_pay}")


class Menu:
    """Menu of the restaurant"""

    def __init__(self):
        """Kep info about dishes {id:"name", ""size", "cost"}"""
        self.id_food = 0
        self.menu_dish_list = {}

    @property
    def dishes(self):
        """Return dishes list from menu {id:"name", ""size", "cost"}"""
        return self.menu_dish_list

    @dishes.setter
    def dishes(self, args):
        """Add dish to dishes list"""
        self.id_food += 1
        food_name, size, price = args
        self.menu_dish_list[self.id_food] = [food_name, size, price]

    def dell_dish(self, id_dish):
        """Dell dish to dishes list"""
        if id_dish in self.menu_dish_list:
            del self.menu_dish_list[id_dish]


class Order:
    """Keep order information"""

    def __init__(self, id_cli_ord):
        """Next order id and saved order list"""
        self.id_order = 0
        self.orders_list = id_cli_ord

    def add_order_to_list(self, client_id, id_dish):
        """Add order to order list"""
        self.id_order += 1
        if self.orders_list.get(client_id):
            self.orders_list[client_id].extend(id_dish)
        else:
            self.orders_list[client_id] = []
            self.orders_list[client_id].extend(id_dish)

    def save_order_list(self, id_cl):
        """Return order list"""
        return self.orders_list[id_cl]


class Waiter:
    """Keep information about waiter"""

    def __init__(self, id_waiter, nun_of_ord, salar_wait):
        """Take id, max number of orders, and his salary"""
        self.id_waiter = id_waiter
        self.max_number_of_orders = nun_of_ord
        self.salary_waiter = salar_wait
        self.waiter_order_status = "No_orders"
        self.taken_orders = []

    def take_order(self, new_order_taken):
        """Waiter take an order, change status"""
        if self.max_number_of_orders > 0:
            self.waiter_order_status = "Order_taken"
            self.max_number_of_orders -= 1
            self.taken_orders.append(new_order_taken)
        else:
            print("This waiter is busy")

    def give_order_to_cook(self):
        """Waiter give an order to cook, and change status"""
        if self.waiter_order_status == "Order_taken":
            self.waiter_order_status = "given_to_the_cook"
        else:
            print("Take order first")

    def give_order_to_client(self):
        """Waiter give an order to client, and change status"""
        if self.max_number_of_orders < 3:
            self.max_number_of_orders += 1
            del self.taken_orders[-1]
            self.waiter_order_status = "No_orders"


class Cook:
    """Keep information about Cook"""

    def __init__(self, id_cook, num_of_cook, salar_cook):
        """Take id, max number of order cooking, and his salary"""
        self.id_cook = id_cook
        self.max_number_of_cooking = num_of_cook
        self.salary_cook = salar_cook
        self.cooking_order_status = "Not_cooking"

    def take_order_to_cooking(self):
        """Begin to cooking, change status"""
        if self.max_number_of_cooking > 0:
            self.cooking_order_status = "Cooking"
            self.max_number_of_cooking -= 1
        else:
            print("This cook is busy")

    def show_cooking_order_status(self):
        """Shows a dish readiness"""
        print(self.cooking_order_status, end=" ")

    def change_order_readiness(self):
        """Order ready, cook is free. Change status"""
        if self.cooking_order_status == "Cooking":
            self.max_number_of_cooking += 1
            self.cooking_order_status = "No_orders"


class Payment:
    """Keep info about client payment"""

    def __init__(self, pay_id):
        """Id payment = client name, discount 15% if sum of order more then 300"""
        self.payment_id = pay_id
        self.sum_of_payment = 0
        self.discount = 300
        self.payment_status = False

    def charge_discount(self, s):
        """Discount 15% if sum of order more then 300"""
        if s > self.discount:
            print("Congratulations, your discount is 15%")
            return s - ((s / 100) * 15)
        return s

    def new_payment_sum(self, dish_li, order_li, clie_name):
        """Sum of client payment"""
        sum_ord = 0
        print("You ordered: ", end=" ")
        for orde in order_li[clie_name]:
            sum_ord += dish_li[orde][-1]
            print(dish_li[orde][0], end=" ")
        print()
        return self.charge_discount(sum_ord)

    def change_payment_status(self):
        """Change payment status"""
        self.payment_status = True


class Admin:
    """Keep information about admin and restaurant salary"""

    def __init__(self, salary_adm):
        """Keep info - unforeseen spending, standard costs, and admin salary"""
        self.salary_admin = salary_adm
        self.unforeseen_spending = 0.0
        self.standard_costs = 0.0
        self.payoff_status = False

    def change_payoff_status(self, salary_cook, salary_waiter, products, un_spend):
        """Standard_costs count, take and save unforeseen spending, change payoff status"""
        self.standard_costs = salary_cook + salary_waiter + self.salary_admin + products
        self.unforeseen_spending = un_spend
        self.payoff_status = True

    def change_all_spendings(self, fraud):
        """If standard_costs is lesser then the administrator spent, increase unforeseen costs"""
        if self.standard_costs < fraud:
            self.unforeseen_spending += (fraud - self.standard_costs)


class Income:
    """Income of restaurant, best seats"""

    def __init__(self, pros_month):
        """keep information about most often taken seats"""
        self.best_seats_list = []
        self.proceeds_per_month = pros_month

    @staticmethod
    def show_best_seats(all_tables, id_tables):
        """Show_best_seats"""
        result = find_the_best(all_tables, id_tables)
        return result

    def add_payment_to_proceeds(self, payment):
        """Add new payment to month proceeds"""
        self.proceeds_per_month += payment

    def show_month_proceeds(self):
        """Show month proceeds"""
        print(self.proceeds_per_month)


class Expense:
    """Keep info about all expense of the restaurant"""

    def __init__(self):
        """All salary, spending and all_costs_per_month"""
        self.all_costs_per_month = 0.0
        self.sum_month_salary = 0.0
        self.sum_month_spending = 0.0

    def watch_all_coasts_per_month(self):
        """Count and show all_coasts_per_month"""
        if self.sum_month_salary != 0.0 and \
                self.sum_month_spending != 0.0:
            self.all_costs_per_month = self.sum_month_salary \
                                       + self.sum_month_spending
            print(self.all_costs_per_month)
        else:
            print("Month salary or coasts not counted yet.")

    def watch_salaries(self, wait, cooki, admin):
        """Show sum of salaries"""
        self.sum_month_salary = wait + cooki + admin
        print(self.sum_month_salary, end=" ")

    def watch_spending(self, unfo_spending, stand_costs):
        """Show month spending"""
        self.sum_month_spending = unfo_spending + stand_costs
        print(self.sum_month_spending, end=" ")


class IncomeExpenses:
    """Keep info about net_profit_per_month, and most_often_ordering_dish"""

    def __init__(self):
        """Net profit per month, and most often ordering dish"""
        self.net_profit_per_month = 0
        self.most_often_ordering_dishes = 0

    @staticmethod
    def most_ordering_dish(ord_li, id_fo):
        """Return most often ordering dishes"""
        find_dish = []
        id_of_food = [id_f + 1 for id_f in range(id_fo)]
        for dish in ord_li.values():
            find_dish.extend(dish)
        best_dish = find_the_best(find_dish, id_of_food)
        return best_dish

    def show_net_profit(self, proceeds, all_costs):
        """Show net profit per month"""
        self.net_profit_per_month = proceeds - all_costs
        print(self.net_profit_per_month)


def find_the_best(a, b):
    """find the best seats in restaurant and dish in menu"""
    best_of_all = list(map(lambda table: a.count(table), list(set(a))))
    return b[best_of_all.index(max(best_of_all))]

