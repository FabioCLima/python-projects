"""Examples of importing modules and global identifiers"""

import sys
sys.path.append("..")

# Import an entire module
from tests import helpers

# Access names in that module following  the dot
helpers.shout("This functionality was imported")

