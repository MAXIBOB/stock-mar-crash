def choose_your_own_adventure():
  print "Welcome to choose your own adventure!"
  print
  print "xyz"
  answer = raw_input("What do you do? ")
  if answer == "a":
    print
    print "abc"
    answer = raw_input("What do you do? ")
    if answer == "b":
      print
      print "def"
      answer = raw_input("What do you do?")
      if answer == "c":
        print
        print "ghi"
        answer = raw_input("What do you do?")
        if answer == "d":
          print
          print "Congratulations!"
          answer = raw_input("Play again? ")
          if answer.lower() == "yes" or answer.lower == "y":
            choose_your_own_adventure()
          else:
            print "Good-bye"
        else:
          print
          print "Too bad"
          answer = raw_input("Play again? ")
          if answer.lower() == "yes" or answer.lower() == "y":
            choose_your_own_adventure()
          else:
            print "Good-bye"
      else:
        print
        print "Too bad"
        answer = raw_input("Play again? ")
        if answer.lower() == "yes" or answer.lower() == "y":
          choose_your_own_adventure()
        else:
          print "Good-bye"
    else:
      print
      print "Too bad"
      answer = raw_input("Play again? ")
      if answer.lower() == "yes" or answer.lower() == "y":
        choose_your_own_adventure()
      else:
        print "Good-bye"
  else:
    print
    print "Too bad"
    answer = raw_input("Play again? ")
    if answer.lower() == "yes" or answer.lower() == "y":
      choose_your_own_adventure()
    else:
      print "Good-bye"
choose_your_own_adventure()
