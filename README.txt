To use the program, there are two different files: database_setup.py and project.py. You must first initialize database_setup.py to create the database file. project.py has the functions to create and edit the website application.

After tournament.sql is initialized, tournament.py must be initialized to be able to use all the functions. Tournament.py has different functions: connect, deleteMatches, deletePlayers, countPlayers, registerPlayer, playerStandings, reportMatch, swissPairings.

*connect: connects to the tournament database.
*deleteMatches: removes all match records from database
*deletePlayers: removes all player records from database
*countPlayers: returns the number of players registered
*registerPlayer: adds a player to tournament database, needs a name input and the database will give it a id number.
*playerStandings: returns a list of the players and their win records sorted by number of wins.
*reportMatch: records a match between two players, needs two name inputs.
*swissPairings: returns a list of pairs of players that will play in the next round.