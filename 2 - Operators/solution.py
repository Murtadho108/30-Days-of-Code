mealCost = float(input())
tip = int(input())
tax = int(input())
tip=tip*mealCost/100;
tax=tax*mealCost/100;
totalcost=mealCost+tip+tax;

print (round(totalcost))
