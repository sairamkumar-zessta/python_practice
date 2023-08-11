#find given word is end of first word or not

first_word = input("Enter First Word:")
second_word = input("Enter Second Word:")
print(first_word[-len(second_word):] == second_word)

'''
Blackhole
hole
(True)
'''


'''
boomerang
boom
(False)
'''