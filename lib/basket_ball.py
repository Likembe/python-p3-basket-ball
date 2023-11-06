from collections import defaultdict

def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

def num_points_per_game(player_name):
    basketball_data = game_dict()
    
    # Combine the players from both the home and away teams
    players = basketball_data["home"]["players"] + basketball_data["away"]["players"]
    
    # Find the player and return the points per game
    for player in players:
        if player["name"] == player_name:
            return player["points_per_game"]
    
    # If the player is not found, return a message stating so
    return "Player not found."

# Example usage:
player_name = "Kevin Love"
print(f"{player_name} scores {num_points_per_game(player_name)} points per game.")


def player_age(player_name):
    basketball_data = game_dict()
    
    # Combine the players from both the home and away teams
    players = basketball_data["home"]["players"] + basketball_data["away"]["players"]
    
    # Find the player and return their age
    for player in players:
        if player["name"] == player_name:
            return player["age"]
    
    # If the player is not found, return a message stating so
    return "Player not found."

# Example usage:
player_name = "Kevin Love"
print(f"{player_name} is {player_age(player_name)} years old.")


def team_colors(team_name):
    basketball_data = game_dict()

    if basketball_data["home"]["team_name"] == team_name:
        return basketball_data["home"]["colors"]
    elif basketball_data ["away"]["team_name"] == team_name:
        return basketball_data["away"]["colors"]
    
    return "Team not found."

#Example
team_name = "Cleveland Cavaliers"
print(f"The colors of the {team_name} are {team_colors(team_name)}.")

team_name = "Chicago Bulls"
print(f"The colors of the {team_name} are {team_colors(team_name)}.")

def team_names():
    basketball_data = game_dict()

    # Get the team names from the 'home' and 'away' keys
    names = [basketball_data["home"]["team_name"], basketball_data["away"]["team_name"]]
    
    return names

# Example usage:
print(f"The teams playing are: {team_names()}")


def player_numbers(team_name):
    basketball_data = game_dict()
    jersey_numbers = []

    # Check the home team and collect jersey numbers if the team name matches
    if basketball_data["home"]["team_name"] == team_name:
        for player in basketball_data["home"]["players"]:
            jersey_numbers.append(player["number"])

    # Check the away team and collect jersey numbers if the team name matches
    elif basketball_data["away"]["team_name"] == team_name:
        for player in basketball_data["away"]["players"]:
            jersey_numbers.append(player["number"])

    # If the team is not found, return a message stating so
    else:
        return "Team not found."

    return jersey_numbers

# Example usage:
team_name = "Cleveland Cavaliers"
print(f"Jersey numbers for the {team_name}: {player_numbers(team_name)}")

team_name = "Washington Wizards"
print(f"Jersey numbers for the {team_name}: {player_numbers(team_name)}")


def player_stats(player_name):
    basketball_data = game_dict()
    
    # Combine the players from both the home and away teams
    players = basketball_data["home"]["players"] + basketball_data["away"]["players"]
    
    # Find the player and return their stats as a dictionary
    for player in players:
        if player["name"] == player_name:
            # Return a copy of the player's dictionary to avoid mutating the original data
            return player.copy()
    
    # If the player is not found, return a message stating so
    return "Player not found."

# Example usage:
player_name = "Kevin Love"
print(f"Stats for {player_name}: {player_stats(player_name)}")


def average_rebounds_by_shoe_brand():
    game_data = game_dict()
    shoe_brand_rebounds = defaultdict(list)

    for team, players in game_data.items():
        for player in players['players']:
            shoe_brand = player['shoe_brand']
            rebounds_per_game = player['rebounds_per_game']
            shoe_brand_rebounds[shoe_brand].append(rebounds_per_game)

    output = ""
    for brand, rebounds_list in shoe_brand_rebounds.items():
        average_rebounds = sum(rebounds_list) / len(rebounds_list)
        output += f"{brand}: {average_rebounds: .2f}\n" 

    print(output, end="")

# Run the function for calculating average rebounds by shoe brand
if __name__ == "__main__":
    average_rebounds_by_shoe_brand()