"""Building the car game ::
Car Game::
            > help
             start- to start the car
               stop - to stop the car
               quit - to exit

           > asd
             I don't understand this.
           > start
              Car started.... Ready to go!!
           > stop
              car stopped...
           > qui"""
'''
  Building the car game ::
  CAR GAME:
        > help
          start - to start the car
          stop - to stop the car
          quit - to exit

        > asd
          I don't understand this
        > start
          Car started... Ready to go!!
        > stop
          Car stopped..
        > quit
'''

# Uses while condition until the user writes quit.

#solution

'''
command = ""
while command != "quit":
    while command.lower() != "quit":
        command = input("> ")
        if command.lower() == "start":
            print("Car Started !!")
        elif command.lower() == "stop":
            print("Car stopped !!")

---- everytime command.lower is inappropriate format 
---- follow dry (don't repeat yourself) -- code culture
'''
#-----------------------------------------------------------------

'''
command = ""
#while command != "quit":
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car started !!")
    elif command == "stop":
        print("Car stopped !!")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that !!")
---------------------------------------------------------------------
'''

command = ""
started = True

# while command != "quit":

while started:
    started = False
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started !!")
        else:
            started = True
            print("Car started !!...")
    elif command == "stop":
        if not started:
            print("Car is already stopped !!")
        else:
            started = False
            print("Car stopped !!..")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "quit" or "exit":
        started = False


    else:
        print("Sorry, I don't understand that !!")
