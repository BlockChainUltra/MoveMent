#Begin with a list for our movement track for simplicity

MoveMentTrack = [['Sydney']] #initialize the track with place of birth

def add_movement():
    """Adds movements to our track. At first only locations.
    Also adds the previous element to the next element."""
    MoveMentTrack.append([MoveMentTrack[-1], 'Korea'])
    print(MoveMentTrack)

add_movement()
add_movement()
add_movement()