
import sys
import numpy as np
import cmath


if len(sys.argv) != 2:
    print("\nUsage : %s <InputFileName>" % sys.argv[0])
    exit()
netlist_name = sys.argv[1]
#netlist_name = input("\nEnter Input file name : ")
(CIRCUIT,END,FREQ) = (".circuit",".end",".ac")
Pi = np.pi            #Storing important connstants

class Res:

    def __init__(self,node1,node2,val):
        self.n1 = int(node1)
        self.n2 = int(node2)
        self.val = float(val)
        
class V_S:
    
    def __init__(self,node1,node2,val,phi):
        self.n1 = int(node1)
        self.n2 = int(node2)
        self.val = cmath.rect(val,(Pi*phi)/180)
        
class I_S:
    
    def __init__(self,node1,node2,val,phi):
        self.n1 = int(node1)
        self.n2 = int(node2)
        self.val = cmath.rect(val,(Pi*phi)/180)
        
class Cap:

    def __init__(self,node1,node2,val):
        self.n1 = int(node1)
        self.n2 = int(node2)
        self.val = float(val)

    def impedance(self,w):
        if w == 0:
            return(float("inf"))
        else:
            return(complex(0,-1/(w*self.val)))
        
class Ind:

    def __init__(self,n1,n2,val):
        self.n1 = int(n1)
        self.n2 = int(n2)
        self.val = float(val)

    def impedance(self,w):
        return(complex(0,w*self.val))

try:
    fh = open(netlist_name,"r")             #Trying to open the mentioned file with File Handle "fh"
    lines = fh.readlines()
    fh.close()                              #Closing the file handle "fh"
    del(fh,netlist_name)
    (cstart,cend) = (-1,-2)                 #Indexes to identify the segment containing the circuit definition

    for i in range(len(lines)):
        if CIRCUIT == lines[i][:len(CIRCUIT)]:  #Checking if the line is ".circuit"
            cstart = i
        elif END == lines[i][:len(END)]:    #Checking if the line is ".end"
            cend = i
            break
    w = 0
    for i in range(cend + 1,len(lines)):
        if FREQ == lines[i][:len(FREQ)]:
            line = lines[i].split("#")[0].rstrip().split(" ")
            w = 2*Pi*float(line[-1])
            break

    if cstart >= cend or cstart*cend < 0:
        print("\nInvalid Circuit")
        exit()

except IOError:                             #If the file specified is Invalid and could not be opened
    print("\nCould not open the File.")
    exit()


"""
Printing the output in the desired format.
i.e. Circuit definition from bottom to top and right to left.
"""
Resistors, V_sources, I_sources, Capacitors, Inductors, nodes = {},{},{},{},{},{}
Shorts = []
#nodes = {}

    
def Identify(line):

    if line[0][0] == "R":
        if sorted([nodes[line[1]],nodes[line[2]]]) not in Shorts:
            Resistors[line[0]] = Res(nodes[line[1]], nodes[line[2]], line[3])
    elif line[0][0] == "V":
        if sorted([nodes[line[1]],nodes[line[2]]]) not in Shorts:
            if line[3].lower() == "dc":
                print("I got here in dc!")
                V_sources[line[0]] = V_S(nodes[line[1]], nodes[line[2]], float(line[4]), 0.0)
            elif line[3].lower() == "ac":
                print("I got here in ac!")
                V_sources[line[0]] = V_S(nodes[line[1]], nodes[line[2]], float(line[4])/2, float(line[5]))
    elif line[0][0] == "I":
        if sorted([nodes[line[1]],nodes[line[2]]]) not in Shorts:
            if line[3].lower() == "dc":
                I_sources[line[0]] = I_S(nodes[line[1]], nodes[line[2]], float(line[4]), 0)
            elif line[3].lower() == "ac":
                I_sources[line[0]] = I_S(nodes[line[1]], nodes[line[2]], float(line[4])/2, line[5])
    elif line[0][0] == "C":
        if sorted([nodes[line[1]],nodes[line[2]]]) not in Shorts:
            Capacitors[line[0]] = Cap(nodes[line[1]], nodes[line[2]], line[3])
    elif line[0][0] == "L":
        if sorted([nodes[line[1]],nodes[line[2]]]) not in Shorts:
            Inductors[line[0]] = Ind(nodes[line[1]], nodes[line[2]], line[3])

def nodes_and_shorts(w):
    node_index = 1
    for line in lines[cstart+1:cend]:
        line = line.split("#")[0].rstrip().split(" ")
        try:
            if line[0][0] not in ['R','V','I','C','L']:
                print("\nThis program currently does not support some of the elements")
                print("that are present in this circuit.Currently only R,L,C,V,I are supported.")
                print("Symbols have their usual meaning")
                exit()            
            for index1 in range(1,3):
                if line[index1] not in nodes.keys():
                    if line[index1] == "GND":
                        nodes[line[index1]] = 0
                    else:
                        nodes[line[index1]] = node_index
                        node_index += 1
            if (line[0][0] == "R") and (float(line[3]) == 0):
                Shorts.append(sorted([nodes[line[1]],nodes[line[2]]]))
            elif (line[0][0] == "V") and (float(line[4]) == 0):
                Shorts.append(sorted([nodes[line[1]],nodes[line[2]]]))
            elif (line[0][0] == "L") and (w == 0):
                Shorts.append(sorted([nodes[line[1]],nodes[line[2]]]))
        
        except IndexError:
            continue
        
    if "GND" not in nodes.keys():
        print("\nThe circuit does not have a conducting path to ground. Feed a proper circuit.")
        exit()

def manage_shorts():
    for short in Shorts:
        for R in Resistors.values():
            if R.n1 == short[1]:
                R.n1 = short[0]
            elif R.n2 == short[1]:
                R.n2 = short[0]
        for C in Capacitors.values():
            if C.n1 == short[1]:
                C.n1 = short[0]
            elif C.n2 == short[1]:
                C.n2 = short[0]
        for L in Inductors.values():
            if L.n1 == short[1]:
                L.n1 = short[0]
            elif L.n2 == short[1]:
                L.n2 = short[0]
        for V in V_sources.values():
            if V.n1 == short[1]:
                V.n1 = short[0]
            elif V.n2 == short[1]:
                V.n2 = short[0]
        for I in I_sources.values():
            if I.n1 == short[1]:
                I.n1 = short[0]
            elif I.n2 == short[1]:
                I.n2 = short[0]
                
def Read_Ciruit():
    for line in lines[cstart+1:cend]:
        line = line.split("#")[0].rstrip().split(" ")
        if len(line) in [4,5,6]:
            Identify(line)


def Create_MNA_matrix():

    for R in Resistors.values():
        r = R.n1
        c = R.n2
        if r == c:
            continue
        elif r == 0:
            G[c-1,c-1] += 1/R.val
        elif c == 0:
            G[r-1,r-1] += 1/R.val
        else:
            G[r-1,r-1] += 1/R.val
            G[r-1,c-1] -= 1/R.val
            G[c-1,r-1] -= 1/R.val
            G[c-1,c-1] += 1/R.val

    for C in Capacitors.values():
        r = C.n1
        c = C.n2
        if r == c:
            continue
        elif r == 0:
            G[c-1,c-1] += 1/C.impedance(w)
        elif c == 0:
            G[r-1,r-1] += 1/C.impedance(w)
        else:
            G[r-1,r-1] += 1/C.impedance(w)
            G[r-1,c-1] -= 1/C.impedance(w)
            G[c-1,r-1] -= 1/C.impedance(w)
            G[c-1,c-1] += 1/C.impedance(w)

    for In in Inductors.values():
        r = In.n1
        c = In.n2
        if r == c:
            continue
        elif r == 0:
            if In.impedance(w) != 0:
                G[c-1,c-1] += 1/In.impedance(w)
        elif c == 0:
            if In.impedance(w) != 0:
                G[r-1,r-1] += 1/In.impedance(w)             
        else:
            if In.impedance(w) != 0:
                G[r-1,r-1] += 1/In.impedance(w)
                G[r-1,c-1] -= 1/In.impedance(w)
                G[c-1,r-1] -= 1/In.impedance(w)
                G[c-1,c-1] += 1/In.impedance(w)               

    aux_index = len(nodes) - 1 - len(Shorts)
    for V in V_sources.values():
        r = V.n1
        c = V.n2
        if r == c:
            continue
        elif c == 0:
            G[r-1,aux_index] += 1
            G[aux_index,r-1] += 1
            I[aux_index] += V.val
            aux_index += 1
        elif r == 0:
            G[c-1,aux_index] -= 1
            G[aux_index,c-1] -= 1
            I[aux_index] += V.val
            aux_index += 1
        else:
            G[r-1,aux_index] += 1
            G[c-1,aux_index] -= 1
            G[aux_index,r-1] += 1
            G[aux_index,c-1] -= 1
            I[aux_index] += V.val
            aux_index += 1

    for Is in I_sources.values():
        r = Is.n1
        c = Is.n2
        if r == c:
            continue
        elif c == 0:
            I[r-1] -= Is.val
        elif r == 0:
            I[c-1] += Is.val
        else:
            I[r-1] -= Is.val
            I[c-1] += Is.val

def Solve():
    sol = np.linalg.solve(G, I)
    for i in range(len(nodes)-1-len(Shorts),len(nodes) + len(V_sources) -len(Shorts)-1):
        #print("I(V%d) : %4.4f + j%4.4f (A)" % (i - len(nodes) + 2,solution[i].real,solution[i-1].imag))
        print("I(V",i - len(nodes) + 2 - len(Shorts),") :",sol[i])
    for i in range(1,len(nodes)-len(Shorts)):
        #print("V(node%d) : %4.4f + j%4.4f (V)" % (i,solution[i-1].real,solution[i-1].imag))
        print("V(node",i,") :",sol[i-1])
    print(sol)


nodes_and_shorts(w)
Read_Ciruit()
manage_shorts()
order = len(nodes) + len(V_sources) - len(Shorts) - 1
G = np.zeros((order,order),dtype=complex)
I = np.zeros(order,dtype=complex)
Create_MNA_matrix()
Solve()
