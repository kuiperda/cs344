from gps import gps

problem = {
    "start1": ["own a house", "plenty of room for nerf battle"],
    "finish1": ["own a house", "had an EPIC nerf battle"],

    "ops": [
        {
            "action": "set up furniture for bases",
            "preconds": [
                "own a house",
                "plenty of room for nerf battle",
            ],
            "add": [
                "furniture set up",
            ],
            "delete": [
                "plenty of room for nerf battle"
            ]
        },
                {
            "action": "add incendiary grenades for EPIC battle",
            "preconds": [
                "own a house",
                "furniture set up",
            ],
            "add": [
                "ready to blow"
            ],
            "delete": [
            ]
        },
                {
            "action": "invite people and have a blast",
            "preconds": [
                "own a house",
                "ready to blow",
            ],
            "add": [
                "had an EPIC nerf battle",
            ],
            "delete": [
                "own a house"
            ]
        },
                {
            "action": "invite people to a tame nerf battle",
            "preconds": [
                "own a house",
                "furniture set up",
            ],
            "add": [
                "had an EPIC nerf battle",
            ],
            "delete": [
                "furniture set up"
            ]
        },
            ]
        }
#
def main():
    start = problem['start1']
    finish = problem['finish1']
    ops = problem['ops']
    actionSequence = gps(start, finish, ops)
    if actionSequence is None:
        print("plan failure...")
        return
    for action in actionSequence:
        print(action)

if __name__ == '__main__':
    main()
