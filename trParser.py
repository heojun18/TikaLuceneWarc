# TREC Query Parser

def percentage(part, whole):
    return 100 * float(part)/float(whole)

f = open('../TREC/05.efficiency_topics','r')
wf11 = open('./trec_query_highterm.txt','w')
wf21 = open('./trec_query_andhighhigh.txt','w')
wf31 = open('./trec_query_orhighhigh.txt','w')
wf41 = open('./trec_query_highphrase.txt','w')

#wf12 = open('./trec_query_lowterm.txt','w')
#wf22 = open('./trec_query_andhighlow.txt','w')
#wf32 = open('./trec_query_orhighlow.txt','w')
#wf42 = open('./trec_query_lowphrase.txt','w')

lines = f.readlines()
c2 = c3 = c4 = c5 = c6 = 0
tmp_query1 = "nop"
tmp_query2 = "nop"
tmp_query3 = "nop"

for line in lines:
    tmp1 = line.replace(":", " ")
    tmp2 = tmp1.split(" ")
    #print(len(tmp2))
    print(tmp2)
    if len(tmp2) == 2: #print("Single Term query")
        tmp_query1 = "HighTerm: " + tmp2[1] 
        wf11.write(tmp_query1)
        c2 = c2 + 1
    elif len(tmp2) == 3: #print("AND/OR query")
        tmp_query1 = "AndHighHigh: " + "+" + tmp2[1] + " +" + tmp2[2] 
        tmp_query2 = "OrHighHigh: " + "+" + tmp2[1] + " +" + tmp2[2] 
        wf21.write(tmp_query1)
        wf31.write(tmp_query2)
        c3 = c3 + 1
    elif len(tmp2) == 4: #print("Phrase query (3 term)")
        tmp_query1 = "AndHighHigh: " + "+" + tmp2[1] + " +" + tmp2[2] + " + " + tmp2[3]
        tmp_query2 = "OrHighHigh: " + "+" + tmp2[1] + " +" + tmp2[2] + " + " + tmp2[3]
        tmp_query3 = "HighPhrase: " + "\"" + tmp2[1] + " " + tmp2[2] + " " + tmp2[3].rstrip("\n") + "\"\n"
        wf21.write(tmp_query1)
        wf31.write(tmp_query2)
        wf41.write(tmp_query3)
        c4 = c4 + 1
    elif len(tmp2) == 5: #print("Phrase query (4 term)")
        tmp_query1 = "AndHighHigh: " + "+" + tmp2[1] + " +" + tmp2[2] + " + " + tmp2[3] + " +" + tmp2[4]
        tmp_query2 = "OrHighHigh: " + "+" + tmp2[1] + " +" + tmp2[2] + " + " + tmp2[3] + " +" + tmp2[4]
        tmp_query3 = "HighPhrase: " + "\"" + tmp2[1] + " " + tmp2[2] + " " + tmp2[3] + " " + tmp2[4].rstrip("\n") + "\"\n"
        wf21.write(tmp_query1)
        wf31.write(tmp_query2)
        wf41.write(tmp_query3)
        c5 = c5 + 1
    elif len(tmp2) >= 6: #print("Phrase query (many terms)")
        tmp_query1 = "nop" 
        tmp_query2 = "nop" 
        c6 = c6 + 1

    #if tmp_query1 != "nop":
    #    wf.write(tmp_query1)
    #if tmp_query2 != "nop":
    #    wf.write(tmp_query2)

cSum = c2 + c3 + c4 + c5 + c6
#print(c2 , " / " , c3 , " / " , c4 , " / " , c5 , " / " , c6)
print(percentage(c2,cSum) , " / " ,
        percentage(c3,cSum) , " / " , 
        percentage(c4,cSum) , " / " , 
        percentage(c5,cSum) , " / " , 
        percentage(c6,cSum))

f.close()
wf11.close()
wf21.close()
wf31.close()
wf41.close()
