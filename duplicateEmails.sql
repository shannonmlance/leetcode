-- SQL Schema
CREATE TABLE Person (Id int, Email varchar(255))
TRUNCATE TABLE Person
INSERT INTO Person (Id, Email) VALUES ('1', 'a@b.com')
INSERT INTO Person (Id, Email) VALUES ('2', 'c@d.com')
INSERT INTO Person (Id, Email) VALUES ('3', 'a@b.com')

-- Write a SQL query to find all duplicate emails in a table named Person.

-- + -- + ------- +
-- | Id | Email   |
-- + -- + ------- +
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- + -- + ------- +
-- For example, your query should return the following for the above table:

-- + ------- +
-- | Email   |
-- + ------- +
-- | a@b.com |
-- + ------- +
-- Note: All emails are in lowercase.

SELECT Email
FROM (SELECT COUNT(*) AS repeated, Email
FROM Person
GROUP BY Email
HAVING repeated > 1) AS temp
;
