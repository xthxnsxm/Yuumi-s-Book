from riotwatcher import LolWatcher, ApiError

riotApiKey = "RGAPI-d48aa647-b67d-4ef4-bc11-87b458db0cbc"
watcher = LolWatcher(riotApiKey)
myRegion = 'na1'
summoner = watcher.summoner.by_name(myRegion, 'cweefers69')
summoner_stats = watcher.league.by_summoner(myRegion, summoner['id'])
#spectate = watcher.spectator.by_summoner(myRegion, summoner['id'])

versions = watcher.data_dragon.versions_for_region(myRegion)
champions_version = versions['n']['champion']
current_champ_list = watcher.data_dragon.champions(champions_version)

def other_summoners_in_game(summoner_name: str):
    """
    Given a summoner's name (currently in game), returns the summoner names of
    all other summoners currently participating in the match in the form of a
    list.
    """
    summoner = watcher.summoner.by_name(myRegion, summoner_name)
    spectate = watcher.spectator.by_summoner(myRegion, summoner['id'])
    summoners = []
    for participant in spectate['participants']:
        summoners.append(participant['summonerName'])
    return summoners


def match_victory(summoner_name: str, matchId: str):
    """
    Given a summoner name and matchId, returns whether the summoner has won
    the match or not. If summoner not in game return None.
    """
    match = watcher.match.by_id(myRegion, matchId)
    for participant in match['info']['participants']:
        if participant['summonerName'] == summoner_name:
            return participant['win']
    return None


def match_champion(summoner_name: str, matchId: str):
    """
    Given summoner name and match id, returns the champion the summoner played
    during the match
    """
    match = watcher.match.by_id(myRegion, matchId)
    for participant in match['info']['participants']:
        if participant['summonerName'] == summoner_name:
            return participant['championName']
    return None


def list_of_matches(summoner_name: str):
    """
    Given summoner name, returns a list of the last 20 matches they've played
    """
    puuid = watcher.summoner.by_name(myRegion, summoner_name)['puuid']
    matches = watcher.match.matchlist_by_puuid(myRegion, puuid)
    return matches


def winrate_over_last_games(summoner_name: str):
    """
    Given a summoner name, display their winrate over the last 20 games
    """
    matches = list_of_matches(summoner_name)
    wins = 0
    for match in matches:
        if match_victory(summoner_name, match):
            wins += 1
    return wins / 20


print(winrate_over_last_games('EarHairz'))




