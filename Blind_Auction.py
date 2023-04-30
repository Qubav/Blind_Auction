from os import system as sys

def blind_auction():
    # variables
    auction_book = {}
    bidding_finished = False
    highest_bidder = ""
    highest_bid = 0
    
    # communication with user
    print("Welcome to the secret auction!")

    # main loop where all actions connected with submitting new bid take place
    # loop last as long as user tell program there are other bidders left
    while not bidding_finished:
        bidders_name = input("What is yourn name? ")
        bid = float(input("What is your bid? $"))

        # adding new bidders name and bid to auction book 
        auction_book[bidders_name] = bid

        # asking if there are other bidders left and based on answer variable responsible for loop might be changed
        should_continue = input("Are there any other bidders? Type \"yes\" or \"no\".\n")
        if should_continue == "no":
            bidding_finished = True
        
        # clearing terminal so other bidders won't see earlier bids
        sys("cls")

    # looping through dictionary to find highest bid and bidder who bidded it
    for bidder in auction_book:
        if auction_book[bidder] > highest_bid:
            highest_bidder = bidder
            highest_bid = auction_book[bidder]
    
    # communication with user
    print(f"The auction has ended!\nHighest bidder is {highest_bidder} and highest bid is {highest_bid}!")


if __name__ == "__main__":
    blind_auction()

            

    