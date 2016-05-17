#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
	
	system("date '+%D/%T' > web.txt");
	
	FILE *rtp;
	
	rtp =  fopen("./web.txt", "rt");
	char strTemp[255];
	
	
    char *pStr;
    
	if( rtp != NULL )
    {
        
		
		int i=0;
        while( !feof( rtp ) )
        {
            pStr = fgets( strTemp, sizeof(strTemp), rtp );
            printf( "%d %s", i, strTemp );
            i++;
        }
        fclose( rtp );
    }
    
   const char s[2] = "/:";
   char *token;
   
   token = strtok(strTemp, s);
   
   /* walk through other tokens */
   while( token != NULL ) 
   {
      printf( "strtok: %s\n", token );
    
      token = strtok(NULL, s);
   }
	
	return 0;
}
