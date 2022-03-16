print("Now we can talk")
topic = []
query ="I can't decide between "
#if wait before speaking is greater than 3 seconds, ask "are you ok?" or "is there anything you need"?
# tone and voice inflection is going to be a big part of this I think

if "today" in query: #and hour<12
  topic.append("aboutDay")
#elif "today" in query: #and hour>12
#  topic.append("planDay")
elif "I can't decide" in query: #or "I might" or ""
  topic.append("decision")
elif "I need to vent" in query:
  topic.append("vent")
elif "how are you" in query:
  topic.append("assistantHealth")




  












print(topic)
input("")