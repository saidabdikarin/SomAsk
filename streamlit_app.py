import streamlit as st
import datetime
import pandas as pd
import calendar

def highlight_dates(s, selected_week):
    """Highlight the week of the selected date."""
    # Ensure selected_date is a datetime.date object for proper comparison
    selected_week = pd.to_datetime(selected_week).date()
    start_of_week = selected_week - datetime.timedelta(days=selected_week.weekday())
    end_of_week = start_of_week + datetime.timedelta(days=6)
    return ['background-color: yellow' if start_of_week <= date.date() <= end_of_week else '' for date in s]

def main():
    st.title("Weeks Calculator")
    start_date = st.date_input("Select a starting date", datetime.datetime.today())
    num_weeks = st.number_input("Enter number of weeks", min_value=0, step=1, format="%d")

    if st.button("Calculate"):
        result_date = start_date + datetime.timedelta(weeks=num_weeks)
        st.write(f"Date after {num_weeks} weeks: {result_date.strftime('%Y-%m-%d')}")

        # Generate calendar for the month containing the result date's week
        result_week = result_date - datetime.timedelta(days=result_date.weekday())
        result_month = result_week.month
        result_year = result_week.year
        cal = calendar.monthrange(result_year, result_month)
        first_day_of_month = datetime.date(result_year, result_month, 1)
        last_day_of_month = datetime.date(result_year, result_month, cal[1])

        # Create date range for the month
        date_range = pd.date_range(start=first_day_of_month, end=last_day_of_month, freq='D')
        df = pd.DataFrame(date_range, columns=['Date'])

        # Create a calendar matrix
        calendar_matrix = df['Date'].apply(lambda x: (x.day, x.strftime('%A'))).values.reshape(-1, 7)

        # Display the month with the selected week highlighted and day names at the top
        st.write(f"Month containing the selected week: {result_date.strftime('%B')} {result_year}")
        st.write("Mon\tTue\tWed\tThu\tFri\tSat\tSun")
        for week in calendar_matrix:
            st.write('\t'.join([str(day[0]) for day in week]))

if __name__ == "__main__":
    main()
