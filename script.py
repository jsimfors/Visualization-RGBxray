import bpy
from mathutils import Color
import numpy as np

 
class ADDONNAME_PT_main_panel(bpy.types.Panel):
    # Class that disorts the color of the x-ray vectors. 
    
    # Step 1: Add labels (will show up in the side menu)
    bl_label = "Make life harder for scientist:"
    bl_idname = "ADDONNAME_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Sneaky stuff'
 
    def draw(self, context):
        layout = self.layout
        layout.operator("addonname.addbasic_operator")
        layout.operator("addonname.addhelp_operator")
 
class ADDONNAME_OT_add_basic(bpy.types.Operator):
    bl_label = "Change the colors"
    bl_idname = "addonname.addbasic_operator"
 
    def execute(self, context):
        # HAND X-RAY
        
        # COLOR 1
        emCol1 = bpy.data.materials["Material.001"].node_tree.nodes["Emission.001"].inputs[0].default_value 
        # Check if no clean RGB value
        rgb_vector = np.array([emCol1[0],emCol1[1],emCol1[2]])
        if(np.linalg.norm(rgb_vector) != 1):
            print("vector does not have length 1")
            # Lets just make it all red
            col1_mixed = (0, 1, 0, emCol1[3])
        else:
            print("vector has length 1!")
            # Lets mix it up
            col1_mixed = (emCol1[1], emCol1[2], emCol1[0], emCol1[3])
        bpy.data.materials["Material.001"].node_tree.nodes["Emission.001"].inputs[0].default_value = col1_mixed
        
        # COLOR 2
        emCol2 = bpy.data.materials["Material.001"].node_tree.nodes["Emission.002"].inputs[0].default_value
        # Check if no clean RGB value
        rgb_vector2 = np.array([emCol2[0],emCol2[1],emCol2[2]])
        if(np.linalg.norm(rgb_vector2) != 1):
            print("vector does not have length 1")
            # Lets just make it all green
            col2_mixed = (1, 0, 0, emCol2[3])
        else:
            print("vector has length 1!")
            # Lets mix it up
            col2_mixed = (emCol2[1], emCol2[2], emCol2[0], emCol2[3])
            
        bpy.data.materials["Material.001"].node_tree.nodes["Emission.002"].inputs[0].default_value = col2_mixed

        # XRAY APPLE
        em2Col1 = bpy.data.materials["apple"].node_tree.nodes["Emission.001"].inputs[0].default_value
        rgb_vector2_1 = np.array([em2Col1[0],em2Col1[1],em2Col1[2]])
        if(np.linalg.norm(rgb_vector2_1) != 1):
            print("vector does not have length 1")
            # Lets just make it all red
            em2col1_mixed = (0, 1, 0, em2Col1[3])
        else:
            print("vector has length 1!")
            # Lets mix it up
            em2col1_mixed = (em2Col1[1], em2Col1[2], em2Col1[0], em2Col1[3])
        bpy.data.materials["apple"].node_tree.nodes["Emission.001"].inputs[0].default_value = em2col1_mixed
        
        # COLOR 2
        em2Col2 = bpy.data.materials["apple"].node_tree.nodes["Emission.002"].inputs[0].default_value
        rgb_vector2_2 = np.array([em2Col2[0],em2Col2[1],em2Col2[2]])
        if(np.linalg.norm(rgb_vector2_2) != 1):
            print("vector does not have length 1")
            # Lets just make it all red
            em2col2_mixed = (1, 0, 0, em2Col2[3])
        else:
            print("vector has length 1!")
            # Lets mix it up
            em2col2_mixed = (em2Col2[1], em2Col2[2], em2Col2[0], em2Col2[3])
           
        bpy.data.materials["apple"].node_tree.nodes["Emission.002"].inputs[0].default_value = em2col2_mixed


        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
   
class ADDONNAME_OT_add_help(bpy.types.Operator):
    # changes the color of the background plane
    bl_label = "Change background"
    bl_idname = "addonname.addhelp_operator"
    
    def execute(self, context):
        # REMOVE CURRENT LAYER MASKS ON PLANE
        #Get the material you want (replace the name below)
        plane_mat = bpy.data.materials['Material.plane']

        #Remove it
        try:
            plane_mat.node_tree.nodes.remove(plane_mat.node_tree.nodes["Mix Shader"])
            plane_mat.node_tree.nodes.remove(plane_mat.node_tree.nodes["RGB"])
            plane_mat.node_tree.nodes.remove(plane_mat.node_tree.nodes["Light Path"])
            # LINK BSDF to Output, so we can change color:
            principled_bsdf = bpy.data.materials["Material.plane"].node_tree.nodes["Principled BSDF"]
            matOutput = bpy.data.materials["Material.plane"].node_tree.nodes["Material Output"]
            bpy.data.materials['Material.plane'].node_tree.links.new(principled_bsdf.outputs[0], matOutput.inputs[0]) 
        except:
            print("Nothing to delete")
        
        
        # CHANGE COLOR PLANE
        current_background = bpy.data.materials["Material.plane"].node_tree.nodes["Principled BSDF"].inputs[0].default_value
        print(current_background)
        current_value = (current_background[0], current_background[1], current_background[2], current_background[3])
        if(current_value == (1, 0, 0, 1)):
            bpy.data.materials["Material.plane"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0, 1, 0, 1)
        else:
            bpy.data.materials["Material.plane"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 0, 0, 1)
            

        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)



class ADDONNAME_PT_second_main_panel(bpy.types.Panel):
    bl_label = "Make things right"
    bl_idname = "ADDONNAME_PT_second_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Fixes'
 
    def draw(self, context):
        layout = self.layout
        layout.operator("addonname.addsecondbasic_operator")
 

class ADDONNAME_OT_add_second_basic(bpy.types.Operator):
    bl_label = "Bring in new glasses"
    bl_idname = "addonname.addsecondbasic_operator"
    
    def execute(self, context):
        print("Fixing ...")
        # STEP 1: Fix emissions:
        bpy.data.materials["Material.001"].node_tree.nodes["Emission.001"].inputs[0].default_value = (0, 0, 1, 1)
        bpy.data.materials["Material.001"].node_tree.nodes["Emission.002"].inputs[0].default_value = (1, 0.5, 0,  1)
        bpy.data.materials["apple"].node_tree.nodes["Emission.001"].inputs[0].default_value = (0, 0, 1,  1)
        bpy.data.materials["apple"].node_tree.nodes["Emission.002"].inputs[0].default_value = (1, 0.5, 0,  1)
        
         
        # STEP 2: Fix emission color background
        
        # ADD AND LINK: MIXER:
        bpy.data.materials['Material.plane'].node_tree.nodes.new("ShaderNodeMixShader")
        principled_bsdf = bpy.data.materials["Material.plane"].node_tree.nodes["Principled BSDF"]
        shadeMixer = bpy.data.materials["Material.plane"].node_tree.nodes["Mix Shader"]
        bpy.data.materials['Material.plane'].node_tree.links.new(principled_bsdf.outputs[0], shadeMixer.inputs[1]) 
        matOutput = bpy.data.materials["Material.plane"].node_tree.nodes["Material Output"]
        bpy.data.materials['Material.plane'].node_tree.links.new(shadeMixer.outputs[0], matOutput.inputs[0]) 
       
        # ADD AND LINK: RGB (New background color)
        bpy.data.materials['Material.plane'].node_tree.nodes.new("ShaderNodeRGB")
        RGBNode = bpy.data.materials["Material.plane"].node_tree.nodes["RGB"]
        RGBNode.outputs[0].default_value = (0.002, 0.002, 0.005, 1)
        #shadeMixer = bpy.data.materials["Material.plane"].node_tree.nodes["Mix Shader"]
        bpy.data.materials['Material.plane'].node_tree.links.new(RGBNode.outputs[0], shadeMixer.inputs[2]) 
       
        # ADD AND LINK: Light path node (The layer mask)
        bpy.data.materials["Material.plane"].node_tree.nodes.new('ShaderNodeLightPath')
        lightPathNode = bpy.data.materials["Material.plane"].node_tree.nodes["Light Path"]
        bpy.data.materials['Material.plane'].node_tree.links.new(lightPathNode.outputs[6], shadeMixer.inputs[0]) 
       
         
        # STEP 3: Animate glasses (New in and old out)
        
        # Remove old glasses:
        obj1 = bpy.data.objects["glasses"]
        obj1.location = (0, -1, -20)
        
        
        for i in range(0, 100):
            obj2 = bpy.data.objects["fixing_glasses"]
            if(i<51):
                obj2.location = (0, -1, (50-i)/20)
            else:
                obj2.location = (0, -1, 0)
            obj2.keyframe_insert(data_path="location", frame=i)
            
        obj2.location = (0, -1, 0)
        obj2.keyframe_insert(data_path="location", frame=100)
        bpy.context.scene.frame_set(1)

        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    


classes = [ADDONNAME_PT_main_panel, ADDONNAME_OT_add_basic, ADDONNAME_OT_add_help,  ADDONNAME_PT_second_main_panel, ADDONNAME_OT_add_second_basic]
 
 
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
 
 
 
if __name__ == "__main__":
    register()