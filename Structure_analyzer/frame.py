import os
import solver
cwd=os.getcwd()

def draw():
    import Draw_skeleton
def assign_pload():
    import node_load
def assign_dload():
    import udl
def assign_support():
    import supports
def preview_solve():
    solver.show_model()
def solve():
    solver.run_analysis()
    print('Solved successfully !!\nuse following commands \nframe.RD() to see Reaction Diagram\nframe.AFD() to see Axial Force Diagram\nframe.SFD() to see Shear Force Diagram\nframe.BMD() to see Bending Moment Diagram and\nframe.DSD() to see Deformed Shape Diagram')
def RD():
    solver.show_reaction()
def AFD():
    solver.show_afd()
def SFD():
    solver.show_sfd()
def BMD():
    solver.show_bmd() 
def DSD():
    solver.show_deflected_shape() 
print("success")