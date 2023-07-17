import Display
import SellBike
import OrderBike

Display.welcome_message()
message = "n"
while message == "n":
    Display.display_options()
    try:
        num = int(input("Enter the number that you want to choose"))
    except:
        print(
            "INVALID Input. Please enter the number of the options provided in the screen"
        )
        continue
    dateAndTime = Display.date_and_time()
    updatedListAfterSell = []
    bikes2D = Display.bike_2d_list()
    if num == 1:
        Display.option_sell_bikes()
        customerInformation = SellBike.customer_information()
        sellRecieptList = []
        message = "y"
        while message == "y":
            bikeId = SellBike.entered_bike_id(bikes2D)
            bikeQuantity = SellBike.bike_supply_check(bikeId, bikes2D)
            updatedListAfterSell = SellBike.updated_list_after_sell(
                bikeId, bikeQuantity, bikes2D
            )
            SellBike.updated_file_after_sell(updatedListAfterSell)
            sellRecieptList = SellBike.sell_reciept_list(
                bikeId, bikeQuantity, sellRecieptList, bikes2D
            )
            message = Display.end_message(num)
        SellBike.sell_reciept_file(
            customerInformation, dateAndTime, sellRecieptList)
    elif num == 2:
        Display.option_order_bikes()
        companyInformation = OrderBike.companyName()
        orderRecieptList = []
        message = "y"
        while message == "y":
            orderInformation = OrderBike.order_bike_information(bikes2D)
            updatedListAfterOrder = OrderBike.updated_list_after_order(
                bikes2D, orderInformation
            )
            OrderBike.updated_file_after_order(updatedListAfterOrder)
            orderRecieptList = OrderBike.order_reciept_list(
                bikes2D, orderInformation, orderRecieptList
            )
            message = Display.end_message(num)
        OrderBike.order_reciept_file(
            companyInformation, dateAndTime, orderRecieptList)
    elif num == 3:
        Display.option_exit()
    else:
        Display.option_invalid()
        continue
