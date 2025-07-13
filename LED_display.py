digits = [''' # 
 # 
 # 
 # 
 # 
''',
'''###
  #
###
#  
###
''',
'''###
  #
###
  #
###
''',
'''# #
# #
###
  #
  #
''',
'''###
#  
###
  #
###
''',
'''###
#  
###
# #
###
''',
'''###
  #
  #
  #
  #
''',
'''###
# #
###
# #
###
''',
'''###
# #
###
  #
###
''',
'''###
# #
# #
# #
###
'''
          ]

def display(num):
  num = str(num)
  res = ''
  seg1, seg2, seg3, seg4, seg5 = '', '', '', '', ''

  for i in range(len(num)):
    seg1 += digits[int(num[i]) - 1][:3] + ' '
    seg2 += digits[int(num[i]) - 1][4:7] + ' '
    seg3 += digits[int(num[i]) - 1][8:11] + ' '
    seg4 += digits[int(num[i]) - 1][12:15] + ' '
    seg5 += digits[int(num[i]) - 1][16:19] + ' '

  segs = [seg1, seg2, seg3, seg4, seg5]
  for i in range(len(segs)):
    res += segs[i] + '\n'

  return res

# print(display(9081726354))
# print(display(8675309))
try:
  number = int(input("Choose the number you want to display: "))
except ValueError:
  print("Enter digits only")
  quit()

print()
print(display(number))
