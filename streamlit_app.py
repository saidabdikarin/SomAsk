import streamlit as st
import datetime
import pandas as pd
import calendar

def highlight_dates(s, selected_date):
    """Highlight the week of the selected date."""
    # Ensure selected_date is a datetime.date object for proper comparison
    selected_date = pd.to_datetime(selected_date).date()
    start_of_week = selected_date - datetime.timedelta(days=selected_date.weekday())
    end_of_week = selected_date + datetime.timedelta(days=6 - selected_date.weekday())
    return ['background-color: yellow' if start_of_week <= date.date() <= end_of_week else '' for date in s]

def main():
    st.title("Weeks Calculator")
    start_date = st.date_input("Select a starting date", datetime.datetime.today())
    num_weeks = st.number_input("Enter number of weeks", min_value=0, step=1, format="%d")

    if st.button("Calculate"):
        result_date = start_date + datetime.timedelta(weeks=num_weeks)
        st.write(f"Date after {num_weeks} weeks: {result_date.strftime('%Y-%m-%d')}")

        # Generate calendar for the month of the result date
        result_month = result_date.month
        result_year = result_date.year
        cal = calendar.monthrange(result_year, result_month)
        first_day_of_month = datetime.date(result_year, result_month, 1)
        last_day_of_month = datetime.date(result_year, result_month, cal[1])
        
        # Create date range for the month
        date_range = pd.date_range(start=first_day_of_month, end=last_day_of_month, freq='D')
        df = pd.DataFrame(date_range, columns=['Date'])

        # Display the month with the week highlighted
        st.write(f"{calendar.month_name[result_month]} {result_year}")
        st.dataframe(df.style.apply(highlight_dates, selected_date=result_date, axis=0))

if __name__ == "__main__":
    main()
