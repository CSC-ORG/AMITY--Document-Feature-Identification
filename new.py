import nltk
import os
from Category import retrieve,directoryScan

matter=directoryScan.give_file()
retrieve.categorization(matter)