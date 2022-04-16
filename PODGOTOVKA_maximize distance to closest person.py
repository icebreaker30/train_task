prev_seat = None
dist = float("-inf")

for indx in range (len(seats)):
    if seats[indx] == 1:
        if prev_seat == None:
            dist = indx
        else:
            dist = max(dist, (indx - prev_seat))
dist max(dist, len(seats) - 1 - prev_seat)
return dist