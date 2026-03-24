student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
'''
student_scores = [180, 124, 165]

sum = 0
for score in student_scores:
    sum += score
    
print(sum)
'''

scores = [8, 65, 89, 86, 55, 91, 64, 89]
max = scores[0]
for score in scores:
    if score > max:
        max  = score
print(max)

min = scores[0]
for score in scores:
    if score < min:
        min = score
print(min)