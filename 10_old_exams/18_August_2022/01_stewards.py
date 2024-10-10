from collections import deque

seats = input().split(', ')
first_sequence = deque(int(x) for x in input().split(', '))
second_sequence = deque(int(x) for x in input().split(', '))

rotations = 0
taken_seats = []
while True:
    if len(taken_seats) == 3:
        break
    elif rotations == 10:
        break

    firs_number = first_sequence.popleft()
    second_number = second_sequence.pop()
    sum_ = firs_number + second_number
    ascii_ch = chr(sum_)

    firs_seat_num = str(firs_number) + ascii_ch
    second_seat_num = str(second_number) + ascii_ch

    if firs_seat_num in seats:
        taken_seats.append(firs_seat_num)
        seats.remove(firs_seat_num)
    elif second_seat_num in seats:
        taken_seats.append(second_seat_num)
        seats.remove(second_seat_num)
    elif firs_seat_num in taken_seats or second_seat_num in taken_seats:
        rotations += 1
        continue
    else:
        first_sequence.append(firs_number)
        second_sequence.appendleft(second_number)
    rotations += 1
print(f"Seat matches: {', '.join(taken_seats)}")
print(f'Rotations count: {rotations}')
