# 💰 Investment Recommendation System

A **Python-based Investment Recommendation System** that analyzes a user's income, expenses, savings, investment amount, risk-taking ability, and investment duration to generate a personalized financial report.

The project calculates a **Financial Health Score**, suggests suitable investment options based on risk and duration, and estimates the future value of regular monthly investments.

---

## 📌 Features

* 👤 Takes basic user financial information
* 💵 Calculates monthly financial surplus
* 📊 Calculates savings rate
* 🏦 Calculates how many months current savings can cover expenses
* 📈 Calculates monthly investment rate
* ⭐ Generates a **Financial Health Score out of 100**
* 📝 Classifies financial health as:

  * Excellent
  * Good
  * Moderate
  * Needs more improvement
* ⚖️ Considers three levels of risk:

  * Low
  * Medium
  * High
* ⏳ Considers three investment durations:

  * Short – 2 years
  * Medium – 5 years
  * Long – 10 years
* 💡 Provides investment recommendations
* 📋 Provides suggested investment allocation
* 🔮 Calculates projected future value
* 💹 Calculates estimated investment gain
* 📄 Generates a complete financial report in the terminal

---

## 🛠️ Technologies Used

* **Python 3**
* Python Conditional Statements
* User Input
* Arithmetic Operations
* Variables
* `if-elif-else`
* Mathematical calculations
* Formatted output

No external Python libraries are required.

---

## ⚙️ How It Works

The system follows this basic workflow:

```text
User Input
    ↓
Financial Calculations
    ↓
Financial Health Score
    ↓
Risk & Duration Analysis
    ↓
Investment Recommendation
    ↓
Future Value Calculation
    ↓
Financial Report
```

---

## 📊 Financial Calculations

### 1. Monthly Surplus

The monthly surplus is calculated as:

```text
Monthly Surplus = Monthly Income - Monthly Expenditure
```

### 2. Savings Rate

```text
Savings Rate = (Monthly Surplus / Monthly Income) × 100
```

### 3. Months of Savings

This estimates how many months the current savings can cover the user's expenditure.

```text
Months of Savings = Current Savings / Monthly Expenditure
```

### 4. Investment Rate

```text
Investment Rate = (Monthly Investment / Monthly Income) × 100
```

---

## ⭐ Financial Health Score

The system assigns points based on three financial factors.

| Factor            | Maximum Score |
| ----------------- | ------------: |
| Savings Rate      |            40 |
| Months of Savings |            30 |
| Investment Rate   |            30 |
| **Total**         |       **100** |

The final score is classified as:

|    Score | Financial Profile      |
| -------: | ---------------------- |
|   80–100 | Excellent              |
|    60–79 | Good                   |
|    40–59 | Moderate               |
| Below 40 | Needs more improvement |

---

## ⚖️ Risk-Based Recommendation

The system considers three risk levels:

### Low Risk

Recommendations may include:

* Savings Account
* Fixed Deposit
* Government Securities
* Debt Instruments

### Medium Risk

Recommendations may include:

* Large-Cap Oriented Investments
* Hybrid Funds
* Diversified Equity
* Fixed Income

### High Risk

Depending on the investment duration, recommendations may include exposure to:

* Large-Cap
* Mid-Cap
* Small-Cap investments

The recommendations are generated using the combination of **risk-taking ability and investment duration** entered by the user.

---

## ⏳ Investment Duration

The program provides three investment periods:

```text
Short  → 2 years
Medium → 5 years
Long   → 10 years
```

The duration affects both the investment recommendation and the future-value calculation.

---

## 🔮 Future Value Calculation

The program estimates the future value of monthly investments using the expected annual return.

The annual return is converted into a monthly rate:

```text
Monthly Rate = Annual Return / 100 / 12
```

For a non-zero monthly return, the future value is calculated using:

```text
FV = P × ((1 + r)^n - 1) / r
```

Where:

* `P` = Monthly Investment
* `r` = Monthly Rate of Return
* `n` = Total Number of Months
* `FV` = Projected Future Value

The program also calculates:

```text
Total Investment = Monthly Investment × Number of Months
```

and:

```text
Estimated Gain = Future Value - Total Investment
```

---

## 🖥️ Sample Input

```text
INVESTMENT RECOMMENDATION SYSTEM

Enter your name: Aadi
Enter your monthly earning (₹): 20000
Enter your monthly expenditure (₹): 15000
Enter your currently savings (₹): 14000
Enter your monthly savings (₹): 5000
Enter your expected annually return (%): 20

Risk-Taking Ability
1. Low
2. Medium
3. High
Enter your choice(1/2/3): 3

Investment Duration
1. Short(2 years)
2. Medium(5 years)
3. Long(10 years)
Enter your choice(1/2/3): 3
```

---

## 📄 Sample Output

```text
FINANCIAL REPORT

USER DETAILS
Name                     : Aadi
Monthly Earnings         : ₹ 20000.00
Monthly Expenditure      : ₹ 15000.00
Current Savings          : ₹ 14000.00
Monthly Investment       : ₹ 5000.00

FINANCIAL ANALYSIS
Monthly Surplus          : ₹ 5000.00
Savings Rate             : 25.00 %
Savings Available For    : 0.93 months
Financial Health Score   : 40 out of 100
Financial Profile        : Moderate

INVESTMENT PROFILE
Risk Taking Ability      : High
Investment Duration      : Long
Expected Annual Return   : 20.0 %

RECOMMENDATION
Suggested Investments    : Large-Cap + Mid Cap + Small Cap Equity Exposure
Suggested Allocation     : Large-Cap + Mid-Cap + Small-Cap

INVESTMENT PROJECTION
Investment Period        : 10 years
Total Investment Amount  : ₹ 600000.00
Projected Future Value   : ...
Estimated Gain           : ...

END OF FINANCIAL REPORT
```

*The exact projected value depends on the expected annual return and monthly investment entered by the user.*

---

## 📁 Project Structure

```text
Investment-Recommendation-System/
│
├── investment_recommendation.py
└── README.md
```

---

## ▶️ How to Run

### 1. Install Python

Make sure **Python 3** is installed on your computer.

### 2. Clone the Repository

```bash
git clone <your-repository-url>
```

### 3. Open the Project Folder

```bash
cd Investment-Recommendation-System
```

### 4. Run the Program

```bash
python investment_recommendation.py
```

### 5. Enter Your Details

Follow the instructions displayed in the terminal.

---

## 🎯 Project Objective

The main objective of this project is to demonstrate how **Python programming and basic financial calculations** can be combined to create a simple investment recommendation system.

It helps users understand their:

* Income
* Expenses
* Savings
* Investment capacity
* Financial health
* Investment duration
* Risk preference
* Potential future investment value

---

## 🚀 Future Improvements

Possible improvements include:

* [ ] Add a graphical user interface using Tkinter
* [ ] Add multiple investment categories
* [ ] Add inflation adjustment
* [ ] Add tax calculations
* [ ] Add graphical charts
* [ ] Save financial reports to a file
* [ ] Add input validation
* [ ] Add an emergency-fund recommendation
* [ ] Allow users to compare different investment scenarios
* [ ] Add a database to store previous reports


the repository a star!
