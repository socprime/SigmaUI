ES_host = ['localhost']
ES_http_auth = None #('login', 'password')
ES_port = 9200
ES_scheme = "http" # "http" or "https"

### if X-Pack is NOT installed
### use these configs
#ES_use_ssl=False
#ES_verify_certs=False
#ES_ca_certs=None

### if X-Pack IS installed
## use these configs
#ES_use_ssl=True
### make sure we verify SSL certificates
#ES_verify_certs=True
### provide a path to CA certs on disk
#ES_ca_certs='/path/to/certs/cas.crt'

SIGMA_DOC_INDEX_NAME = "sui_sigma_doc"
