# Natalia Raz

import nuke

def set_current_frame_as_in_frame():
    current_frame = nuke.frame()  # Get the current frame
    selected_node = nuke.selectedNode()  # Get the selected node
    if selected_node.Class() == "FrameRange":
        selected_node['first_frame'].setValue(current_frame)
    else:
        nuke.message("The selected node is not a FrameRange node")

# Call the function
set_current_frame_as_in_frame()
