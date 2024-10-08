def positives_sum():
    positives = [num for num in numbers if num > 0]
    sum_pos = sum(positives)
    return sum_pos


def negative_sum():
    negatives = [num for num in numbers if num < 0]
    sum_neg = sum(negatives)
    return sum_neg


numbers = [int(x) for x in input().split()]
sum_of_positives = positives_sum()
sum_of_negatives = negative_sum()

print(sum_of_negatives)
print(sum_of_positives)
if abs(sum_of_negatives) > sum_of_positives:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')
