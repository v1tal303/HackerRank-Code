--Problem Statement
/*

Query the Western Longtitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less that 137.2345.
Round your answer to 4 decimal places.

*/

SELECT ROUND(LONG_W,4)
FROM STATION
WHERE LAT_N = (SELECT MAX(LAT_N) FROM STATION WHERE LAT_N < 137.2345);