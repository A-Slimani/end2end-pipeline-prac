# README 

This project is practice to create an end to end pipeline.
Currently following this video as a starting point https://www.youtube.com/watch?v=PHsC_t0j1dU

## TODO
- Learn Airflow

### Low Priority
- Add more potential dbt transformations (under Dbt notes)
- Scrape the age of the fighter
- split the event location columns into country, state, city (maybe create a CTE or subquery for it for dbt)
- Convert to enum
    - weight classes
    - Method (of victory)
- Move the scraper to a docker instance 

## Dbt Notes
- What are some potential sub-tables / queries to write for a ufc db
    - Fighter career aggregates
        - Total fights
        - Win Percentage
        - Avg
            - Time
            - Sig. Strikes
            - Takedowns
            - Sub Attempts
            - knockdowns
            - wins by DEC / KO / TKO / SUB
    - Time based aggregatation e.g. for the year 
    - Location ( by country / state )

## Docker

Create the db by using the compose yaml with the command `docker-compose up -d`

## Scrapy

Commands to run the scrapy crawlers
```

```

## DB

To access the db in the terminal use the command `docker exec -it container_name bash`

Open the db with the command `psql -U username -d database_name`