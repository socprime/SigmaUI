rs





 
Message List
Loading history...

Artur Golovko [3:22 PM]
kibana/socprime_sigma_ui/package.json

Roman Starenky [3:26 PM]
PDF 
Sigma UI for Kibana Installation Guide (3).pdf
497 kB PDF

Roman Starenky [8:20 AM]
Доброе утро. Я попал в большую пробку. Опоздаю минут на 25-30 ( прошу прощения

Artur Golovko [8:21 AM]
Привет. А попал потому что выехал позже ) Ок.

Artur Golovko [11:57 AM]
https://github.com/Cyb3rWard0g/HELK
GitHub
Cyb3rWard0g/HELK
The Hunting ELK. Contribute to Cyb3rWard0g/HELK development by creating an account on GitHub.

Artur Golovko [12:21 PM]
Pasted image at 2018-10-03, 12:21 PM 


Roman Starenky [12:55 PM]
Binary 
resources.rar
184 kB Binary
README.md 
# Sigma-UI
​
In the last months observed a growth of online platforms that allow webmasters to install coin miners into their websites as an alternative means of monetization. For a long time now, cybercriminals have taken advantage of cryptocurrency mining in order to make a profit. However, they generally use malware or potentially unwanted applications they install on the victim’s machine. In this particular case, the mining is performed directly within the browser when the user browses to certain websites. Thus, there is no need to infect the victim’s machine or to exploit vulnerabilities. All that is needed is a browser with JavaScript activated, which is the default state of most browsers. Even if it can be considered as an alternative to traditional ads, this behavior is unwanted when there is no user consent. The New Jersey Division of Consumer Affairs considered that mining bitcoins on a user’s machine without consent is equivalent to gaining access to the computer. Thus, the developers of such services should advertise it clearly before starting mining, which is clearly not the case in a distribution scheme using malvertising. Web Mining Detector basic package is a set of correlation rules and dashboard that enables detection of malicious communications with online JavaScript miners distribution platforms.
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
​
​
#### 1. Copy the file sigma-ui-xxxxx.zip to Kibana server and run the command:
​
```sh
/usr/share/kibana/bin/./kibana-plugin install file:///PATH_TO_FILE/sigma-ui-xxxxx.zip
```
Wait until the installation finishes, it may take few minutes to optimize and cache browser
bundles. Restart Kibana to apply the changes
> If you get error: “Plugin installation was unsuccessful due to error "Incorrect Kibana version in
plugin [sigmaui]. Expected [6.2.2]; found [6.2.1]“, please open zip archive and modify file
“. /kibana/socprime_sigma_ui/package.json”: put version of your Kibana to field "version"
​
​
### 2. **Restart Kibana** to apply the changes.
​
>In case after restart Kibana you don’t see any changes, go to /usr/share/kibana/optimize.
Delete all files in the folder ‘optimize’ including subfolders. And restart Kibana.This will make
Kibana to refresh it’s cache.
​
### 3. Sigma UI plugin is using indices:
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
### 4. Now you can use Sigma UI plugin.
# TO-Do
​
- [X] ...
- [ ] ...
​
Collapse 

Message Input

Message @Roman Starenky 
