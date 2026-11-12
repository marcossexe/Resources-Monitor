#include <stdio.h>
#include <dirent.h>
#include <string.h>

int count_proc(){
	DIR *diretorio;
	struct dirent *processos;
	int count =0;
	diretorio = opendir("/proc/");
	while((processos = readdir(diretorio)) != NULL){
	if ((processos ->d_name[0]) < '9' && (processos->d_name[0]) > '0' ){
		count++;
		}
	}
	printf("%d \n", count);
	return count;

}
int count_active_proc(){
DIR *diretorio;
        struct dirent *processos;
        int count =0;
        diretorio = opendir("/proc/");
        while((processos = readdir(diretorio)) != NULL){
        if ((processos ->d_name[0]) <= '9' && (processos->d_name[0]) > '0' ){
                
		FILE * fp;
		char *line = NULL;
		size_t buffer =0;
		int line_v;
		DIR *subdiretorio;
		char sub_name[64];
		int i =0;
		while((processos ->d_name[i]) != '\0' ){
			sub_name[i]= processos ->d_name[i];
			i++; 	}
		sub_name[i] = '\0';
		
		char proc_dir[64] = "/proc/";		
		strcat(proc_dir, sub_name);
		
		subdiretorio = opendir(proc_dir);
		char stat[10]="/status";
		strcat(proc_dir, stat);  
		
		fp = fopen(proc_dir, "r");
		for(int j =0; j<3; j++){
		line_v = getline(&line, &buffer, fp );
		if(j ==2){
			if (line[7] == 'I' || line[7] == 'R'){
				count++;}
			}
		
        	}
        }
}

printf("%d \n", count);
return count;


}
