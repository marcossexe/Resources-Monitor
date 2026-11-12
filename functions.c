#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


char* display_memory(void){
	FILE *fp;

	fp =  fopen("/proc/meminfo", "rw");
	if(fp == NULL){
		printf("Error");
		char *erp =NULL;
		return erp;
			}
	char buffer[1024];
	char *bfp  = buffer; 
 
	int line_max = 2;
	for (int i = 0 ; i< line_max; i++ ) {
		fgets(buffer, sizeof(buffer), fp);
	
}





fclose(fp);
return bfp;

	}

double display_cpu_usage(){
	FILE *fp;
	fp = fopen("/proc/stat", "r");
	if(fp ==NULL){
		printf("Error");
		return 1;
		}
	int long long user, nice, system, idle, iowait, irq, softirq, steal,
	guest, guest_nice;
	char not_useful[4];
 	long long gsum = 0;
 	long long acsum = 0;
	for (int i =0; i<1;i++ ){
		fscanf(fp,"%s %lld %lld %lld %lld %lld %lld %lld" 
		"%lld %lld %lld", &not_useful[0], &user, &nice,

		&system, &idle, &iowait, &irq, &softirq, &steal,
 		&guest, &guest_nice );
		}
	gsum =  user+ nice+ system +idle+ iowait+ irq +softirq +steal; 
	acsum = user + nice + system + irq + softirq + steal;
	
	fclose(fp);
	sleep(1);
	FILE *fp2;
 	long long gsum2 = 0;
 	long long acsum2 = 0;
	fp2 = fopen("/proc/stat", "r");
	if(fp2 ==NULL){
		printf("Error");
		return 1;
		}
	for (int i =0; i<1;i++ ){
		fscanf(fp2,"%s %lld %lld %lld %lld %lld %lld %lld "
		"%lld %lld %lld", &not_useful[0], &user, &nice,
		&system, &idle, &iowait, &irq, &softirq, &steal,
		 &guest, &guest_nice );
		}
	gsum2 =  user+ nice+ system +idle+ iowait+ irq +softirq +steal;
	acsum2 = user + nice + system + irq + softirq + steal;
	int test1 = (double) acsum2 - (double)acsum;
	double  result = ((double)((double)acsum2 -(double) acsum)/ ((double)gsum2 -(double) gsum)) * 100; 

	fclose(fp2);
	sleep(1);
	return result;
	}

int display_cpu_temp(){
	FILE * fp;
	int temp;
	fpt = fopen("/sys/devices/virtual/thermal/thermal_zone8/temp", "r");
	if(fp == NULL){
		printf("error");
		return -1;	}
	fscanf(fp,"%d",&temp );
	fclose(fp);
	return temp;
	
}
