def team_weights(weights):
    team1 = sum(weights[::2])
    
    team2 = sum(weights[1::2])
    return (team1, team2)


if __name__ == '__main__':
    user_input = input("Введите веса людей через пробел: ")
    
    if user_input.strip() == "":
        weights_list = []
    else:
        weights_list = [int(x) for x in user_input.split()]
        
    ans = team_weights(weights_list)
    print(f"Вес команд: {ans}")
