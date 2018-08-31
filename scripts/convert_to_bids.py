import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
from biacpype.biac2bids.generate_json.convert import generate_all_json_files
from biacpype.biac2bids.bxh2bids.run_bxh2bids import bxh_to_bids
from biacpype.biac2bids.clean_names.clean_name import group_sessions
from biacpype.util.constants import set_paths

### CHANGE HERE ###
STUDY_PATH = "/Users/lpjiang/Documents/CBT.01-copy/"
JSON_OUTPUT_PATH = "/Users/lpjiang/Documents/CBT.01-copy/JSONS" 
BIDS_PATH = "/Users/lpjiang/Documents/CBT.01-copy/bids-try"
LOG_PATH = "/Users/lpjiang/Documents/CBT.01-copy/logs"

# ---------pipe begins---------  # 

# set paths
set_paths(STUDY_PATH=STUDY_PATH, JSON_OUTPUT_PATH=JSON_OUTPUT_PATH, BIDS_PATH=BIDS_PATH, LOG_PATH=LOG_PATH)
# generate jsons
generate_all_json_files()
# convert to bids
bxh_to_bids()
# clean up
group_sessions()
