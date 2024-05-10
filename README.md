# streamlit-up-application
- a web application for intergation into the devops for the Universitat Potsdam. Exporting the image link from the moddle web [moddle](https://moodle2.uni-potsdam.de/pluginfile.php/1/theme_adaptable/logo/1708349742/Unilogo_01_60.png)
- in future you can updated this application using the module listing and i enclose how to do that:
```
for i in $(cat module2.txt | cut -f 1 -d "/" | sort | uniq -c | awk '{ print $2 }'); do grep $i module2.txt > ${i}.listed.modules.txt; done
```
 To run this:

 ![slum configurator1](https://github.com/gauravcodepro/streamlit-up-application/blob/main/slurm_1.png)
 ![slurm configurator2](https://github.com/gauravcodepro/streamlit-up-application/blob/main/slurm_2.png)
 ![slurm configurator3](https://github.com/gauravcodepro/streamlit-up-application/blob/main/slurm_3.png)

 - No need of any modules files to load. Just select your module and it will dynamixally updated the selected list to show all the sub modules listed under that module.

Gaurav  \
Academic Staff Member \
Bioinformatics \
Institute for Biochemistry and Biology \
University of Potsdam \
Potsdam,Germany
