










#ee2703 final exam
#assignment based on radiation of antenna
#in pdf all esssential stufff are given
''' psedocode
'''


'''author:sunil kumar
    roll no:ee19b120'''
#first of all we import essentil tool we used herre ,import here



from mpl_toolkits.mplot3d import Axes3D
'''it is 3d plotiing tool which is mainly used in advance
python and scientic python
it give 3d visualigation'''
from matplotlib import cm#it is for coloring graph and other

from matplotlib.ticker import LinearLocator, FormatStrFormatter
'''this module is used for formating user defined
 mainly for this purpose we used it'''

import numpy as n#numpy contain many fn also contain lstsq and linalg which is used in this program
import matplotlib.pyplot as p#here pyplot is used for grid ,x,y axis mainly all work related to graph
import scipy as s#it is scientific python

'''here scipy is very use full scientific 
   python module which  provide fn like MATLAB'''
from mpl_toolkits.mplot3d import Axes3D
'''HERE MPL TOOLKIT provid eploting in 3d plane'''
from matplotlib import cm  #it mis used for colormaps handelling
from matplotlib.ticker import LinearLocator, FormatStrFormatter#format specifireb use d

fig=p.figure()
fig.tight_layout()#it automatically use for adjust subplot in our code
'''############################################'''
ax = fig.gca(projection='3d')


def s():
    p.style.use('ggplot')
    '''here we choose style for plot'''
    p.rcParams['font.size'] = 10
    '''here we used font sized as 10 
    appropriatly'''
    p.rcParams['axes.labelsize'] = 10
    '''here  we level size as 10 for that'''
    p.rcParams['axes.labelweight'] = 'bold'
    '''here we choosed weighth'''
    p.rcParams['axes.titlesize'] = 10
    '''title plot with the help of this module'''
    p.rcParams['xtick.labelsize'] = 8
    '''here we size taken as 8'''
    p.rcParams['legend.fontsize'] = 10#here legend size taken as 10
    p.rcParams['figure.titlesize'] = 12
    '''here we taken figure title size as 12 '''
    p.rcParams['figure.figsize'] = 15, 10
    '''here we taken horizontal and vertical length of figure as 15,10'''
    p.rcParams['figure.dpi'] = 150


s()


x=n.linspace(0,2,3)#creating no.between 0,3 of 3
y=n.linspace(0,2,3)#creating no.between 0,3 of 3
z=n.linspace(0,1000-1,1000)#creating no.between 0,3 of 1000
X,Y,Z=n.meshgrid(x,y,z)#it used line and like as graphpaper
get_ipython().run_line_magic('matplotlib','inline')
'''for inline we use get ipython'''
a=10
'''here we taken radius as 10'''
sn=100 #we take 100 part here
r=n.vstack((a*n.cos(n.linspace(0,2*n.pi,sn)).T,a*n.sin(n.linspace(0,2*n.pi,sn)).T))
'''it provide stack like creating matrices'''
r=r.T
r.shape
p.scatter(r[:,0],r[:,1])     #used for drawing scatter plot diagram here dotted plot is observed
'''actially our image formed virtuly in laptop 
 we have 
 to show it so we used p.show()'''
p.show()
xi,yi=i(r[:,0],r[:,1])
p.quiver(r[:,0],r[:,1],xi,yi)
'''here quiver plot denote just like velocity
 vector as arrows with components 
(u,v) at the point (x,y)
the above command plot vector as arrows at the 
 coordinate  specified in each corresponding specified in
  
 each corres  pair of element in x and y direction'''
def i(x,y):#we here assumed here that it is time independent
    return n.array([(n.cos(n.arctan(y/x)))*y,n.cos(n.arctan(y/x))*-x])#returning value  of required current
    return math.sqrt((r[0, :, :] - r_[l, 0]) ** 2 + (r[1, :, :] - r_[l, 1]) ** 2 + r[2, :, :] ** 2)
    return math.sum((r - r_.reshape((100, 2, 1)))) ** 2
b=2*n.pi*10/sn*n.vstack((n.cos(n.linspace(0,2*n.pi,sn)).T,n.sin(n.linspace(0,2*n.pi,sn)).T))#making temporary variable  and vertical column
b=b.T#T is used for transpose purpose for hre
b.shape()#ity provid eshape  for our b
'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
d=n.array((X,Y,Z))#provide a array for using in length
d.shape
def calc(l):# we find  ri jk l for data distance l

    ma = d.reshape((1, 3, 3, 3, 1000))#reshaping data
    ma_ = n.hstack((d, n.zeros((100, 1))))#making vertical data in no of 0 to 6

    return n.linalg.norm(n.tile(d, (100, 1, 1, 1)).reshape((100, 3, 3, 3, 1000)) - ma_.reshape((101, 3, 1, 1, 1)),
                          axis=1)#it return our notmali9srred grapph
'''here n.tile fn create 
new repeating   array
no.of time we can want we can create per 
repeatation'''
'''linalg
    is ver7y use full module which cerate ax=b and solve it'''
    #here return fn it maily for n.sqrt and for returning
'''%%%%%%%%%%%%%%%%%%%%%%%%
###########################'''

fi= n.linspace(0, 2 * n.pi, sn)#for fi space angle we create 100 different  value we create
A = n.sum(n.cos())#sum all cosine and store in A
R=calc(0)#we calling our previously define function calcc()l
display(R.shape)# it showing our arrange manner ans  show r.shape
coses=n.cos(fi).reshape((100,1,1,1))#we reshaping cos term
g_u=g[:,0].reshape((100,1,1,1))#here we make instance for and reshaping it with 100
k_1=coses*b*n.exp(1j*R)*g_u/R#here we make instance for and reshaping it with 100

g_u=g[:,1].reshape((100,1,1,1))#reshaping g
k_2=coses*g_u*n.exp(1j*R)*g_u/R#reshaping k  with our intial define fn coses which contain cos(fi)

display(k_1.shape)#we displayed our output by fig and by this which provide graph and figure
xA=n.sum(k_1,axis=0)#here we sumed k_1 by this which is just like summation sum.
yA=n.sum(k_2,axis=0)##here we sumed k_1 by this which is just like summation sum.
xA.shape#shaping our xA for further use
'''shaping proper shape for both
xA,yA'''
print(yA.shape)#printing itself is for showing output at screen here we print the the result of yA.shape
'''here we taking output of yA only because only thi
needed'''
k=(yA[1,0,:]-A_x[0,1,:]-yA[-1,0,:]+xA[0,-1,:])/(4)#here we findthe mag fild which stored nin variable k
'''this magnetic field contained in space
 which is given by cylindrical coordinate
  for finding this we calculated vector potential 
  with the help of mag.potential we can find magnetic field variation in space 
  which is to be find in qws'''
#divide by 4 as for qs
'''$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''

k.shape()#shapin khere for appropriatly ,this is ordered in fig = p.figure()# for plotimg figure
p.loglog(z,n.abs(k))#here abs provide absolute value
#means no sign concider
'''now we are going to find
best fit for our 
magnetic field '''

A=n.hstack([n.ones(len(k[300:]))[:,n.newaxis],n.log(z[300:])[:,n.newaxis]])#it is our vector potential
'''it is very importamt quantity in antenna for magnetic field 
in vector potential'''
log_ll,mm=n.linalg.lstsq(A,n.log(n.abs(k[300:]))) [0]#we use only first c olumn result
#rest are error
ll=n.exp(log_ll)#make a variable named ll
display(mm)#we display required graph
#which created virtually by operation