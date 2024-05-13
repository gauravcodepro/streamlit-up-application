# streamlit-up-application

- it is a multi page web application specifically for Universitat Potsdam DevOPs. 
- Allows you to view and configure your own slurm configuration.
- Allows you to submit the jobs to the cluster without logging into the server.
- Allows you to see and select the modules.
- Help options are listed on each option for selection. 
- You can browse all the main modules and the sub-modules in the sidebar.
- dynamically updated the selected list to show all the sub modules listed under that module.
- It is hosted on the cloud for access from anywhere: [streamlit-up-configurator](https://sup-application.streamlit.app/)
- New modules will be updated monthly and if you cant find your module then kindly let us know by opening a issue, fork the repository. 
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
 
 - if you leave everything empty then it will give a default configuration file. 
 ![slum configurator1](https://github.com/gauravcodepro/streamlit-up-application/blob/main/slurm1.png)

Gaurav  \
Academic Staff Member \
Bioinformatics \
Institute for Biochemistry and Biology \
University of Potsdam \
Potsdam,Germany
