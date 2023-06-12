API Interface for Account Management System
This repository contains the implementation of a basic API interface for populating and querying an account management system for RocketGames, a game publishing platform. The API allows for managing players, games, studios, and the relationship between players and games.

Data Models
The following data models are used in the API:

Players: Represents the players who create accounts to play games.

    pid (Primary Key): Unique identifier for each player as a player id.
    uname: Username chosen by the player.
    email: Email address associated with the player's account.
    contact: Contact number provided by the player.
    age: Age information provided by the player.
    gender: Gender information provided by the player.
    country: Player country information provided.
    password: Password for the player's account.
    account_status: Indicates whether the account is active or closed.

Games: Represents the games published by RocketGames.
    gid (Primary Key): Unique identifier for each game.
    game_title: Title of the game.
    cost: Price of the game fixed by the studio.
    studio_id: Foreign key referencing the Studio entity.
    Studio: Represents the studios that develop the games.

studio_id (Primary Key): Unique identifier for each studio.
    studio_name: Name of the studio.
    studio_location: Location of the studio.

GamePlay: Represents the relationship between players and the games they play.
    pid (Foreign Key): Foreign key referring to the Players table.
    gid (Foreign Key): Foreign key referring to the Games table.

API Endpoints
The API provides the following endpoints for interacting with the account management system:
    # Player routes
    POST /players: Creates a new player account.
    DELETE /players/{pid}: Closes the account of a specific player.
    DELETE /players/{pid}/games/{gid}: Unregister or Removes a game from the player's collection.

    # Publisher routes
    GET /publishers/popularity: report the popularity of all our published titles.
    GET /publishers/studios/{studio_id}/players: Retrieves information list of all the players playing on a given studios' titles.

    # Studio routes
    DELETE /studios/{studio_id}/players/{pid}/games: Removes or unregister a user from one or more games in our collection.
    GET /studios/{studio_id}/popularity: Retrieves information aboutreport the popularity of all our published games.
    

Running the API
To run the API, follow these steps:

Install the required dependencies mentioned in the requirements.txt file.
Set up a database connection and configure the connection details in the Flask app.
Run the Flask application using the command python app.py.
The API will be accessible at http://localhost:5000/
