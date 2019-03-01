# -*- coding: utf-8 -*-
#!/usr/bin/env python

################################################################################
# License text
################################################################################

__author__ = 'Nikolay Trofimyuk'
__version__ = '1.0'

from elasticsearch import Elasticsearch
from es_config import *

class ES_DB_Connector(object):

    def __init__(self):
        self.es = Elasticsearch(
            ES_host,
            http_auth=ES_http_auth,
            scheme=ES_scheme,
            port=ES_port,

## uncomment if X-pack installed           
#            use_ssl=ES_use_ssl,
#            verify_certs=ES_verify_certs,
#            ca_certs=ES_ca_certs
        )

    def get_all_doc_list(self, index):
        query = {
            "size": 10000,
            "_source": ["_id"]
            }
        try:
            res = self.es.search(index=index, body=query)
            sigma_doc_list = []
            for hit in res['hits']['hits']:
                sigma_doc_list.append(hit['_id'])
            
            return sigma_doc_list
        except:
            raise   
   
    def get_doc_id(self, doc_id, index, doc_type=None):
        if doc_type is None:
            doc_type = index
        try:
            res = self.es.get(index=index, doc_type=doc_type, id=doc_id)
            return res["_source"]
        except:
            raise Exception('Not found doc with id: {}'.format(doc_id))      
                          
    def insert_doc(self, index, doc_id, doc):
        res = self.es.index(index=index, doc_type=index, id=doc_id, body=doc)

    def delete_index(self, index):
        return self.es.indices.delete(index=index, ignore=[400, 404]) 
           
if __name__ == "__main__":
    es = ES_DB_Connector()
    
    print es.get_all_doc_list(SIGMA_DOC_INDEX_NAME)
    
        