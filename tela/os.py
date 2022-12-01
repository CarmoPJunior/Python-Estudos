import psutil 

# total_memory, used_memory, free_memory = map( 
#     int, os.popen('free -t -m').readlines()[-1].split()[1:]) 


# infoCpu = psutil.cpu_times_percent(interval=1, percpu=False)

# infoCpu = psutil.cpu_percent(interval=1)


porcentagemCpuUtilizada = psutil.cpu_percent(interval=1)
porcentagemMemoriaUtilizada = psutil.virtual_memory().percent
print("CPU utilizada: ",porcentagemCpuUtilizada)   
print("Memória utilizada: ", psutil.virtual_memory().percent) 

# psutil.virtual_memory()
# svmem(total=10367352832, available=6472179712, percent=37.6, used=8186245120, free=2181107712, active=4748992512, inactive=2758115328, buffers=790724608, cached=3500347392, shared=787554304)
# >>> psutil.swap_memory()
# sswap(total=2097147904, used=296128512, free=1801019392, percent=14.1, sin=304193536, sout=677842944)
# >>>