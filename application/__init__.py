import os
from .speakers import ChildSpeaker
from .translators import HumanTranslator
from .filehandling import Files

app_path = os.path.dirname(os.path.abspath(__file__))
input_folder_path = os.path.join(app_path, 'INPUT')
output_folder_path = os.path.join(app_path, 'OUTPUT')
