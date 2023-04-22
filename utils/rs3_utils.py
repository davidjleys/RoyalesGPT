from rs3_api import Runemetrics
from urllib.parse import quote

runemetrics = Runemetrics()

def get_player_stats(player_name):
    try:
        encoded_player_name = quote(player_name)
        profile = runemetrics.get_profile(encoded_player_name)
        if 'error' in profile:
            return None
        else:
            return profile['skillvalues']
    except Exception as e:
        print(f"Error fetching player stats: {e}")
        return None