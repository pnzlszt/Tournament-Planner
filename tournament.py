#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("failed connection")



def deleteMatches():
    """Remove all the match records from the database."""
    db, c = connect()
    query = "delete from matches;"
    c.execute(query)
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, c = connect()
    query = "delete from players;"
    c.execute(query)
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, c = connect()
    query = "select count(*) from players;"
    c.execute(query)
    count = c.fetchall()[0][0]
    db.close()
    
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db, c = connect()
    query = "insert into players (names) values (%s) "
    parameter = (name,)
    c.execute(query,parameter)
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, c = connect()
    query = "select id,names,wins_no_null,\
                wins_no_null+losses_no_null as matches\
                from match_records_no_null\
                order by wins_no_null;"
    c.execute(query)
    results = c.fetchall()
    db.close()    
    return results   


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    
    db, c = connect()
    query = "insert into matches (id_winner,id_loser) values (%s,%s) "
    parameter = (winner,loser)
    c.execute(query,parameter)
    db.commit()   
    db.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """    
    list_of_matches = playerStandings()
    pairings = []
    for i in range(0,len(list_of_matches),2):
        pairings.append((list_of_matches[i][0],list_of_matches[i][1],list_of_matches[i+1][0],list_of_matches[i+1][1]))
    
    return pairings


