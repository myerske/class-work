str = 'X-DSPAM-Confidence:0.8475'
colonpos = str.find(':')
print(colonpos)
endpos = str.find('5',colonpos)
print(endpos)
answer = str[colonpos+1:endpos+1]
print(answer)
answer = float(answer)
print(answer)