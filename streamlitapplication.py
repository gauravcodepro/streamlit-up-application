#/usr/bin/python3
# Author Gaurav 
# Universitat Potsdam 
# Date 2024-05-3
import streamlit as st

st.set_page_config(
                 page_title="slurm configurator",
                 page_icon="Universitat Potsdam",
                 layout="wide",
                 initial_sidebar_state="expanded",
)
st.markdown("slurm confirgurator for the Universitat Potsdam")
st.markdown("developed by Gaurav Sablok, Academic Staff Member, Bioinformatics, Universitat Potsdam")
st.markdown("generating the slurm configuration for the high performance computing")
name = ''.join(["#","SBATCH"," ","-","J"," "]) \
                            + st.text_input("name")
email = ''.join(["#","SBATCH"," ","-","-","mail"," "]) \
                            + st.text_input("email")
workdir = ''.join(["#","SBATCH"," ","-","-","workdir"," ","="," "]) \
                            + st.text_input("enter_your_working_dir")
core = st.multiselect("select_the_number_of_cores",["32","64","128","256"])
queue = st.multiselect("select_the_queue_name", ['queue1', 'queue2', 'queue3'])
threads = st.multiselect("select_the_number_of_threads", ["12","24","28","32","64","48","56"])
memory = st.multiselect("select_the_amount_of_the_memory", ["24","32","48","56","128","256","512"])
command = st.text_input("Enter_your_server_command")
num_command = st.text_input("please enter the number of the commands \
                                        that you have configured for the slurm run")

file_storage = st.text_input("please enter the file storage")
scratch = st.text_input("please enter the scratch if any")
working_dir = st.text_input("please enter the workingdir")
analysis_dir = st.text_input("please enter the analysis directory")
exportpath = st.text_input("please enter the path to be exported")
moduleload = st.multiselect("select the modules to be loaded", [ "hasing array" ])
top = ''.join(["#","SBATCH","-","p","constraint","=","snb","|","hsw"])
end = ''.join(["#","SBATCH"," ","--","mail","-","type","=","END"])

configuration = st.button("please write the slurm for analysis")

if configuration:
    st.write(f"Your server configuration file written by \
             {name}\n{top}\n{queue}\n{threads}\n{core}\n{memory}\n{workdir}\n{email}\n{end}\n{command}")
    
