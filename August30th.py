print("""Todays date is 8/30/2022, and these are nots on Starting System


Today we are going over the some North Caroloina State Univesity, oddly enough)


-- MENU --
''''''''''

Please choose on of the options below, and press enter.


1) System and Legacy Systems
2) Planning
3) Feasibility, including TELOS
4) Change Management
5) Business Merger
6) Real World Example: and US Post Office
7) Hypothetical Example: and Encyclopedia Sales


Yo YO YO Mr. WHIIITEEEEE, type a number with corresponding topics.""")

answer = "empty"

while (answer == "empty"):
  userchoice = input()
  if(userchoice == "1"):
    print("Systems: A computer system is a full IT system of all related parts, including the people and the immediate environment. The system may include training employees and/or users, as well as maintaining and protecting data or hardware.")
    
    print("\n \n answer: Ultimately though, the new system should improve the cost-to-benefit ratio in contrast to not implementing the system. However, sometimes new systems must work in tandem with a legacy system. If a legacy system contains lots of data or storage, it may not be realistic to transfer everything to a new system if there is no automated way to transfer the data. A legacy system is outdated computing software or hardware that is still in use, but its older technology won't allow it to interact with newer systems.")
    
  elif(userchoice == "2"):
    print(" \n \n When planning and implementing a new system, this would include discussing new hardware, changing potential locations of technology, new policies, new training and upskilling,  and potentially hiring and firing employees as well. There are a variety of issues that should be considered when planning")
    print("""\n a lack of:
  - organizational & business strategy
  - stakeholder & end-user participation
  - end-user 'ownership'
  attention to: 
  - required training
  - organizational issues, including group culture
  - design of tasks & job roles
  - overall usability of the system""")

  elif(userchoice == "3"):
    print("After considering and attempting to anticipate issues related to the above, a feasibility study should be conducted. A feasibility study should cover several different areas. A common acronym is TELOS.")
    print("James A. Hall presented the TELOS framework in Accounting Information Systems (2007). Hall explains it use as the basis of a feasibility study to make a project more successful and identify fundamentally flaws before investing time and effort into it. TELOS is an acronym for five key area.")
    print("""TELOS is an acronym for five key areas that you need to explore as part of your study:

- Technological.
- Economic.
- Legal.
- Organizational.
- Scheduling.""")

  elif(userchoice == "4"):
    print("What is Organziational Change is in charge of shifting, hiring, or letting employees or whole departments go. It also changes the process or work the employees do. Its goal is to maximize benefits and minimums negatvies for all the stakeholders involved in the process Organizational change management (OCM) is a framework for managing the effect of new business processes, changes in organizational structure or cultural changes within an enterprise. Simply put, OCM addresses the people side of change management.")

  elif(userchoice == "5"):
    print("In corporate finance, mergers and acquisitions are transactions in which the ownership of companies, other business organizations, or their operating units are transferred or consolidated with other entities.")
    
  elif(userchoice == "6"):
    print("Real World Example: and US Post Office")
    print("\n \n basically you put all three letters space 1, it was a video with that guy that apparently is in every subject. 3 + 1")

  elif(userchoice == "7"):
    print("An encyclopedia company currently uses door-to-door and person-to-person style salespersons to find potential customers and take orders. The orders are then taken to a company office and are then input by a secretary. The company has decided that the salespeople will instead input the orders themselves, using their own personal technology.") 
    print("What potential effects, related to today's topics, might arise from this system change? Include this in your Python program for today.")
    print(" ")
  
  else: 
    print("INVALID INPUT, please try again")
    answer = "empty"
    userchoice = input()
  
