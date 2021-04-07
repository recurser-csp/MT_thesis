def generae_algo(set, k): 
  
    n = len(set)  
    # dataset = open("dataset.txt","w")
    recursive_algo(set, "", n, k)
    # dataset.close()

def recursive_algo(set, prefix, n, k): 
      
 
    # print prefix 
    if (k == 0) : 
        # dataset.write("%s\n"% prefix)
        global stringsarr
        stringsarr.append(prefix)
        return

    for i in range(n): 
  
        newPrefix = prefix + set[i] 

        recursive_algo(set, newPrefix, n, k - 1)

stringsarr = []
char_list = ['a','b','c','d']
string_length = 14
generae_algo(char_list,string_length)
with open('./dataset_'+str(string_length)+'.txt','w') as file:
	for item in stringsarr:
		file.write("%s\n"% item)


