# streamlit-up-application

- it is a multi page web application specifically for Universitat Potsdam DevOPs. **Updated modules list monthly**
- Allows you to view and configure your own slurm needs.
- Allows you to submit the jobs to the cluster without logging into the server.
- Allows you to see and select the modules.
- No need of the terminal to write your configuration scripts. 
- you can updated this application using the module listing and i enclose how to do that:
```
for i in $(cat module2.txt | cut -f 1 -d "/" | sort | uniq -c | awk '{ print $2 }'); do grep $i module2.txt > ${i}.listed.modules.txt; done
```
- To run this:
```
 pip3 install streamlit
 streamlit run streamlitapplication.py
```
 ![slum configurator1](https://github.com/gauravcodepro/streamlit-up-application/blob/main/slurm.png)

 - No need of any modules files to load. Just select your module and it will dynamically updated the selected list to show all the sub modules listed under that module.
 - You can browse all the main modules and the sub-modules in the sidebar. 
##### Footnotes
 - The complete application is due for release next week 2024-5-14. 
 - Adding the support for the direct job submission. 
 - Adding the support for the job fetcher and log fetcher. 

Gaurav  \
Academic Staff Member \
Bioinformatics \
Institute for Biochemistry and Biology \
University of Potsdam \
Potsdam,Germany
