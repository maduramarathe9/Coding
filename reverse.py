word = raw_input("Please enter any word that you wish  to reverse")

rev_word = []

for i in range(len(word)):
    rev_word.append(word[len(word)-i-1])
 
print "The reverse of %s is %s" %(word,"".join(rev_word))











