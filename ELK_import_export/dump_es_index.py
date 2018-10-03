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

def save_file(filename, text):
    with open(os.path.normpath(currentdir +'/index/'+ filename), 'wb') as f:
        if type(text) == type({}):
            f.write(json.dumps(text))
        else:
            f.write(text)   

def dump_index(index_name, doc_type=None):
    if doc_type is None:
        doc_type = index_name        
    doc_id_list = es_dbc.get_all_doc_list(index_name)
    i = 0 
    count = len(doc_id_list)    
    doc_list = {}
    for doc_id in doc_id_list:
        i += 1
        doc = es_dbc.get_doc_id(doc_id, index_name, doc_type)
        doc_list[doc_id] = doc
        print i,'/',count
     
    save_file('{}_index.json'.format(index_name), doc_list)            

                
if __name__ == '__main__':
    logger = Logger("dump_index")

    es_dbc = ES_DB_Connector()

    dump_index(SIGMA_DOC_INDEX_NAME)
     
    
   