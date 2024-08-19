print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


bill = 0
bill_log = []


if size == "M":
    bill += 20
    bill_log.append(str(20))

elif size == "L":
    bill += 25
    bill_log.append(str(25))

elif size == "S":
    bill += 15
    bill_log.append(str(15))

else:
    print("There is no size choice as the one you type\n"
          "only 'S', 'M' and 'L' are available")
    bill_log.append(str(0))



if pepperoni == "Y":
    if size == "S":
        bill += 2
        bill_log.append(str(2))
    elif size == "M" or size == "L":
        bill += 3
        bill_log.append(str(3))
    else:
        bill_log.append(str(0))
else:
    bill_log.append(0)


if extra_cheese == "Y":
    bill += 1
    bill_log.append(str(1))
else:
    bill_log.append(str(0))

print(f"Your final bill is: (${bill}).\n"
      f"You paid (${bill_log[0]}) for pizza size, "
      f"(${bill_log[1]}) for pepperoni and "
      f"(${bill_log[2]}) for extra cheese")

