from django.shortcuts import render
import random

# Create your views here.

fortuneList = ["All will go well with your new project.",
   "If you continually give, you will continually have.",
   "Self-knowledge is a life long process.",
   "You are busy, but you are happy.",
   "Your abilities are unparalleled.",
   "Those who care will make the effort.",
   "Now is the time to try something new.",
   "Miles are covered one step at a time.",
   "Don’t just think, act!",
   "The Best Way To Get Started Is To Quit Talking And Begin Doing.",
   "The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.",
   "Don’t Let Yesterday Take Up Too Much Of Today.",
   "You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.",
   "It’s Not Whether You Get Knocked Down, It’s Whether You Get Up.",
   "If You Are Working On Something That You Really Care About, You Don’t Have To Be Pushed. The Vision Pulls You.",
   "Failure Will Never Overtake You If Your Determination To Succeed Is Strong Enough."]

def fortune(request):
  fortune = random.choice(fortuneList)
  context = {
    "fortune": fortune
  }
  return render(request, "randomfortune/fortune.html", context)



