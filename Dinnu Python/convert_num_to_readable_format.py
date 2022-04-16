def get_in_words(number):
    num_in_word = []
    for i in number:
        if i == "1":
            num_in_word.append("one")
        elif i == "2":
            num_in_word.append("two")
        elif i == "3":
            num_in_word.append("three")
        elif i == "4":
            num_in_word.append("four")
        elif i == "5":
            num_in_word.append("five")
        elif i == "6":
            num_in_word.append("six")
        elif i == "7":
            num_in_word.append("seven")
        elif i == "8":
            num_in_word.append("eight")
        elif i == "9":
            num_in_word.append("nine")
        elif i == "0":
            num_in_word.append("zero")
    return (num_in_word)
    

def starting_four_set(item):
    seq = []
    i = 0
    while i < 4:
        num = item[i]
        s = []
        for j in range(i+1,4):
            if num == item[j]:
                s.append(1)
            else:
                break
        if len(s) == 0:
            seq.append(num)
            i += 1
        elif len(s) == 1:
            seq.append("double " + num)
            i += 2
        elif len(s) == 2:
            seq.append("tripple " + num)
            i += 3
        elif len(s) == 3:
            seq.append("quadruple " + num)
            i += 4
        # print(seq)
    return (seq)

def next_three(item):
    seq = []
    i = 0
    while i < 3:
        num = item[i]
        s = []
        for j in range(i+1,3):
            if num == item[j]:
                s.append(1)
            else:
                break
        if len(s) == 0:
            seq.append(num)
            i += 1
        elif len(s) == 1:
            seq.append("double " + num)
            i += 2
        elif len(s) == 2:
            seq.append("tripple " + num)
            i += 3
    return (seq)


#Input 
n = input("Enter a 10 digit number : ")

f_four = n[:4]
s_three = n[4:7]
t_three = n[7:11]
# print(f_four,s_three,t_three)

first_four = get_in_words(f_four)
second_three = get_in_words(s_three)
third_three = get_in_words(t_three)
# print(first_four,second_three,third_three)

ff = starting_four_set(first_four)
ss = next_three(second_three)
tt = next_three(third_three)

print(*ff,*ss,*tt)