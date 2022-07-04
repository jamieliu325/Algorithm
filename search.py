def seq_search(arr,ele):
    pos = 0
    found = False
    while pos < len(arr) and not found:
        if arr[pos] == ele:
            found = True
        else:
            pos += 1
    return found

def binary_search(arr,ele):

    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        mid = (first+last)//2
        if arr[mid]==ele:
            found=True
        else:
            if ele<arr[mid]:
                last=mid-1
            else:
                first=mid+1
    return found

def rec_bin_search(arr,ele):
    if len(arr)==0:
        return False
    else:
        mid=len(arr)//2

        if arr[mid]==ele:
            return True
        else:
            if ele<arr[mid]:
                return rec_bin_search(arr[:mid],ele)
            else:
                return rec_bin_search(arr[mid+1:],ele)

class HashTable(object):

    def __init__(self,size):
        self.size = size
        self.slots=[None]*self.size
        self.data=[None]*self.size

    def hashfunction(self,key,size):
        return key%size

    def rehas(self,oldhash,size):
        return (oldhash+1)%size

    def put(self,key,data):
        hashvalue = self.hashfuction(key,len(self.slots))
        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        else:
            if self.slots[hashvalue]==key:
                self.data[hashvalue]=data
            else:
                nextslot=self.rehash(hashvalue,len(self.slots))
            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot,len(self.slots))
            if self.slots[nextslot]==None:
                self.slots[nextslot]=key
                self.data[nextslot]=data
            else:
                self.data[nextslot]=data

    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))
        data=None
        stop=False
        found=False
        position=startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position]==key:
                found=True
                data=self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key,data)