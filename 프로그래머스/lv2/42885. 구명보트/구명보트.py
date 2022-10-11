def solution(people, limit):
    people.sort(reverse = True)
    lens = len(people)
    answer = 0
    s, f = 0, lens -1
    while(s <= f):
        if people[s] + people[f] <= limit:
            s += 1
            f -= 1
        else:
            s += 1
        
        answer += 1

    return answer