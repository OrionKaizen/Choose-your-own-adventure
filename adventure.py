#This will be my first game with tutorials. :)
#a bit about me, I'm a very new programmer who is trying to land an internship before the end of October 2022, and I am going to be programming everyday until I get there

print("Hello! And welcome to my first game! Answer the prompts with correct spelling and choose your own adventure!")
name = input("What is your name? ")
age = input("What is your age? ")
print("Hello", name,"you are", age, "years old.")



is_older = int(age) >= 18
if (int(age) < 18):
  print("You're too young to play...")
  
    
else :
  print("You're old enough to play!")
  
  wants_to_play = input("Do you want to play? ").lower()
  if wants_to_play == "yes":
   print("Let's play!")

  left_or_right = input("First choice! Left or Right (left/right)? ").lower()
  if left_or_right == "left":
    ans = input("Good job. You follow a path and come across a lake. Do you want to follow the path around the lake or swim through the lake (around/across)? ").lower() 
    if ans == "around":
      ans = input("Well it took you forever, but you made it around. In front of you is a house and an ominous looking forest. Do you choose to go into the house or the forest (house/forest)? ").lower()
      if ans == "house":
        print("Congratulations! You walked into a house full of lead paint and asbestos. You inhale the fumes and die. Weak.")

      elif ans == "forest":
        ans = input("As you walk through the forest you come across an animal. It seems to be larger in size but you can't quite make out what it is. Do you go up to it or go around (up/around)? ")
        if ans == "around":
          ans = input("As you're going around you happen to glance over and notice the largest bear you've ever seen as the animal you couldn't make out. Lucky you it doesn't notice you (unlike the plebs who chose up). You continue walking and come across a road and a mountain. You know if you choose the road, you have a high likelihood of finding civilization, however, cool big rock on mountain. Where do you go (road/mountain)? ")
          if ans == "road":
            print("Well, despite your attempt at an intelligent decision, you get hit by a car driven by a 96 year old woman going 101 mph. Try standing to the SIDE of the road instead of IN it next time.")
          elif ans == "mountain":
            ans = input("After nearly passing out climbing the mountain, you reach the top and get to see big rock. nice. However, now you've got to go down. Do you choose to jump off a cliff (please don't) or do you hike down slowly (cliff/hike)? ")
            if ans == "cliff":
              print("Well you're dead... Don't know what you thought was gonna happen...")
            elif ans == "hike":
              ans = input("You hike down, stand on the side of the road and hitch-hike to a nearby town in one of those open door Jeeps. However on the wayhik you cross a huge bridge. Do you submit to the intrusive thoughts and jump or do you do nothing an assure your safety (jump/nothing)? ")
              if ans == "jump":
                print("... Why?")
              elif ans == "nothing":
                print("You've survived a lot, now you're safe. Try not to do anything stupid for a while, I think you used up all your luck for the year.")

        elif ans == "up":
          print("You walk up and notice it's probably the largest bear you've ever seen. You hope it doesn't notice you. It does. You can now add 'brutally mauled by a bear' to your completed bucket list. Also you died.")


    elif ans == "across":
      ans = input("You managed to get across, but a snapping turtle ate your toes (lmao nerd). You lost 5 health. In front of you is a house and an ominous looking forest, do you choose to enter the house or the forest (house/forest) ?")
      if ans == "house":
        print("Congratulations! You walked into a house full of lead paint and asbestos. You inhale the fumes and die. Weak.")
      elif ans == "forest":
        ans = input("You walk into the forest and trip on a branch immediatly. You have now decided you hate wood and set fire to the forest. Do you choose to stay and watch your handiwork or leave and find somewhere else to explore (stay/leave)? ").lower()
        if ans == "stay":
          print("Congratulations dipshit, you burned alive. Didn't think modern humans had to be reminded that 'Fire Bad' ")
        elif ans == "leave":
          print("Congratulations! By some miracle of God you found a road and hitchiked back to civilization. Guess you made it out alive, which is pretty surprising. Try not to get lost again I don't think your cave-man brain can handle another set of life changing decisions.")

    else: 
      print("That wasn't an option dumbass.")

  if left_or_right == "right":
    print("You just walked off a cliff. Smooth.")
  else:
    print("Bye-bye. :(")

  