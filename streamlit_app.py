import streamlit as st
import datetime
import pandas as pd
import calendar

def highlight_dates(s, selected_date):
    """Highlight the week of the selected date."""
    selected_date = pd.to_datetime(selected_date).date()
    start_of_week = selected_date - datetime.timedelta(days=selected_date.weekday())
    end_of_week = selected_date + datetime.timedelta(days=6 - selected_date.weekday())
    return ['background-color: yellow' if start_of_week <= date.date() <= end_of_week else '' for date in s]

def display_calendar(selected_date):
    """Generate and display a calendar month with the selected week highlighted."""
    # Create date range for the month
    result_month = selected_date.month
    result_year = selected_date.year
    first_day_of_month = datetime.date(result_year, result_month, 1)
    last_day_of_month = datetime.date(result_year, result_month, calendar.monthrange(result_year, result_month)[1])
    date_range = pd.date_range(start=first_day_of_month, end=last_day_of_month, freq='D')
    df = pd.DataFrame(date_range, columns=['Date'])
    df['Day'] = df['Date'].dt.day

    # Prepare a grid-like view for the calendar
    df['Weekday'] = df['Date'].dt.weekday
    month_calendar = pd.pivot_table(df, values='Day', index=df['Date'].dt.week, columns='Weekday', fill_value='')

    # Apply styling to highlight the selected week
    styled_calendar = month_calendar.style.applymap(lambda x: 'background-color: yellow' if x != '' and 
        (first_day_of_month + datetime.timedelta(days=int(x)-1)).date() in pd.date_range(start_of_week, end_of_week) else '')
    return styled_calendar

def main():
    st.title("Weeks Calculator")
    start_date = st.date_input("Select a starting date", datetime.datetime.today())
    num_weeks = st.number_input("Enter number of weeks", min_value=0, step=1, format="%d")

    if st.button("Calculate"):
        result_date = start_date + datetime.timedelta(weeks=num_weeks)
        st.write(f"Date after {num_weeks} weeks: {result_date.strftime('%Y-%m-%d')}")

        # Display the month of the result date with the selected week highlighted
        styled_calendar = display_calendar(result_date)
        st.write(styled_calendar.render(), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
