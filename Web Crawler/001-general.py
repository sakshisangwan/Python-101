import os

def create_project_directory(directory):
    if not os.path.exists(directory):
        print ("creating project "+ directory)
        os.makedirs(directory)

#Create queue and crawled files (if they don't already exist)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.text'
    crawled = project_name + '/crawled.text'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

#Create a new files
def write_file(path, data):
    f = open(path , 'w')
    f.write(data)
    f.close()

#Add data on to existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + "\n")

#Delete contents of a file
def delete_file_contents(path):
    with open(path , 'w'):
        pass

#Read file and convert each line to set item
def file_to_set(file_name):
    results=set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))

#Read set and convert each item to line
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file,link)




#creat_project_directory("xkcd")
#creat_data_files("xkcd","www.xkcd.com")
