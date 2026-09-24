# Investment Recommendation System

## Overview

The **Investment Recommendation System** is a Python-based project designed to analyze a user's financial situation and provide a basic investment recommendation. It considers factors such as **income, expenditure, savings, monthly investment, risk-taking ability, and investment duration**.

The system generates a **Financial Health Score**, suggests suitable investment options, and calculates the projected future value and estimated gain from regular investments.

## Features

* Accepts user financial information
* Calculates monthly surplus and savings rate
* Calculates savings available in months
* Calculates investment rate
* Generates a **Financial Health Score out of 100**
* Classifies the user's financial profile
* Provides recommendations based on risk and investment duration
* Suggests a basic investment allocation
* Calculates projected future value
* Calculates estimated investment gain
* Generates a complete financial report

## Technologies / Tools Used

* **Python 3**
* Variables and User Input
* Conditional Statements
* Arithmetic Operations
* Mathematical Calculations
* Formatted Output
* Python IDE / Terminal

**No external libraries are required.**

## Steps to Install & Run

### 1. Install Python

Make sure **Python 3** is installed on your system.

### 2. Clone the Repository

```bash
git clone <repository-url>
cd Investment-Recommendation-System
```

### 3. Run the Program

```bash
python investment_recommendation.py
```

### 4. Enter the Required Information

The program will ask for:

* Name
* Monthly income
* Monthly expenditure
* Current savings
* Monthly investment
* Expected annual return
* Risk-taking ability
* Investment duration

The final financial report will then be displayed in the terminal.

## Instructions for Testing

The program can be tested by entering different financial values and selecting different risk levels and investment durations.

### Test Case 1 — Medium Risk

```text
Income: ₹20,000
Expenditure: ₹15,000
Current Savings: ₹14,000
Monthly Investment: ₹5,000
Expected Return: 10%
Risk: Medium
Duration: 5 years
```

**Expected:** The program should calculate the financial health score and display a medium-risk investment recommendation with the projected future value.

### Test Case 2 — Low Risk

Select **Low Risk** with a short or medium duration.

**Expected:** The program should display lower-risk investment options such as fixed-income or government securities.

### Test Case 3 — High Risk

Select **High Risk** with a long-term duration.

**Expected:** The program should display an equity-oriented recommendation and the corresponding allocation.

### Test Case 4 — Zero Return

Enter `0%` as the expected annual return.

**Expected:** The projected future value should equal the total amount invested because no return is applied.

## Financial Health Score

The system calculates the score using three financial factors:

| Factor            | Maximum Score |
| ----------------- | ------------: |
| Savings Rate      |            40 |
| Savings Available |            30 |
| Investment Rate   |            30 |
| **Total**         |       **100** |

## Investment Duration

The system supports three investment periods:

* **Short Term** → 2 years
* **Medium Term** → 5 years
* **Long Term** → 10 years

The recommendation is determined by combining the user's **risk-taking ability and investment duration**.

