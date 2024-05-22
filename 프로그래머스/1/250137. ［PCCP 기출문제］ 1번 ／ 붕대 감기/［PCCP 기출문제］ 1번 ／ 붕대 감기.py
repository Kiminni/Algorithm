def solution(bandage, health, attacks):
    con = 0
    max_health = health
    for i in range(attacks[-1][0] + 1):
        
        if i == attacks[0][0]:
            health -= attacks[0][1]
            attacks.remove(attacks[0])
            con = 0
            if health <= 0 :
                return -1

        elif health == max_health:
            con += 1
        
        elif health < max_health:
            health += bandage[1]
            con += 1
            if health >= max_health:
                health = min(health, max_health)
            
        if con == bandage[0]:
            health += bandage[2]

            if health >= max_health:
                health = min(health, max_health)
            con = 0
        print(health, con, i)
    return health
        
