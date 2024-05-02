import streamlit as st
import datetime
import pandas as pd
import calendar

def display_calendar(selected_date):
    """Generate and display a calendar month containing the selected week."""
    result_month = selected_date.month
    result_year = selected_date.year
    first_day_of_month = datetime.date(result_year, result_month, 1)
    last_day_of_month = datetime.date(result_year, result_month, calendar.monthrange(result_year, result_month)[1])
    date_range = pd.date_range(start=first_day_of_month, end=last_day_of_month, freq='D')
    df = pd.DataFrame(date_range, columns=['Date'])
    df['Day'] = df['Date'].dt.day
    df['Weekday'] = df['Date'].dt.weekday
    df['Week'] = df['Date'].dt.isocalendar().week

    # Filter the DataFrame to include only rows corresponding to the selected week
    start_of_week = selected_date - datetime.timedelta(days=selected_date.weekday())
    end_of_week = selected_date + datetime.timedelta(days=6 - selected_date.weekday())
    filtered_df = df[(df['Date'] >= start_of_week) & (df['Date'] <= end_of_week)]

    # Prepare a grid-like view for the calendar
    month_calendar = pd.pivot_table(filtered_df, values='Day', index='Week', columns='Weekday', fill_value='')

    return month_calendar

def main():
    st.title("Weeks Calculator")
    start_date = st.date_input("Select a starting date", datetime.datetime.today())
    num_weeks = st.number_input("Enter number of weeks", min_value=0, step=1, format="%d")

    if st.button("Calculate"):
        result_date = start_date + datetime.timedelta(weeks=num_weeks)
        st.write(f"Date after {num_weeks} weeks: {result_date.strftime('%Y-%m-%d')}")

        # Display the entire month containing the selected week
        month_calendar = display_calendar(result_date)
        st.dataframe(month_calendar)

if __name__ == "__main__":
    main()
