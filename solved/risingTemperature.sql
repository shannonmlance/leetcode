CREATE TABLE Weather(Id int, RecordDate date, Temperature int)
TRUNCATE TABLE Weather
INSERT INTO Weather (Id, RecordDate, Temperature) VALUES ('1', '2015-01-01', '10')
INSERT INTO Weather (Id, RecordDate, Temperature) VALUES ('2', '2015-01-02', '25')
INSERT INTO Weather (Id, RecordDate, Temperature) VALUES ('3', '2015-01-03', '20')
INSERT INTO Weather (Id, RecordDate, Temperature) VALUES ('4', '2015-01-04', '30')

-- Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.
-- + -- + ---------- + ----------- +
-- | Id | RecordDate | Temperature |
-- + -- + ---------- + ----------- +
-- | 1  | 2015-01-01 | 10          |
-- | 2  | 2015-01-02 | 25          |
-- | 3  | 2015-01-03 | 20          |
-- | 4  | 2015-01-04 | 30          |
-- + -- + ---------- + ----------- +

-- For example, return the following Ids for the above Weather table:
-- + -- +
-- | Id |
-- + -- +
-- | 2  |
-- | 4  |
-- + -- +

SELECT w1.Id
FROM Weather w1, Weather w2
WHERE w1.Temperature > w2.Temperature
AND DATEDIFF(w1.RecordDate, w2.RecordDate) = 1
;