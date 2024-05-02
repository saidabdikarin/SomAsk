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

def create_monthly_table(year, month):
    """Create a pandas DataFrame representing a monthly calendar table."""
    # Get the number of days in the month
    _, num_days = calendar.monthrange(year, month)

    # Create a list of dates for the month
    dates = pd.date_range(start=datetime.date(year, month, 1), end=datetime.date(year, month, num_days), freq='D')

    # Create a DataFrame with the dates
    df = pd.DataFrame(dates, columns=['Date'])

    # Add weekday names as column headers
    df['Weekday'] = df['Date'].dt.day_name().str[:3]

    # Rearrange the columns to match a typical monthly calendar layout
    df = df[['Weekday', 'Date']]

    # Fill in empty cells with an empty string
    df = df.reindex(pd.date_range(start=df['Date'].min(), end=df['Date'].max(), freq='D')).fillna('')

    return df

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
        monthly_table = create_monthly_table(result_year, result_month)

        # Highlight the week of the result date
        monthly_table = monthly_table.style.apply(highlight_dates, selected_date=result_date, axis=0)

        # Display the monthly table
        st.dataframe(monthly_table)

if __name__ == "__main__":
    main()
