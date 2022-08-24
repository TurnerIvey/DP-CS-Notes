print("""15th Century POLAND

The 15th Centruy Poland was apart of the Polish Lithuanian Common wealth


-- MENU --
''''''''''

Please choose on of the options below, and press enter.


1) Question and Answer 1
2) Question and Answer 2
3) Question and Answer 3
""")

answer = "empty"

while (answer == "empty"):
  userchoice = input()
  if(userchoice == "1"):
    print("What are your thoughts in response to this video? How might these new technologies affect education?")
    print("answer: Well these robots are kinda scary, I don't understand how cows affect education. 3D printing houses are definitely interesting, and the brick building robot is very new. Amazon changed the world and these new drones are impeccable. It seems virtually every job is being taken over by robots… Why teach children to do math when a computer can do it indefinitely better? Education is virtually teaching us nothing that a computer can not do. Maybe it's time for a more ethical base teaching program instead of the one we currently have. I would love to see a world where Humans can live in unison and all the Robots can take care of us. Like in Wall-E I want to be lazy and play chess all day.")
  elif(userchoice == "2"):
    print("Have you heard of the 4th Industrial Revolution?")
    print("answer: I have not heard of the 4th Industrial Revolution but I think it is technically the “third” we already had this conversation in person Mr. Wegschied but as you put it, I am a lumper. I am curious if modern technology is plateauing, I have not heard of an absurd technology breakthrough in awhile, just improvements on the past. Probably because I am young but still, I want a crazy new invention. ")
  elif(userchoice == "3"):
    print("Should we change how our school systems work?")
    print("I think that our education system is relatively good, It is very versatile… I think that school should be a little more history intensive just because I like history….")
  else: 
    print("INVALID INPUT, please try again")
    answer = "empty"
    userchoice = input()
  
