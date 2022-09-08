print("""Todays date is 9/6/2022, and these are nots on Starting System


Warm-up is some video about "potential future of robots and robot/human interaction related to the workforce."


-- MENU --
''''''''''

Please choose on of the options below, and press enter.


1) SaaS
2) On-Premise Software
3) System Life Cycle
4) Functional Testing

5) issues in Data Migration
6) related to Business M&A includes Merger vs Acquisitio and System Integration follow M&A
7) find examples and todays assignment. 


Yo YO YO Mr. WHIIITEEEEE, type a number with corresponding topics.""")

answer = "empty"

while (answer == "empty"):
  userchoice = input()
  if(userchoice == "1"):
    print("""
By 'centrally hosted', what we mean is that the software is not run on the local computer system, but instead uses the internet to connect to servers from the software manufacturer. It is on the software manufacturer's servers that the software is run, managed, and maintained. An everyday example would be Google Docs. An example in the business would be the widely used enterprise software by German software company SAP SE. """)
    print("""
    Advantages: 
Lower initial costs, likely faster implementation
Maintenance and updates by software manufacturer
No staff needed to maintain the system 
Software manufacturer likely provides more support
On-site natural disasters do not put data at risk 

    Disadvantages: 
continued subscription fees may ultimately be more expensive than On-premises software or custom designed software for large companies
Potential data-risk from software manufacturer
Potential differing time zones, maintenance and support may not be at convenient times
Specialized or unusual needs of a specific client may not be a priority of the software manufacturer
Because host is not the user itself, user feedback is harder to get
System change may be required sooner than ideal if the service is discontinued, the company seeks new functionality that the manufacturer is not interested in adding, or the manufacturer goes out of business 

So is SaaS the better and less expensive option? because the other stuff like Paas and Iaas
Is cost a factor? ofc it is a limitation. Points to consider, resource pooling cpu, mem and storage. 
Factor in eddeinicnes, and shifts i
""")
    
  elif(userchoice == "2"):
    print("On-Premise Software")
    print("""On-Premise Software is software that is installed and runs on computers on the premises of the person or organization using the software, rather than at a remote facility such as a server farm or cloud. On-premises software is sometimes referred to as “shrinkwrap” software, and off-premises software is commonly called “software as a service” (SaaS) or “cloud computing”.
    On-premise software or systems typically require having on-staff IT professionals. If there is an issue that local staff can't solve, it may require remote access with the software/system provider, or may even require IT Support or a Software Engineer to travel to help resolve the issue. This can result in further expenses as well as lost time. For small companies, on-premise software or systems may have a lot of unexpected costs when issues occur. However, with SaaS, you may have additional costs too, such as legal costs related to contracts. Software as a Service is a software licensing and delivery model in which software is licensed on a subscription basis and is centrally hosted. It is sometimes referred to as "on-demand software", and was formerly referred to as "software plus services" by Microsoft.""")

  elif(userchoice == "3"):
    print("Software Development Lifecycle")
    print("This refers to the stages we move through when developing a new system. There are a variety of ways to illustrate and discuss this, and no specific way is accurate all the time, as needs and situations can vary significantly. Ideally, we move through the stages one at a time, without having to backtrack.Realistically thought, we often talk about it as a cycle as we know we know we will probably have to move back and forth between stages as well as move through the whole cycle again as time progresses and our needs change.We can look at System Life Cycles related specifically to systems, or specifically related to software. However, the two are not significantly different. Below, you can see how it specifically relates to Software Development.")
    print("""Do note that the Planning & Analysis stage should also include analysis of existing systems, both that may be in use by the client, or that may be available to the client.

While we generally consider all of these stages in the SDLC, for the IA, you'll focus on Planning & Anaylsis, Evaluation, Design Overview, and Development.
1. Planning
2. Requirment Analysis
3. Design
4. Implementation / coding
5. Testing
6. Deployment
7. Maintenance """)

  elif(userchoice == ""):
    print("""Do note that the Planning & Analysis stage should also include analysis of existing systems, both that may be in use by the client, or that may be available to the client.

While we generally consider all of these stages in the SDLC, for the IA, you'll focus on Planning & Anaylsis, Evaluation, Design Overview, and Development. In functional testing, each software function, or feature, is compared with an organization's specifications to ensure that the software provides the output that an end user or business requires. Software developers use functional testing as a method to perform quality assurance (QA). """)

  elif(userchoice == "5"):
    print("""Choose a streaming service. 
Is it SaaS or on-premise? NETFLIXS 
List some of the functionalities of the service that you would test prior to its release. Yes, Netflix is a SaaS company that sells software to watch licensed videos on demand. It follows a subscription-based model whereby the user chooses a subscription plan and pays a fixed sum of money to Netflix monthly or annually. I would test first if the platform actually works and if the video application works. Then I will test if the payment plans work. Like USER REGISTRATION. Passwords and other things, logout button, clear session and things
if the main oage wokrs, how it redirects 

Choose an app or software that is NOT a streaming service. 
Is it SaaS or on-premise?
List some of the functionalities of the service that you would test prior to its release. 
Subway Surfers is an endless runner mobile game co-developed by Kiloo and SYBO Games, private companies based in Denmark. It is available on Android, iOS, ... so yes? I don't know but I am pretty sure it is on-premise anyway I would defintly make sure the game works. """)
    
  elif(userchoice == "6"):
    print(" ")
    print(" ")

  elif(userchoice == "7"):
    print(""" """)
  else: 
    print("INVALID INPUT, please try again")
    answer = "empty"
    userchoice = input()
