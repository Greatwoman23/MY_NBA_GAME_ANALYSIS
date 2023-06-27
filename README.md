# Welcome to My Nba Game Analysis
***

## Task
Create a function analyze_nba_game(play_by_play_moves) 
which receives an array of play and will return a dictionary summary of the game.

## Description
The provided solution is a Python code designed to analyze play-by-play data from an NBA game and generate a comprehensive game summary in the form of a dictionary.
 The solution comprises two main components: the analyse_nba_game function and the print_nba_game_stats function.
The analyse_nba_game function processes an array of play-by-play moves as its input. It iterates through each play and extracts relevant details, such as the period, remaining seconds, teams involved, scores, and description. 
The function maintains separate data for the home team and the away team. It updates the statistics for each player, including field goals (FG), field goal attempts (FGA), three-pointers (3P), three-point attempts (3PA), free throws (FT), free throw attempts (FTA), offensive rebounds (ORB), defensive rebounds (DRB), total rebounds (TRB), assists (AST), steals (STL), blocks (BLK), turnovers (TOV), personal fouls (PF), and points (PTS). 
Once all the plays have been processed, the function returns a dictionary containing a summary of the game, including the team names and the players' data.

The print_nba_game_stats function takes the game summary dictionary as input. It formats and prints the game statistics in a tabular format. 
The header row lists various statistical categories such as FG, FGA, FG%, 3P, 3PA, 3P%, FT, FTA, FT%, ORB, DRB, TRB, AST, STL, BLK, TOV, PF, and PTS. For each player in the team's player_data, the function prints their individual statistics. Finally, it prints the "Totals" row, which represents the aggregate statistics for the team. This allows for a comprehensive overview of player performance and team statistics for the NBA ga
The solution shows a thorough examination of player performance and team statistics for the specified NBA game. 
It efficiently computes and presents essential measurements, including field goal percentage, three-point percentage, free throw percentage, rebounds, assists, steals, blocks, turnovers, personal fouls, and total points. 
This analysis grants an understanding of the game dynamics and the contributions made by individual players, as well as the collective performance of the team.

## Installation
There was no major installation, the only installation was the data used to write the code which is the https://storage.googleapis.com/qwasar-public/nba_game_warriors_thunder_20181016.txt

## Usage
By running the code with the given example data, you can see the output of the NBA game analysis 
which displays the games model in a tabular format for the nba game warrior thunder.
```
To run the code use ./python my_nba_game_analysis.py
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
