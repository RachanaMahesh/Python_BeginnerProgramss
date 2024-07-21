def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    stuart_score = kevin_score = 0
    n=len(string)
    for i in range(n):
        if string[i] in vowels:
            kevin_score+=(n-i)
        else:
            stuart_score+=(n-i)
    if kevin_score>stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)




# def minion_game(string):
#     vowels="AEIOU"
#     stuart_score=0
#     kevin_score=0
#     arr_set = set()
#     n=len(string)
#     for start in range(n):
#         for end in range(start+1,n+1):
#                 arr_set.add(string[start:end])
#     for s in arr_set:
#         if s[0] in vowels:
#             print((s,string.count(s)))
#             kevin_score+=string.count(s)
#         else:
#             stuart_score+=string.count(s)
#     print(arr_set)
#     print(kevin_score)
#     print(stuart_score)
#     # for i in range(n):
#     #     if string[i] not in vowels:
#     #         start=i
#     #         for end in range(start+1,n+1):
#     #             print(string[start:end])
#     #         break
#
#
#
#
#
#
# if __name__ == '__main__':
#     s = input()
#     minion_game(s)
#
