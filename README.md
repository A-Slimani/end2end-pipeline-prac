# README 

This project is practice to create an end to end pipeline.
Currently following this video as a starting point https://www.youtube.com/watch?v=PHsC_t0j1dU

# TODO

- Learn about dbt and incorporate to the project
- Find potential SQL scripts that can be used with the current db
- Scrape page 'events and fights' and 'stat leaders' (will need this to continue with the dbt part of the video) 
- split the event location columns into country, state, city (maybe create a CTE or subquery for it for dbt)

# Notes
- UFC tables
    - fights
        - winner
        - loser
        - knockdowns
        - strikes
        - takedowns
        - submission_attempts
        - method
        - finish_type
        - round_finish 
        - time_finish



## Docker

Create the db by using the compose yaml with the command `docker-compose up -d`

To access the db in the terminal use the command `docker exec -it container_name bash`

## DB

Open the db with the command `psql -U username -d database_name`