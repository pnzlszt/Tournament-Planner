Tournament project 25/03/2016

This project is composed of a python module that uses the 
PostgreSQL database in order to keep track of players and 
matches in a game tournament with a Swiss pairing system.

The zipped file includes the following files:
- tournament.sql which containts the database schema and all the
  tables and views necessary;
- tournament.py in which are defined different python functions
  that can perform queries on the database;
- tournament_test.py that can test the correctness of the python
  functions defined in tournament.py;
- this README.

In order to run this project: 
1) cd to /vagrant/forum and run psql,
2) run\i tournament.sql to import the tournament.sql
   file and build the database,
3) from the command line run $ python tournament_test.py

