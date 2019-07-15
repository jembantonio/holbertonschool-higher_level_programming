-- a script that displays the max temperature of each state
-- ordered by state name

SELECT state, max(value) AS max_temp FROM temperatures GROUP BY state
