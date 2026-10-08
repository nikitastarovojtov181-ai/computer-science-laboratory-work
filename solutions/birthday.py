import random

def birthday_probability(people):
    if people > 365:
        return 1.0
    
    p = 1.0
    for i in range(people):
        p *= (365 - i) / 365
        
    return 1 - p

def simulate_birthday(people, trials):
    matches = 0
    
    for _ in range(trials):
        days = []
        for _ in range(people):
            days.append(random.randint(1, 365))
            
        if len(set(days)) < people:
            matches += 1
            
    return matches / trials

if __name__ == '__main__':
    print(birthday_probability(1))
    print(birthday_probability(23))
    print(birthday_probability(50))
    print(birthday_probability(366))
    
    print(simulate_birthday(23, 100000))
