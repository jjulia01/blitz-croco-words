import os
from pptx import Presentation
current_file=os.path.realpath(__file__)
current_directory=os.path.dirname(current_file)
print(current_file) 
prs = Presentation('Osennyaya_igra_3.pptx')