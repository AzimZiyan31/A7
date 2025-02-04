import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore

# Streamlit application layout
st.sidebar.title("Personal Finance Manager")
section = st.sidebar.selectbox("Choose a section", ["Expense Categorization", "Budget Alerts", "Financial Goal Tracking", "Investment Portfolio Management"])

if section == "Expense Categorization":
    st.title("Expense Categorization")

    # Sample data for expenses
    expense_data = {
        'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
        'Amount': np.random.uniform(10, 100, 100),
        'Category': np.random.choice(['Food', 'Entertainment', 'Bills', 'Shopping', 'Miscellaneous'], 100)
    }
    df = pd.DataFrame(expense_data)

    st.write("## Add New Expense")
    with st.form(key='expense_form'):
        date = st.date_input("Date")
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        category = st.selectbox("Category", ['Food', 'Entertainment', 'Bills', 'Shopping', 'Miscellaneous'])
        submit_button = st.form_submit_button(label='Add Expense')

        if submit_button:
            new_expense = {'Date': date, 'Amount': amount, 'Category': category}
            df = df.append(new_expense, ignore_index=True)
            st.success("Expense added successfully!")

    st.write("## Expense Data")
    st.dataframe(df)

    st.write("## Expense by Category")
    expense_by_category = df.groupby('Category')['Amount'].sum().reset_index()
    fig, ax = plt.subplots()
    ax.bar(expense_by_category['Category'], expense_by_category['Amount'])
    st.pyplot(fig)

if section == "Budget Alerts":
    st.title("Budget Alerts")

    st.write("## Set Budget Limits")
    with st.form(key='budget_form'):
        category = st.selectbox("Category", ['Food', 'Entertainment', 'Bills', 'Shopping', 'Miscellaneous'])
        budget_limit = st.number_input("Budget Limit", min_value=0.0, format="%.2f")
        submit_button = st.form_submit_button(label='Set Budget')

        if submit_button:
            st.success(f"Budget for {category} set to {budget_limit}")

    st.write("## Current Budget Status")
    budget_data = {
        'Category': ['Food', 'Entertainment', 'Bills', 'Shopping', 'Miscellaneous'],
        'Budget': [200, 150, 300, 250, 100],
        'Spent': [180, 160, 290, 240, 90]
    }
    budget_df = pd.DataFrame(budget_data)
    st.dataframe(budget_df)

    st.write("## Budget Alerts")
    alerts = budget_df[budget_df['Spent'] > budget_df['Budget']]
    if not alerts.empty:
        st.error(f"Budget exceeded for: {', '.join(alerts['Category'].tolist())}")
    else:
        st.success("No budget limits exceeded")

if section == "Financial Goal Tracking":
    st.title("Financial Goal Tracking")

    st.write("## Set Financial Goals")
    with st.form(key='goal_form'):
        goal_name = st.text_input("Goal Name")
        goal_amount = st.number_input("Goal Amount", min_value=0.0, format="%.2f")
        target_date = st.date_input("Target Date")
        submit_button = st.form_submit_button(label='Set Goal')

        if submit_button:
            st.success(f"Goal '{goal_name}' set for {goal_amount} by {target_date}")

    st.write("## Current Goals")
    goals_data = {
        'Goal Name': ['Vacation', 'Emergency Fund', 'New Laptop'],
        'Amount': [2000, 5000, 1000],
        'Target Date': [pd.to_datetime('2024-12-31'), pd.to_datetime('2024-06-30'), pd.to_datetime('2024-09-30')],
        'Saved': [500, 2000, 300]
    }
    goals_df = pd.DataFrame(goals_data)
    st.dataframe(goals_df)

    st.write("## Goal Progress")
    goals_df['Progress'] = goals_df['Saved'] / goals_df['Amount'] * 100
    st.bar_chart(goals_df.set_index('Goal Name')['Progress'])

if section == "Investment Portfolio Management":
    st.title("Investment Portfolio Management")

    st.write("## Add New Investment")
    with st.form(key='investment_form'):
        investment_name = st.text_input("Investment Name")
        investment_amount = st.number_input("Investment Amount", min_value=0.0, format="%.2f")
        investment_date = st.date_input("Investment Date")
        submit_button = st.form_submit_button(label='Add Investment')

        if submit_button:
            st.success(f"Investment '{investment_name}' of {investment_amount} added on {investment_date}")

    st.write("## Current Investments")
    investment_data = {
        'Investment Name': ['Stocks', 'Bonds', 'Real Estate'],
        'Amount': [10000, 5000, 20000],
        'Date': [pd.to_datetime('2024-01-01'), pd.to_datetime('2023-06-01'), pd.to_datetime('2023-09-01')],
        'Current Value': [15000, 5500, 21000]
    }
    investment_df = pd.DataFrame(investment_data)
    st.dataframe(investment_df)

    st.write("## Investment Portfolio Value")
    portfolio_value = investment_df['Current Value'].sum()
    st.metric(label="Total Portfolio Value", value=f"${portfolio_value}")

    st.write("## Investment Distribution")
    fig, ax = plt.subplots()
    ax.pie(investment_df['Current Value'], labels=investment_df['Investment Name'], autopct='%1.1f%%')
    st.pyplot(fig)