student_score=[150,130,100,250,350,450,600,300]
# total=sum(student_score)
# print(total)
sum=0
for score in student_score:
    sum+=score
print(sum)       

# print(max(student_score))
#max functionality
max=0
for maxi in student_score:
    if(maxi>max):
        max=maxi
print(max)