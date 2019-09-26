#Process level parallelism for shell commands
import sys
import subprocess as sp
import multiprocessing as mp
import concurrent.futures

def read_file(in_file, queue):
    """Defines the work unit on an input file"""
    for line in open(in_file):
        if line[0] == '#' or line[0] == '\n':
            continue
        print (line)
        queue.put(line)
    return 0;

def do_work(command):
    sp.check_output(command, shell=True);
    return 0;

if __name__ == '__main__':
    #Specify files to be worked with typical shell syntax and glob module
    tasks = sys.argv[1]
    queue = mp.Queue()
    
    read_file(tasks, queue);

    #Set up the parallel task pool to use all available processors
    count = mp.cpu_count()
    print ("cpu_count: ", count)
    #pool = mp.Pool(processes=count);

    #Run the jobs
    with concurrent.futures.ThreadPoolExecutor(max_workers=count) as executor:
        while(queue.empty() == False):
            executor.map(do_work,iter(queue.get, None)) 

