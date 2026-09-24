print("             INVESTMENT RECOMMENDATION SYSTEM")

#INPUTS
name=input("Enter your name:")
income=float(input("Enter your monthly earning (₹):"))
expenditure=float(input("Enter your monthly expenditure (₹):"))
savings=float(input("Enter your currently savings (₹):"))
investment=float(input("Enter your monthly savings (₹):"))
expected_return=float(input("Enter your expected annually return (%):"))
print("\nRisk-Taking Ability")
print("1. Low")
print("2. Medium")
print("3. High")
risk_choice=int(input("Enter your choice(1/2/3)"))

if risk_choice==1:
    risk="Low"
elif risk_choice==2:
    risk="Medium"
elif risk_choice==3:
    risk="High"

print("\nInvestment Duration")
print("1. Short(2 years)")
print("2. Medium(5 years)")
print("3. Long(10 years)")
duration_choice=int(input("Enter your choice(1/2/3)"))

if duration_choice==1:
    duration="Short"
    years=2
elif duration_choice==2:
    duration="Medium"
    years=5
elif duration_choice==3:
    duration="Long"
    years=10
else:
    print("Invalid Choice")
    duration="medium"
    years=5
#CALCULATION
surplus=income-expenditure
savings_rate=(surplus/income)*100

if expenditure>0:
    months_of_savings=savings/expenditure
else:
    months_of_savings=0

investment_rate=(investment/income)*100

#FINANCIAL HEALTH SCORE
score=0
if savings_rate>=40:
    score+=40
elif savings_rate>=25:
    score+=30
elif savings_rate>=15:
    score+=20
elif savings_rate>=5:
    score+=10

if months_of_savings>=6:
    score+=30
elif months_of_savings>=3:
    score+=20
elif months_of_savings>=1:
    score+=10

if investment_rate>=20:
    score+=30
elif investment_rate>=10:
    score+=20
elif investment_rate>=5:
    score+=10

if score>=80:
    profile="Excellent"
elif score>=60:
    profile="Good"
elif score>=40:
    profile="Moderate"
else:
    profile = "Needs more improvement"

#INVESTMENT RECOMMENDATION LOGIC
if risk=="Low":
    if duration=="Short":
        recommendation="Savings Account/Fixed Deposit/Government Securities"
    elif duration=="Medium":
        recommendation = "Debt Instruments/Fixed Deposit/Government Securities"
    else:
        recommendation = "Fixed Deposit/Government Securities"

elif risk == "Medium":
    if duration == "Short":
        recommendation = "Fixed Deposit/Short Term Government Securities"
    elif duration == "Medium":
        recommendation = "Large-Cap Oriented Investments/Hybrid Funds"
    else:
        recommendation = "Large-Cap Oriented Investments/Diversified Equity"

else:
    if duration == "Short":
        recommendation = "Lower-Risk Investments are more suitable for shorter duration"
    elif duration == "Medium":
        recommendation = "Large-Cap + Mid Cap Equity Exposure"
    else:
        recommendation = "Large-Cap + Mid Cap + Small Cap Equity Exposure"

#SUGGESTED ALLOCATION
if risk=="Low":
    allocation="Mostly Fixed Income with Limited Equity Exposure"

elif risk=="Medium":
    if duration=="Short":
        allocation="Mostly Fixed Income"
    elif duration=="Medium":
        allocation="Large-Cap + Hybrid + Fixed Income"
    else:
        allocation="Large-Cap + Mid Cap + Hybrid"

else:
    if duration=="Short":
        allocation="Mostly Lower-Risk Investments"
    elif duration=="Medium":
        allocation="Large-Cap + Mid-Cap + Limited Small-Cap"
    else:
        allocation="Large-Cap + Mid-Cap + Small-Cap"

#FUTURE VALUE CALCULATION
months=years*12
monthly_rate=expected_return/100/12

if monthly_rate==0:
    future_value=investment*months
else:
    future_value=investment*(((1+monthly_rate)**months-1)/monthly_rate)

total_invested=investment*months
estimated_return=future_value-total_invested

#FINAL FINANCIAL REPORT
print("\n")
print("                 FINANCIAL REPORT")

print("\nUSER DETAILS")
print("Name                     :", name)
print("Monthly Earnings         :₹", format(income, ".2f"))
print("Monthly Expenditure      :₹", format(expenditure, ".2f"))
print("Current Savings          :₹", format(savings, ".2f"))
print("Monthly Investment       :₹", format(investment, ".2f"))

print("\nFINANCIAL ANALYSIS")
print("Monthly Surplus          :₹", format(surplus, ".2f"))
print("Savings Rate             :", format(savings_rate, ".2f"), "%")
print("Savings Available For    :", format(months_of_savings, ".2f"), "months")
print("Financial Health Score   :", score, "out of 100")
print("Financial Profile        :", profile)

print("\nINVESTMENT PROFILE")
print("Risk Taking Ability      :", risk)
print("Investment Duration      :", duration)
print("Expected Annual Return   :", expected_return, "%")

print("\nRECOMMENDATION")
print("Suggested Investments    :", recommendation)
print("Suggested Allocation     :", allocation)

print("\nINVESTMENT PROJECTION")
print("Investment Period        :", years, "years")
print("Total Investment Amount  :₹", format(total_invested, ".2f"))
print("Projected Future Value   :₹", format(future_value, ".2f"))
print("Estimated Gain           :₹", format(estimated_return, ".2f"))

print("\n             END OF FINANCIAL REPORT")














