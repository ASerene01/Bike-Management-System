import Display


def customer_information():
    customerFirstName = input("Enter the first name of the customer")
    while not customerFirstName.isalpha():
        print("Invalid customer's first name!")
        print("Just use alpabets to the customer's first name")
        customerFirstName = input(
            "Please enter the first name of the customer correctly")
    customerSecondName = input("Enter the second name of the customer")
    while not customerSecondName.isalpha():
        print("Invalid customer's second name!")
        print("Just use alpabets to the customer's second name")
        customerSecondName = input(
            "Please enter the second name of the customer correctly")
    customerName = customerFirstName + "_" + customerSecondName
    customerAddress = input("Enter the address of the customer")
    customerNumber = input("Enter the number of the customer")
    while not customerNumber.isdigit():
        print("Invalid customer number!")
        print("Just use numbers to the customer's number")
        customerNumber = input(
            "Please enter the number of the customer correctly")
    return customerName, customerAddress, customerNumber


def entered_bike_id(bike2D):

    bikeId = 0
    loop = True
    while loop == True:
        Display.display_bikes()
        try:
            validBikeId = int(input("Enter ID of the bike to sells:"))
            while validBikeId <= 0 or validBikeId > len(bike2D):
                print("Please provide a valid bike ID!!!")
                Display.display_bikes()
                validBikeId = int(input("Enter ID of bike to sell:"))
            for bike in bike2D:
                if int(bike[0]) == validBikeId:
                    if int(bike[4]) == 0:
                        bikeId = int(bike[0])

            while validBikeId == bikeId:
                print("Out of stock!!!")
                Display.display_bikes()
                validBikeId = int(input("Enter ID of bike to sell:"))
                while validBikeId <= 0 or validBikeId > len(bike2D):
                    print("Please provide a valid bike ID!!!")
                    Display.display_bikes()
                    validBikeId = int(input("Enter ID of bike to sell:"))
                for bike in bike2D:
                    if int(bike[0]) == validBikeId:
                        if int(bike[4]) == 0:
                            bikeId = int(bike[0])
            return validBikeId
            loop = False
        except:
            print("You seem to have entered invalid bike id")
            print("Please enter the id of bike that you want to sell")
            continue


def bike_supply_check(bikeId, bikes2D):
    loop = True
    while loop == True:
        try:
            quantity = 0
            validquantity = 0
            for line in bikes2D:
                if bikeId == int(line[0]):
                    quantity = int(line[4])
                    validquantity = int(
                        input(
                            "Enter the quantity of the bike that you want to sell"
                        ))
                    while validquantity > quantity:
                        Display.display_bikes()
                        print(
                            "Please provide a valid quanty of bike that you want to sell!!!"
                        )
                        validquantity = int(
                            input(
                                "Enter the quantity of the bike that you want to sell:"
                            ))
            return validquantity
            loop = False
        except:
            print("You seem to have entered invalid bike quantity")
            print("Please enter a valid quantity of bikes to sell")
            Display.display_bikes()
            continue


def updated_list_after_sell(bikeId, bikeQuantity, bikes2D):

    for line in range(len(bikes2D)):
        if bikeId == int(bikes2D[line][0]):
            bikes2D[line][4] = int(bikes2D[line][4]) - bikeQuantity
            return bikes2D


def updated_file_after_sell(updatedListAfterSell):
    file = open("bike.txt", "w")
    for bike in updatedListAfterSell:
        file.write(
            str(bike[0]) + "," + str(bike[1]) + "," + str(bike[2]) + "," +
            str(bike[3]) + "," + str(bike[4]) + "," + str(bike[5]) + "\n")
    file.close()


def sell_reciept_list(bikeId, bikeQuantity, sellRecieptList, bikes2D):
    check = False
    for bike in range(len(sellRecieptList)):
        if bikeId == int(sellRecieptList[bike][0]):
            sellRecieptList[bike][4] = int(
                sellRecieptList[bike][4]) + bikeQuantity
            check = True
            break
        else:
            check = False
    if check == False:
        for line in bikes2D:
            if bikeId == int(line[0]):
                line[4] = bikeQuantity
                sellRecieptList.append(line)
    return sellRecieptList


def sell_reciept_file(customerInformation, dateAndTime, sellRecieptList):
    fileName = customerInformation[0] + "_" + dateAndTime + ".txt"
    # generation of the new file for reciept
    file = open(fileName, "w")
    header = [[
        "S.N.", "Bike Name", "Company", "Color", "Quantity",
        "Price per bike", "\n"
    ]]
    file.write("Customer Name: ")
    file.write(customerInformation[0] + "\t\t\t")
    file.write("Customer Address: ")
    file.write(customerInformation[1] + "\n")
    file.write("Customer Number: ")
    file.write(customerInformation[2] + "\t\t\t")
    file.write("Sold Date: ")
    file.write(dateAndTime + "\n")
    file.write(
        "=========================================================================\n"
    )
    for head in header:
        file.write(
            "{: <8} {: <12} {: <10} {: <10} {: <10} {: <10}".format(*head))
    file.write(
        "\n=========================================================================\n"
    )
    for bike in sellRecieptList:
        i = 1
        bike[0] = i
        file.write(
            "{: <8} {: <12} {: <10} {: <10} {: <10} {: <10}".format(*bike))
        file.write(
            "\n------------------------------------------------------------------------\n"
        )
    totalPrice = 0
    for bike in sellRecieptList:
        totalPrice = totalPrice + (bike[4] * int(bike[5]))
    totalPrice = str(totalPrice)
    totalPriceList = [["Total Price: ", totalPrice]]
    for price in totalPriceList:
        file.write("{: >54} {: >3}".format(*price))

    # print of the reciept inside the program
    print("Customer Name: ")
    print(customerInformation[0] + "\t\t\t")
    print("Customer Address: ")
    print(customerInformation[1] + "\n")
    print("Customer Number: ")
    print(customerInformation[2] + "\t\t\t")
    print("Sold Date: ")
    print(dateAndTime + "\n")
    print(
        "=========================================================================\n"
    )
    for head in header:
        print(
            "{: <8} {: <12} {: <10} {: <10} {: <10} {: <10}".format(*head))
    print(
        "\n=========================================================================\n"
    )
    for bike in sellRecieptList:
        i = 1
        bike[0] = i
        print(
            "{: <8} {: <12} {: <10} {: <10} {: <10} {: <10}".format(*bike))
        print(
            "\n------------------------------------------------------------------------\n"
        )
    for price in totalPriceList:
        print("{: >54} {: >3}".format(*price))
    file.close
