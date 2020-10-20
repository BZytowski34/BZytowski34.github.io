print(5)
x=5
print(x+1)


price = 24.95
discount = .4
num_copies = 60
shipping_cost = 3 +.75*(num_copies -1)
total_cost = price*discount*num_copies + shipping_cost

start_time_hour = 6
start_time_mins = 52
start_time_in_seconds = start_time_hour*3600 + start_time_mins*60
easy_mile_mins = 8
easy_mile_seconds = 15
easy_mile_time_in_seconds = easy_mile_mins*60 + easy_mile_seconds
fast_mile_mins = 7
fast_mile_seconds = 12
fast_mile_time_in_seconds = fast_mile_mins*60 +fast_mile_seconds
num_easy_miles = 2
num_fast_miles = 3
total_run_time_seconds = easy_mile_time_in_seconds*2 + fast_mile_time_in_seconds*3
end_time_in_seconds = start_time_in_seconds + total_run_time_seconds
end_time_hour = end_time_in_seconds//3600
end_time_min = (end_time_in_seconds-(end_time_hour*3600))//60
end_time_seconds = end_time_in_seconds - (end_time_hour*3600) - (end_time_min*60)
print(end_time_hour,':', end_time_min, ':', end_time_seconds)