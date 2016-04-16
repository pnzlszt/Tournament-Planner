-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

create database tournament;

\c tournament

drop table if exists players,matches;

create table players (
	id serial primary key,
	names text
);

create table matches (
	id_winner INT REFERENCES players(id),
	id_loser INT REFERENCES players(id) 
);

DROP VIEW IF EXISTS wins,losses,match_records,match_records_no_null;

create VIEW wins as select id_winner,count(*) as wins
       from matches
       group by id_winner;

create VIEW losses as select id_loser,count(*) as losses
       from matches
       group by id_loser;

create VIEW match_records as select
       players.id,players.names,wins.wins,losses.losses from players
       left join wins on players.id = wins.id_winner
       left join losses on players.id = losses.id_loser;

CREATE VIEW match_records_no_null as select
	id,names,wins,
        case when wins IS NOT NULL then wins
        else 0
        end as wins_no_null,
        losses,
        case when losses IS NOT NULL then losses
        else 0
        end as losses_no_null
        from match_records;

