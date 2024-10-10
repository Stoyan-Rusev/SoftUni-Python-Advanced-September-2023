from collections import deque

portions = deque(int(x) for x in input().split(', '))
stamina = deque(int(x) for x in input().split(', '))

peaks_to_climb = deque([('Vihren', 80), ('Kutelo', 90),
                        ('Banski Suhodol', 100), ('Polezhan', 60),
                        ('Kamenitza', 70)])
climbed_peaks = []

while portions and stamina and peaks_to_climb:
    last_portion = portions.pop()
    first_stamina = stamina.popleft()
    sum_ = last_portion + first_stamina

    current_info = peaks_to_climb.popleft()
    current_peak_name = current_info[0]
    current_peak_value = current_info[1]
    if sum_ >= current_peak_value:
        climbed_peaks.append(current_peak_name)
    else:
        peaks_to_climb.appendleft(current_info)

if not peaks_to_climb:
    print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')
if climbed_peaks:
    print('Conquered peaks:')
    for peak in climbed_peaks:
        print(peak)
