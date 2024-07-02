import streamlit as st
import random
from itertools import combinations

def generate_matches(num_players, matches_per_player):
    players = list(range(1, num_players + 1))
    all_matches = list(combinations(players, 2))
    random.shuffle(all_matches)
    
    schedule = {player: set() for player in players}
    
    for _ in range(100):  # Try multiple times to find a valid schedule
        temp_schedule = {player: set() for player in players}
        for match in all_matches:
            player1, player2 = match
            if (len(temp_schedule[player1]) < matches_per_player and
                len(temp_schedule[player2]) < matches_per_player):
                temp_schedule[player1].add(player2)
                temp_schedule[player2].add(player1)
        
        if all(len(opponents) == matches_per_player for opponents in temp_schedule.values()):
            return temp_schedule
    
    # If we couldn't find a perfect schedule, return the best we have
    return schedule

def main():
    st.title("Tournament Match Draw")
    
    num_players = st.number_input("Number of players in the tournament", min_value=2, value=4, step=1)
    matches_per_player = st.number_input("Number of matches each player should play", min_value=1, max_value=num_players-1, value=2, step=1)
    
    player_names = st.text_area("Enter player names (one per line)").split('\n')
    player_names = [name.strip() for name in player_names if name.strip()]  # Remove empty names
    
    if st.button("Generate Match Draw"):
        if len(player_names) != num_players:
            st.error(f"Please enter exactly {num_players} player names.")
        else:
            schedule = generate_matches(num_players, matches_per_player)
            
            # Randomly assign player numbers to names
            player_numbers = list(range(1, num_players + 1))
            random.shuffle(player_numbers)
            player_assignments = dict(zip(player_names, player_numbers))
            
            st.subheader("Player Assignments:")
            # Display player assignments in numeric order
            for number in sorted(player_numbers):
                name = [name for name, num in player_assignments.items() if num == number][0]
                st.write(f"Player {number}: {name}")
            
            st.subheader("Match Schedule:")
            for player, opponents in sorted(schedule.items()):
                st.write(f"Player {player}: vs {', '.join(map(str, sorted(opponents)))}")
            
            # Check if all players have the correct number of matches
            incomplete = [player for player, opponents in schedule.items() if len(opponents) < matches_per_player]
            if incomplete:
                st.warning(f"Note: Players {', '.join(map(str, incomplete))} have fewer than {matches_per_player} matches.")
            else:
                st.success("All players have the correct number of unique matches.")

if __name__ == "__main__":
    main()



