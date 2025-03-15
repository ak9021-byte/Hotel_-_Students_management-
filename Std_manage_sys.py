db={1:{"name":"john","city":"pune","percentage":78,"course":"python"}}

# db[roll]['name']="john"
#db[roll]['course']="python"
print("-"*80)
print(" "*30,"The Kiran Academy ")
print("-"*80)

while True:
    print(""" 
        1.Create record
        2.Display record
        3.Update record
        4.Delete record  
    """)
    i=int(input("Enter choice="))
    if i==1:
        details={}
        roll=int(input("Enter rollno= "))#2
        name=input("Enter name= ") #blake
        city=input("Enter city= ") #mumbai
        percentage=int(input("Enter percentage")) #75
        course=input("Enter course=")#java
     
        #varname[key]=value
        details['name']=name  #name:blake
        details['city']=city #city:mumbai
        details['percentage']=percentage #percentage:75
        details['course']=course # course:java
       
        db[roll]=details
        #print(db)

    elif i==2:
      print("-"*106)
      print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("roll","name","city","percentage","course"))
      print("-"*106)

      for roll in db:
          print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(roll,db[roll]['name'],db[roll]['city'], db[roll]['percentage'],db[roll]['course']))

    elif i==3:
        roll = int(input("Enter roll no = "))
        print('''
              1. name
              2.city 
              3.persentage
              4.course
              ''')
        c = int(input("Enter your choice to update : "))
        if c==1:
            upname = input("Enter name : ")
            db[roll]['name']= upname
            print("Update successfully")
        elif c==2:
            upcity = input("Enter city name : ")
            db[roll]['city']= upcity
            print("Update successfully")
        elif c==3:
            upper= int(input("Enter persentage : "))
            db[roll]['percentage']= upper
            print("Update successfully")
        elif c==4:
            upcource = input("Enter cource name : ")
            db[roll]['course']= upcource
            print("Update successfully")
        else:
            print("Invalid choice")

    elif i==4:
        roll = int(input("Enter roll :"))
        del db[roll]
        print("Record delete successfully")
    else:
        print("invlid choose")


