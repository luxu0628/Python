scores={'Alice':85,'Bob':58,"Chris":92,'David':45}
dict={x:y for x,y in scores.items() if y>=60}
print(list(dict.items()))