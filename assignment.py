# Define the friendships as a dictionary
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

def friends(ip):
    og_friends = [k for k, v in friendships.items() if ip in v]
    return og_friends

def find(ip):
    og_friends = friends(ip)
    stack = [ip] + og_friends
    contacted = set()
    ans = []

    while stack:
        ch = stack.pop()
        if ch not in contacted:
            contacted.add(ch)
            ans.append(ch)
            # Add current's friends to the stack
            if ch in friendships:
                for friend in friendships[ch]:
                    if friend not in contacted:
                        stack.append(friend)
    
    return ans

ip = 'M'
candidates_contacted = find(ip)
print(" ".join(candidates_contacted))

