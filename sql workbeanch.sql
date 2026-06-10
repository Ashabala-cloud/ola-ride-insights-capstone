create database Ola;
use Ola;
Use ola;
#1. Retrieve all successful bookings:
create view all_Successful_Bookings as
SELECT * FROM bookings
WHERE Booking_Status = 'Success';

select * from Successful_Bookings;

#2. Find the average ride distance for each vehicle type:
create view  average_ride_distance_for_each_vehicle as
SELECT Vehicle_Type, AVG(Ride_Distance)
as avg_distance FROM bookings
GROUP BY Vehicle_Type;

select * from ride_distance_for_each_vehicle;

#3. Get the total number of canceled rides by customer:
Create View Canceled_rides_by_customers as
SELECT COUNT(*) FROM bookings
WHERE Booking_Status = 'Canceled by Customer';

select * from Canceled_rides_by_customers;

#4. List the top 5 customers who booked the highest number of rides:
create view Top_5_Customers as
SELECT Customer_ID, COUNT(Booking_ID) as total_rides
FROM bookings
GROUP BY Customer_ID
ORDER BY total_rides DESC LIMIT 5;

select * from Top_5_Customers;

#5.Get the number of rides canceled by drivers due to personal and car-related issues:
Create View Rides_cancelled_by_Drivers_P_C_Issues As
select count(*)from bookings
where Canceled_rides_by_Driver ='Personal & Car related issue';

select * from Rides_cancelled_by_Drivers_P_C_Issues;

#6. Find the maximum and minimum driver ratings for Prime Sedan bookings:
create view max_min_Driver_Ratings as
select max(Driver_Ratings)as max_ratings,
min(Driver_Ratings)as min_ratings
from bookings where Vehicle_Type='Prime Sedan';

select * from max_min_Driver_Ratings;

#7. Retrieve all rides where payment was made using UPI:
create view  UPI_payments as
select * from bookings
Where payment_method='UPI';

select * from UPI_payments;

#8. Find the average customer rating per vehicle type:
create view avg_Customer_Rating as
SELECT Vehicle_Type,
    AVG(Customer_Rating) AS Avg_Customer_Rating
FROM bookings
GROUP BY Vehicle_Type;

select * from avg_Customer_Rating;

#9. Calculate the total booking value of rides completed successfully:
create view total_successful_ride as
select sum(booking_value) as total_successful_ride_value
from bookings
where booking_status ='success';

select * from total_successful_ride;

#10. List all incomplete rides along with the reason:
create view Incomplete_rides_reason as
select booking_ID,Incomplete_rides_reason
from bookings
where Incomplete_rides ='yes';

select * from Incomplete_rides_reason;

