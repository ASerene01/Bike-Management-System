import Display


def companyName():
    companyName = input("Enter the name of the Company")
    return companyName


def order_bike_information(bikes):
    loop = 'n'
    while loop == 'n':
        print("-------------------Current Stocks---------------------------")
        Display.display_bikes()
        print(
            "If you want to add the same bike from the table then enter the id of that bike")
        print("---------------------------OR--------------------------------------")
        newBikeId = input(
            "If you want to add a new bike then enter anything to continue")
        loop = input("Are you sure you want to add a new bike(Y/N").lower()

    check = False
    for line in bikes:
        if(line[0] == newBikeId):
            check = True
            newBikeName = line[1]
            newBikeCompany = line[2]
            newBikeColor = line[3]
            newBikePrice = line[5]
            break

    for line in bikes:
        if(check == False):
            newBikeId = int(line[0]) + 1

    if check == False:
        newBikeName = input("Enter the name of the bike")
        newBikeCompany = input("Enter the name of the company of the bike")
        newBikeColor = input("Enter the color of the bike")
        newBikePrice = input("Enter the price of per bike")

    newBikeStock = input("Enter how many bikes that you want to order")
    print()
    while not(newBikeStock.isdigit()):
        print("You seem to have entered the invalid infomation of how many bikes that you want to order")
        newBikeStock = input(
            "Please enter the right amount of bikes that you want to order")
    while int(newBikeStock) == 0:
        print("You seem to have entered the invalid infomation of how many bikes that you want to order")
        newBikeStock = input(
            "Please enter the right amount of bikes that you want to order")
    return(newBikeId, newBikeName, newBikeCompany, newBikeColor, newBikeStock, newBikePrice)


def updated_list_after_order(bikes, orderInformation):

    orderList1d = list(orderInformation)
    check = False
    while check == False:
        for bike in bikes:
            if(orderList1d[0] == bike[0]):
                bike[4] = int(bike[4]) + int(orderList1d[4])
                check = True
                break
        if(check == False):
            bikes.append(orderList1d)
            check = True
    return(bikes)


def updated_file_after_order(updatedListAfterOrder):
    file = open("bike.txt", "w")

    for bike in updatedListAfterOrder:
        file.write(str(bike[0]) + "," + str(bike[1]) + "," + str(bike[2]) +
                   "," + str(bike[3]) + "," + str(bike[4]) + "," + str(bike[5]) + "\n")

    file.close()


def order_reciept_list(bikes, orderInformation, orderRecieptList):
    orderInformation = [list(orderInformation)]
    for line in orderInformation:
        orderRecieptList.append(line)
    return(orderRecieptList)


def order_reciept_file(companyInformation, dateAndTime, orderRecieptList):
    fileName = companyInformation + "_" + dateAndTime + ".txt"
    #generation of the new file for the reciept
    file = open(fileName, "w")
    header = [["Bike Id", "Bike Name", "Company",
               "Color", "Quantity", "Price", "\n"]]
    file.write("Comapny Name: ")
    file.write(companyInformation + "\t\t\t")
    file.write("Ordered Date: ")
    file.write(dateAndTime + "\n")
    file.write(
        "=========================================================================\n")
    for head in header:
        file.write(
            "{: <8} {: <12} {: <10} {: <10} {: <10} {: <10}".format(*head))
    file.write(
        "\n=========================================================================\n")
    for bike in orderRecieptList:
        file.write(
            "{: <8} {: <12} {: <10} {: <10} {: <10} {: <10}".format(*bike))
        file.write(
            "\n------------------------------------------------------------------------\n")
    totalPrice = 0
    for bike in orderRecieptList:
        totalPrice = totalPrice + (int(bike[4]) * int(bike[5]))
    totalPriceList = [["Total Price: ", str(totalPrice)]]
    for price in totalPriceList:
        file.write("{: >54} {: >3}".format(*price))
        
    #print of the order recipt inside the python program
    print("Comapny Name: ")
    print(companyInformation + "\t\t\t")
    print("Ordered Date: ")
    print(dateAndTime + "\n")
    print(
        "=========================================================================\n")
    for head in header:
        print(
            "{: <8} {: <12} {: <10} {: <10} {: <10} {: <10}".format(*head))
    print(
        "\n=========================================================================\n")
    for bike in orderRecieptList:
        print(
            "{: <8} {: <12} {: <10} {: <10} {: <10} {: <10}".format(*bike))
        print(
            "\n------------------------------------------------------------------------\n")
    for price in totalPriceList:
        print("{: >54} {: >3}".format(*price))
    file.close
