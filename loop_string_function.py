# Given a non-empty string like code returns a string like "CCoCodCode"
# string_splosion('Code') --> 'CCoCodCode'
# string_splosion('abc') --> 'aababc'
# string_splosion('ab') --> 'aab'

def string_splosion(str):
  out_str = ""
  n = len(str) # 4,   0,1,2,3,
  for i in range(n):
  out_str = out_str + str[:i=1]
return out_str
