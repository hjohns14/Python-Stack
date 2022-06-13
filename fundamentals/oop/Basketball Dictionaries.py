players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32, "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33, "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32, "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "Empty",
        "age": 16,
        "position": "Bench",
        "team": "Chilli's"
    }
]

kevin = {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    }
    
jason = {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    }

kyrie = {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    }

damian = {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    }

joel = {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
}





class Player:
    #Challenge 1
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]
    #Ninja Bonus
    @classmethod
    def get_team(cls, team_list):
        cls.team = [Player(p) for p in team_list]

# Challenge 2
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)
player_damian = Player(damian)
player_joel = Player(joel)

#Challenge 3
new_team = [Player(player) for player in players]
for item in new_team:
    print(item.name)

print("\n\nNinja Challenge \n")

#Testing Ninja bonus
Player.get_team(players)
for item in Player.team:
    print(item.name)


