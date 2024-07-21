#  PROGRAM TO PRINT ALPHABET RANGOLI
# def print_rangoli(size):
    # your code goes here
#     alphabet=[chr(i) for i in range(97,123)][:size]
#     alphabet.reverse()
#     w=size+(size-1)
#     w+=(w-1)
#
#     for i in range(size):
#         alphabet_to_print=alphabet[:i+1]
#         alphabet_to_print+=alphabet_to_print[:-1][::-1]
#         print(("-".join(alphabet_to_print)).center(w,'-'))
#     for i in range(size-1):
#         alphabet_to_print=alphabet[:i+1]
#         alphabet_to_print=alphabet[:size-i-1]
#         alphabet_to_print+=alphabet_to_print[:-1][::-1]
#         print(("-".join(alphabet_to_print).center(w,'-')))
#
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)




thickness=int(input("Enter the input:"))
c='H'
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
for i in range (thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


#---------------
#s=input().split(" ")
# m=int(s[1])
# n=int(s[0])
#
# c='.|.'
# for i in range(1,n,2):
#     print((c*i).center(m,'-'))
# print("WELCOME".center(m,"-"))
# for i in range(1,n,2):
#     print((c*(n-i-1)).center(m,'-'))