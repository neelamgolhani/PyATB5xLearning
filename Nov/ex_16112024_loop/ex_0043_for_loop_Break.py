for i in range (0,10):
    print(i)
    if i==5:
        break
    else:  #// will not execute
        print(i) # // will not execute


#|i | Condition | o/p
#|0| 0==5 -> False | O/P = 0
#|1| 1==5 -> False | O/P = 1
#|2| 2==5 -> False | O/P = 2
#|3| 3==5 -> False | O/P = 3
#|4| 4==5 -> False | O/P = 4
#|5| 5==5 -> True | O/P = Five // break out from for loop
#|6| 6==5 -> False | O/P = 6 // will not execute
#|7| 7==5 -> False | O/P = 7 // will not execute
