#Definied friendships dictionary
friendships = {
    'A': ['B', 'C', 'J'],
    'D': ['E', 'F', 'G'],
    'H': ['I', 'K', 'V'],
    'J': ['V'],
    'K': ['L', 'M', 'N', 'A'],
    'O': ['P', 'V', 'U'],
    'Q': ['S', 'T', 'D'],
    'U': ['H', 'J'],
    'V': ['W', 'X', 'Y', 'Z']
}

def og_friends(candidate):
    # Person who have the given candidate as a friend
    friends_of_candidate = [key for key, val in friendships.items() if candidate in val]
    return friends_of_candidate

def friends_main(ip):
    #Initial friends of the candidate
    initial_friends = og_friends(ip)
    #Initialize the queue with the starting candidate and initial friends
    queue = [ip] + initial_friends
    #Keep track of contacted candidates
    contacted = set()
    #Order of contacted candidates
    contacted_list = []

    while queue:
        current = queue.pop(0)
        if current not in contacted:
            contacted.add(current)
            contacted_list.append(current)
            # Add current's friends to the queue
            if current in friendships:
                for friend in friendships[current]:
                    if friend not in contacted:
                        queue.append(friend)
    
    return contacted_list

if __name__ == "__main__":
    ip_candidate = 'D'
    contacted_candidates = friends_main(ip_candidate)
    print(contacted_candidates)
