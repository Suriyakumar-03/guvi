starting_dst=int(input("the starting distance is:"))
ending_dst=int(input("the ending distance is:")) 
peaktime=int(input("enter peaktime is 2 for normal time 0 :"))
total_dst=(ending_dst-starting_dst)

if(total_dst>5):
 basic_fare=((total_dst-5)*8)+100
else:
 print("the fare is 100")
if(peaktime==2):
 total_fare=basic_fare+(basic_fare*0.25)
 print("the total fare",total_fare)
else:
 print("the basic_fare",basic_fare)
 

