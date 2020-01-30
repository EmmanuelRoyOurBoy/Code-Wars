Hours, Miles, Speed = input().split()
Hours, Miles, Speed = int(Hours), int(Miles), int(Speed)
#Miles is Miles to travel
#Hours is hours until code wars starts
#Speed is mph
#Read 3 integers on one line separated by spaces "H M S", 
# representing the Hours until CodeWars starts, the miles you need to travel, and your speed in miles per hour.

#Repeat the input, then add a period and space and either "I will make it!" or "I will be late!"
distance = Speed * Miles
if Hours <= distance:
    print("I can do this")
else:
    print("I will miss it")