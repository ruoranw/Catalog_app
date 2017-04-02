-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament；


CREATE TABLE players(id serial PRIMARY KEY,
                     name text);


CREATE TABLE matches(match_id serial PRIMARY KEY,
                     winner integer REFERENCES players(id),
                     loser integer REFERENCES players(id));


CREATE VIEW complete AS SELECT players.id, players.name,
                     COUNT (matches.winner) as wins,
                     COUNT (matches.loser) + COUNT(matches.loser) as total_m
                     FROM players LEFT JOIN matches ON id = winner AND id = loser
                     GROUP BY players.id
                     ORDER BY wins DESC;


CREATE OR REPLACE FUNCTION updated_complete()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $BODY$
  BEGIN
      IF TG_OP = 'UPDATE' THEN
          UPDATE complete SET wins = wins+1, total_m = total_m+1 WHERE id = NEW.id;
          UPDATE complete SET loses = loses+1, total_m = total_m+1 WHERE id = NEW.id;
          RETURN NEW;
      END IF;
      RETURN NEW;
  END;
  $BODY$;

CREATE TRIGGER updated_complete_trig
    INSTEAD OF UPDATE
    ON complete FOR EACH ROW EXECUTE PROCEDURE updated_complete();
















