# Fixing Players table

### 1) Export the sqlite table `Player` to csv

- In the terminal, navigate to the folder where the `database.sqlite` file is located.

- Run the following: `sqlite3 < data/export_player_from_sqlite.txt` 
    - This assumes that the file is in the same folder. If not, edit accordingly.
    - This outputs `Player.csv` into the same folder
    - I then moved it to `data/` e.g.:
        - `mv Player.csv data/Player.csv`

### 2) Import the `Player.csv` table into the PostgreSQL db.

- Prep by navigating to the folder where you have the `Player.csv` file.

- Start `psql`

- Connect to database: `connect soccer`

- Backup the `player` table in case something goes wrong. Run:
    - `create table player_backup (like player including all);`
    - It should return message: `CREATE TABLE`

- Next, fix the `player` table. I think it failed before because the values for `height` are `numeric`, but 
    the PostgreSQL table schema has them as `bigint`. So run the following to force them to `numeric`:
    - `alter table player alter column height type numeric;`
    - It should return message: `ALTER TABLE`

- Now, import the `Player.csv` table into the `player` table by running the following line in psql:
    - `\copy player from 'Player.csv' delimiter ',' csv header;`

- It should have returned a message `COPY 11060`. Make sure by looking at a few rows, for example:
    - `select * from player limit 10;`

- If that's good you're done! 
    - `\quit`

