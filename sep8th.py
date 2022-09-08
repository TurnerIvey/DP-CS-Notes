print("""Todays date is 9/8/2022, and these are nots on Starting System


Warm-up is some video about "potential future of robots and robot/human interaction related to the workforce."


-- MENU --
''''''''''

Please choose on of the options below, and press enter.


1) debugging
2) validation vs verification, testing & types of testing
3) types of data used in testing 


Yo YO YO Mr. WHIIITEEEEE, type a number with corresponding topics.""")

answer = "empty"

while (answer == "empty"):
  userchoice = input()
  if(userchoice == "1"):
    print("""Testing & Bugs
   
   Testing is used to check for potential costly bugs, verify the system and related processes run successfully, as well as to validate that the product or system meets the requirements.
The systematic process of correcting (and finding) bugs or errors in a program is referred to as debugging.

Watching the video I realzied we killed a lot of people and wasted a lot of money becuase of a few sympol bucks. planes, radiation machines and rockets... In may in 1966 823 random people got several million dollars. """)
    print(""" """)
    
  elif(userchoice == "2"):
    print("Overview of Testing")
    print("""Traditionally, testing was not a big thing. It was often an afterthought after the product was basically done. Now, in present times, testing is huge. It has become its own specialized area, and some people make whole careers just out of testing. \n \n Firstly, testing can be divided into two categories, dynamic and static. 
    Dynamic testing 
    \n relates to directly using the system to test it. That is, you are actually running and operating the software or system (or a portion of it) for testing. For example, if you write a python program that calculates the interest gained on a CD available at your bank over years of time, a dynamic test would be to actually run it and make sure what the program says matches what it should say.
   Static testing relates to testing where the software or system is not actually run. You may be analyzing the algorithm design, reviewing the code, or checking client's requests related to the design documents. Examples of static testing includes methods such as reviewing technical documentation related to the software's design, or dry-runs. A dry-run is when you manually move through the code with pen-and-paper, to determine the expected outcome when the code is executed. 
   
   Functional testing relates to testing individual commands, text input, menu functions, etc. For example, if try to take a photo on your phone's camera app, does it take a picture? If you tell it to delete the picture, does it actually delete it? Unit testing relates to separately testing the individual components or parts of the system or software. These are both in contrast to integration testing, where the components are testing together within the system or software to verify that everything works correctly with each other.
   User acceptance testing relates to determining if the system satisfies the customer's needs. This is usually done on-premise before the system or software is shipped or trasnfered to the customer. Combined and Tested as a group, Data transfer between the moduels is tested thoroughly.
   
   Big - Bang
   Wait for all moduels to be developed
   Time Comsuming 
   Difficult to trace root cause of bugs
   Top to down in my opinion is the best option. However, you need a driver. """)

  elif(userchoice == "3"):
    print("Fefect Clustering.")
    print("\n \n A small number of modueles contain most of the defects detected by experience you can identify such risky moduels.")
    print("""If the same tests are repeated over and over again, eventually the same test cases will no longer find new bugs. This is the another principele of pesticide paradox.
    To overcome this, the test cases needed to be regualrly reviewed and revised, adding new and different test cases to help find more defects.
    
    YOU CAN  NOT CLAIM THAT YOUR SOFTWARE IS BUG-FREE
    
    
    As we looked over the concepts of testing, this all predominantly relates to testing by developers and QA (quality assurance) professionals. This may include a 3rd party organization outside of the company that is contracted specifically for testing.
Additionally, you should also be aware of alpha and beta testing. Alpha and beta testing goes beyond the developers testing the software in specific testing environments, and instead is closer to testing the software or system out in the wild.
In alpha testing, the software or system is released to those within the company or organization who are not specifically involved in the development or implementation of the product. For example, if you are a developer for Apple's Final Cut Pro software, when a new iPhone model is available, they may ask if you'd like one of the early models that's still in testing. This allows them to get feedback and testing data more similar to how actual customers would use the new phone model.
In beta testing, the software system is available to the public (or a group consisting of the public). As this includes the actual public, this is the closest and most realistic testing data a company or organization can get before the product is fully available. At this point, the product should be very stable, and testing may be more related to any unusual cases where the system or software may interact in an unexpected way with other software or systems, or also as a stress test if the system or software has to connect to servers or other internet-based resources.""")

  elif(userchoice == "4"):
    print("""Typcial Data (expected) that shoudld be accepted by the system. Extreme test data is when it requires values that are heavily scewed from one side or another. Boundary Test data. 
    - A pair of values of each end of a range.
    The data at the upper or ower limits of expectations that should be accepted.
    the immedidate values before or beyond the limits of expectations that should be REJECTED. 
    
    Abnormal test Data. 
    Data the falls outside of what is acceptable and should be rejected by the system. """)

  elif(userchoice == "5"):
    print(""" """)
    
  elif(userchoice == "6"):
    print(" ")
    print(" ")

  elif(userchoice == "7"):
    print(""" """)
  else: 
    print("INVALID INPUT, please try again")
    answer = "empty"
    userchoice = input()
