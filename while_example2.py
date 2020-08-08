#Count By Check
#Suppose you want to count from some number start_num by \
# another number count_by until you hit a final number end_num, \
# and calculate break_num the way you did in the last quiz.

#Now in addition, address what would happen if someone gives a \
# start_num that is greater than end_num. If this is the case,\
#  set result to "Oops! Looks like your start value is greater\
#  than the end value. Please try again." Otherwise, set result\
#  to the value of break_num.



def test(start_num):
    end_num = 20
    count_by =1
    break_num = 1
    if start_num <= end_num:
        while start_num < end_num:
            break_num += count_by
            print(break_num)
            if break_num == end_num:
                break_num += count_by
                break
        print(break_num)
    else :
        result = 'Oops! Looks like your start value is greater than the end value. Please try again.'
        print(result)

test(21)
