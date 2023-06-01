from pandas import read_csv
from anastruct import SystemElements
from tkinter import messagebox

se=SystemElements()

def show_model():
    #Reading and processing prepared node data
    try:
        nodes=read_csv('input\\nodes.csv')
        nodes['node_id'] = nodes['node_id'].str.replace('N', '').astype(int)
    except:
        messagebox.showinfo("Message", "Perform skeleton drawing first!")
    
    #Reading and processing element data
    try:
        elements=read_csv('input\\elements.csv')
        elements['element_id'] = elements['element_id'].str.replace('E', '').astype(int)
    except:
        messagebox.showinfo("Message", "Perform skeleton drawing first!")   
    
    #Reading and processing support conditions
    try:
        supports=read_csv('input\\supports.csv')
        supports['Node'] = supports['Node'].str.replace('N', '').astype(int)
    except:
        messagebox.showinfo("Message", "Define support conditions first!") 
    
    #Importing point loads and moments
    try:
        node_load=read_csv('input\\node_load.csv')
        node_load['Node'] = node_load['Node'].str.replace('N', '').astype(int)
        node_load.fillna(0, inplace=True)
    except:
        messagebox.showinfo("Message", "You have not worked for nodal loads!")
    
    #importing UDL
    try:
        element_load=read_csv('input\\udl.csv')
        element_load['Element'] = element_load['Element'].str.replace('E', '').astype(int)
    except:
        messagebox.showinfo("Message", "You have not worked for UDL loads!")
    
    
    
    #Creating members
    for i in range(len(elements)):
        se.add_element(location=[[elements.x1[i],elements.y1[i]],[elements.x2[i],elements.y2[i]]])
        
    #Creating supports
    
    for i in range(len(supports)):
        if supports.Support[i]=='Fixed':
            se.add_support_fixed(node_id=supports.Node[i])
        elif supports.Support[i]=='Hinged':
            se.add_support_hinged(node_id=supports.Node[i])
        elif supports.Support[i]=='Roller':
            se.add_support_roll(node_id=supports.Node[i])
        elif supports.Support[i]=='Internal Hinge':
            se.add_internal_hinge(node_id=supports.Node[i])
        else:
            pass
    
    #assigning point loads and moments
    for i in range(len(node_load)):
        if node_load.Force_kN[i]!=0:
            se.point_load(node_id=node_load.Node[i],Fx=node_load.Force_kN[i],rotation=node_load.Angle_Degrees[i])
        if node_load.Moment_kNm[i]!=0:
            se.moment_load(node_id=node_load.Node[i], Ty=node_load.Moment_kNm[i])
    
    #assigning element load
    for i in range(len(element_load)):
        se.q_load(q=element_load.UDL[i],element_id=element_load.Element[i],rotation=360-element_load.Angle[i])
    
    se.solve() 
    se.show_structure()
#%%_________________________________________________________________________
#def run_analysis():
    #se.solve()   
def show_reaction():
    se.show_reaction_force()
def show_afd():
    se.show_axial_force()
def show_sfd():
    se.show_shear_force()
def show_bmd():
    se.show_bending_moment()
def show_deflected_shape():
    se.show_displacement()
