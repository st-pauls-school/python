


s = "ab .,cd.ef,gh"
for c in s: 
	if not (ord('a') <= ord(c) <= ord('z')):
		s = s.replace(c, "")




print(s)