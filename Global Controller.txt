import os                                                                                                                                         
                                                                                                                                                  
threshold = 75.0                                                                                                                                  
while True:                                                                                                                                       
        slave1 = open("slave1_output.txt","r")                                                                                                    
        slave2 = open("slave2_output.txt","r")                                                                                                    
                                                                                                                                                  
        slave1_lines = slave1.readlines()                                                                                                         
        slave2_lines = slave2.readlines()                                                                                                         
                                                                                                                                                  
        avg_cpu_s1 = 0.0                                                                                                                          
        avg_cpu_s2 = 0.0            
	                                                                                                                                          
        for lines in slave1_lines:                                                                                                                
                if "NODEINFO" in lines:                                                                                                           
                        idx=lines.find("NODEINFO")                                                                                                
                        avg_cpu_s1 = (avg_cpu_s1 + float(lines[idx+9:idx+14].split(' ')[0]))/2                                                    
                                                                                                                                                  
        for lines in slave2_lines:
                if "NODEINFO" in lines:                                                                                                           
                        idx=lines.find("NODEINFO")                                                                                                
                        avg_cpu_s2 = (avg_cpu_s2 + float(lines[idx+9:idx+14].split(' ')[0]))/2                                                    
                                                                                                                                                  
        avg_cpu = (avg_cpu_s1 + avg_cpu_s1)/2                                                                                                     
                                                                                                                                                  
        xml = open("/home/hadoop/hadoop/etc/hadoop/capacity-scheduler.xml","r")                                                                   
        temp_xml = open("temp.xml","w")                                                                                                           
        xml_lines=xml.readlines()                                                                                                                 
        flag=False                                                                                                                                
        for lines in xml_lines:                                                                                                                   
                if "yarn.scheduler.capacity.maximum-am-resource-percent" in lines:                                                                
                        flag=True                                                                                                                 
                        temp_xml.write(lines)                                                                                                     
                        continue                                                                                                                  
                if flag:                                                                                                                          
                        idx=lines.find('>')                                                                                                       
                        value=lines[idx+1:lines[idx:].find('<')+idx]                                                                              
                        if avg_cpu<threshold:    
                                new_value=max(0.05,float(value)-0.01)                                                                             
                        else:                                                                                                                     
                                new_value=float(value)+0.01                                                                                       
                        lines = lines.replace(value,str(new_value))                                                                               
                        flag=False                                                                                                                
                temp_xml.write(lines)                                                                                                             
        xml.close()                                                                                                                               
        temp_xml.close()                                                                                                                          
        bashc="cp -f temp.xml /home/hadoop/hadoop/etc/hadoop/capacity-scheduler.xml"                                                              
        os.system(bashc)
	os.system("yarn rmadmin -refreshQueues")                                                                                                                          		                                                                                                                                        	                                                          

