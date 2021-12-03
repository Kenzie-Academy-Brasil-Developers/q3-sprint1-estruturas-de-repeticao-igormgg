####### FUNÇÃO 1 #######
def corresponding_parenthesis(text):
    open_par_list = []
    close_par_list = []
    output = ''

    for char in text:
        if char == ')':
            close_par_list.append(char)
        if char == '(':
            open_par_list.append(char)

    if len(open_par_list) > len(close_par_list):
        for i in range(len(open_par_list) - len(close_par_list)):
            output += open_par_list[i]
    if len(open_par_list) < len(close_par_list):
        for i in range(len(close_par_list) - len(open_par_list)):
            output += close_par_list[i]

    return output


####### FUNÇÃO 2 #######
def remove_more_than_two_repetitions(text):
    output = ''

    for i in range(len(text)):
        try:
            if text[i] == text[i+1] == text[i+2]:
                continue
            else:
                output += text[i]
        except:
            output += text[i]
    
    return output