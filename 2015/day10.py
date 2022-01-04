# input_string = '1321131112'
# output_string = ''
# for index in range(50):
#     current_char = input_string[0]
#     current_count = 0
#     for i in input_string:
#         if i == current_char:
#             current_count = current_count + 1
#         else:
#             output_string = output_string + str(current_count) + str(current_char)
#             current_char = i
#             current_count = 1
#         # print(f'"{i}"     {current_count}')
#     input_string = output_string + str(current_count) + str(current_char)
#     output_string = ''
#     print(f'output {index + 1}: {len(input_string)}')












# def string_split(string):
#     arr = []
#     current_char = string[0]
#     count = 0
#     for s in string:
#         if s == current_char: count = count + 1
#         else:
#             arr.append(current_char * count)
#             current_char = s
#             count = 1
#     arr.append(current_char * count)
#     return arr


# # input_string = '1321131112'

# input_string = '1321131112'
# output_string = ''
# for index in range(50):
#     res = string_split(input_string)

#     for chunk in res:
#         output_string = output_string + str(len(chunk)) + chunk[0]
#     input_string = output_string
#     output_string = ''
#     print(f'output {index}: {len(input_string)}')






def string_split2(string):
    arr = []
    current_char = string[0]
    count = 0
    for s in string:
        if s == current_char: count = count + 1
        else:
            arr.append(str(count) + current_char)
            current_char = s
            count = 1
    arr.append(str(count) + current_char)
    return arr

input_string = '1321131112'
for index in range(50):
    res = ''.join(string_split2(input_string))
    print(f"output {index + 1}: {len(res)}")
    input_string = res