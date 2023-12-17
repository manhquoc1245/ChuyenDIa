def addState(Towers, steps):
    state = []
    # Sorting
    for Tower in Towers:
        if Tower[0] == 'A':
            state.insert(0, Tower[1:])
        if Tower[0] == 'B':
            state.insert(1, Tower[1:])
        if Tower[0] == 'C':
            state.insert(2, Tower[1:])
    steps.append(state)
# Move a disc from f position to t position

def Algorithm(n, Tower1, Tower3, Tower2, Towers, steps):
    if n > 0:
        # Move n - 1 disks from source to auxiliary, so they are out of the way
        Algorithm(n - 1, Tower1, Tower2, Tower3, Towers, steps)
        # Move the nth disk from source to target
        Tower3.append(Tower1.pop())
        print("Chuyển từ", Tower1[0], "sang", Tower3[0])
        addState(Towers, steps)
        # Move the n - 1 disks that we left on auxiliary onto target
        Algorithm(n - 1, Tower2, Tower3, Tower1, Towers, steps)

if __name__ == "__main__":
    steps = []
    Tower1 = ['A', 4, 3, 2, 1]
    Tower2 = ['B']
    Tower3 = ['C']
    Towers = [Tower1, Tower2, Tower3]
    Algorithm(4, Tower1, Tower3, Tower2, steps)
    for step in steps:
        print(step)

