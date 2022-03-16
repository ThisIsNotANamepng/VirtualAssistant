import random
import datetime

name = "Fake"
assistantName = "Melissa"

import chat
#query = input("Query:   ")
def authenticate(passphrase):
  from Cryptodome.Hash import SHA3_512

  h_obj = SHA3_512.new()
  h_obj.update(bytes(passphrase, 'utf-8'))
  passphrase = (h_obj.hexdigest())

#  fff = open("passphrase.txt", "w")
#  fff.write(passphrase)
#  fff.close()




def hello():
  now = datetime.datetime.now()
  h = now.hour
  
  
  if h<12:
    greetings = ["Good Morning", "Good morning "+name]

  if h<14:
    greetings = ["Good Afternoon", "Good afternoon "+name]
  
  if h<24:
    greetings = ["Good Evening", "Good evening "+name]

  print(random.choice(greetings))

def whatTimeIsIt():
  now = datetime.datetime.now()
  h = (now.hour)
  m = (now.minute)

  if h <13:
    
    print("It is ", h, m, "in the morning")
  
  if h >13:
    h = h-12
    print("It is ", h, m, "in the afternoon")

def whatsTheDateToday():
  now = datetime.datetime.now()
  b = (str(now.day))
  bb = b[-1]
  if (bb == "1"):
    attatch = "st"
  if (bb == "2"):
    attatch = "nd"
  if (bb == "3"):
    attatch = "rd"
  else:
    attatch = "th"
  
  if (now.month == 1):
    month = "January"
  if (now.month == 2):
    month = "Febuary"
  if (now.month == 3):
    month = "March"
  if (now.month == 4):
    month = "April"
  if (now.month == 5):
    month = "May"
  if (now.month == 6):
    month = "June"
  if (now.month == 7):
    month = "July"  
  if (now.month == 8):
    month = "August"
  if (now.month == 9):
    month = "September"
  if (now.month == 10):
    month = "October"
  if (now.month == 11):
    month = "November"
  if (now.month == 12):
    month = "December"
  
  year = str(now.year)
  day = str(now.day)

  print("It is the "+day + attatch+ " of "+ month+", "+ year)

def calculate(fnum, operation, snum):
  if operation == "addition":
    answer = fnum+snum
    fnum = str(fnum)
    snum = str(snum)
    answer = str(answer)
    print(fnum+" plus "+snum+" equals "+answer)
  if operation == "multiplication":
    answer = fnum*snum
    fnum = str(fnum)
    snum = str(snum)
    answer = str(answer)
    print(fnum+" times "+snum+" equals "+answer)
  if operation == "subtraction":
    answer = fnum-snum
    fnum = str(fnum)
    snum = str(snum)
    answer = str(answer)
    print(fnum+" minus "+snum+" equals "+answer)
  if operation == "division":
    answer = fnum/snum
    fnum = str(fnum)
    snum = str(snum)
    answer = str(answer)
    print(fnum+" divided by "+snum+" equals "+answer)
    
def open(application):
  print("open app")

def weather(time):
  if time == "today":
    print("right now")
  if time == "tomorrow":
    print("tomorrow")

def isItUp(site):
  from pythonping import ping

  #have it be able to tell a difference from home servers to websites

def makeANote():
  title = input("What do you want the title to be? ")
  content = input("What do you want to write ")

  #f = open("notes/"+title+".txt", "x")
  #f.write(content)
  #f.close()#This will overwrite any other notes with the same title

def iPutThisHere():
  queryl = []
  queryl.append(query)
  queryl = (queryl[0].split())
  print(queryl)


  position = (queryl.index("my"))

  print("You put your "+queryl[position+1]+" "+queryl[position+2]+  " your "+queryl[position+4])

def identify():
  print("I am "+assistantName+", your personal assistant")

#def howToSpell:



if "good morning" in query or "hello" in query or "good afternoon" in query or "good evening" in query:
  hello()
elif "put my" in query or "put the" in query:
  iPutThisHere()
elif "make a note" in query:
  makeANote()
elif "who are you" in query:
  identify()



