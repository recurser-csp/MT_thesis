def generae_algo(set, k): 
  
    n = len(set)  
    # dataset = open("dataset.txt","w")
    recursive_algo(set, "", n, k)
    # dataset.close()
# The main recursive method 
# to print all possible  
# strings of length k 
def recursive_algo(set, prefix, n, k): 
      
    # Base case: k is 0, 
    # print prefix 
    if (k == 0) : 
        # dataset.write("%s\n"% prefix)
        global stringsarr
        stringsarr.append(prefix)
        return
  
    # One by one add all characters  
    # from set and recursively  
    # call for k equals to k-1 
    for i in range(n): 
  
        # Next character of input added 
        newPrefix = prefix + set[i] +","
          
        # k is decreased, because  
        # we have added a new character 
        recursive_algo(set, newPrefix, n, k - 1)

stringsarr = []
char_list = ['1','2','3','4']
string_length = 50
generae_algo(char_list,string_length)
with open('../Data/10/dataset_'+str(string_length)+'.txt','w') as file:
	for item in stringsarr:
		file.write("%s0,\n"% item)


