import numpy as np
from skimage import draw   #To create shape arrays


def mkquad(h, v):
    #A quadralateral
    o = np.zeros(shape = (4,3), dtype=np.int)
    o[:,0] = [0,v,0,-v]
    o[:,1] = [h, 0, -h, 0]
    o[:,2] = 1
    return o
    
def mkarc(h, v, r):
    #An arc; r indicates rotation
    o = np.zeros(shape=(3,3), dtype=np.int)
    if(r==1):
        o[:,0] = [0,v,0]
        o[:,1] = [h,0,-h]
    elif r==2:
        o[:,0] = [h,0,-h]
        o[:,1] = [0,-v,0]
    elif r==3:
        o[:,0] = [0,v,0]
        o[:,1] = [-h,0,h]
    elif r==4:
        o[:,0] = [-v,0,v]
        o[:,1] = [0,h,0]
    
    o[:,2] = 1
        
    return o

def mkang(h,v,r):
    #A right angle; r indicates rotation
    o = np.zeros(shape=(2,3), dtype=np.int)
    if(r==1):
        o[:,0] = [v,0]
        o[:,1] = [0,h]
    elif r==2:
        o[:,0] = [0,v]
        o[:,1] = [h,0]
    elif r==3:
        o[:,0] = [-v,0]
        o[:,1] = [0,h]
    elif r==4:
        o[:,0] = [0,-v]
        o[:,1] = [h,0]
        
    o[:,2] = 1

    return o  

def mklin(h,v):
    #A line
    o = np.zeros(shape=(1,3), dtype=np.int)
    o[0,:] = [v,h,1]
    return o
        



def mktable(h= -1, v= -1, li= -1):
    
    if(h == -1): #Sample width if not specified from 20-50
        tmp = np.arange(30, dtype=np.int) + 20
        h = np.random.choice(tmp, 1)
    
    if(v == -1): #Sample height if not specified from 1 - width
        tmp = np.arange(h -1 , dtype=np.int) + 1
        v = np.random.choice(tmp, 1)
        
        
    if(li== -1): #Sample if not specified
        tmp = np.arange(h/3, dtype=np.int)
        li = np.random.choice(tmp)
        
    o = np.zeros(shape=(5,3), dtype=np.int)
    o[0,:] = mklin(h=h, v=0) #Surface
    o[1,:] = [0, -h + li, -1] #Move left
    o[2,:] = mklin(h=0, v=v) #First leg
    o[3,:] = [-v, h - (2*li), -1] #Move to second leg
    o[4,:] = mklin(h=0, v=v) #Second leg
    
    return o


def mkstool(h= -1, v= -1, li= -1):
    
    if(v == -1): #Sample height if not specified from 20-50
        tmp = np.arange(30, dtype=np.int) + 20
        v = np.random.choice(tmp, 1)
    
    if(h == -1): #Sample width if not specified from 1 - height
        tmp = np.arange(v -1 , dtype=np.int) + 1
        h = np.random.choice(tmp, 1)
        
        
    if(li== -1): #Sample if not specified
        tmp = np.arange(h/3, dtype=np.int)
        li = np.random.choice(tmp)
        
    o = np.zeros(shape=(5,3), dtype=np.int)
    o[0,:] = mklin(h=h, v=0) #Surface
    o[1,:] = [0, -h + li, -1] #Move left
    o[2,:] = mklin(h=0, v=v) #First leg
    o[3,:] = [-v, h - (2*li), -1] #Move to second leg
    o[4,:] = mklin(h=0, v=v) #Second leg
    
    return o

def mkchair(h= -1, v= -1, sh= -1):
    
    if(v == -1): #Sample height if not specified from 20-50
        tmp = np.arange(30, dtype=np.int) + 20
        v = np.random.choice(tmp, 1)
    
    if(h == -1): #Sample width if not specified from 1 - height
        tmp = np.arange(v - 10 , dtype=np.int) + 5
        h = np.random.choice(tmp, 1)
              
    if(sh== -1): #Sample seat height if not specified
        tmp = np.arange(v/2, dtype=np.int) + np.round(v/10)
        sh = np.random.choice(tmp)
        
    o = np.zeros(shape=(4,3), dtype=np.int)
    o[0,:] = mklin(v=v, h=0) #Back
    o[1,:] = [-sh, 0, -1] #Move up to seat height
    o[2:4,:] = mkang(v=sh, h = h, r=2) #Seat and econd leg
    
    return o


def mkmug(h= -1, v= -1, hsz= -1):
    
    if(v == -1): #Sample height if not specified from 20-50
        tmp = np.arange(30, dtype=np.int) + 20
        v = np.random.choice(tmp, 1)[0]
    
    if(h == -1): #Sample width if not specified from 1 - height
        tmp = np.arange(v - 10 , dtype=np.int) + 5
        h = np.random.choice(tmp, 1)[0]
              
    if(hsz== -1): #Sample handle size if not specified
        tmp = np.arange(v/3, dtype=np.int) + np.int(v/3)
        hsz = np.random.choice(tmp,1)[0]
        
    handloc = np.int((v - hsz)/2)
    o = mkquad(v=v, h=h)
    o = np.append(o, [[handloc, h, -1]], axis=0) #Move to handle top
    o = np.append(o, mkarc(h = np.int(h/2), v = hsz, r=1), axis=0)
    
    return o

def mkcase(h= -1, v= -1, hsz= -1):
    
    if(h == -1): #Sample height if not specified from 20-50
        tmp = np.arange(30, dtype=np.int) + 20
        h = np.random.choice(tmp, 1)[0]
    
    if(v == -1): #Sample width if not specified from 1 - height
        tmp = np.arange(h - 10 , dtype=np.int) + 5
        v = np.random.choice(tmp, 1)[0]
              
    if(hsz== -1): #Sample handle size if not specified
        tmp = np.arange(v/3, dtype=np.int) + np.int(v/3)
        hsz = np.random.choice(tmp,1)[0]
        
    handloc = np.int((h - hsz)/2)
    o = mkquad(v=v, h=h)
    o = np.append(o, [[0, handloc, -1]], axis=0) #Move to handle top
    o = np.append(o, mkarc(h = hsz, v = np.int(v/3), r=4), axis=0)
    
    return o

def mkbird(hd = -1, bd = -1, nc = -1, bk = -1, lg = -1):
    if hd == -1: #Sample head size
        tmp = np.arange(10, dtype=np.int) + 5
        hd = np.random.choice(tmp, 1)[0]
        
    if bd == -1: #Sample body size
        tmp = np.arange(hd, dtype=np.int) + hd + 5
        bd = np.random.choice(tmp, 1)[0]
        
    if nc == -1: #Sample neck length
        tmp = np.arange(2 * hd, dtype=np.int)
        nc = np.random.choice(tmp, 1)[0]
    
    if bk == -1: #Sample beak length
        tmp = np.arange(2 * hd, dtype=np.int) + 3
        bk = np.random.choice(tmp, 1)[0]
    
    if lg == -1: #Sample leg length
        tmp = np.arange(2 * hd, dtype=np.int) + 3
        lg = np.random.choice(tmp, 1)[0]

    bp = np.int(hd * .8) #Beak position
    o = mkquad(v=hd, h=hd) #draw head
    o = np.append(o, [[bp, 0, -1]], axis=0) #Move to beak
    o = np.append(o, [[0, -1 * bk, 1]], axis=0) #Draw beak
    
    o = np.append(o, [[hd - bp, bk + hd, -1]], axis=0) #Move to neck
    o = np.append(o, mklin(v=nc, h=0), axis=0) #Draw neck
    o = np.append(o, mkquad(bd, bd), axis = 0) #Draw body

    lp = np.int(bd/2) - 4
    o = np.append(o, [[bd, lp, -1]], axis=0) #Move to leg 1
    o = np.append(o, mklin(v=lg, h=0), axis=0) #Draw leg 1
    o = np.append(o, [[-lg, 8, -1]], axis=0) #Move to leg 2
    o = np.append(o, mklin(v=lg, h=0), axis=0) #Draw leg 2
    
    return o
        
        
def mksheep(hd = -1, bd = -1, nc = -1, lg = -1):
    if hd == -1: #Sample head size
        tmp = np.arange(10, dtype=np.int) + 5
        hd = np.random.choice(tmp, 1)[0]
        
    if bd == -1: #Sample body size
        tmp = np.arange(hd, dtype=np.int) + hd + 5
        bd = np.random.choice(tmp, 1)[0]
        
    if nc == -1: #Sample neck length
        tmp = np.arange(hd/2, dtype=np.int) + np.int(hd/2)
        nc = np.random.choice(tmp, 1)[0]
    
    if lg == -1: #Sample leg length
        tmp = np.arange(hd, dtype=np.int) + np.int(hd/2)
        lg = np.random.choice(tmp, 1)[0]

    o = mkquad(v=hd, h=np.int(hd * 1.3)) #draw head
    o = np.append(o, [[hd, np.int(hd * 1.3), -1]], axis=0) #Move to neck
    o = np.append(o, mklin(v=nc, h=0), axis=0) #Draw neck
    o = np.append(o, mkquad(v=bd, h=np.int(bd * 1.3)), axis = 0) #Draw body

    o = np.append(o, [[bd, 0, -1]], axis=0) #Move to leg 1
    o = np.append(o, mklin(v=lg, h=0), axis=0) #Draw leg 1
    o = np.append(o, [[-lg, np.int(bd * 1.3), -1]], axis=0) #Move to leg 2
    o = np.append(o, mklin(v=lg, h=0), axis=0) #Draw leg 2
    
    return o
        

def mkdog(hd = -1, bd = -1, nc = -1, bk = -1, lg = -1):
    if hd == -1: #Sample head size
        tmp = np.arange(10, dtype=np.int) + 5
        hd = np.random.choice(tmp, 1)[0]
        
    if bd == -1: #Sample body size
        tmp = np.arange(hd, dtype=np.int) + 2 * hd
        bd = np.random.choice(tmp, 1)[0]
        
    if nc == -1: #Sample neck length
        tmp = np.arange(hd/2, dtype=np.int) + np.int(hd/2)
        nc = np.random.choice(tmp, 1)[0]
    
    if lg == -1: #Sample leg length
        tmp = np.arange(hd, dtype=np.int) + np.int(hd/2)
        lg = np.random.choice(tmp, 1)[0]

    o = mkquad(v=hd, h=np.int(hd * 1.3)) #draw head
    o = np.append(o, [[hd, np.int(hd * 1.3), -1]], axis=0) #Move to neck
    o = np.append(o, mklin(v=nc, h=0), axis=0) #Draw neck
    o = np.append(o, mklin(v=0, h=bd), axis = 0) #Draw body

    o = np.append(o, [[0, -bd, -1]], axis=0) #Move to leg 1
    o = np.append(o, mklin(v=lg, h=0), axis=0) #Draw leg 1
    o = np.append(o, [[-lg, bd, -1]], axis=0) #Move to leg 2
    o = np.append(o, mklin(v=lg, h=0), axis=0) #Draw leg 2
    
    return o
        
def mkliz(h= -1, v= -1, bd= -1):
    
    if(h == -1): #Sample width if not specified from 20-50
        tmp = np.arange(10, dtype=np.int) + 5
        h = np.random.choice(tmp, 1)[0]
    
    if(v == -1): #Sample height if not specified from 1 - width
        tmp = np.arange(h, dtype=np.int) + 3
        v = np.random.choice(tmp, 1)[0]
        
        
    if(bd== -1): #Sample if not specified
        tmp = np.arange(h*3, dtype=np.int) + h*2
        bd = np.random.choice(tmp,1)[0]
        
    o = mkquad(h,h) #Draw head
    o = np.append(o, [[np.int(h/2), h, -1]], axis = 0) #Move to body
    o = np.append(o, mklin(h=bd, v=0), axis = 0) #Draw body
    o = np.append(o, [[0, np.int(-1 * bd * 7/15), -1]], axis=0)  #Move to back leg
    o = np.append(o, mklin(h=0, v=v), axis = 0) #draw leg
    o = np.append(o, [[-v, np.int(-1 * bd * 5/15), -1]], axis=0)  #Move to front leg
    o = np.append(o, mklin(h=0, v=v), axis = 0) #draw leg
    
    return o
        

def mkpig(hd = -1, bd = -1, lg = -1):
    
    if hd == -1: #Sample head size
        tmp = np.arange(10, dtype=np.int) + 10
        hd = np.random.choice(tmp, 1)[0]
        
    if bd == -1: #Sample body size
        tmp = np.arange(hd, dtype=np.int) + hd + 5
        bd = np.random.choice(tmp, 1)[0]
        
        
    if lg == -1: #Sample leg length
        tmp = np.arange(hd, dtype=np.int) + np.int(hd/2)
        lg = np.random.choice(tmp, 1)[0]

    sn = np.int(hd/3) #Snout size
    o = mkquad(v=hd, h=hd) #draw head
    o = np.append(o, [[2 * sn, -sn, -1]], axis=0) #Move to snout   
    o = np.append(o, mkquad(v=sn, h=sn), axis=0) #Draw snout
    o = np.append(o, [[-bd + sn, hd + sn, -1]], axis=0) #Move to body   
    
    o = np.append(o, mkquad(v=bd, h=np.int(bd * 1.3)), axis = 0) #Draw body

    o = np.append(o, [[bd, 0, -1]], axis=0) #Move to leg 1
    o = np.append(o, mklin(v=lg, h=0), axis=0) #Draw leg 1
    o = np.append(o, [[-lg, np.int(bd * 1.3), -1]], axis=0) #Move to leg 2
    o = np.append(o, mklin(v=lg, h=0), axis=0) #Draw leg 2
 
    return o
    