-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;
\c tournament

CREATE TABLE players(id serial PRIMARY KEY,
                     name text);


CREATE TABLE matches(match_id serial PRIMARY KEY,
                     winner INT REFERENCES players(id) ON DELETE CASCADE,
                     loser INT REFERENCES players(id) ON DELETE CASCADE
                     CHECK (winner <> loser));


CREATE VIEW standings AS SELECT players.id, players.name,
                      SUM(CASE WHEN players.id = matches.winner THEN 1 ELSE 0 END) AS wins,
                      COUNT(matches) as total_m
                      FROM players LEFT JOIN matches
                      ON players.id = matches.winner OR players.id = matches.loser
                      GROUP BY players.id
                      ORDER BY wins DESC,
                               total_m ASC;


CREATE VIEW random AS SELECT *
                   FROM players
                   ORDER BY random();















