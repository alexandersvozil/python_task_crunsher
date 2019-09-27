#Process level parallelism for shell commands
import sys
import subprocess as sp
import concurrent.futures

def read_file(in_file):
    """Defines the work unit on an input file"""
    commands = [];
    for line in open(in_file):
        if line[0] == '#' or line[0] == '\n':
            continue
        print (line)
        commands.append(line);
    return commands;

def do_work(command):
        print ("processing: ", command);
        sp.check_output(command, shell=True);

if __name__ == '__main__':
    #Specify files to be worked with typical shell syntax and glob module
    tasks = sys.argv[1]
    workers = sys.argv[2]
    commands = read_file(tasks);
    print (commands);

    #Run the jobs
    with concurrent.futures.ThreadPoolExecutor(max_workers=int(workers)) as executor:          
        executor.map(do_work,commands);

