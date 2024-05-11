import streamlit as st

selected = st.selectbox("select the list of the modules from the available list",["bio","chem", "compiler", "custom", "data", "debugger", "devel", "lang", "lib", "math", "mpi", "numlib", "perf","phys"])
biomodule = {"bio":['bio/ABySS/2.2.5-foss-2020b',
  'bio/AUGUSTUS/3.4.0-foss-2020b',
  'bio/AlphaFold/2.0.1-fosscuda-2020b',
  'bio/AlphaFold/2.1.1-fosscuda-2020b',
  'bio/AlphaFold/2.2.0-fosscuda-2020b',
  'bio/BCFtools/1.11-GCC-10.2.0',
  'bio/BLAST/2.11.0-Linux_x86_64',
  'bio/BLAST/2.12.0-Linux_x86_64',
  'bio/BLAST+/2.11.0-gompi-2020b',
  'bio/smcpp/1.15.2-foss-2020b'], 
   "chem": ["atl", "atb"]}

if selected == "bio":
  biomode = biomodule["bio"]
  st.selectbox("selected the above",biomode)
#st.multiselect(option)
#select = st.selectbox(option)
