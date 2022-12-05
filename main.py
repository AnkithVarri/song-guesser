import random
import time
import pwinput


def nest_list(list1, rows, columns):
  result = []
  start = 0
  end = columns
  for i in range(rows):
    result.append(list1[start:end])
    start += columns
    end += columns
  return result


def register():
  t = True
  hr = input("Do you want to register! y or n: ")
  if hr == "y":
    l = open("login", "a+")
    global user1
    global pass1
    user = input("Enter a Username you want: ")
    password = pwinput.pwinput(prompt="Enter a Password you want: ")
    while t == True:
      if len(password) == 0 and len(user) == 0:
        print("Both fields are blank, enter again: ")
        user = input("Enter a Username you want: ")
        password = input("Enter a password you want: ")
        t = True
      elif len(user) == 0:
        print("Enter username, field is blank!")
        user = input("Enter a Username you want: ")
      elif len(password) == 0:
        print("Enter password, field is blank!")
        password = pwinput.pwinput(prompt="Enter a Password you want: ")
      elif len(user) != 0 and len(password) != 0:
        u = True
        while u == True:
          pc = pwinput.pwinput(prompt="Confirm your password: ")
          if pc == password:
            u2 = user + "\n"
            p2 = password + "\n"
            l.write(u2)
            l.write(p2)
            user1 = user
            pass1 = password
            print("You have successfully registered !")
            u = False
            l.close()
            t = False
          else:
            print("Passwords don't match! Enter password again ")
  l = open("login", "r")
  g = l.read()
  f = g.split()
  y = len(f)
  z = y // 2
  global final
  final = nest_list(f, z, 2)
  final = final
  return final
  l.close()


def login():
  global user1
  global pass1
  found = False
  valid = False
  print("\n")
  while found == False:
    def check():
      while len(final) == 0:
        print("No account was created, please create an account! ")
        print("\n")
        register()
        check()
        break
    check()
    username = input("Enter username: ")
    for i in final:
      for j in range(1):
        if i[0] == username:
          found = True
          v = final.index(i)
          user1 = username
    if found == True:
      y = True
      while y == True:
        pas = pwinput.pwinput(prompt = "Enter password: ")
        if pas == final[v][1]:
          valid = True
          print("\n")
          print(f"You are now logged in {user1}")
          print("------------------------------------------------------------------------")
          y = False
          found = True
          pass1 = pas
          break
        elif pas != final[v][1]:
          print("incorrect password")
    else:
      print("incorrect username")
  if valid == True:
    return 1
  else:
    return 0


def questions():
  score = 0
  f = open("score", "a+")
  tries = 1
  while tries < 2:
    random_lines = random.choice(open("song_names.txt").readlines())
    data = random_lines.split("by")
    #print(data)
    band = data[1]
    band = band.replace("\n", "")
    song = str(data[0])
    song = song.rstrip()
    song_list = list(song)
    song_letter = song_list[0]
  
    print("\n")
    global anse
    anse = str(input(f"What song that starts with {song_letter} does {band} sing? "))
    anse = anse.title()
    if anse == song:
      score = score + 3
      print(f"Correct! You have scored 3 points. You are on {score} points")
    elif anse != song:
      again = input(("That was wrong... try again: "))
      again = again.title()
      if again == song:
        score = score + 1
        tries = 1
        print(f"Correct! You have scored 1 point! You are on {score} points")
      else:
        tries = tries + 1
        print("\n")
        print("Unlucky! ")
        print(f"You scored {score} points")
        print("\n")
        jac = user1 + " " + str(score)
        jac = jac + "\n"
        f.write(jac)
        f.close()
        f = open("score", "r")
        j = f.read()
        z = j.split()
        ye = len(z)
        ze = ye // 2
        global k
        k = nest_list(z,ze,2)
        N = 5
        global res
        res = sorted(k, key=lambda x: x[1], reverse=True)[:N]
        break


def main():
  car = True
  while car == True:
    print("Hello everyone")
    time.sleep(1)
    print("Welcome to the Song Guesser")
    time.sleep(1)
    register()
    logon = login()
    run = True
    while run:
      if logon == 1:
        questions()
        print("Thank you for playing")
        again = input("Do you want to play again? y or n: ")
        if again == "y":
          run = True
          print("----------------------------------------------------------")
        elif again == "n":
          run = False
          car = False
          print("Ok, Bye")
          break
        elif again == "c":
          run = False
          car = False
          j = 0
          print("\n")
          print("The top 5 highest scores are:")
          for sublist in res:
            j = j+1
            for item in sublist:
              a = sublist[0]
              b = sublist[1]
            print(f"{j}.. {a} with {b} points")
          break
      elif logon == 0:
        print("Sorry, You might not have an account or you have entered the wrong password, do you want to try again? ")
        time.sleep(1)
        r = input("Do you want to register or login? r for register or l for login or no for quit")
        if r == "r":
          register()
          login()
          run = True
          logon = 1
        elif r == "l":
          login()
          run = True
          logon = 1
        elif r == "no":
          run = False
          logon = 0
          break


if __name__ == "__main__":
  main()
