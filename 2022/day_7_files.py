##NOT WORKING YET

class Directory():
    def __init__(self,name):
        self.name=name
        self.directories=[]
        self.files=[]
        self.parent=None
    def addDir(self,dir):
        self.directories.append(dir)
    def addFile(self,file):
        self.files.append(file)
    def addParent(self,Directory):
        self.parent=Directory
    def getParent(self):
        return self.parent
    def __eq__(self, other): 
        if not isinstance(other, Directory):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.name == other.name
    def __str__(self):
        string=self.name
        for i in range(len(self.directories)):
            string+="\n - dir: "+self.directories[i].name
        for i in range(len(self.files)):
            string+="\n - file: "+self.files[i].name+" size: "+str(self.files[i].size)
        return string


class File():
    def __init__(self,size,name):
        self.size=int(size)
        self.name=name

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def DirInList(list, dir):
    for i in range(len(list)):
        if list[i].name==dir.name:
            return True
    return False


def main():
    with open('7_input.txt') as f:
        lines=f.read().splitlines()
        directories=[]
        i=0
        currentDir=None
        while(i<len(lines)):
            line=lines[i].split()
            if "cd" in line and ".." not in line:
                newdir = Directory(line[2])
                if not DirInList(directories,newdir):
                    directories.append(newdir)
                currentDir=newdir
                i+=1
            elif ".." in line:
                #currentDir=currentDir.getParent()
                i+=1
            elif "dir" in line:
                babyDir=Directory(line[1])
                babyDir.addParent(currentDir)
                currentDir.addDir(babyDir)
                if not DirInList(directories,babyDir):
                    directories.append(babyDir)
                i+=1
            elif has_numbers(line[0]):
                newFile=File(line[0],line[1])
                currentDir.addFile(newFile)
                i+=1
            else:
                i+=1
        print(currentDir)
        for i in range(len(directories)):
            print(directories[i])


main()
