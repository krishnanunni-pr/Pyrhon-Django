# re- regular pattern matching

# 1 x='[abc]' either a b or c
# 2 x='[^abc]' except abc
# 3 x='[a-z]' a to z
# 4 x='[A-Z]' A to Z
# 5 x='[a-zA-Z]' both lower and upper case are checked
# 6 x='[0-9]' check digits
# 7 x='[^a-zA-Z0-9]' special symbols
# 8 x='\s' check space
# 9 x='\d' check the digits
# 10 x='\D' except digits
# 11 x='\w' all words except special characters
# 12 x='\W' for special characters

# quantifiers
# 1 x='a+' a including group
# 2 x='a*' count including zero number of a
# 3 x='a?' count a as each including zero no of a
# 4 x='a{2}' 2 no of a position
# 5 x='a{2,3}' minimum 2 a and maximum 3 a
# 6 x='^a' check starting with a
# 7 x='a$' check ending with a