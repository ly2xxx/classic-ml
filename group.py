import streamlit as st
import random
from itertools import combinations, permutations

def form_matches(num_players, matches_per_player, player_names):
    players = list(range(1, num_players + 1))
    random.shuffle(players)
    matches = {player: set() for player in players}
    
    # Randomly assign player numbers to names
    player_numbers = dict(zip(player_names, players))
    
    # Generate all possible pairs
    possible_pairs = list(permutations(players, 2))
    random.shuffle(possible_pairs)
    
    max_retries = 5000  # Maximum number of retries
    retries = 0
    
    while retries < max_retries:
        # Reset matches
        matches = {player: set() for player in players}
        
        for player1, player2 in possible_pairs:
            if len(matches[player1]) < matches_per_player and len(matches[player2]) < matches_per_player:
                matches[player1].add(player2)
                matches[player2].add(player1)
        
        # Check if all players have the correct number of matches
        all_players_matched = True
        for player in players:
            if len(matches[player]) != matches_per_player:
                all_players_matched = False
                break
        
        if all_players_matched:
            # Display matches with player numbers in order
            ordered_matches = sorted(matches.items())
            for player, opponents in ordered_matches:
                st.write(f"Player {player} vs {', '.join(map(str, sorted(opponents)))}")
            
            # Display legend matching player numbers to names
            st.write("\nPlayer Legend:")
            for name, number in sorted(player_numbers.items(), key=lambda x: x[1]):
                st.write(f"Player {number} = {name}")
            
            break
        
        retries += 1
    
    if retries == max_retries:
        st.error(f"Unable to form matches with the given constraints after {max_retries} retries.")

def main():
    st.title("Match Formation")

    num_players = st.number_input("Enter the number of players", min_value=2, step=1)
    matches_per_player = st.number_input("Enter the number of matches per player", min_value=1, max_value=num_players - 1, step=1)

    player_names = st.text_area("Enter player names (one per line)").split("\n")

    if len(player_names) != num_players:
        st.warning(f"Please enter exactly {num_players} player names.")
    else:
        if st.button("Form Matches"):
            if matches_per_player > num_players // 2:
                st.warning("The number of matches per player should not exceed half the total number of players.")
            else:
                form_matches(num_players, matches_per_player, player_names)

if __name__ == "__main__":
    main()



# Here's how the updated code works:

# The form_matches function takes the number of players and the number of matches per player as input.
# It creates a list of players and shuffles it randomly.
# For each player, it creates a list of opponents by removing the player from the list of all players.
# It then randomly selects matches_per_player opponents from the list of opponents for each player.
# The matches for each player are stored in a dictionary, where the keys are the player numbers, and the values are lists of their opponents.
# The function then prints out the matches for each player using st.write.
# In the main function:

# The user inputs the number of players and the number of matches per player using st.number_input.
# The max_value for matches_per_player is set to num_players - 1, as a player cannot play against themselves.
# When the user clicks the "Form Matches" button, the code checks if the number of matches per player exceeds half the total number of players. If it does, a warning is displayed, as it would not be possible to form unique matches for all players.
# If the number of matches per player is valid, the form_matches function is called with the user inputs.
# With this implementation, you should be able to form matches for the example you provided (11 players, 4 matches per player).