from llist import *

def find(lst, num):
    if lst.head:
        nex = lst.head
        while nex.val != num and nex.next != None:
            nex = nex.next
        if nex.val == num:
            return nex

def findtail(lst):
    if lst.head:
        nex = lst.head
        while nex.next:
            nex = nex.next
        lst.tail = nex

def llprint(lst, num):
    if lst.head:
        nex = lst.head
        i = 0
        while i < num and nex.next:
            print(nex.val)
            i += 1
            nex = nex.next

def find_cycle(lst):
    if lst.head:
        nex = lst.head
        if lst.head.next:
            nev = lst.head.next
            while nex != nev and nev.next: 
                nev = nev.next
                if nev == nex:
                    csl = []
                    csl.append(nex.val)
                    nec = nex.next
                    while nec != nex:
                        csl.append(nec.val)
                        nec = nec.next
                    nei = 0
                    neo = lst.head
                    while neo != nec:
                        neo = neo.next
                        nei += 1
                    return csl, nei
                nev = nev.next
                if nev == nex:
                    csl = []
                    csl.append(nex.val)
                    nec = nex.next
                    while nec != nex:
                        csl.append(nec.val)
                        nec = nec.next
                    nei = 0
                    neo = lst.head
                    while neo != nec:
                        neo = neo.next
                        nei += 1
                    return csl, nei
                nex = nex.next
        else:
            return False
    else:
        return False
        



if __name__ == "__main__":

    lst = LList()
    for i in range(0,15):
        append(lst, Node(2**i))
    findtail(lst)
    lst.tail.next = find(lst, 1024)

    
    print(find_cycle(lst))


from gencyclic import cyclic
print(find_cycle(cyclic(47077)))