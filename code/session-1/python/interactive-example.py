low = 0
high = int(input())
state = "initial"
while state != "correct":
    mid = (high+low)//2
    _, state = print(mid, flush=True), input().strip()
    if state == "higher":
        low = mid+1
    if state == "lower":
        high = mid - 1
