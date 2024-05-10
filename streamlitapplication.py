#/usr/bin/python3
# Author Gaurav 
# Universitat Potsdam 
# Date 2024-05-10
import streamlit as st

st.set_page_config(
                 page_title="Universitat Potsdam Slurm Configurator",
                 page_icon="Universitat Potsdam",
                 layout="centered",
                 initial_sidebar_state="expanded")
st.image("https://www.uni-potsdam.de/typo3conf/ext/up_template/Resources/Public/Images/logos/up_logo_international_2.png", width = 100)
st.markdown("Universitat Potsdam Slurm Configurator for the Universitat Potsdam")
st.markdown("Developed by Gaurav Sablok, Academic Staff Member, Bioinformatics, Universitat Potsdam")
st.markdown("Slurm configurator for the high performance computing")
name = st.text_input("enter_your_name")
email = st.text_input("enter_your_email")
workdir = st.text_input("enter_your_working_directory")
core = st.selectbox("select_the_number_of_cores",["32","64","128","256"])
queue = st.selectbox("select_the_queue_name", ['queue1', 'queue2', 'queue3'])
threads = st.selectbox("select_the_number_of_threads", ["12","24","28","32","64","48","56"])
memory = st.selectbox("select_the_amount_of_the_memory", ["24","32","48","56","128","256","512"])
nodes = st.text_input("please enter the number of the nodes")
task = st.text_input("please enter the number of the task")
command = st.text_input("Enter_your_server_command")
file_storage = st.text_input("please enter the file storage")
analysis_dir = st.text_input("please enter the analysis directory")
exportpath = st.text_input("please enter the path to be exported")
selected = st.selectbox("select the list of the modules from the available list", ["bio","chem", "compiler", "custom", "data", "debugger", "devel", "lang", "lib", "math", "mpi", "numlib", "perf","phys","system","toolchain","tools","vis"])
modeavail = {'bio': ['bio/ABySS/2.2.5-foss-2020b',
  'bio/AUGUSTUS/3.4.0-foss-2020b',
  'bio/AlphaFold/2.0.1-fosscuda-2020b',
  'bio/AlphaFold/2.1.1-fosscuda-2020b',
  'bio/AlphaFold/2.2.0-fosscuda-2020b',
  'bio/BCFtools/1.11-GCC-10.2.0',
  'bio/BLAST/2.11.0-Linux_x86_64',
  'bio/BLAST/2.12.0-Linux_x86_64',
  'bio/BLAST+/2.11.0-gompi-2020b',
  'bio/BUSCO/4.1.4-foss-2020b',
  'bio/BUSCO/5.0.0-foss-2020b',
  'bio/BUSCO/5.1.2-foss-2020b',
  'bio/BWA/0.7.17-GCC-10.2.0',
  'bio/BamTools/2.5.1-GCC-10.2.0',
  'bio/Beast/2.5.1-foss-2018b',
  'bio/BioPerl/1.7.8-GCCcore-10.2.0',
  'bio/Biopython/1.78-foss-2020b',
  'bio/Biopython/1.78-fosscuda-2020b',
  'bio/Bowtie/1.2.2-foss-2018b',
  'bio/Bowtie/1.3.0-GCC-10.2.0',
  'bio/Bowtie2/2.3.4.2-foss-2018b',
  'bio/Bowtie2/2.4.2-GCC-10.2.0',
  'bio/CAFE5/5.0.0-GCC-10.2.0',
  'bio/CD-HIT/4.8.1-GCC-10.2.0',
  'bio/Clustal-Omega/1.2.4-foss-2018b',
  'bio/DendroPy/4.5.2-GCCcore-10.2.0',
  'bio/EMBOSS/6.6.0-foss-2018b',
  'bio/Exonerate/2.4.0-GCC-10.2.0',
  'bio/FASTX-Toolkit/0.0.14-GCC-9.3.0',
  'bio/FLASH/2.2.00-foss-2018b',
  'bio/FastQC/0.11.9-Java-1.8',
  'bio/GROMACS/2021.2-fosscuda-2020b',
  'bio/GROMACS/2021.2-fosscuda-2020b-znver1',
  'bio/Gctf/1.06',
  'bio/GenomeThreader/1.7.3-Linux_x86_64-64bit',
  'bio/GenomeTools/1.6.1-GCC-10.2.0',
  'bio/HH-suite/3.3.0-gompic-2020b',
  'bio/HISAT2/2.2.1-gompi-2020b',
  'bio/HMMER/3.3.2-gompi-2020b',
  'bio/HMMER/3.3.2-gompic-2020b',
  'bio/HTSlib/1.11-GCC-10.2.0',
  'bio/HTSlib/1.12-GCC-10.2.0',
  'bio/HyPhy/2.5.1-gompi-2020b',
  'bio/IMAGIC/20100209',
  'bio/IMAGIC/20101031',
  'bio/InterProScan/5.28-67.0-foss-2020b',
  'bio/InterProScan/5.55-88.0-foss-2020b',
  'bio/Jellyfish/2.3.0-GCC-8.3.0',
  'bio/Kalign/3.3.1-GCCcore-10.2.0',
  'bio/Kent_tools/411-GCC-10.2.0',
  'bio/Kraken/1.1.1-GCCcore-10.2.0',
  'bio/Kraken2/2.1.1-gompi-2020b',
  'bio/LTR_retriever/2.9.0-foss-2020b',
  'bio/MAFFT/7.453-GCC-9.3.0-with-extensions',
  'bio/MAFFT/7.475-gompi-2020b-with-extensions',
  'bio/MAKER/3.01.03-foss-2020b',
  'bio/MUMmer/4.0.0beta2-GCCcore-10.2.0',
  'bio/MaxQuant/2.0.3.0-foss-2018b-aot',
  'bio/MaxQuant/2.0.3.0-foss-2018b',
  'bio/MetaEuk/4-GCC-10.2.0',
  'bio/Mothur/1.46.1-foss-2020b',
  'bio/MotionCor2/1.4.2-GCCcore-10.2.0',
  'bio/MrBayes/3.2.7-GCC-10.2.0',
  'bio/NGS/2.10.9-GCCcore-10.2.0',
  'bio/OMA/2.5.0-GCCcore-10.2.0',
  'bio/PAML/4.9j-GCCcore-9.3.0',
  'bio/PHYLIP/3.697-GCC-9.3.0',
  'bio/PLINK/1.9b_6.21-x86_64',
  'bio/PRANK/170427-GCC-9.3.0',
  'bio/RAxML/8.2.12-foss-2020b-pthreads-avx2',
  'bio/RAxML/8.2.12-gompi-2020a-hybrid-avx2',
  'bio/RECON/1.08-GCC-10.2.0',
  'bio/RELION/3.0_beta.2018.08.02-fosscuda-2020b',
  'bio/RELION/3.1.1-fosscuda-2020b',
  'bio/RELION/4.0.0-fosscuda-2020b',
  'bio/RELION/4git1fb5b8f-fosscuda-2020b',
  'bio/RELION/4git44c8b38-fosscuda-2018b',
  'bio/RELION/4git44c8b38-fosscuda-2020b',
  'bio/RELION/4git44c8b38-2-fosscuda-2020b',
  'bio/RMBlast/2.11.0-gompi-2020b',
  'bio/RSEM/1.3.3-foss-2020b',
  'bio/RepeatMasker/4.1.2-p1-foss-2020b',
  'bio/RepeatModeler/2.0.2a-foss-2020b',
  'bio/RepeatScout/1.0.6-GCC-10.2.0',
  'bio/ResMap/1.1.4-Linux_x86_64',
  'bio/SAMtools/1.11-GCC-10.2.0',
  'bio/SAMtools/1.12-GCC-10.2.0',
  'bio/SAMtools/1.15-GCC-10.2.0',
  'bio/SEPP/4.4.0-foss-2020b',
  'bio/SNAP-HMM/20190603-GCC-10.2.0',
  'bio/SRA-Toolkit/2.10.9-gompi-2020b',
  'bio/SRAssembler/1.0.0-foss-2020b',
  'bio/STAR/2.7.7a-GCC-10.2.0',
  'bio/Salmon/1.4.0-gompi-2020b',
  'bio/Stacks/2.54-foss-2020a',
  'bio/TCoffee/13.45.0-GCCcore-10.2.0',
  'bio/TRF/4.09-linux64',
  'bio/TRF/4.09.1-GCCcore-10.2.0',
  'bio/TWL-NINJA/0.97-cluster_only-GCC-10.2.0',
  'bio/Trimmomatic/0.39-Java-1.8',
  'bio/Trinity/2.8.4-foss-2018b',
  'bio/Vmatch/2.3.1-Linux_x86_64-64bit',
  'bio/Vmatch/2.3.1',
  'bio/angsd/0.935-GCC-10.2.0',
  'bio/beta-psmc/git1e9ab32-foss-2020b',
  'bio/ctffind/4.1.14-foss-2020b',
  'bio/ctffind/4.1.14-fosscuda-2020b',
  'bio/ctffind/4.1.14-Linux_x86_64',
  'bio/cutadapt/2.10-GCCcore-9.3.0-Python-3.8.2',
  'bio/dssp/2.3.0-GCC-10.2.0',
  'bio/fastStructure/1.0-foss-2020b-Python-2.7.18',
  'bio/hssp/3.1.5-GCC-10.2.0',
  'bio/mrcfile/1.3.0-fosscuda-2020b',
  'bio/ncbi-vdb/2.10.9-gompi-2020b',
  'bio/phyx/1.3-foss-2020b',
  'bio/prodigal/2.6.3-GCCcore-10.2.0',
  'bio/psmc/0.6.5-foss-2020b',
  'bio/smcpp/1.15.2-foss-2020b'],
 'chem': ['chem/LAMMPS/3Mar2020-foss-2020a-Python-3.8.2-kokkos',
  'chem/PLUMED/2.6.0-foss-2020a-Python-3.8.2',
  'chem/kim-api/2.1.3-foss-2020a',
  'chem/topaz/0.2.5-fosscuda-2020b',
  'chem/yaff/1.6.0-foss-2020a-Python-3.8.2'],
 'compiler': ['compiler/Clang/11.0.1-GCCcore-10.2.0',
  'compiler/Clang/11.0.1-gcccuda-2020b',
  'compiler/GCC/7.3.0-2.30',
  'compiler/GCC/8.3.0',
  'compiler/GCC/9.3.0',
  'compiler/GCC/10.2.0',
  'compiler/GCCcore/7.3.0',
  'compiler/GCCcore/8.3.0',
  'compiler/GCCcore/9.3.0',
  'compiler/GCCcore/10.2.0',
  'compiler/Go/1.13.1',
  'compiler/LLVM/6.0.0-GCCcore-7.3.0',
  'compiler/LLVM/9.0.1-GCCcore-9.3.0',
  'compiler/LLVM/10.0.1-GCCcore-10.2.0',
  'compiler/LLVM/11.0.0-GCCcore-10.2.0'],
 'custom': ['custom/R_umweltgeo/1.0'],
 'data': ['data/CDO/1.9.10-gompi-2020b',
  'data/DB_File/1.855-GCCcore-10.2.0',
  'data/GDAL/3.2.1-foss-2020b',
  'data/GDAL/3.2.1-fosscuda-2020b',
  'data/HDF/4.2.15-GCCcore-10.2.0',
  'data/HDF5/1.10.2-fosscuda-2018b',
  'data/HDF5/1.10.6-gompi-2020a',
  'data/HDF5/1.10.7-gompi-2020b',
  'data/HDF5/1.10.7-gompic-2020b',
  'data/LAME/3.100-GCCcore-9.3.0',
  'data/LAME/3.100-GCCcore-10.2.0',
  'data/MariaDB/10.5.8-GCC-10.2.0',
  'data/PostgreSQL/13.2-GCCcore-10.2.0',
  'data/XML-LibXML/2.0206-GCCcore-10.2.0',
  'data/XML-Parser/2.44_01-GCCcore-7.3.0-Perl-5.28.0',
  'data/dask/2021.2.0-foss-2020b',
  'data/dask/2021.2.0-fosscuda-2020b',
  'data/h5py/2.10.0-foss-2020a-Python-3.8.2',
  'data/h5py/3.1.0-foss-2020b',
  'data/netCDF/4.6.1-fosscuda-2018b',
  'data/netCDF/4.7.4-gompi-2020a',
  'data/netCDF/4.7.4-gompi-2020b',
  'data/netCDF/4.7.4-gompic-2020b',
  'data/scikit-learn/0.23.2-fosscuda-2020b'],
 'debugger': ['debugger/GDB/10.1-GCCcore-10.2.0'],
 'devel': ['devel/Autoconf/2.69-GCCcore-7.3.0',
  'devel/Autoconf/2.69-GCCcore-9.3.0',
  'devel/Autoconf/2.69-GCCcore-10.2.0',
  'devel/Automake/1.16.1-GCCcore-7.3.0',
  'devel/Automake/1.16.1-GCCcore-9.3.0',
  'devel/Automake/1.16.2-GCCcore-10.2.0',
  'devel/Autotools/20180311-GCCcore-7.3.0',
  'devel/Autotools/20180311-GCCcore-9.3.0',
  'devel/Autotools/20200321-GCCcore-10.2.0',
  'devel/Bazel/3.7.2-GCCcore-10.2.0',
  'devel/Boost/1.72.0-gompi-2020a',
  'devel/Boost/1.74.0-GCC-10.2.0',
  'devel/CMake/3.11.4-GCCcore-7.3.0',
  'devel/CMake/3.12.1-GCCcore-7.3.0',
  'devel/CMake/3.16.4-GCCcore-9.3.0',
  'devel/CMake/3.18.4-GCCcore-10.2.0',
  'devel/DBus/1.13.6-GCCcore-7.3.0',
  'devel/DBus/1.13.12-GCCcore-9.3.0',
  'devel/DBus/1.13.18-GCCcore-10.2.0',
  'devel/Doxygen/1.8.14-GCCcore-7.3.0',
  'devel/Doxygen/1.8.17-GCCcore-9.3.0',
  'devel/Doxygen/1.8.20-GCCcore-10.2.0',
  'devel/GConf/3.2.6-GCCcore-10.2.0',
  'devel/GObject-Introspection/1.54.1-fosscuda-2018b-Python-2.7.15',
  'devel/GObject-Introspection/1.66.1-GCCcore-10.2.0',
  'devel/JUnit/4.12-Java-1.8',
  'devel/LZO/2.10-GCCcore-10.2.0',
  'devel/LevelDB/1.22-GCCcore-10.2.0',
  'devel/M4/1.4.17',
  'devel/M4/1.4.18-GCCcore-7.3.0',
  'devel/M4/1.4.18-GCCcore-8.3.0',
  'devel/M4/1.4.18-GCCcore-9.3.0',
  'devel/M4/1.4.18-GCCcore-10.2.0',
  'devel/M4/1.4.18',
  'devel/Mako/1.0.7-fosscuda-2018b-Python-2.7.15',
  'devel/Mako/1.1.2-GCCcore-9.3.0',
  'devel/Mako/1.1.3-GCCcore-10.2.0',
  'devel/Maven/3.6.3',
  'devel/PCRE/8.41-GCCcore-7.3.0',
  'devel/PCRE/8.44-GCCcore-9.3.0',
  'devel/PCRE/8.44-GCCcore-10.2.0',
  'devel/PCRE2/10.34-GCCcore-9.3.0',
  'devel/PCRE2/10.35-GCCcore-10.2.0',
  'devel/PyTorch/1.7.1-fosscuda-2020b',
  'devel/Qt5/5.10.1-fosscuda-2018b',
  'devel/Qt5/5.14.1-GCCcore-9.3.0',
  'devel/Qt5/5.14.2-GCCcore-10.2.0',
  'devel/SQLite/3.24.0-GCCcore-7.3.0',
  'devel/SQLite/3.31.1-GCCcore-9.3.0',
  'devel/SQLite/3.33.0-GCCcore-10.2.0',
  'devel/SWIG/4.0.2-GCCcore-10.2.0',
  'devel/ZeroMQ/4.3.2-GCCcore-9.3.0',
  'devel/ZeroMQ/4.3.3-GCCcore-10.2.0',
  'devel/ant/1.10.1-Java-1.8',
  'devel/ant/1.10.5-Java-1.8',
  'devel/ant/1.10.8-Java-11',
  'devel/ant/1.10.9-Java-11',
  'devel/dbus-glib/0.110-GCCcore-10.2.0',
  'devel/flatbuffers/1.12.0-GCCcore-10.2.0',
  'devel/flatbuffers-python/1.12-GCCcore-10.2.0',
  'devel/gflags/2.2.2-GCCcore-10.2.0',
  'devel/glog/0.5.0-GCCcore-10.2.0',
  'devel/gperf/3.1-GCCcore-7.3.0',
  'devel/gperf/3.1-GCCcore-9.3.0',
  'devel/gperf/3.1-GCCcore-10.2.0',
  'devel/intltool/0.51.0-GCCcore-7.3.0-Perl-5.28.0',
  'devel/intltool/0.51.0-GCCcore-9.3.0',
  'devel/intltool/0.51.0-GCCcore-10.2.0',
  'devel/makeinfo/6.7-GCCcore-9.3.0',
  'devel/makeinfo/6.7-GCCcore-10.2.0',
  'devel/ncurses/6.0',
  'devel/ncurses/6.1-GCCcore-7.3.0',
  'devel/ncurses/6.1',
  'devel/ncurses/6.2-GCCcore-9.3.0',
  'devel/ncurses/6.2-GCCcore-10.2.0',
  'devel/ncurses/6.2',
  'devel/nsync/1.24.0-GCCcore-10.2.0',
  'devel/pkg-config/0.29.2-GCCcore-7.3.0',
  'devel/pkg-config/0.29.2-GCCcore-9.3.0',
  'devel/pkg-config/0.29.2-GCCcore-10.2.0',
  'devel/pkgconfig/1.5.1-GCCcore-9.3.0-Python-3.8.2',
  'devel/pkgconfig/1.5.1-GCCcore-10.2.0-python',
  'devel/protobuf/3.14.0-GCCcore-10.2.0',
  'devel/protobuf-python/3.14.0-GCCcore-10.2.0',
  'devel/sparsehash/2.0.4-GCCcore-10.2.0',
  'devel/typing-extensions/3.7.4.3-GCCcore-10.2.0',
  'devel/wget/1.20.3-GCCcore-10.2.0',
  'devel/xorg-macros/1.19.2-GCCcore-7.3.0',
  'devel/xorg-macros/1.19.2-GCCcore-9.3.0',
  'devel/xorg-macros/1.19.2-GCCcore-10.2.0'],
 'lang': ['compiler/Clang/11.0.1-GCCcore-10.2.0',
  'compiler/Clang/11.0.1-gcccuda-2020b',
  'lang/Anaconda2/5.3.0',
  'lang/Anaconda3/2020.11',
  'lang/Anaconda3/2021.05',
  'lang/Bison/3.0.4-GCCcore-7.3.0',
  'lang/Bison/3.0.4',
  'lang/Bison/3.0.5-GCCcore-7.3.0',
  'lang/Bison/3.3.2-GCCcore-8.3.0',
  'lang/Bison/3.3.2',
  'lang/Bison/3.5.3-GCCcore-9.3.0',
  'lang/Bison/3.5.3',
  'lang/Bison/3.7.1-GCCcore-10.2.0',
  'lang/Bison/3.7.1',
  'lang/Cython/0.29.22-GCCcore-10.2.0',
  'lang/FriBidi/1.0.5-GCCcore-7.3.0',
  'lang/FriBidi/1.0.9-GCCcore-9.3.0',
  'lang/FriBidi/1.0.10-GCCcore-10.2.0',
  'lang/Guile/1.8.8-GCCcore-9.3.0',
  'lang/Guile/3.0.7-GCCcore-10.2.0',
  'lang/Java/1.8.0_281',
  'lang/Java/11.0.2',
  'lang/Julia/1.6.1-linux-x86_64',
  'lang/Julia/1.7.3-linux-x86_64',
  'lang/Lua/5.1.5-GCCcore-7.3.0',
  'lang/Lua/5.4.2-GCCcore-10.2.0',
  'lang/Miniconda2/4.7.10',
  'lang/Miniconda3/4.9.2',
  'lang/Mono/6.4.0.198-foss-2018b',
  'lang/NASM/2.13.03-GCCcore-7.3.0',
  'lang/NASM/2.14.02-GCCcore-9.3.0',
  'lang/NASM/2.15.05-GCCcore-10.2.0',
  'lang/Perl/5.28.0-GCCcore-7.3.0',
  'lang/Perl/5.30.2-GCCcore-9.3.0',
  'lang/Perl/5.32.0-GCCcore-10.2.0-minimal',
  'lang/Perl/5.32.0-GCCcore-10.2.0',
  'lang/Python/2.7.15-fosscuda-2018b',
  'lang/Python/2.7.15-GCCcore-7.3.0-bare',
  'lang/Python/2.7.18-GCCcore-9.3.0',
  'lang/Python/2.7.18-GCCcore-10.2.0',
  'lang/Python/3.8.2-GCCcore-9.3.0',
  'lang/Python/3.8.6-GCCcore-10.2.0',
  'lang/R/3.6.3-foss-2020a',
  'lang/R/4.0.0-foss-2020a',
  'lang/R/4.0.3-foss-2020b',
  'lang/R/4.0.3-fosscuda-2020b',
  'lang/R/4.0.4-foss-2020b',
  'lang/Ruby/2.7.2-GCCcore-10.2.0',
  'lang/Rust/1.42.0-GCCcore-9.3.0',
  'lang/SciPy-bundle/2020.03-foss-2020a-Python-3.8.2',
  'lang/SciPy-bundle/2020.11-foss-2020b-Python-2.7.18',
  'lang/SciPy-bundle/2020.11-foss-2020b',
  'lang/SciPy-bundle/2020.11-fosscuda-2020b',
  'lang/Tcl/8.6.8-GCCcore-7.3.0',
  'lang/Tcl/8.6.10-GCCcore-9.3.0',
  'lang/Tcl/8.6.10-GCCcore-10.2.0',
  'lang/Tkinter/2.7.18-GCCcore-10.2.0',
  'lang/Tkinter/3.8.2-GCCcore-9.3.0',
  'lang/Tkinter/3.8.6-GCCcore-10.2.0',
  'lang/Yasm/1.3.0-GCCcore-9.3.0',
  'lang/Yasm/1.3.0-GCCcore-10.2.0',
  'lang/dotNET-SDK/3.1.300-linux-x64',
  'lang/flex/2.6.4-GCCcore-7.3.0',
  'lang/flex/2.6.4-GCCcore-8.3.0',
  'lang/flex/2.6.4-GCCcore-9.3.0',
  'lang/flex/2.6.4-GCCcore-10.2.0',
  'lang/flex/2.6.4',
  'lang/nodejs/12.19.0-GCCcore-10.2.0',
  'lang/numba/0.52.0-foss-2020b',
  'lang/numba/0.52.0-fosscuda-2020b'],
 'lib': ['lib/alsa-lib/1.2.4-GCCcore-10.2.0',
  'lib/argtable/2.13-foss-2018b',
  'lib/double-conversion/3.1.5-GCCcore-9.3.0',
  'lib/double-conversion/3.1.5-GCCcore-10.2.0',
  'lib/gc/7.6.12-GCCcore-10.2.0',
  'lib/giflib/5.2.1-GCCcore-10.2.0',
  'lib/libaio/0.3.112-GCCcore-10.2.0',
  'lib/libdrm/2.4.92-GCCcore-7.3.0',
  'lib/libdrm/2.4.100-GCCcore-9.3.0',
  'lib/libepoxy/1.5.4-GCCcore-10.2.0',
  'lib/libevent/2.1.11-GCCcore-9.3.0',
  'lib/libevent/2.1.12-GCCcore-10.2.0',
  'lib/libfabric/1.11.0-GCCcore-9.3.0',
  'lib/libfabric/1.11.0-GCCcore-10.2.0',
  'lib/libffi/3.3-GCCcore-9.3.0',
  'lib/libgd/2.2.5-GCCcore-7.3.0',
  'lib/libgeotiff/1.6.0-GCCcore-10.2.0',
  'lib/libglvnd/1.2.0-GCCcore-9.3.0',
  'lib/libglvnd/1.3.2-GCCcore-10.2.0',
  'lib/libgpuarray/0.7.6-fosscuda-2020b',
  'lib/libharu/2.3.0-GCCcore-7.3.0',
  'lib/libiconv/1.15-GCCcore-7.3.0',
  'lib/libiconv/1.16-GCCcore-9.3.0',
  'lib/libiconv/1.16-GCCcore-10.2.0',
  'lib/libidn/1.36-GCCcore-10.2.0',
  'lib/libidn2/2.3.0-GCCcore-10.2.0',
  'lib/libjpeg-turbo/2.0.4-GCCcore-9.3.0',
  'lib/libjpeg-turbo/2.0.5-GCCcore-10.2.0',
  'lib/libmatheval/1.1.11-GCCcore-9.3.0',
  'lib/libogg/1.3.4-GCCcore-10.2.0',
  'lib/libpng/1.6.34-GCCcore-7.3.0',
  'lib/libpng/1.6.37-GCCcore-9.3.0',
  'lib/libpsl/0.21.1-GCCcore-10.2.0',
  'lib/libreadline/8.0-GCCcore-9.3.0',
  'lib/libreadline/8.0-GCCcore-10.2.0',
  'lib/libsndfile/1.0.28-GCCcore-10.2.0',
  'lib/libsodium/1.0.18-GCCcore-10.2.0',
  'lib/libspatialite/4.3.0a-foss-2020b-Python-3.8.6',
  'lib/libtasn1/4.16.0-GCCcore-10.2.0',
  'lib/libtirpc/1.3.1-GCCcore-10.2.0',
  'lib/libtool/2.4.6-GCCcore-7.3.0',
  'lib/libtool/2.4.6-GCCcore-9.3.0',
  'lib/libtool/2.4.6-GCCcore-10.2.0',
  'lib/libunistring/0.9.10-GCCcore-10.2.0',
  'lib/libunwind/1.2.1-GCCcore-7.3.0',
  'lib/libunwind/1.3.1-GCCcore-9.3.0',
  'lib/libvorbis/1.3.7-GCCcore-10.2.0',
  'lib/libwebp/1.1.0-GCCcore-10.2.0',
  'lib/libxml2/2.9.8-GCCcore-7.3.0',
  'lib/libxml2/2.9.10-GCCcore-9.3.0',
  'lib/libxml2/2.9.10-GCCcore-10.2.0',
  'lib/libxslt/1.1.34-GCCcore-9.3.0',
  'lib/libxslt/1.1.34-GCCcore-10.2.0',
  'lib/libyaml/0.2.2-GCCcore-9.3.0',
  'lib/libyaml/0.2.5-GCCcore-10.2.0',
  'lib/lxml/4.5.2-GCCcore-9.3.0',
  'lib/lz4/1.9.2-GCCcore-9.3.0',
  'lib/lz4/1.9.2-GCCcore-10.2.0',
  'lib/minizip/2.10.0-GCCcore-10.2.0',
  'lib/nettle/3.4-fosscuda-2018b',
  'lib/nettle/3.6-GCCcore-10.2.0',
  'lib/p11-kit/0.23.22-GCCcore-10.2.0',
  'lib/pocl/1.6-GCC-10.2.0',
  'lib/pocl/1.6-gcccuda-2020b',
  'lib/pybind11/2.4.3-GCCcore-9.3.0-Python-3.8.2',
  'lib/pybind11/2.6.0-GCCcore-10.2.0',
  'lib/scikit-build/0.11.1-fosscuda-2020b',
  'lib/snappy/1.1.8-GCCcore-9.3.0',
  'lib/snappy/1.1.8-GCCcore-10.2.0',
  'lib/tbb/2018_U5-GCCcore-7.3.0',
  'lib/tbb/2020.1-GCCcore-9.3.0',
  'lib/tbb/2020.3-GCCcore-10.2.0',
  'lib/zlib/1.2.11-GCCcore-8.3.0',
  'lib/zlib/1.2.11-GCCcore-9.3.0',
  'lib/zlib/1.2.11-GCCcore-10.2.0',
  'lib/zlib/1.2.11',
  'lib/zstd/1.4.4-GCCcore-9.3.0',
  'lib/zstd/1.4.5-GCCcore-10.2.0',
  'math/libcerf/1.7-GCCcore-7.3.0',
  'math/libcerf/1.14-GCCcore-10.2.0',
  'numlib/Armadillo/10.5.3-foss-2020b',
  'numlib/FFTW/3.3.8-gompi-2018b',
  'numlib/FFTW/3.3.8-gompi-2020b',
  'numlib/FFTW/3.3.8-gompic-2018b',
  'numlib/FFTW/3.3.8-gompic-2020b',
  'numlib/GSL/2.6-GCC-10.2.0',
  'numlib/LAPACK/3.9.1-GCC-10.2.0',
  'numlib/NLopt/2.6.1-GCCcore-9.3.0',
  'numlib/OpenBLAS/0.3.1-GCC-7.3.0-2.30',
  'numlib/OpenBLAS/0.3.9-GCC-9.3.0',
  'numlib/OpenBLAS/0.3.12-GCC-10.2.0',
  'numlib/ScaLAPACK/2.0.2-gompi-2018b-OpenBLAS-0.3.1',
  'numlib/ScaLAPACK/2.1.0-gompi-2020a',
  'numlib/ScaLAPACK/2.1.0-gompi-2020b',
  'numlib/ScaLAPACK/2.1.0-gompic-2020b',
  'numlib/SuiteSparse/5.8.1-foss-2020b-METIS-5.1.0',
  'numlib/beagle-lib/3.0.2-foss-2018b',
  'numlib/beagle-lib/3.1.2-GCC-10.2.0',
  'numlib/cuDNN/8.0.4.30-CUDA-11.1.1',
  'numlib/imkl/2020.4.304-gompi-2020b',
  'system/libgcrypt/1.9.2-GCCcore-10.2.0',
  'system/libpciaccess/0.14-GCCcore-7.3.0',
  'system/libpciaccess/0.16-GCCcore-9.3.0',
  'tools/libarchive/3.4.3-GCCcore-10.2.0',
  'vis/libGLU/9.0.1-GCCcore-9.3.0',
  'vis/libGLU/9.0.1-GCCcore-10.2.0',
  'vis/matplotlib/3.2.1-foss-2020a-Python-3.8.2',
  'vis/matplotlib/3.3.3-foss-2020b'],
 'math': ['lib/libmatheval/1.1.11-GCCcore-9.3.0',
  'math/Eigen/3.3.7-GCCcore-9.3.0',
  'math/Eigen/3.3.8-GCCcore-10.2.0',
  'math/GEOS/3.9.1-GCC-10.2.0',
  'math/GMP/6.2.0-GCCcore-9.3.0',
  'math/GMP/6.2.0-GCCcore-10.2.0',
  'math/ISL/0.23-GCCcore-10.2.0',
  'math/Keras/2.4.3-fosscuda-2020b',
  'math/MATLAB/2023b',
  'math/METIS/5.1.0-GCCcore-10.2.0',
  'math/MPC/1.2.1-GCCcore-10.2.0',
  'math/MPFR/4.1.0-GCCcore-10.2.0',
  'math/Theano/1.1.2-fosscuda-2020b-PyMC',
  'math/Voro++/0.4.6-GCCcore-9.3.0',
  'math/libcerf/1.7-GCCcore-7.3.0',
  'math/libcerf/1.14-GCCcore-10.2.0',
  'math/lpsolve/5.5.2.11-GCC-10.2.0',
  'math/magma/2.5.4-fosscuda-2020b',
  'math/molmod/1.4.5-foss-2020a-Python-3.8.2'],
 'mpi': ['mpi/MPICH/3.3.2-GCC-10.2.0',
  'mpi/OpenMPI/3.1.1-GCC-7.3.0-2.30',
  'mpi/OpenMPI/3.1.1-gcccuda-2018b',
  'mpi/OpenMPI/4.0.3-GCC-9.3.0',
  'mpi/OpenMPI/4.0.5-GCC-10.2.0',
  'mpi/OpenMPI/4.0.5-gcccuda-2020b',
  'mpi/OpenMPI/4.1.0-GCC-10.2.0',
  'numlib/FFTW/3.3.8-gompi-2018b',
  'numlib/FFTW/3.3.8-gompi-2020b',
  'numlib/FFTW/3.3.8-gompic-2018b',
  'numlib/FFTW/3.3.8-gompic-2020b',
  'numlib/ScaLAPACK/2.0.2-gompi-2018b-OpenBLAS-0.3.1',
  'numlib/ScaLAPACK/2.1.0-gompi-2020a',
  'numlib/ScaLAPACK/2.1.0-gompi-2020b',
  'numlib/ScaLAPACK/2.1.0-gompic-2020b',
  'numlib/imkl/2020.4.304-gompi-2020b',
  'toolchain/gompi/2018b',
  'toolchain/gompi/2020a',
  'toolchain/gompic/2018b',
  'toolchain/gompic/2020b',
  'tools/IOR/3.3.0-gompi-2020b',
  'tools/YAXT/0.9.0-gompi-2020b',
  'tools/ecCodes/2.20.0-gompi-2020b'],
 'numlib': ['numlib/Armadillo/10.5.3-foss-2020b',
  'numlib/FFTW/3.3.8-gompi-2018b',
  'numlib/FFTW/3.3.8-gompi-2020b',
  'numlib/FFTW/3.3.8-gompic-2018b',
  'numlib/FFTW/3.3.8-gompic-2020b',
  'numlib/GSL/2.6-GCC-10.2.0',
  'numlib/LAPACK/3.9.1-GCC-10.2.0',
  'numlib/NLopt/2.6.1-GCCcore-9.3.0',
  'numlib/OpenBLAS/0.3.1-GCC-7.3.0-2.30',
  'numlib/OpenBLAS/0.3.9-GCC-9.3.0',
  'numlib/OpenBLAS/0.3.12-GCC-10.2.0',
  'numlib/ScaLAPACK/2.0.2-gompi-2018b-OpenBLAS-0.3.1',
  'numlib/ScaLAPACK/2.1.0-gompi-2020a',
  'numlib/ScaLAPACK/2.1.0-gompi-2020b',
  'numlib/ScaLAPACK/2.1.0-gompic-2020b',
  'numlib/SuiteSparse/5.8.1-foss-2020b-METIS-5.1.0',
  'numlib/beagle-lib/3.0.2-foss-2018b',
  'numlib/beagle-lib/3.1.2-GCC-10.2.0',
  'numlib/cuDNN/8.0.4.30-CUDA-11.1.1',
  'numlib/imkl/2020.4.304-gompi-2020b'],
 'perf': ['perf/CubeWriter/4.6-GCCcore-10.2.0', 'perf/STREAM/5.10-GCC-9.3.0'],
 'phys': ['phys/COMSOL/6.1.0.357',
  'phys/UDUNITS/2.2.26-foss-2020a',
  'phys/UDUNITS/2.2.26-GCCcore-10.2.0'],
 'system': ['system/CUDA/8.0.61',
  'system/CUDA/11.1.1-GCC-10.2.0',
  'system/GnuTLS/3.7.1-GCC-10.2.0',
  'system/OpenPGM/5.2.122-GCCcore-9.3.0',
  'system/OpenPGM/5.2.122-GCCcore-10.2.0',
  'system/hwloc/1.11.10-GCCcore-7.3.0',
  'system/hwloc/2.2.0-GCCcore-9.3.0',
  'system/hwloc/2.2.0-GCCcore-10.2.0',
  'system/libgcrypt/1.9.2-GCCcore-10.2.0',
  'system/libpciaccess/0.14-GCCcore-7.3.0',
  'system/libpciaccess/0.16-GCCcore-9.3.0'],
 'toolchain': ['toolchain/foss/2018b',
  'toolchain/foss/2020a',
  'toolchain/fosscuda/2018b',
  'toolchain/fosscuda/2020b',
  'toolchain/gcccuda/2020b',
  'toolchain/gompi/2018b',
  'toolchain/gompi/2020a',
  'toolchain/gompic/2018b',
  'toolchain/gompic/2020b'],
 'tools': ['tools/DB/18.1.40-GCCcore-10.2.0',
  'tools/DMTCP/2.6.0-GCCcore-9.3.0',
  'tools/EasyBuild/4.5.0',
  'tools/GLPK/4.65-GCCcore-9.3.0',
  'tools/Ghostscript/9.52-GCCcore-9.3.0',
  'tools/Ghostscript/9.53.3-GCCcore-10.2.0',
  'tools/HPL/2.3-foss-2020b',
  'tools/IOR/3.3.0-gompi-2020b',
  'tools/IPython/7.15.0-foss-2020a-Python-3.8.2',
  'tools/IPython/7.18.1-GCCcore-10.2.0',
  'tools/IRkernel/1.1-foss-2020a-R-3.6.3-Python-3.8.2',
  'tools/ImageJ/1.51k',
  'tools/Meson/0.55.1-GCCcore-9.3.0-Python-3.8.2',
  'tools/Meson/0.55.3-GCCcore-10.2.0',
  'tools/Ninja/1.10.1-GCCcore-10.2.0',
  'tools/Pandoc/2.13',
  'tools/Szip/2.1.1-GCCcore-7.3.0',
  'tools/Szip/2.1.1-GCCcore-10.2.0',
  'tools/UnZip/6.0-GCCcore-10.2.0',
  'tools/VTune/2021.6.0',
  'tools/XZ/5.2.4-GCCcore-7.3.0',
  'tools/XZ/5.2.5-GCCcore-10.2.0',
  'tools/YAXT/0.9.0-gompi-2020b',
  'tools/Zip/3.0-GCCcore-10.2.0',
  'tools/archspec/0.1.0-GCCcore-9.3.0-Python-3.8.2',
  'tools/binutils/2.30-GCCcore-7.3.0',
  'tools/binutils/2.30',
  'tools/binutils/2.32-GCCcore-8.3.0',
  'tools/binutils/2.34-GCCcore-9.3.0',
  'tools/binutils/2.34',
  'tools/binutils/2.35-GCCcore-10.2.0',
  'tools/binutils/2.35',
  'tools/bokeh/2.2.3-foss-2020b',
  'tools/bokeh/2.2.3-fosscuda-2020b',
  'tools/bzip2/1.0.6-GCCcore-7.3.0',
  'tools/bzip2/1.0.8-GCCcore-10.2.0',
  'tools/cURL/7.60.0-GCCcore-7.3.0',
  'tools/cURL/7.72.0-GCCcore-10.2.0',
  'tools/ecCodes/2.20.0-gompi-2020b',
  'tools/expat/2.2.5-GCCcore-7.3.0',
  'tools/expat/2.2.9-GCCcore-9.3.0',
  'tools/expat/2.2.9-GCCcore-10.2.0',
  'tools/gettext/0.19.8.1-GCCcore-7.3.0',
  'tools/gettext/0.20.1-GCCcore-9.3.0',
  'tools/gettext/0.20.1',
  'tools/gettext/0.21-GCCcore-10.2.0',
  'tools/git/2.28.0-GCCcore-10.2.0-nodocs',
  'tools/groff/1.22.4-GCCcore-10.2.0',
  'tools/gzip/1.10-GCCcore-9.3.0',
  'tools/gzip/1.10-GCCcore-10.2.0',
  'tools/help2man/1.47.4-GCCcore-7.3.0',
  'tools/help2man/1.47.4',
  'tools/help2man/1.47.8-GCCcore-8.3.0',
  'tools/help2man/1.47.12-GCCcore-9.3.0',
  'tools/hypothesis/5.41.2-GCCcore-10.2.0',
  'tools/hypothesis/5.41.5-GCCcore-10.2.0',
  'tools/jq/1.6-GCCcore-10.2.0',
  'tools/lftp/4.9.2-GCC-10.2.0',
  'tools/libarchive/3.4.3-GCCcore-10.2.0',
  'tools/likwid/5.1.0-GCCcore-9.3.0',
  'tools/mdtest/1.9.3-foss-2020b',
  'tools/networkx/2.5-foss-2020b',
  'tools/networkx/2.5-fosscuda-2020b',
  'tools/numactl/2.0.11-GCCcore-7.3.0',
  'tools/numactl/2.0.13-GCCcore-10.2.0',
  'tools/oniguruma/6.9.7.1-GCCcore-10.2.0',
  'tools/poetry/1.0.9-GCCcore-9.3.0-Python-3.8.2',
  'tools/pytest-xdist/2.3.0-GCCcore-10.2.0',
  'tools/tcsh/6.20.00-GCCcore-7.3.0',
  'tools/umap-learn/0.4.6-fosscuda-2020b',
  'tools/util-linux/2.35-GCCcore-9.3.0',
  'tools/util-linux/2.36-GCCcore-10.2.0'],
 'vis': ['vis/ATK/2.36.0-GCCcore-10.2.0',
  'vis/ETE/3.1.2-foss-2020a-Python-3.8.2',
  'vis/ETE/3.1.2-foss-2020b',
  'vis/FFmpeg/4.3.1-GCCcore-10.2.0',
  'vis/FLTK/1.3.4-fosscuda-2018b',
  'vis/FLTK/1.3.5-GCCcore-10.2.0',
  'vis/GLib/2.54.3-GCCcore-7.3.0',
  'vis/GLib/2.64.1-GCCcore-9.3.0',
  'vis/GLib/2.66.1-GCCcore-10.2.0',
  'vis/GST-plugins-base/1.18.4-GCC-10.2.0',
  'vis/GStreamer/1.18.3-GCC-10.2.0',
  'vis/GTK+/3.24.23-GCCcore-10.2.0',
  'vis/Gdk-Pixbuf/2.40.0-GCCcore-10.2.0',
  'vis/HarfBuzz/2.2.0-fosscuda-2018b',
  'vis/HarfBuzz/2.6.7-GCCcore-10.2.0',
  'vis/ImageMagick/7.0.10-35-GCCcore-10.2.0',
  'vis/JasPer/2.0.14-GCCcore-9.3.0',
  'vis/JasPer/2.0.24-GCCcore-10.2.0',
  'vis/LittleCMS/2.9-GCCcore-9.3.0',
  'vis/LittleCMS/2.11-GCCcore-10.2.0',
  'vis/Mesa/20.0.2-GCCcore-9.3.0',
  'vis/Mesa/20.2.1-GCCcore-10.2.0',
  'vis/OpenEXR/2.5.5-GCCcore-10.2.0',
  'vis/Pango/1.42.4-fosscuda-2018b',
  'vis/Pillow/8.0.1-GCCcore-10.2.0',
  'vis/PyQt5/5.15.1-GCCcore-9.3.0-Python-3.8.2',
  'vis/PyQt5/5.15.1-GCCcore-10.2.0',
  'vis/SFML/2.5.1-Linux_x86_64',
  'vis/Tk/8.6.10-GCCcore-9.3.0',
  'vis/Tk/8.6.10-GCCcore-10.2.0',
  'vis/X11/20180604-GCCcore-7.3.0',
  'vis/X11/20200222-GCCcore-9.3.0',
  'vis/Xvfb/1.20.9-GCCcore-9.3.0',
  'vis/Xvfb/1.20.9-GCCcore-10.2.0',
  'vis/at-spi2-atk/2.38.0-GCCcore-10.2.0',
  'vis/at-spi2-core/2.38.0-GCCcore-10.2.0',
  'vis/cairo/1.14.12-GCCcore-7.3.0',
  'vis/cairo/1.16.0-GCCcore-9.3.0',
  'vis/cisTEM/1.0.0-beta',
  'vis/fontconfig/2.13.0-GCCcore-7.3.0',
  'vis/fontconfig/2.13.92-GCCcore-9.3.0',
  'vis/fontconfig/2.13.92-GCCcore-10.2.0',
  'vis/freetype/2.9.1-GCCcore-7.3.0',
  'vis/freetype/2.10.1-GCCcore-9.3.0',
  'vis/freetype/2.10.3-GCCcore-10.2.0',
  'vis/gnuplot/5.4.1-GCCcore-10.2.0',
  'vis/jbigkit/2.1-GCCcore-10.2.0',
  'vis/libGLU/9.0.1-GCCcore-9.3.0',
  'vis/libGLU/9.0.1-GCCcore-10.2.0',
  'vis/matplotlib/3.2.1-foss-2020a-Python-3.8.2',
  'vis/matplotlib/3.3.3-foss-2020b',
  'vis/pixman/0.34.0-GCCcore-7.3.0',
  'vis/pixman/0.38.4-GCCcore-9.3.0',
  'vis/scikit-image/0.18.1-foss-2020b',
  'vis/torchvision/0.8.2-fosscuda-2020b-PyTorch-1.7.1',
  'vis/x264/20191217-GCCcore-9.3.0',
  'vis/x264/20201026-GCCcore-10.2.0',
  'vis/x265/3.3-GCCcore-9.3.0',
  'vis/x265/3.3-GCCcore-10.2.0',
  'vis/xprop/1.2.5-GCCcore-10.2.0']}
if selected == "bio":
    selectedmoduleavail = modeavail["bio"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "chem":
    selectedmoduleavail = modeavail["chem"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "compiler":
    selectedmoduleavail = modeavail["compiler"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "custom":
    selectedmoduleavail = modeavail["custom"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "data":
    selectedmoduleavail = modeavail["data"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "debugger":
    selectedmoduleavail = modeavail["debugger"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "devel":
    selectedmoduleavail = modeavail["devel"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "lang":
    selectedmoduleavail = modeavail["lang"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "lib":
    selectedmoduleavail = modeavail["lib"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "math":
    selectedmoduleavail = modeavail["math"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "mpi":
    selectedmoduleavail = modeavail["mpi"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "numlib":
    selectedmoduleavail = modeavail["numlib"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "perf":
    selectedmoduleavail = modeavail["perf"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "phys":
    selectedmoduleavail = modeavail["phys"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "system":
    selectedmoduleavail = modeavail["system"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "toolchain":
    selectedmoduleavail = modeavail["toolchain"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "tools":
    selectedmoduleavail = modeavail["tools"]
    st.selectbox("selected the above", selectedmoduleavail)
if selected == "vis":
    selectedmoduleavail = modeavail["vis"]
    st.selectbox("selected the above", selectedmoduleavail)
configuration = st.button("please write the slurm for analysis")
if configuration:
    st.write(f"Your server configuration file written by Universitat Potsdam Slurm Configurator is:"
             f" {name}\n{top}\n{queue}\n{threads}\n{core}\n{memory}\n{workdir}\n{email}\n{end}\n{command}")

if __name__ == "__main__":
    pass