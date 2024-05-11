#!/usr/bin/python

import streamlit as st 
output = []
select = st.multiselect("please select", ['bio/ABySS/2.2.5-foss-2020b',
'bio/AUGUSTUS/3.4.0-foss-2020b',
 'bio/AlphaFold/2.0.1-fosscuda-2020b',
 'bio/AlphaFold/2.1.1-fosscuda-2020b',
 'bio/AlphaFold/2.2.0-fosscuda-2020b',
 'bio/BCFtools/1.11-GCC-10.2.0',
 'bio/BLAST/2.11.0-Linux_x86_64',
 'bio/BLAST/2.12.0-Linux_x86_64',
 'bio/BLAST+/2.11.0-gompi-2020b',
 'bio/BUSCO/4.1.4-foss-2020b'])
if select:
  intend = st.multiselect("please select", ['ABySS/2.2.5-foss-2020b',
 'AUGUSTUS/3.4.0-foss-2020b'])
if len(select) and len(intend) != 0:
  output.append([select,intend])
out = output 
st.selectbox("listed", out)
  

