--register the python file.
register 'average.py' using jython as udfs;

--remove a file in HDFS if the same name file exists.
rmf heatmap_output;

--load data.
raw = LOAD 'final/problem3/ny_taxi_1.csv' USING PigStorage(',') AS (medallion:chararray, hack_license:chararray, vendor_id:chararray, rate_code:int, store_and_fwd_flag:chararray, pickup_datetime:chararray, dropoff_datetime:chararray, passenger_count:int, trip_time_in_secs:int, trip_distance:double, pickup_longitude:double, pickup_latitude:double, dropoff_longitude:double, dropoff_latitude:double, payment_type:chararray, fare_amount:double, surcharge:double, mta_tax:double, tip_amount:double, tolls_amount:double, total_amount:double);

--filter out DropOffTime.
step1 = FILTER raw BY pickup_datetime is not null AND pickup_datetime != 'null' AND pickup_datetime != '';

--filter out the data based on the bounding box.
step2 = FILTER step1 BY $10 > -74.25 AND $10 < -73.70 AND $11 > 40.49 AND $11 < 40.92;

--generate new records to send down the pipeline to the next operator.
step3 = FOREACH step2 GENERATE $10,$11,$15;

--generate new records based on latitude and longitude  key.
step4 = FOREACH step3 GENERATE $2,(int)(($0 + 74.25)/0.005) AS logkey,(int)(($1 - 40.49)/0.005) AS latkey;

--collect all records with the same latitude and longitude key.
step4_group = GROUP step4 BY (latkey,logkey);

--calculate the average of radiation levels per each cell.
step4_avg = FOREACH step4_group GENERATE group, udfs.getAverage(step6.fare_amount);

--sort data based on the group.
result = ORDER step4_avg BY group;

--dump the results to your screen
--dump result;

--send the output to a folder in HDFS
store result into 'heatmap_output';
