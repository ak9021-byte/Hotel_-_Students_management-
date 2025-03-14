hotel_rooms = {1: 'Standard Room', 2:'Deluxe Room', 3: 'Suite', 4: 'Executive Room', 5: 'Presidential Suite', 6: 'Family Room', 7: 'Twin Room', 8:'Double Room' }
prize = {1:3000, 2:5000, 3:7000, 4: 9000, 5: 5500, 6:6000, 7:4000 , 8:3500}


rooms= []
q= []
name = input("Enter your name : ")
mobile_no = input("Enter mobile number : ")
Aadhar_num = input("Enter aadhar card number : ")

while True:
    print('''
1: Standard Room  
✅ Basic amenities (bed, TV, bathroom)  
💰 Price: ₹3,000 per night  

2: Deluxe Room  
✅ More spacious than standard rooms  
✅ Better furniture and decor  
💰 Price: ₹5,000 per night  

3: Suite  
✅ Large, luxurious room with separate living area  
✅ Often includes a kitchenette and premium services  
💰 Price: ₹7,000 per night  

4: Executive Room  
✅ Designed for business travelers  
✅ Includes a work desk and additional facilities  
💰 Price: ₹9,000 per night  

5: Presidential Suite  
✅ Most luxurious room in a hotel  
✅ Offers top-class service, large space, and high-end amenities  
💰 Price: ₹5,500 per night  

6: Family Room  
✅ Larger room for families  
✅ Often includes multiple beds or a sofa bed  
💰 Price: ₹6,000 per night  

7: Twin Room  
✅ Two separate single beds  
✅ Ideal for friends or colleagues sharing a room  
💰 Price: ₹4,000 per night  

8: Double Room  
✅ One double bed for two people  
✅ Best for couples  
💰 Price: ₹3,500 per night  ''')

    select= int(input("Select room type by room number  : "))
    qunatity = int(input("Enter quantity of rooms: "))

    rooms.append(select)
    q.append(qunatity)

    print(rooms)
    print(q)

    more = input("You want or another type of room's ?  yes/no :")
    if more=="no":
        print(("-"*105))
        print("|Payment Details                                                                    Hotel no:9021587404|" )                                                                                       
        print("  ")
        print(f"| name : {name}            mobile.no : {mobile_no}           aadhar no: {Aadhar_num}                                      |")
        print("-"*105)
       
        print("|{:^20} |{:^20} |{:^20} |{:^20} |{:^15}|" .format("ID", "Room Type", "Price per Day", "Quantity",  "Rent"))
        print("-"*105)
        for i in range(len(rooms)):
            sum=0
            print("|{:^20} |{:^20} |{:^20} |{:^20}| {:^15}|" .format((i+1), hotel_rooms[rooms[i]], prize[rooms[i]], q[i] , prize[rooms[i]]*q[i]))
            sum= sum+prize[rooms[i]]*q[i]
            print("-"*105)
    print(f"|Total amount is: {sum}|")
    print("-"*105)
           
    print("----- Thank you for visit -----")

            






