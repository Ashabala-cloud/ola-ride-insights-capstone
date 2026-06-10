# import os
# import pandas as pd
# import pymysql
# import streamlit as st


# # --- DATABASE CONNECTION ---
# def get_db_connection():
#     try:
#         conn = pymysql.connect(
#             host="localhost",
#             user="root",
#             password="Bala@A20",
#             database="Ola",
#             cursorclass=pymysql.cursors.DictCursor,  # Returns rows as dictionaries
#         )
#         return conn
#     except pymysql.MySQLError as err:
#         st.error(f"Database Connection Error: {err}")
#         return None


# conn = get_db_connection()

# # --- APP TITLE ---
# st.title("🚕 Ola Ride Performance Analytics")
# st.markdown(
#     "Interact with SQL query metrics and view the live executive Power BI dashboard."
# )

# # --- SIDEBAR NAVIGATION ---
# st.sidebar.header("Navigation")
# page = st.sidebar.radio(
#     "Go to:", ["SQL Query Insights", "Power BI Live Dashboard"]
# )

# # --- PAGE 1: SQL QUERY INSIGHTS ---
# if page == "SQL Query Insights":
#     st.header("📊 SQL Query Data Exploration")

#     query_option = st.selectbox(
#         "Choose a business metric to analyze:",
#         [
#             "Select an option...",
#             "1. Retrieve all successful bookings",
#             "2. Find the average ride distance for each vehicle type",
#             "3. Get the total number of cancelled rides by customers",
#             "4. List the top 5 customers who booked the highest number of rides",
#             "5. Get the number of rides cancelled by drivers due to personal and car-related reasons",
#             "6. Find the maximum and minimum driver ratings for Prime Sedan bookings",
#             "7. Retrieve all rides where payment was made using UPI",
#             "8. Find the average customer rating per vehicle type",
#             "9. Calculate the total booking value of rides completed successfully",
#             "10. List all incomplete rides along with the reason",
#         ],
#     )

#     if conn is not None and query_option != "Select an option...":
#         sql_query = ""
#         generate_answer = None

#         # 1. Retrieve all successful bookings
#         if query_option == "1. Retrieve all successful bookings":
#             sql_query = (
#                 "SELECT * FROM bookings WHERE Booking_Status = 'Success';"
#             )
#             st.subheader("📋 All Successful Bookings")

#             def generate_answer(df):
#                 return f"**Answer:** Total of **{len(df)}** successful bookings retrieved from the database."

#         # 2. Avg Ride Distance per Vehicle Type
#         elif (
#             query_option
#             == "2. Find the average ride distance for each vehicle type"
#         ):
#             sql_query = """  
#                 SELECT Vehicle_Type, ROUND(AVG(Ride_Distance), 2) as Avg_Distance   
#                 FROM bookings   
#                 GROUP BY Vehicle_Type;  
#             """
#             st.subheader("🚗 Average Ride Distance by Vehicle Category")

#             def generate_answer(df):
#                 summary = " <br> ".join(
#                     [
#                         f"• {row['Vehicle_Type']}: **{row['Avg_Distance']} km**"
#                         for _, row in df.iterrows()
#                     ]
#                 )
#                 return f"**Answer:** The average distance covered across categories is:<br>{summary}"

#         # 3. Total Cancelled Rides by Customers
#         elif (
#             query_option
#             == "3. Get the total number of cancelled rides by customers"
#         ):
#             sql_query = """  
#                 SELECT COUNT(*) as Total_Customer_Cancellations   
#                 FROM bookings   
#                 WHERE Booking_Status = 'Canceled by Customer';  
#             """
#             st.subheader("❌ Total Bookings Cancelled by Customers")

#             def generate_answer(df):
#                 val = df.iloc[0]["Total_Customer_Cancellations"]
#                 return (
#                     f"**Answer:** Customers cancelled a total of **{val}** rides."
#                 )

#         # 4. Top 5 Customers by Number of Rides
#         elif (
#             query_option
#             == "4. List the top 5 customers who booked the highest number of rides"
#         ):
#             sql_query = """  
#                 SELECT Customer_ID, COUNT(*) as Total_Rides   
#                 FROM bookings   
#                 GROUP BY Customer_ID   
#                 ORDER BY Total_Rides DESC   
#                 LIMIT 5;  
#             """
#             st.subheader("🏆 Top 5 Most Frequent Customers")

#             def generate_answer(df):
#                 summary = ", ".join(
#                     [
#                         f"ID {row['Customer_ID']} ({row['Total_Rides']} rides)"
#                         for _, row in df.iterrows()
#                     ]
#                 )
#                 return f"**Answer:** The top 5 loyal clients are: {summary}."

#         # 5. Driver Cancellations by Specific Reasons
#         elif (
#             query_option
#             == "5. Get the number of rides cancelled by drivers due to personal and car-related reasons"
#         ):
#             sql_query = """
#                 SELECT COUNT(*) AS Driver_Cancellations
#                 FROM bookings
#                 WHERE Canceled_rides_by_Driver = 'Personal & Car related issue';
#             """
#             st.subheader(
#                 "🔧 Rides Cancelled by Drivers (Personal/Car Reasons)"
#             )

#             def generate_answer(df):
#                 val = df.iloc[0]["Driver_Cancellations"]
#                 return f"**Answer:** Drivers cancelled **{val}** rides due to personal/car-related reasons."

#         # 6. Max and Min Ratings for Prime Sedan
#         elif (
#             query_option
#             == "6. Find the maximum and minimum driver ratings for Prime Sedan bookings"
#         ):
#             sql_query = """  
#                 SELECT MAX(Driver_Ratings) as Max_Rating, MIN(Driver_Ratings) as Min_Rating   
#                 FROM bookings   
#                 WHERE Vehicle_Type = 'Prime Sedan' AND Driver_Ratings IS NOT NULL;  
#             """
#             st.subheader("⭐ Driver Rating Range for Prime Sedan")

#             def generate_answer(df):
#                 return f"**Answer:** For Prime Sedans, the highest driver rating registered is **{df.iloc[0]['Max_Rating']}★** and the minimum is **{df.iloc[0]['Min_Rating']}★**."

#         # 7. UPI Payment Method Rides
#         elif (
#             query_option
#             == "7. Retrieve all rides where payment was made using UPI"
#         ):
#             sql_query = "SELECT * FROM bookings WHERE Payment_Method = 'UPI';"
#             st.subheader("💳 Bookings Paid via UPI Transaction")

#             def generate_answer(df):
#                 return f"**Answer:** Found **{len(df)}** bookings completely cleared using UPI payments."

#         # 8. Avg Customer Rating per Vehicle Type
#         elif (
#             query_option
#             == "8. Find the average customer rating per vehicle type"
#         ):
#             sql_query = """  
#                 SELECT Vehicle_Type, ROUND(AVG(Customer_Rating), 2) as Avg_Customer_Rating   
#                 FROM bookings   
#                 WHERE Customer_Rating IS NOT NULL
#                 GROUP BY Vehicle_Type;  
#             """
#             st.subheader("📈 Average Customer Feedback Score by Vehicle")

#             def generate_answer(df):
#                 summary = " | ".join(
#                     [
#                         f"{row['Vehicle_Type']}: **{row['Avg_Customer_Rating']}★**"
#                         for _, row in df.iterrows()
#                     ]
#                 )
#                 return f"**Answer:** Average scores split: {summary}"

#         # 9. Total Revenue from Successful Bookings
#         elif (
#             query_option
#             == "9. Calculate the total booking value of rides completed successfully"
#         ):
#             sql_query = """  
#                 SELECT SUM(Booking_Value) as Total_Successful_Revenue   
#                 FROM bookings   
#                 WHERE Booking_Status = 'Success';  
#             """
#             st.subheader("💰 Total Revenue Earned from Completed Rides")

#             def generate_answer(df):
#                 val = df.iloc[0]["Total_Successful_Revenue"]
#                 return f"**Answer:** Gross volume generated from successful completions equates to **₹{val:,.2f}**."

#         # 10. Incomplete Rides and Reasons
#         elif (
#             query_option == "10. List all incomplete rides along with the reason"
#         ):
#             sql_query = """  
#                 SELECT Booking_ID, Incomplete_Rides, Incomplete_Rides_Reason   
#                 FROM bookings   
#                 WHERE Incomplete_Rides = 'Yes';
#             """
#             st.subheader("⚠️ Incomplete Rides and Reasons")

#             def generate_answer(df):
#                 return f"**Answer:** There are currently **{len(df)}** incomplete trips logged with specific failure parameters."

#         # Execution Engine
#         if sql_query:
#             try:
#                 cursor = conn.cursor()
#                 cursor.execute(sql_query)
#                 data = cursor.fetchall()

#                 if data:
#                     df = pd.DataFrame(data)
#                     st.metric(label="Total Rows Retrieved", value=len(df))

#                     # Display Live Dynamic QA Box
#                     if generate_answer:
#                         st.info(generate_answer(df), icon="💡")

#                     # Display Interactive Data View
#                     st.dataframe(df, use_container_width=True)
#                 else:
#                     st.warning("Query executed successfully but returned 0 rows.")

#             except pymysql.MySQLError as err:
#                 st.error(f"Failed to execute query: {err}")
#             finally:
#                 cursor.close()

#     elif conn is None:
#         st.warning(
#             "Please configure your database credentials in the code to view live SQL metrics."
#         )

# # --- PAGE 2: POWER BI LIVE DASHBOARD ---
# elif page == "Power BI Live Dashboard":
#     st.header("📈 Interactive Power BI Dashboard Views")

#     dashboard_view = st.selectbox(
#         "Select a Dashboard View to display:",
#         [
#             "1. Overall Performance Overview",
#             "2. Vehicle Type Breakdown",
#             "3. Revenue Analysis",
#             "4. Cancellation Insights",
#             "5. Customer & Driver Ratings",
#         ],
#     )

#     script_dir = (
#         os.path.dirname(os.path.abspath(__file__))
#         if "__file__" in locals()
#         else os.getcwd()
#     )

#     image_name = ""
#     caption_text = ""

#     if dashboard_view == "1. Overall Performance Overview":
#         image_name = "page1.png.png"
#         caption_text = "Ola Executive Performance - Overall View"
#     elif dashboard_view == "2. Vehicle Type Breakdown":
#         image_name = "page2.png.png"
#         caption_text = "Ola Executive Performance - Vehicle Type Analysis"
#     elif dashboard_view == "3. Revenue Analysis":
#         image_name = "page3.png.png"
#         caption_text = "Ola Executive Performance - Revenue Metrics"
#     elif dashboard_view == "4. Cancellation Insights":
#         image_name = "page4.png.png"
#         caption_text = "Ola Executive Performance - Cancellation Breakdown"
#     elif dashboard_view == "5. Customer & Driver Ratings":
#         image_name = "page5.png.png"
#         caption_text = "Ola Executive Performance - Ratings & Feedback Analysis"

#     image_path = os.path.join(script_dir, image_name)

#     if os.path.exists(image_path):
#         st.image(image_path, caption=caption_text, use_container_width=True)
#     else:
#         st.error(
#             f"❌ Cannot find the specific dashboard image file: '{image_name}'"
#         )
#         st.info(
#             f"Please save your question-specific screenshot in `{script_dir}` named exactly as `{image_name}`"
#         )

import os
import pandas as pd
import streamlit as st
from pandasql import sqldf

# --- SET PAGE CONFIG (Must be the very first Streamlit command) ---
st.set_page_config(page_title="Ola Ride Analytics", layout="wide")

# --- LOAD CSV DATA FROM GITHUB ---
@st.cache_data
def load_csv_data():
    try:
        # Looks for bookings.csv right next to main.py in your GitHub repo
        df = pd.read_csv("bookings.csv")
        return df
    except Exception as e:
        st.error(f"Error loading bookings.csv file: {e}")
        return None

# Load the dataframe globally so pandasql can access it
bookings = load_csv_data()

# Simulated connection check to satisfy the UI logic
conn = True if bookings is not None else None


# --- APP TITLE ---
st.title("🚕 Ola Ride Performance Analytics")
st.markdown(
    "Interact with SQL query metrics and view the live executive Power BI dashboard."
)

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Navigation")
page = st.sidebar.radio(
    "Go to:", ["SQL Query Insights", "Power BI Live Dashboard"]
)

# --- PAGE 1: SQL QUERY INSIGHTS ---
if page == "SQL Query Insights":
    st.header("📊 SQL Query Data Exploration")

    query_option = st.selectbox(
        "Choose a business metric to analyze:",
        [
            "Select an option...",
            "1. Retrieve all successful bookings",
            "2. Find the average ride distance for each vehicle type",
            "3. Get the total number of cancelled rides by customers",
            "4. List the top 5 customers who booked the highest number of rides",
            "5. Get the number of rides cancelled by drivers due to personal and car-related reasons",
            "6. Find the maximum and minimum driver ratings for Prime Sedan bookings",
            "7. Retrieve all rides where payment was made using UPI",
            "8. Find the average customer rating per vehicle type",
            "9. Calculate the total booking value of rides completed successfully",
            "10. List all incomplete rides along with the reason",
        ],
    )

    if conn is not None and query_option != "Select an option...":
        sql_query = ""
        generate_answer = None

        # 1. Retrieve all successful bookings
        if query_option == "1. Retrieve all successful bookings":
            sql_query = (
                "SELECT * FROM bookings WHERE Booking_Status = 'Success';"
            )
            st.subheader("📋 All Successful Bookings")

            def generate_answer(df):
                return f"**Answer:** Total of **{len(df)}** successful bookings retrieved from the database."

        # 2. Avg Ride Distance per Vehicle Type
        elif (
            query_option
            == "2. Find the average ride distance for each vehicle type"
        ):
            sql_query = """  
                SELECT Vehicle_Type, ROUND(AVG(Ride_Distance), 2) as Avg_Distance   
                FROM bookings   
                GROUP BY Vehicle_Type;  
            """
            st.subheader("🚗 Average Ride Distance by Vehicle Category")

            def generate_answer(df):
                summary = " <br> ".join(
                    [
                        f"• {row['Vehicle_Type']}: **{row['Avg_Distance']} km**"
                        for _, row in df.iterrows()
                    ]
                )
                return f"**Answer:** The average distance covered across categories is:<br>{summary}"

        # 3. Total Cancelled Rides by Customers
        elif (
            query_option
            == "3. Get the total number of cancelled rides by customers"
        ):
            sql_query = """  
                SELECT COUNT(*) as Total_Customer_Cancellations   
                FROM bookings   
                WHERE Booking_Status = 'Canceled by Customer';  
            """
            st.subheader("❌ Total Bookings Cancelled by Customers")

            def generate_answer(df):
                val = df.iloc[0]["Total_Customer_Cancellations"]
                return (
                    f"**Answer:** Customers cancelled a total of **{val}** rides."
                )

        # 4. Top 5 Customers by Number of Rides
        elif (
            query_option
            == "4. List the top 5 customers who booked the highest number of rides"
        ):
            sql_query = """  
                SELECT Customer_ID, COUNT(*) as Total_Rides   
                FROM bookings   
                GROUP BY Customer_ID   
                ORDER BY Total_Rides DESC   
                LIMIT 5;  
            """
            st.subheader("🏆 Top 5 Most Frequent Customers")

            def generate_answer(df):
                summary = ", ".join(
                    [
                        f"ID {row['Customer_ID']} ({row['Total_Rides']} rides)"
                        for _, row in df.iterrows()
                    ]
                )
                return f"**Answer:** The top 5 loyal clients are: {summary}."

        # 5. Driver Cancellations by Specific Reasons
        elif (
            query_option
            == "5. Get the number of rides cancelled by drivers due to personal and car-related reasons"
        ):
            sql_query = """
                SELECT COUNT(*) AS Driver_Cancellations
                FROM bookings
                WHERE Canceled_rides_by_Driver = 'Personal & Car related issue';
            """
            st.subheader(
                "🔧 Rides Cancelled by Drivers (Personal/Car Reasons)"
            )

            def generate_answer(df):
                val = df.iloc[0]["Driver_Cancellations"]
                return f"**Answer:** Drivers cancelled **{val}** rides due to personal/car-related reasons."

        # 6. Max and Min Ratings for Prime Sedan
        elif (
            query_option
            == "6. Find the maximum and minimum driver ratings for Prime Sedan bookings"
        ):
            sql_query = """  
                SELECT MAX(Driver_Ratings) as Max_Rating, MIN(Driver_Ratings) as Min_Rating   
                FROM bookings   
                WHERE Vehicle_Type = 'Prime Sedan' AND Driver_Ratings IS NOT NULL;  
            """
            st.subheader("⭐ Driver Rating Range for Prime Sedan")

            def generate_answer(df):
                return f"**Answer:** For Prime Sedans, the highest driver rating registered is **{df.iloc[0]['Max_Rating']}★** and the minimum is **{df.iloc[0]['Min_Rating']}★**."

        # 7. UPI Payment Method Rides
        elif (
            query_option
            == "7. Retrieve all rides where payment was made using UPI"
        ):
            sql_query = "SELECT * FROM bookings WHERE Payment_Method = 'UPI';"
            st.subheader("💳 Bookings Paid via UPI Transaction")

            def generate_answer(df):
                return f"**Answer:** Found **{len(df)}** bookings completely cleared using UPI payments."

        # 8. Avg Customer Rating per Vehicle Type
        elif (
            query_option
            == "8. Find the average customer rating per vehicle type"
        ):
            sql_query = """  
                SELECT Vehicle_Type, ROUND(AVG(Customer_Rating), 2) as Avg_Customer_Rating   
                FROM bookings   
                WHERE Customer_Rating IS NOT NULL
                GROUP BY Vehicle_Type;  
            """
            st.subheader("📈 Average Customer Feedback Score by Vehicle")

            def generate_answer(df):
                summary = " | ".join(
                    [
                        f"{row['Vehicle_Type']}: **{row['Avg_Customer_Rating']}★**"
                        for _, row in df.iterrows()
                    ]
                )
                return f"**Answer:** Average scores split: {summary}"

        # 9. Total Revenue from Successful Bookings
        elif (
            query_option
            == "9. Calculate the total booking value of rides completed successfully"
        ):
            sql_query = """  
                SELECT SUM(Booking_Value) as Total_Successful_Revenue   
                FROM bookings   
                WHERE Booking_Status = 'Success';  
            """
            st.subheader("💰 Total Revenue Earned from Completed Rides")

            def generate_answer(df):
                val = df.iloc[0]["Total_Successful_Revenue"]
                return f"**Answer:** Gross volume generated from successful completions equates to **₹{val:,.2f}**."

        # 10. Incomplete Rides and Reasons
        elif (
            query_option == "10. List all incomplete rides along with the reason"
        ):
            sql_query = """  
                SELECT Booking_ID, Incomplete_Rides, Incomplete_Rides_Reason   
                FROM bookings   
                WHERE Incomplete_Rides = 'Yes';
            """
            st.subheader("⚠️ Incomplete Rides and Reasons")

            def generate_answer(df):
                return f"**Answer:** There are currently **{len(df)}** incomplete trips logged with specific failure parameters."


        # --- CSV-BASED SQL EXECUTION ENGINE ---
        if sql_query:
            try:
                # pandasql queries the 'bookings' dataframe directly
                data = sqldf(sql_query, globals())

                if not data.empty:
                    df = pd.DataFrame(data)
                    st.metric(label="Total Rows Retrieved", value=len(df))

                    # Display Live Dynamic QA Box
                    if generate_answer:
                        st.info(generate_answer(df), icon="💡")

                    # Display Interactive Data View
                    st.dataframe(df, use_container_width=True)
                else:
                    st.warning("Query executed successfully but returned 0 rows.")

            except Exception as err:
                st.error(f"Failed to execute query: {err}")

    elif conn is None:
        st.warning(
            "Please ensure 'bookings.csv' is present in your repository to analyze metrics."
        )

# --- PAGE 2: POWER BI LIVE DASHBOARD ---
elif page == "Power BI Live Dashboard":
    st.header("📈 Interactive Power BI Dashboard Views")

    dashboard_view = st.selectbox(
        "Select a Dashboard View to display:",
        [
            "1. Overall Performance Overview",
            "2. Vehicle Type Breakdown",
            "3. Revenue Analysis",
            "4. Cancellation Insights",
            "5. Customer & Driver Ratings",
        ],
    )

    script_dir = (
        os.path.dirname(os.path.abspath(__file__))
        if "__file__" in locals()
        else os.getcwd()
    )

    image_name = ""
    caption_text = ""

    if dashboard_view == "1. Overall Performance Overview":
        image_name = "page1.png.png"
        caption_text = "Ola Executive Performance - Overall View"
    elif dashboard_view == "2. Vehicle Type Breakdown":
        image_name = "page2.png.png"
        caption_text = "Ola Executive Performance - Vehicle Type Analysis"
    elif dashboard_view == "3. Revenue Analysis":
        image_name = "page3.png.png"
        caption_text = "Ola Executive Performance - Revenue Metrics"
    elif dashboard_view == "4. Cancellation Insights":
        image_name = "page4.png.png"
        caption_text = "Ola Executive Performance - Cancellation Breakdown"
    elif dashboard_view == "5. Customer & Driver Ratings":
        image_name = "page5.png.png"
        caption_text = "Ola Executive Performance - Ratings & Feedback Analysis"

    image_path = os.path.join(script_dir, image_name)

    if os.path.exists(image_path):
        st.image(image_path, caption=caption_text, use_container_width=True)
    else:
        st.error(
            f"❌ Cannot find the specific dashboard image file: '{image_name}'"
        )
        st.info(
            f"Please save your question-specific screenshot in `{script_dir}` named exactly as `{image_name}`"
        )
