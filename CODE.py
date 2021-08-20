cm=0.01
foot=0.3048
inch=0.0254
print("If you choose foot as a metric then in the first option type the feet side of your height (eg. 5 in 5'7),and then in the second option type the inch side (eg.7 in 5'7)")
metric=input("Please type any one of the metrics given, as it is, i.e(cm,foot,inch,m,inches)\n")
height=input("What is your height in the metric you chose above?\n")
if metric=="foot":
  inches=input("please write inches as well.\n")
  height=int(height)*foot + float(inches)*inch
elif metric=="cm":
  height=float(height)*cm
elif metric=="inches":
  height=float(height)*inch
weight=float(input("What is your weight in Kgs?\n"))
# bmi=float("%.2f" % (float(weight)/(height**2)))
bmi=round(weight/height**2)
if bmi<18.5:
  print("according to your bmi which is {}".format(bmi)+" "+ "you are Underweight")
  print("you have to gain  {}".format(19-bmi)+" "+ "points to be considered Normal weight")
elif bmi<=25:
  print("according to your bmi which is {}".format(bmi)+ " " + "you are Normalweight")
elif bmi<=30:
  print("according to your bmi which is {}".format(bmi)+ " " + "you are Overweight")
  print("you have to lose {}".format(bmi-25)+" "+ "points to be considered Normal weight")
elif bmi<=35:
  print("according to your bmi which is {}".format(bmi)+ " " + "you are Obese")
  print("you have to lose {}".format(bmi-25)+" "+ "points to be considered Normal weight")
else:
  print("according to your bmi which is {}".format(bmi)+ " " + "you are clinically Obese")
  print("you have to lose {}".format(bmi-25)+" "+ "points to be considered Normal weight")
