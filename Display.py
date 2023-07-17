import datetime


def welcome_message():
    print("Welcome to Bike management System")


def display_options():
    print("1. Sell Bikes")
    print("2. Order Bikes")
    print("3. Exit")


def option_sell_bikes():
    print("Let's sell Bikes")
    print("------------------------------------------------------")


def option_order_bikes():
    print("Let's order Bikes")
    print("------------------------------------------------------")


def option_exit():
    print("------------------------------------------------------")
    print("Thank you for using Bike management System")
    print("------------------------------------------------------")
    quit()


def option_invalid():
    print("INVALID Input. Please enter the number of the options provided in the screen")


def end_message(num):
    if(num == 1):
        message = input("Do you want to sell more bike(Y/N)").lower()
    elif(num == 2):
        message = input("Do you want to order more bike(Y/N)").lower()
    while message != 'y' and message != 'n':
        print("You seem to have entered the wrong keyword please enter only (Y/N)")
        if(num == 1):
            message = input("Do you want to sell more bike(Y/N)").lower()
        elif(num == 2):
            message = input("Do you want to order more bike(Y/N)").lower()
    return message


def display_bikes():
    heading = [["Bike Id", "Bike Name", "Company", "Color", "Stock", "Price"]]
    print("----------------------------------------------------------------------")
    for head in heading:
        print("{: <8} {: <12} {: <10} {: <10} {: <10} {: <10}".format(*head))
    print("----------------------------------------------------------------------")
    bikes = bike_2d_list()
    for bike in bikes:
        print("{: <8} {: <12} {: <10} {: <10} {: <10} {: <10}".format(*bike))

        print("----------------------------------------------------------------------")


def bike_2d_list():
    file = open("bike.txt")
    list_2d = []

    for line in file:

        line = line.replace("\n", "")
        line = line.split(",")

        list_2d.append(line)
    file.close()
    return list_2d


def date_and_time():

    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    microsecond = str(datetime.datetime.now().microsecond)
    dateAndTime = year + "-" + month + "-" + day + "_" + \
        hour + "." + minute + "." + second + "." + microsecond
    return(dateAndTime)
