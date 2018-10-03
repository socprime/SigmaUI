# Sigma UI
​
SIGMA UI is a free open-source application based on the Elastic stack and Sigma Converter (sigmac). It simplifies development, use and sharing of Sigma, a generic rule format for SIEM systems. It is now possible to write, update and export Sigma rules straight from Kibana web UI for all supported Sigma backends including: Elastic stack, ArcSight, QRadar, Splunk, Qualys, Logpoint, Graylog and Windows Defender ATP. If you’re using the Elastic stack for threat hunting purposes or as a primary SIEM, SIGMA UI has capabilities to drill-down directly from a rule to a search in Discover section of Kibana. Community Sigma rules are included with the application. Integration with Sigma official Github and SOC Prime TDM repositories in on the short-term roadmap.
​

![alt text](resources/images/sigmaui.png "Sigma-UI")

​
Sigma UI isusing **sigmac** script to convert sigma to different SIEM languages. It requires
**python3** with libraries:
```sh
PyYAML>=3.11
```
Details: https://github.com/Neo23x0/sigma/tree/master/tools
## To install Sigma UI plugin for your Kibana ###
##### 1. Copy the file sigma-ui-xxxxx.zip to Kibana server and run the command:
```sh
/usr/share/kibana/bin/./kibana-plugin install file:///PATH_TO_FILE/sigma-ui-xxxxx.zip
```
Wait until the installation finishes, it may take few minutes to optimize and cache browser
bundles. Restart Kibana to apply the changes
> If you get error: “Plugin installation was unsuccessful due to error "Incorrect Kibana version in
plugin [sigmaui]. Expected [6.2.2]; found [6.2.1]“, please open zip archive and modify file
“. /kibana/socprime_sigma_ui/package.json”: put version of your Kibana to field "version"
​
#### 2. **Restart Kibana** to apply the changes.
>In case after restart Kibana you don’t see any changes, go to /usr/share/kibana/optimize.
Delete all files in the folder ‘optimize’ including subfolders. And restart Kibana.This will make
Kibana to refresh it’s cache.
#### 3. Sigma UI plugin is using indices:
  * sigma_doc” - for sigma documents;
​
Create index templates for these index from file **[index_template_sigme_doc.txt]**
To fill sigma docs and to index:
Copy to server which has access to Elasticsearch **database file sigma_import.zip**
- Unzip archive **sigma_import.zip**
- Modify script **es_config.py**, put there Elasticsearch hostname, user and password.
- Run command
```sh
python /PATH_TO_FILE/import_es_index.py
```
Indices will be created and filled with sigma rules.
#### 4. Now you can use Sigma UI plugin.
### TO-Do
- [X] ...
- [ ] ...
​

