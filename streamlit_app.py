import streamlit as st
import datetime
import pandas as pd
import numpy as np
import calendar

def highlight_dates(s, selected_date):
    """Highlight the week of the selected date."""
    is_selected_week = (s >= selected_date - datetime.timedelta(days=selected_date.weekday())) & \
                       (s <= selected_date + datetime.timedelta(days=6 - selected_date.weekday()))
    return ['background-color: yellow' if v else '' for v in is_selected_week]

def main():
    st.title("Weeks Calculator")
    # User input for starting date and number of weeks
    start_date = st.date_input("Select a starting date", datetime.datetime.today())
    num_weeks = st.number_input("Enter number of weeks", min_value=0, step=1, format="%d")
    
    if st.button("Calculate"):
        # Calculate the result date
        result_date = start_date + datetime.timedelta(weeks=num_weeks)
        st.write(f"Date after {num_weeks} weeks: {result_date.strftime('%Y-%m-%d')}")
        
        # Generate the calendar for the month of the result date
        result_month = result_date.month
        result_year = result_date.year
        cal = calendar.monthrange(result_year, result_month)
        first_day_of_month = datetime.date(result_year, result_month, 1)
        last_day_of_month = datetime.date(result_year, result_month, cal[1])

        # Create date range for the month
        date_range = pd.date_range(first_day_of_month, last_day_of_month, freq='D')
        df = pd.DataFrame(date_range, columns=['Date'])
        
        # Display the month with the week highlighted
        st.dataframe(df.style.apply(highlight_dates, selected_date=result_date, axis=0))

if __name__ == "__main__":
    main()
