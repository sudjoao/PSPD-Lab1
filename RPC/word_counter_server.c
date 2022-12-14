/*
 * This is sample code generated by rpcgen.
 * These are only templates and you can use them
 * as a guideline for developing your own functions.
 */

#include "word_counter.h"
#include <string.h>
#include <stdio.h>

int countOccurrences(char * str, char * toSearch); 
int countWords(char * str); 

result *
count_word_100_svc(params *argp, struct svc_req *rqstp)
{
	static result  res;
	printf("SERVER WORKING\n"); 
    res.count = countWords(argp->data.data_val); 
	res.occurrences = countOccurrences(argp->data.data_val, argp->word.word_val); 
	return &res; 
}


int countWords(char * str) {
	int count = 1;
        int i = 0; 	
	int stringLen = strlen(str);

	 while(str[i]!='\0'){
        	/* check whether the current character is white space or new line or tab character*/
        	if(str[i]==' ' || str[i]=='\n' || str[i]=='\t'){
            		count++;
        	}

        	i++;
    	}
	
	 return count; 
}

int countOccurrences(char * str, char * toSearch){
    int i, j, found, count;
    int stringLen, searchLen;

    stringLen = strlen(str);      // length of string
    searchLen = strlen(toSearch); // length of word to be searched

    count = 0;

    for(i=0; i <= stringLen-searchLen; i++)
    {
        /* Match word with string */
        found = 1;
        for(j=0; j<searchLen; j++)
        {
            if(str[i + j] != toSearch[j])
            {
                found = 0;
                break;
            }
        }

        if(found == 1)
        {
            count++;
        }
    }

    return count;
}
