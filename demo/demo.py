import shift
import sys
import time


def demo01(trader):
    """
    This method submits a limit buy order by indicating symbol, limit price, limit size and order type.
    :param trader:
    :return:
    """

    limitBuy = shift.Order(shift.Order.LIMIT_BUY, "AAPL", 1, 10.00)
    trader.submitOrder(limitBuy)

    return


def demo02(trader):
    """
    This method submits 2 limit buy orders by indicating symbol, limit price, limit size and order type.
    :param trader:
    :return:
    """

    aaplLimitBuy = shift.Order(shift.Order.LIMIT_BUY, "AAPL", 10, 10.00)
    trader.submitOrder(aaplLimitBuy)

    xomLimitBuy = shift.Order(shift.Order.LIMIT_BUY, "XOM", 10, 10.00)
    trader.submitOrder(xomLimitBuy)

    return


def demo03(trader):
    """
    This method prints the local bid order book for corresponding symbols.
    :param trader:
    :return:
    """

    print("AAPL:")
    print("Price\tSize\tDest\tTime")
    for order in trader.getOrderBook("AAPL", shift.OrderBookType.LOCAL_BID):
        print("%5.2f\t%4d\t%s\t%s" %
              (order.price, order.size, order.destination, order.time))

    print()

    print("XOM:")
    print("Price\tSize\tDest\tTime")
    for order in trader.getOrderBook("XOM", shift.OrderBookType.LOCAL_BID):
        print("%5.2f\t%4d\t%s\t%s" %
              (order.price, order.size, order.destination, order.time))


def demo04(trader):
    """
    This method prints all current waiting orders information.
    :param trader:
    :return:
    """

    print("Symbol\tType\t\t\t\t\tPrice\tSize\tID\t\t\t\t\t\t\t\t\t\tTimestamp")
    for order in trader.getWaitingList():
        print("%6s\t%s\t\t%5.2f\t%4d\t%s\t%s" %
              (order.symbol, order.type, order.price, order.size, order.id, order.timestamp))

    return


def demo05(trader):
    """
    This method cancels all the orders in the waiting list.
    :param trader:
    :return:
    """

    print("Symbol\tType\t\t\t\t\tPrice\tSize\tID\t\t\t\t\t\t\t\t\t\tTimestamp")
    for order in trader.getWaitingList():
        print("%6s\t%s\t\t%5.2f\t%4d\t%s\t%s" %
              (order.symbol, order.type, order.price, order.size, order.id, order.timestamp))

    print()

    print("Waiting list size: " + str(trader.getWaitingListSize()))

    print("Canceling all pending orders...", end=" ")

    # trader.cancelAllPendingOrders() also works
    for order in trader.getWaitingList():
        if order.type == shift.Order.LIMIT_BUY:
            order.type = shift.Order.CANCEL_BID
        else:
            order.type = shift.Order.CANCEL_ASK
        trader.submitOrder(order)

    i = 0
    while trader.getWaitingListSize() > 0:
        i += 1
        print(i, end=" ")
        time.sleep(1)

    print()

    print("Waiting list size: " + str(trader.getWaitingListSize()))

    return


def demo06(trader):
    """
    This method shows how to submit market buy orders.
    :param trader:
    :return:
    """

    aaplMarketBuy = shift.Order(shift.Order.MARKET_BUY, "AAPL", 1)
    trader.submitOrder(aaplMarketBuy)

    xomMarketBuy = shift.Order(shift.Order.MARKET_BUY, "XOM", 1)
    trader.submitOrder(xomMarketBuy)

    return


def demo07(trader):
    """
    This method provides information on the structure of PortfolioSummary and PortfolioItem objects:
     getPortfolioSummary() returns a PortfolioSummary object with the following data:
     1. Total Buying Power (totalBP)
     2. Total Shares (totalShares)
     3. Total Realized Profit/Loss (totalRealizedPL)
     4. Timestamp of Last Update (timestamp)

     getPortfolioItems() returns a dictionary with "symbol" as keys and PortfolioItem as values, with each providing the following information:
     1. Symbol (getSymbol())
     2. Shares (getShares())
     3. Price (getPrice())
     4. Realized Profit/Loss (getRealizedPL())
     5. Timestamp of Last Update (getTimestamp())
    :param trader:
    :return:
    """

    print("Buying Power\tTotal Shares\tTotal P&L\tTimestamp")
    print("%12.2f\t%12d\t%9.2f\t%s" % (trader.getPortfolioSummary().getTotalBP(),
                                       trader.getPortfolioSummary().getTotalShares(),
                                       trader.getPortfolioSummary().getTotalRealizedPL(),
                                       trader.getPortfolioSummary().getTimestamp()))

    print()

    print("Symbol\t\tShares\t\tPrice\t\tP&L\t\tTimestamp")
    for item in trader.getPortfolioItems().values():
        print("%6s\t\t%6d\t%9.2f\t%7.2f\t\t%s" %
              (item.getSymbol(), item.getShares(), item.getPrice(), item.getRealizedPL(), item.getTimestamp()))

    return


def demo08(trader):
    """
    This method shows how to submit market sell orders.
    :param trader:
    :return:
    """

    aaplMarketSell = shift.Order(shift.Order.MARKET_SELL, "AAPL", 1)
    trader.submitOrder(aaplMarketSell)

    xomMarketSell = shift.Order(shift.Order.MARKET_SELL, "XOM", 1)
    trader.submitOrder(xomMarketSell)

    return


def demo09(trader):
    """
    This method prints all submitted orders information.
    :param trader:
    :return:
    """

    print("Symbol\tType\t\t\t\t\tPrice\tSize\tID\t\t\t\t\t\t\t\t\t\tTimestamp")
    for order in trader.getSubmittedOrders():
        print("%s\t%s\t\t%5.2f\t%4d\t%s\t%s" %
              (order.symbol, order.type, order.price, order.size, order.id, order.timestamp))

    return


def demo10(trader):
    """
    This method prints the global bid order book for a corresponding symbol and type.
    :param trader:
    :return:
    """

    print("Price\tSize\tDest\tTime")
    for order in trader.getOrderBook("AAPL", shift.OrderBookType.GLOBAL_BID, 5):
        print("%5.2f\t%4d\t%s\t%s" %
              (order.price, order.size, order.destination, order.time))


def demo11(trader):
    """
    This method prints the global bid order book for a corresponding symbol and type,
    with routing (destination) information.
    :param trader:
    :return:
    """

    print("Price\tSize\tDest\tTime")
    for order in trader.getOrderBookWithDestination("AAPL", shift.OrderBookType.GLOBAL_BID):
        print("%5.2f\t%4d\t%s\t\t%s" %
              (order.price, order.size, order.destination, order.time))


def main(argv):
    # create trader object
    trader = shift.Trader("democlient")

    # connect and subscribe to all available order books
    try:
        trader.connect("initiator.cfg", "password")
        trader.subAllOrderBook()
    except shift.IncorrectPassword as e:
        print(e)
    except shift.ConnectionTimeout as e:
        print(e)

    # demo01(trader)
    # demo02(trader)
    # demo03(trader)
    # demo04(trader)
    # demo05(trader)
    # demo06(trader)
    # demo07(trader)
    # demo08(trader)
    # demo09(trader)
    # demo10(trader)
    # demo11(trader)

    # disconnect
    trader.disconnect()

    return


if __name__ == "__main__":
    main(sys.argv)
