# 2. You have a list of your favourite marvel super heroes
# heroes=['spider man','thor','hulk','iron man','captain america']
# Using this list find:
#  1. Length of the list
#  2. Add 'black panther' at the end of this list
#  3. You realize that you need to add 'black panther' after 'hulk',
#     so remove it from the list first and then add it after 'hulk'
#  4. Now you don't like thor and hulk because they get angry easily :)
#     So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#     Do that with one line of code.
#  5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

Heroes=['Spiderman','Thor','Hulk','Ironman','Captain America']
# 1. Length of the list
print(len(Heroes))
# 2. Add 'black panther' at the end of the list
Heroes.append('Black Panther')
print(Heroes)
# 3.
Heroes.remove('Black Panther')
Heroes.insert(3, 'Black Panther')
print(Heroes)
# 4.
Heroes[1:3] = ['Doctor Strange']
print(Heroes)
# 5.
Heroes.sort()
print(Heroes)
