#Process level parallelism for shell commands
import glob
import sys
import subprocess as sp
import multiprocessing as mp

def work(in_file):
    """Defines the work unit on an input file"""
    for line in open(in_file):
        print (line)
        sp.check_output(line, shell=True)
    return 0

if __name__ == '__main__':
    #Specify files to be worked with typical shell syntax and glob module
    #file_path = './*.data'
    #tasks = glob.glob(file_path)
    tasks = glob.glob(sys.argv[1])
    
    #Set up the parallel task pool to use all available processors
    count = mp.cpu_count()
    print ("cpu_count: ", count)
    pool = mp.Pool(processes=count)

    #Run the jobs
    pool.map(work, tasks)
