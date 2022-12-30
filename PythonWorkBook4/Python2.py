row1 = [ "", " ", ""]
row2 = [ "", " ", ""]
row3 = [ "", " ", ""]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input(" Where do you Want to put the treasure?")

horizontal = int(position[0])
veritcal = int(position[1]) 


selected_row = map[veritcal -1]
selected_row[horizontal - 1] = "X"

print(map[veritcal -1 ]) 