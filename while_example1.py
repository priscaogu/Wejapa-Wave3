#Count By




start_num =1 
end_num = 20
count_by = 1 

#setting the break_num 
#comparing count_by and end_num
break_num = 1
while start_num < end_num:
	break_num += count_by
	print(break_num)
	if break_num == end_num:
    		
    		break_num += count_by
    		break
print(break_num)