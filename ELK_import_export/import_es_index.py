# -*- coding: utf-8 -*-
#!/usr/bin/env python

################################################################################
# License text
################################################################################

__author__ = 'Nikolay Trofimyuk'
__version__ = '1.0'

import os
import json

from logger import Logger
from es_db_connector import ES_DB_Connector
from es_config import *

currentdir = os.path.dirname(os.path.abspath(__file__))

def load_file(filename):
    with open(os.path.normpath(currentdir +'/index/'+ filename), 'rb') as f:
        return json.load(f)       
         
def import_index(filename, index_name):    
    doc_list = load_file(filename)
    print es_dbc.delete_index(index_name)
    i, ln = 0, len(doc_list) 
    for doc_id, doc in doc_list.iteritems():
        i += 1
        print i,'/',ln, doc_id 
        es_dbc.insert_doc(index_name, doc_id, doc)   
        
        
if __name__ == '__main__':
    logger = Logger("import_index")

    es_dbc = ES_DB_Connector()

    import_index(SIGMA_DOC_INDEX_NAME+'_index.json', SIGMA_DOC_INDEX_NAME)