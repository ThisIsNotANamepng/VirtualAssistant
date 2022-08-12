import random
import datetime
from Cryptodome.Hash import SHA3_512
from os.path import exists


name = "Fake"
assistantName = "Melissa"
query = "what time is it"
query = query.lower()


access = False
#import chat
#query = input("Query:   ")

def speak(response):
  print(response)

def ask(question):
  #Say something and then listen for a response
  speak(question)
  answer = "Listen for a repsone"
  return answer
  
def authenticate():
  #passphrase = input("What's the passphrase?")
  test_passphrase = "elephants are lovely"
  
  test_passphrase = test_passphrase.lower()

  h_obj = SHA3_512.new()
  h_obj.update(bytes(test_passphrase, 'utf-8'))
  test_passphrase = (h_obj.hexdigest())
  
  abcdfff = open("passphrase.txt", "r")
  passphrase = abcdfff.read()
  abcdfff.close()

  if test_passphrase == passphrase:
    speak("Access granted  ")
    access = True
  else:
    speak("Access denied")
    access = False


def hello():
  now = datetime.datetime.now()
  h = now.hour
  
  if h<12:
    greetings = ["Good Morning", "Good morning "]

  if h<14:
    greetings = ["Good Afternoon", "Good afternoon "]
  
  if h<24:
    greetings = ["Good Evening", "Good evening "]

  speak(random.choice(greetings))

def whatTimeIsIt():
  now = datetime.datetime.now()
  h = (now.hour)
  m = (now.minute)


  if h < 13:
    sh=str(h)
    sm=str(m)
    text = "It is "+ sh + " " + sm+ " in the morning"
    
    speak(text)
  
  if h > 13:
    sh=str(h)
    sm=str(m)
    h = h-12
    text = "It is "+ sh + " " + sm + " in the afternoon"
    
    speak(text)

def turnOnTheLights():
  #Turn in the secret stuff
  speak("what?")


  
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

  speak("It is the "+day + attatch+ " of "+ month+", "+ year)

def calculate(fnum, operation, snum):
  if operation == "addition":
    answer = fnum+snum
    fnum = str(fnum)
    snum = str(snum)
    answer = str(answer)
    speak(fnum+" plus "+snum+" equals "+answer)
  if operation == "multiplication":
    answer = fnum*snum
    fnum = str(fnum)
    snum = str(snum)
    answer = str(answer)
    speak(fnum+" times "+snum+" equals "+answer)
  if operation == "subtraction":
    answer = fnum-snum
    fnum = str(fnum)
    snum = str(snum)
    answer = str(answer)
    speak(fnum+" minus "+snum+" equals "+answer)
  if operation == "division":
    answer = fnum/snum
    fnum = str(fnum)
    snum = str(snum)
    answer = str(answer)
    speak(fnum+" divided by "+snum+" equals "+answer)
    


def weather(time):
  if time == "today":
    speak("right now")
  if time == "tomorrow":
    speak("tomorrow")



def makeANote():
  title = ask("What do you want the title to be? ")
  content = ask("What do you want to write? ")

  path = "notes/"+title+".txt"
  f = open(path, "w")
  f.write(content)
  f.close()
  file_exists = exists(path)

  if file_exists == True:
    speak("Note taken succesfully")
  else:
    speak("Something went wrong, note not saved")

def iPutThisHere():
  thing = ask("What are you leaving?")
  place = ask("Where are you leaving it?")
  speak("You put your " + thing + " in " + place)
  #Need to make this enter into a database

def identify():
  speak("I am "+assistantName+", your personal assistant")

#def howToSpell:

def dayOfTheWeek():
  dn = datetime.datetime.today().weekday()
  if dn == 0:
    day = "Monday"
  if dn == 1:
    day = "Tuesday"
  if dn == 2:
    day = "Wednesday"
  if dn == 3:
    day = "Thursday"
  if dn == 4:
    day = "Friday"
  if dn == 5:
    day = "Saturday"
  if dn == 6:
    day = "Sunday"


  speak("Today is "+day)


if "good morning" in query or "hello" in query or "good afternoon" in query or "good evening" in query:
  hello()
elif "put my" in query or "put the" in query:
  iPutThisHere()
elif "make a note" in query or "take a note" in query:
  makeANote()
elif "who are you" in query:
  identify()
elif "authenticate" in query:
  authenticate()
elif "what time is it" in query or query == "time":
  whatTimeIsIt()
elif "turn on the lights" in query:
  turnOnTheLights()
elif "what day is it" in query or "what's the date" in query:
  whatsTheDateToday()
elif "day of the week" in query:
  dayOfTheWeek()


