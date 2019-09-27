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
    queue.put(None)
    return 0;

def do_work(queue):
    while True:
        command = queue.get()
        if (command is None):
            break;
        print ("processing: ", command, " on processor: ");#, multiprocessing.current_process().name)
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

    #Run the jobs
    with concurrent.futures.ThreadPoolExecutor(max_workers=count) as executor:     
        executor.submit(do_work,queue) 

