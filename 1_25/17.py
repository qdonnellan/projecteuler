# If the numbers 1 to 5 are written out in words: 
#one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 
# letters used in total.

# If all the numbers from 1 to 1000 (one thousand)
# inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 
# (three hundred and forty-two) contains 23 letters and 115 
# (one hundred and fifteen) contains 20 letters. The use of "and" 
# when writing out numbers is in compliance with British usage.

tens = {'2':'twen', '3':'thir', '4':'for', '5':'fif', '6':'six', '7':'seven', '8':'eigh', '9':'nine'}
ones = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
special = {'10':'ten','11':'eleven', '12':'twelve'}


def num_word(n):
  s = ''
  if n > 999:
    s += ones[str(n)[-4]] + 'thousand'

  if n > 99:
    if str(n)[-3] != '0':
      s += ones[str(n)[-3]] + 'hundred'

    if str(n)[-2:] != '00':
      s += 'and'

  if n > 9:
    n = str(n)
    if n[-2] == '0':
      if n[-1] != '0':
        s += ones[n[-1]]
    elif n[-2:] in ['10','11', '12']:
      s += special[n[-2:]]
    elif n[-2] == '1':
      if n[-1] == '4':
        s += 'fourteen'
      else:
        s += tens[n[-1]] + 'teen'
    else:
      s += tens[n[-2]] + 'ty'
      if n[-1] != '0':
        s += ones[n[-1]]
  else:
    n = str(n)
    s += ones[n[-1]]

  return s

string = ''
for i in range(1,1001):
  string += num_word(i)

print len(string)




