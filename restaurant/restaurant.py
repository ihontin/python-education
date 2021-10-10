"""Module with scenario"""
import time
from datetime import datetime
from classes import *

current_datetime = datetime.now()
month_expence = Expense()
month_proceeds = 1000000
used_seats = [1, 4, 5, 2, 6, 7, 7, 6, 2, 5, 1, 4, 3, 3]
GoldDragon = Restaurant(used_seats)
income_proceeds = Income(month_proceeds)
restaurant_final_data = IncomeExpenses()
orders_list_file = []
GoldDragon_menu = Menu()
GoldDragon_menu.dishes = "soup", 190, 79
GoldDragon_menu.dishes = "puree", 220, 89
GoldDragon_menu.dishes = "tea", 150, 69
GoldDragon_menu.dishes = "bread", 100, 39
waiter1 = Waiter(101, 3, 15400)
cook1 = Cook(2, 5, 19200)
admin1 = Admin(27800)
client = None
id_client_orders = {
    "Ivan": [1, 1, 4, 2],
    "Masha": [3, 3],
    "Brien": [1, 4, 3],
    "Jinger": [2, 2, 4]
}
new_order = Order(id_client_orders)

if __name__ == "__main__":
    while True:
        print("New day! Wait for a client.")
        time.sleep(2)
        new_id_table = int(input("Hello! please choose number of table 1 - 7 :"))
        if 1 <= new_id_table <= 7:
            GoldDragon.add_client(new_id_table)
            name = input("Enter you name")
            client = Client(name, new_id_table)
            payment_of_client = Payment(client.name)  # create personal invoice
        else:
            print("Wron number. We have only 7 tables. Please try again.")
            continue
        print("You watch menu")
        client.watch_menu(GoldDragon_menu.dishes)
        print("Are you ready to make order.")
        new_order.add_order_to_list(client.name, client.make_order())
        print(new_order.orders_list[client.name])
        print("You decided to save it in the restaurant database by you own.")
        time.sleep(2)
        try:
            raise SystemError
        except SystemError as oh_no:
            print("Due to my mistake in UML table.", end=" ")
        time.sleep(2)
        orders_list_file.extend(new_order.save_order_list(client.name))
        print("Only then waiter save orders in his pocket.")
        time.sleep(2)
        waiter1.take_order(orders_list_file[-1])  # waiter take the order and leave
        if waiter1.waiter_order_status == "given_to_the_cook":
            cook1.take_order_to_cooking()
        print(" - You ask about order readiness.")
        time.sleep(2)
        waiter1.give_order_to_cook()  # waiter give order to cook
        print("Waiter gives the order to cook.")
        cook1.take_order_to_cooking()
        print(" - You ask about your order readiness again.")
        time.sleep(2)
        cook1.show_cooking_order_status()
        time.sleep(2)
        print(" - Answer waiter.")
        time.sleep(2)
        cook1.change_order_readiness()
        print(" - You ask about order readiness third time.")
        time.sleep(2)
        waiter1.give_order_to_client()
        print("Waiter serves steaming dish to you.")
        time.sleep(2)
        print("Are you want to watch sum of payment?")
        # save payment sum of client
        payment_sum = payment_of_client.new_payment_sum(
            GoldDragon_menu.menu_dish_list, new_order.orders_list, client.name)
        # show  payment sum
        client.watch_sum_of_payment(payment_sum)
        time.sleep(2)
        print("You pay,", end=" ")
        client.payoff_change()  # client payoff
        income_proceeds.add_payment_to_proceeds(payment_sum)
        payment_of_client.change_payment_status()  # change payment status
        if client.payoff:
            print("and looking at the tables.")
            print(GoldDragon.id_table_free_or_not)  # Table №5 if busy
            time.sleep(2)
            print("Bye bye!")
            GoldDragon.client_payoff(new_id_table)
            print(GoldDragon.id_table_free_or_not)  # Table №5 if free
        if current_datetime.day == current_datetime.day:
            # it must be current_datetime.day == 30 - payday
            print("Now admin must issue salary and conduct monthly report.")
            products_cost = float(input("First of all he must enter monthly cost"
                                        " of the products. For example 80000: "))
            unf_spent = float(input("Then enter unforeseen spending. For example 15000: "))
            admin1.change_payoff_status(cook1.salary_cook, waiter1.salary_waiter,
                                        products_cost, unf_spent)
            time.sleep(2)
            print("Discreetly corrects something in unforeseen expenses.")
            # If standard_costs is lesser then the administrator spent, increase unforeseen costs
            admin1.change_all_spendings(135000)
            time.sleep(2)
            print("And leaves with broad smile.")
            time.sleep(2)
            print("Now we can count Income, Expenses and other information.")
            time.sleep(2)
            print("For example, you can find out what the most popular table is: ", end="")
            if input("Pres y if you want: ").lower() == "y":
                print(income_proceeds.show_best_seats(GoldDragon.add_idtable_when_servicing,
                                                      GoldDragon.tables))
            if input("Pres y if you want to see restaurant month proceeds: ").lower() == "y":
                income_proceeds.show_month_proceeds()
            print("Month salary", end=" ")
            month_expence.watch_salaries(waiter1.salary_waiter,
                                         cook1.salary_cook, admin1.salary_admin)
            print("Different spending", end=" ")
            month_expence.watch_spending(admin1.unforeseen_spending, admin1.standard_costs)
            print("And all restaurant costs per month: ", end=" ")
            month_expence.watch_all_coasts_per_month()
            print("The last data, net profit per year: ", end=" ")
            restaurant_final_data.show_net_profit(income_proceeds.proceeds_per_month,
                                                  month_expence.all_costs_per_month)
            best_dish_ever = restaurant_final_data.most_ordering_dish(new_order.orders_list,
                                                                      GoldDragon_menu.id_food)
            print(f"And most of all, humanity like "
                  f"{GoldDragon_menu.menu_dish_list[best_dish_ever][0]}")
        if input("Pres y if you don't want to start all over again: ").lower() == "y":
            break
