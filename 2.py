def vowel_constant(string):
     a = set(string)
     b = len(string) - len(set(string))
     for vowel in a:
         if vowel in 'aeiou':
             print(sorted(vowel),b)
     
vowel_constant("aabbccc")