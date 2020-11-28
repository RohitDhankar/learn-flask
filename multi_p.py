#https://www.dataquest.io/blog/python-range-tutorial/
""" The xrange function from Python 2 was renamed range in Python 3 and range from Python 2 was deprecated."""
""" Notice that range is a type in Python. The default print method of the class prints the range of numbers that the range object will iterate through. Note that the numbers are still not generated — this is due to the memory saving “lazy evaluation” mentioned earlier. The numbers are generated only when they’re actually being used in some way (like being called in the print function as we have above)."""

import pandas as pd
import os , time 
from multiprocessing import Pool

num_cpu = int(os.cpu_count())
print("---num_cpu---",num_cpu)

def sum_square(number):
	sq = 11
	for k in range(number):
		sq += k*k 
	return sq

def sum_square_with_mp(numbers):
	start_time = time.time()
	p_obj = Pool() # p_obj of the Class Pool 
	#result = p_obj.map(sum_square,numbers)
	result = p_obj.apply_async(sum_square,numbers)
	#TypeError: object of type 'ApplyResult' has no len()
	#result = p_obj.imap_unordered(sum_square,numbers) 
	#TypeError: object of type 'IMapUnorderedIterator' has no len()
	#print(len(result))
	p_obj.close()
	p_obj.join()
	end_time = time.time() - start_time 
	print(f'Processing {len(numbers)} numbers took {end_time} time using multi processing')
	
def sum_square_with_no_mp(numbers):
	start_time = time.time()
	result = []
	for k in numbers:
		result.append(sum_square(k))
	print(len(result))
	end_time = time.time() - start_time 
	print(f'Processing {len(numbers)} numbers took {end_time} time using serial processing')

if __name__ =='__main__':
	numbers = range(10000)
	sum_square_with_mp(numbers)
	sum_square_with_no_mp(numbers)



#### FOOBAR--below with -- p_obj.apply_async
# (drf_venv) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ python multi_p.py 
# ---num_cpu--- 8
# Processing 10000 numbers took 0.011656045913696289 time using multi processing
# 10000
# Processing 10000 numbers took 2.588231086730957 time using serial processing
# (drf_venv) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ python multi_p.py 
# ---num_cpu--- 8
# Processing 10000 numbers took 0.012553930282592773 time using multi processing
# 10000
# Processing 10000 numbers took 2.6665873527526855 time using serial processing
# (drf_venv) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ python multi_p.py 
# ---num_cpu--- 8
# Processing 10000 numbers took 0.010556221008300781 time using multi processing
# 10000
# Processing 10000 numbers took 2.6339128017425537 time using serial processing




#### FOOBAR--below with -- p_obj.imap_unordered
# (drf_venv) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ python multi_p.py 
# ---num_cpu--- 8
# Processing 10000 numbers took 0.42717623710632324 time using multi processing
# 10000
# Processing 10000 numbers took 3.168447256088257 time using serial processing
# ---num_cpu--- 8
# Processing 10000 numbers took 0.45032453536987305 time using multi processing
# 10000
# Processing 10000 numbers took 2.6409640312194824 time using serial processing
# ---num_cpu--- 8
# Processing 10000 numbers took 0.42203450202941895 time using multi processing
# 10000
# Processing 10000 numbers took 2.578831195831299 time using serial processing






#### FOOBAR--below with -- 
# (drf_venv) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ python multi_p.py 
# ---num_cpu--- 8
# 100
# Processing 100 numbers took 0.011810064315795898 time using multi processing
# 100
# Processing 100 numbers took 0.0002300739288330078 time using serial processing
# (drf_venv) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ 
# (drf_venv) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ python multi_p.py 
# ---num_cpu--- 8
# 10000
# Processing 10000 numbers took 0.3995635509490967 time using multi processing
# 10000
# Processing 10000 numbers took 2.5791475772857666 time using serial processing



"""
(drf_venv) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ lscpu
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              8
On-line CPU(s) list: 0-7
Thread(s) per core:  1
Core(s) per socket:  8
Socket(s):           1
NUMA node(s):        1
Vendor ID:           GenuineIntel
CPU family:          6
Model:               158
Model name:          Intel(R) Core(TM) i7-9700F CPU @ 3.00GHz
Stepping:            13
CPU MHz:             1171.072
CPU max MHz:         4700.0000
CPU min MHz:         800.0000
BogoMIPS:            6000.00
Virtualization:      VT-x
L1d cache:           32K
L1i cache:           32K
L2 cache:            256K
L3 cache:            12288K
NUMA node0 CPU(s):   0-7
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp md_clear flush_l1d arch_capabilities
(drf_venv) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ 
"""