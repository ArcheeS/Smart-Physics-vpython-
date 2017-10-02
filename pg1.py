########################################################################################
#                                     SMART PHYSICS                                    #
########################################################################################

"""This is a basic idea of developing a Student-friendly education  envionment
   to allow the students to learn complex and tricky cocepts of physics via
   3-Dimensional image construction. This project can be worked upon on a
   larger scale to be applied in schools."""  

#based completely on the basics of python,vpython and GUI

#importing necessary fules of vpython and GUI
from visual import *
from Tkinter import *
import tkMessageBox


#####################################DISPERSION OF LIGHT################################

#Function to show the dispersion of light

def dispersion():
    scene=display(title='dispersion of light',width=650,height=650,range=(650,650,650),center=(0,0,0))
    scene.autoscale=True                              #adjusting the screen dimensions

    s1=sphere(pos=vector(0,0,0),radius=1,color=color.cyan)
    ar1=arrow(pos=vector(-10,0,0),axis=vector(1,0,0),color=color.white,make_trail=True,retain=200)
    l1=local_light(pos=ar1.pos,color=ar1.color)
    labeld=label(pos=ar1.pos,text="white light",color=color.white,opacity=100)
    r1=ar1.pos
    while r1.x<=s1.x:
        rate(10)
        ar1.pos=r1
        r1.x=r1.x+1
        l1.pos=r1
    ar1.visible=False

    ar11=arrow(pos=s1.pos,axis=vector(1,1.5,0),color=color.blue,make_trail=True,retain=200)
    ar12=arrow(pos=s1.pos,axis=vector(1,1,0),color=color.cyan,make_trail=True,retain=200)
    ar13=arrow(pos=s1.pos,axis=vector(1,.6,0),color=color.blue,make_trail=True,retain=200)
    ar14=arrow(pos=s1.pos,axis=vector(1,0,0),color=color.green,make_trail=True,retain=200)
    ar15=arrow(pos=s1.pos,axis=vector(1,-.6,0),color=color.yellow,make_trail=True,retain=200)
    ar16=arrow(pos=s1.pos,axis=vector(1,-1,0),color=color.orange,make_trail=True,retain=200)
    ar17=arrow(pos=s1.pos,axis=vector(1,-1.5,0),color=color.red,make_trail=True,retain=200)
    r11=ar11.pos
    r12=ar12.pos
    r13=ar13.pos
    r14=ar14.pos
    r15=ar15.pos
    r16=ar16.pos
    r17=ar17.pos
    i=0
    ar11.visible=False
    ar12.visible=False
    ar13.visible=False
    ar14.visible=False
    ar15.visible=False
    ar16.visible=False
    ar17.visible=False
    while i<8:
        rate(10)
        ar11.pos=r11
        ar12.pos=r12
        ar13.pos=r13
        ar14.pos=r14
        ar15.pos=r15
        ar16.pos=r16
        ar17.pos=r17
        r11.x=r11.x+1
        r11.y=r11.y+1.5
        r12.x=r12.x+1
        r12.y=r12.y+1
        r13.x=r13.x+1
        r13.y=r13.y+.6
        r14.x=r14.x+1
        r15.x=r15.x+1
        r15.y=r15.y-.6
        r16.x=r16.x+1
        r16.y=r16.y-1
        r17.x=r17.x+1
        r17.y=r17.y-1.5
        i=i+1
    
########################################PATH OF LIGHT#######################################

#function to show the path of reflected and refracted light
        
def light_travel():
    scene=display(title='behaviour of light',width=650,height=650,range=(650,650,650),center=(0,0,0))
    scene.autoscale=True

    wall=box(pos=vector(+8,0,0),length=0.1,width=5,height=30,color=(0.5,0.5,0.5),material=materials.rough)
    ar1=arrow(pos=vector(-4,7,0),axis=vector(1,0,0),color=color.green,make_trail=True,retain=200,material=materials.emissive)
    r1=ar1.pos
    ar1.visible=False
    label1=label(text="normal",pos=vector(-10,10,0),color=color.white,opacity=100)
    while  r1.x<9:
        rate(20)
        ar1.pos=r1
        r1.x=r1.x+1
    ar2=arrow(pos=vector(-4,12,0),axis=vector(1,0,0),color=color.green,make_trail=True,retain=200,material=materials.emissive)
    r2=ar2.pos
    ar2.visible=False
    while  r2.x<9:
        rate(20)
        ar2.pos=r2
        r2.x=r2.x+1
    b=arrow(pos=vector(-4,0,0),axis=vector(1,1,0),color=color.green,make_trail=True,retain=200,material=materials.emissive)
    l1=local_light(pos=b.pos,color=b.color)
    r=b.pos
    label2=label(text="incident ray",pos=vector(-10,-7,0),color=color.white,opacity=100)
    i=0
    while r.x<8:
        rate(20)
        b.pos=r
        r.x=r.x+1
        r.y=r.y+1
        l1.pos=b.pos
            
    b.axis=(-1,1,0)
    while i<10:
        rate(20)
        b.pos=r
        r.y=r.y+1
        r.x=r.x-1
        l1.pos=b.pos
        i=i+1
    b.visible=False
    label3=label(text="reflected ray",pos=vector(-10,17,0),color=color.white,opacity=100)
    c=arrow(pos=vector(-4,-5,0),axis=vector(1,1,0),color=color.yellow,make_trail=True,retain=200,material=materials.emissive)
    q=c.pos

    l2=local_light(pos=c.pos,color=c.color)
    i=0
    while q.x<8:
        rate(20)
        c.pos=q
        q.x=q.x+1
        q.y=q.y+1
        l2.pos=c.pos
            
    c.axis=(-1,1,0)
    while i<10:
        rate(20)
        c.pos=q
        q.y=c.y+1
        q.x=c.x-1
        l2.pos=c.pos
        i=i+1
    c.visible=False
    d=arrow(pos=vector(-4,-10,0),axis=vector(1,1,0),color=color.cyan,make_trail=True,retain=200,material=materials.emissive)
    t=d.pos
    l3=local_light(pos=d.pos,color=d.color)
    i=0
    while d.x<20:
        rate(20)
        d.pos=t
        t.x=t.x+1
        t.y=t.y+1
        l3.pos=t

    w=arrow(pos=vector(-4,-15,0),axis=vector(1,1,0),color=color.orange,make_trail=True,retain=200,material=materials.emissive)
    m=w.pos
    d.visible=False
    l4=local_light(pos=w.pos,color=w.color)
    i=0
    while w.x<20:
        rate(20)
        w.pos=m
        m.x=m.x+1
        m.y=m.y+1
        l4.pos=m
    label4=label(text="refracted ray",pos=vector(15,-5,0),color=color.white,opacity=100)
    w.visible=False
##########################################SOLAR SYSTEM############################################

#function to show the orbital bath of various planets in solar system

def solarsystem():
    
 scene=display(title='planet earth around sun',width=1000,height=1000,range=(40000,40000,40000),center=(0,0,0))
 scene.autoscale=True

 scene.text='Solar System'                                #to displat text on screen
 sss=sphere(pos=(-500,500,0),radius=5,color=color.white)
 labeld=label(pos=sss.pos,text="Solar System",color=color.green,opacity=100)

 sun=sphere(pos=(0,0,0),radius=100,material=materials.marble,color=color.yellow)
 labeld=label(pos=sun.pos,text="Sun",color=color.white,opacity=100)
 mercury=sphere(pos=(130,0,0),radius=5,material=materials.rough,color=color.white,make_trail=true)
 mercuryv=vector(0,3,5)
 venus=sphere(pos=(170,0,0),radius=10,material=materials.wood,color=color.orange,make_trail=true)
 venusv=vector(0,4,3)
 earth=sphere(pos=(220,0,0),radius=20,material=materials.BlueMarble,make_trail=true)
 earthv=vector(0,0,5)
 labeld=label(pos=earth.pos,text="Earth",color=color.white,opacity=0)
 mars=sphere(pos=(270,0,0),radius=13,material=materials.rough,color=color.red,make_trail=true)
 marsv=vector(0,2,4)
 jupiter=sphere(pos=(370,0,0),radius=60,material=materials.marble,color=color.white,make_trail=true)
 jupiterv=vector(0,1.5,3.5)
 labeld=label(pos=jupiter.pos,text="Jupiter",color=color.white,opacity=0)
 saturn=sphere(pos=(500,0,0),radius=45,material=materials.marble,color=color.blue,make_trail=true)
 saturnv=vector(0,1,3)
 neptune=sphere(pos=(640,0,0),radius=20,material=materials.plastic,color=color.magenta,make_trail=true)
 neptunev=vector(0,.9,2.5)

 for i in range(100000):
    rate(20)
    mercury.pos= mercury.pos+mercuryv
    dist=(mercury.x**2+mercury.y**2+mercury.z**2)**0.5            #ditance=(a**2+b**2+c**2)**0.5
    RadialVector=(mercury.pos - sun.pos)/dist                     #position vector =(initial_pos-final_pos)/2
    Fgrav=-10000*RadialVector/dist**2                             #force due to gravity=(G*m1*m2/(distance**2))
    mercuryv=mercuryv+Fgrav                                                  #G= gravitational force
    mercury.pos +=mercuryv                                                   #m1 and m2 are masses of the two bodies
    venus.pos= venus.pos+venusv
    dist=(venus.x**2+venus.y**2+venus.z**2)**0.5
    RadialVector=(venus.pos - sun.pos)/dist
    Fgrav=-10000*RadialVector/dist**2
    venusv=venusv+Fgrav
    venus.pos +=venusv
    earth.pos= earth.pos+earthv
    dist=(earth.x**2+earth.y**2+earth.z**2)**0.5
    RadialVector=(earth.pos - sun.pos)/dist
    Fgrav=-10000*RadialVector/dist**2
    earthv=earthv+Fgrav
    earth.pos +=earthv
    mars.pos= mars.pos+marsv
    dist=(mars.x**2+mars.y**2+mars.z**2)**0.5
    RadialVector=(mars.pos - sun.pos)/dist
    Fgrav=-10000*RadialVector/dist**2
    marsv=marsv+Fgrav
    mars.pos +=marsv
    jupiter.pos= jupiter.pos+jupiterv
    dist=(jupiter.x**2+jupiter.y**2+jupiter.z**2)**0.5
    RadialVector=(jupiter.pos - sun.pos)/dist
    Fgrav=-10000*RadialVector/dist**2
    jupiterv=jupiterv+Fgrav
    jupiter.pos +=jupiterv
    saturn.pos=saturn.pos+saturnv
    dist=(saturn.x**2+saturn.y**2+saturn.z**2)**0.5
    RadialVector=(saturn.pos - sun.pos)/dist
    Fgrav=-10000*RadialVector/dist**2
    saturnv=saturnv+Fgrav
    saturn.pos +=saturnv
    neptune.pos= neptune.pos+neptunev
    dist=(neptune.x**2+neptune.y**2+neptune.z**2)**0.5
    RadialVector=(neptune.pos - sun.pos)/dist
    Fgrav=-10000*RadialVector/dist**2
    neptunev=neptunev+Fgrav
    neptune.pos +=neptunev
    if dist <= sun.radius: break

#######################################SOLAR ECLIPSE###########################################

#function to show the formation of solar eclipse

def eclipse():

    import math
    window = display(x=0,y=0,height=1200,width=1200,background = color.black)

    lamp = local_light(pos=(0,0,0), color=color.orange)
    sun = sphere(pos = vector(0,0,0),radius = 20,color = color.orange)
    earth = sphere(pos = vector(10,0,0), radius = 10,axis = (1,0,0),material=materials.earth, interval = 5,make_tail=true)
    moon = sphere(pos=vector(12,0,12),radius = 2.5, color = (0.96,0.96,0.96))
    tx=text(text='My text is\ngreen',align='center', depth=-0.3, color=color.green)
    i=0
    j=0
    t=0
    while t<1080:
        rate(100)
    
        i= i + ((2*pi)/365)
        j= j + ((2*pi)/28)

        x = 100*cos(i)
        z = 100*sin(i)
        earth.pos = (x,0,z)

        moon.pos.x = earth.pos.x + 20*cos(j)
        moon.pos.z = earth.pos.z + 20*sin(j)

        earth.rotate(angle=pi/60, axis=(0,1,0),origin=earth.pos)
        sun.rotate(angle=pi/60,axis=(0,1,0),origin=sun.pos)
        t+=1

##################################SATELLITES OF EARTH##################################

#function to show the two satellites of earth

def satellite():
    
 x = arrow( color=color.red)

 tip = label( text="EARTH", space=0.1, pos=(0,0), opacity=0.5)
 x = arrow( color=color.red)

 tip = label( text="LEO", space=0.1, pos=(-5e10,0), opacity=0.5)
 x = arrow( color=color.red)

 tip = label( text="GEO", space=0.1, pos=(2.5e11,0), opacity=0.5)

 G = 6.7e-11 
 earth = sphere(pos=(0,0,0),radius= 3e10,material=materials.earth)
 leo= sphere(pos=(-5e10,0,0), radius=2e10, color=color.white, interval=10, retain=200,make_trail=True)
 leo.mass = 2e30
 leo.p = vector(0, 0, -1e4) * leo.mass

 geo = sphere(pos=(2.5e11,0,0), radius=1e10, color=color.white,interval=10, retain=200,make_trail=True)
 geo.mass = 1e30
 geo.p = -leo.p

 dt = 1e5

 while True:
  rate(50)

  dist = geo.pos - leo.pos
  force = G * leo.mass * leo.mass * dist / mag(dist)**3
  leo.p = leo.p + force*dt
  geo.p = geo.p - force*dt

  for star in [leo, geo]:
    star.pos = star.pos + star.p/star.mass * dt
  earth.rotate(angle=pi/60,axis=(0,1,0),origin=earth.pos)



###############################                        ##########################
###############################GRAPHICAL USER INTERFACE##########################
###############################                        ##########################


gui=Tk()
gui.title("SMART PHYSICS")
gui.geometry("650x400+200+200")
b1=Button(gui,text="Dispersion",command=dispersion)
b1.pack(padx=20,pady=20)
b2=Button(gui,text="Light Behaviour",command=light_travel)
b2.pack(padx=20,pady=20)
b3=Button(gui,text="Solar System",command=solarsystem)
b3.pack(padx=20,pady=20)
b4=Button(gui,text="Eclipse",command=eclipse)
b4.pack(padx=20,pady=20)
b5=Button(gui,text="Satellite",command=satellite)
b5.pack(padx=20,pady=20)
gui.mainloop()


    
#*****************************************THANKYOU************************************#        
        
