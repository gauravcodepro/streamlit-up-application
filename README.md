# streamlit-up-application
- a web application for intergation into the devops for the Universitat Potsdam. Exporting the image link from the moddle web [moddle](https://moodle2.uni-potsdam.de/pluginfile.php/1/theme_adaptable/logo/1708349742/Unilogo_01_60.png)
- in future you can updated this application using the module listing and i enclose how to do that:
```
for i in $(cat module2.txt | cut -f 1 -d "/" | sort | uniq -c | awk '{ print $2 }'); do grep $i module2.txt > ${i}.listed.modules.txt; done
```

Gaurav  \
Academic Staff Member \
Bioinformatics \
Institute for Biochemistry and Biology \
University of Potsdam \
Potsdam,Germany
