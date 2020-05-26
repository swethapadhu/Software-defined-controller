import os 
import time                                                                                                                                       
          
threshold = 75.0
avg_cpu = 0.0
control_flag = 0
mem = 32768  
vcores = 16
onekb = 1024                                                                                                                                      

tempptr = open("output.txt","w")                                                                                                                  
tempptr.close()                                                                                                                                   

while(True):                                                                                                                                      
        text=""
        f=os.popen("sar -u -d -q -r -w -n DEV 1 1")                                                                                               
        temp=f.read()                                                                                                                             
        fptr=open("sar_log.txt", "w")
        outptr=open("output.txt","a")                                                                                                             
        fptr.write(temp)                                                                                                                          
        fptr.close()                                                                                                                              
        f=os.popen("awk 'FNR == 1 {print $4} FNR == 4 {print $1,$2}' ORS=' ' sar_log.txt")                                                        
        temp=f.read()                                                                                                                             
        text+=temp                                                                                                                                
        f=os.popen("awk 'FNR == 1 {print $3}' ORS=' ' sar_log.txt")                                                                               
        temp=f.read()                                                                                                                             
        text+=temp+"NODEINFO "                                                                                                                    
                                                                                                                                                  
        f=os.popen("awk 'FNR == 4 {print $4+$5+$6+$8;} FNR == 4 {print $7,$9} FNR == 7 {print $4} FNR ==  16 {print $4}' ORS=' ' sar_log.txt")    
        temp=f.read()                                                                                                                             
        avg_cpu = (avg_cpu + float(temp.split(' ')[0]))/2                                                                                         
        text+=temp                                                                                                                                
        f=os.popen("awk 'FNR == 10 {print $3+$4,$4,$5} FNR == 13 {print $3,$8} FNR == 16 {print $11} FNR  == 19 {print $11}' ORS=' ' sar_log.txt")
        temp=f.read()                                                                                                                             
        text+=temp+"\n"                                                                                                                           
        f=os.popen("awk 'FNR == 1 {print $4} FNR == 4 {print $1,$2}' ORS=' ' sar_log.txt")                                                        
        temp=f.read()          
	text+=temp+"TASKINFO "                                                                                                                    
        f=os.popen("ps -w aux | grep org.apache.hadoop | awk '{sum1+=$3} {sum2+=$4} END {print sum1/4,su m2/4}'")                                 
        temp=f.read()                                                                                                                             
        text+=temp                                                                                                                                
        f=os.popen("jps -l | grep YarnChild | wc -l")                                                                                             
        Yarn=f.read()                                                                                                                             
        f=os.popen("jps -l | grep MRAppMaster | wc -l")                                                                                           
        AM=f.read()                                                                                                                               
        text+=str(int(Yarn)+2*int(AM))+" "+AM+Yarn                                                                                                
        outptr.write(text)                                                                                                                        
        outptr.close()                                                                                                                            
        if control_flag==100:                                                                                                                     
                control_flag=0                                                                                                                    
        if control_flag%2==0:                                                                                                                     
                if avg_cpu<threshold:                                                                                                             
                        mem = max(20480, mem - onekb)                                                                                             
                        vcores = max(8, vcores - 1)                                                                                               
                        bashc="yarn rmadmin -updateNodeResource ms0945.utah.cloudlab.us:46258 " + str(mem) + " " + str(vcores)
			os.system(bashc)                                                                                                          
                        print avg_cpu, "below"                                                                                                    
                else:                                                                                                                             
                        mem = mem + onekb                                                                                                         
                        vcores = vcores + 1                                                                                                       
                        bashc="yarn rmadmin -updateNodeResource ms0945.utah.cloudlab.us:46258 " + str(mem) + " " + str(vcores)                    
                        os.system(bashc)                                                                                                          
                        print avg_cpu, "above"                                                                                                    
                avg_cpu=0.0                                                                                                                       
        control_flag+=1                                                                                                                           
        time.sleep(1)            
