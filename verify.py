# Python script for interacting with the GW2 API

import requests; requests = requests.session()

ACCOUNTS_URL = 'https://api.guildwars2.com/v2/account'
GUILDS_URL = 'https://api.guildwars2.com/v1/guild_details.json?guild_id='
WORLDS_URL = 'https://api.guildwars2.com/v2/worlds?id='

def account_api(key):
    auth = {'Authorization': 'Bearer ' + key}
    api = requests.get(
        ACCOUNTS_URL, headers=auth
    )
    return api.json()

def guild_api(guild_id):
    api = requests.get(
        GUILDS_URL + guild_id
    )
    return api.json()

def world_api(world_id):
    api = requests.get(
        WORLDS_URL + world_id
    )
    return api.json()

def define_person(api_key):
    result = {}
    guild_list = []

    account = account_api(api_key)

    if 'name' in account.keys():
        world = world_api(str(account['world']))
        guilds = account['guilds']

        result['Account Name'] = account['name']
        result['Created'] = account['created']
        result['World'] = world['name']
        result['World ID'] = str(world['id'])

        for guild_id in guilds:
            guild = guild_api(guild_id)
            guild_list.append(guild['guild_name'] + " [" + guild['tag'] + "]")

        result['Guilds'] = ', '.join(guild_list)
    else:
        result['Error'] = 'Invalid key.'
    return result
