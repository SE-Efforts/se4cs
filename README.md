# SE4CS: The Changing Nature of Computational Science 

| Category  | Characteristic |
|:-:|---|
| nature of  | Requirements are Not Known up Front  |
| scientific | Verification and Validation are Difficult and Strictly Scientific  |
| challenge | Overly Formal Software Processes Restrict Research  |
| | |
| limitations  | Development is Driven and Limited by Hardware |
| of | Use of Old Programming Languages and Technologies  |
| computer | Intermingling of Domain Logic and Implementation Details |
| hardware | Conflicting Software Quality Requirements  |
| | |
|  | Different Terminology  |
|  limitations | Creating a Shared Understanding of a Code is Difficult |
| of  | Little Code Reuse |
|  cultural  | Scientific Software in Itself has No Value But Still It is Long-Lived  |
| differences  | Few Scientists are Trained in Software Engineering |
|   | Disregard of Most Modern Software Engineering Methods  |



a) Labelled Commits:
- Retrieve the commits data by running ```python commits/commits_data.py```, file can be adjusted to subset a sample for manual labelling. 
- The guideline for the labelling is included [here](https://github.com/se4cs/se4cs/blob/master/labelling_guide.md). 

b) Github Attributes of the projects: 
- Update the `access_token` column in `data/project_list_[cs/se]` with your Github token.
- Retrieve the cs or se projects attributes by running ```python attributes/mine_attributes.py [cs/se]```.  
- Plot the box plots comparison graph of SE and CS by ```python attributes/plot_attributes.py``` 

Approaches to reproduce results for each beliefs: 

1.a) https://docs.google.com/spreadsheets/d/1qmoA3pzpi0oAhq0PtpVOfsRkTVmonvBD3zyLXPD0VPY/edit?usp=sharing

1.b) Manual Labels of the commits from (a)

2.b) and 3.f) Manual checking for the language usage and the Travis CI of all projects

2.c) Combination results taken from 1.a) and 1.b) 

3.d) 1.a), 3.b), and 3.c)



### Data (CS Projects Selected for this study):

<table>
                          <tr>
                              <th>Project Name</th>
                              <th>Link</th>
                          </tr>
                        <tr>
                                <td>abaco</td>
                                <td><a href="https://github.com/TACC/abaco">https://github.com/TACC/abaco</a></td>
                            </tr>
                            <tr>
                                <td>abinit</td>
                                <td><a href="https://github.com/abinit/abinit">https://github.com/abinit/abinit</a></td>
                            </tr>
                            <tr>
                                <td>apbs-pdb2pqr</td>
                                <td><a href="https://github.com/Electrostatics/apbs-pdb2pqr">https://github.com/Electrostatics/apbs-pdb2pqr</a></td>
                            </tr>
                            <tr>
                                <td>blis</td>
                                <td><a href="https://github.com/flame/blis">https://github.com/flame/blis</a></td>
                            </tr>
                            <tr>
                                <td>cctools</td>
                                <td><a href="https://github.com/cooperative-computing-lab/cctools">https://github.com/cooperative-computing-lab/cctools</a></td>
                            </tr>
                            <tr>
                                <td>changa</td>
                                <td><a href="https://github.com/N-BodyShop/changa">https://github.com/N-BodyShop/changa</a></td>
                            </tr>
                            <tr>
                                <td>clowder</td>
                                <td><a href="https://github.com/ncsa/clowder">https://github.com/ncsa/clowder</a></td>
                            </tr>
                            <tr>
                                <td>cpptraj</td>
                                <td><a href="https://github.com/Amber-MD/cpptraj">https://github.com/Amber-MD/cpptraj</a></td>
                            </tr>
                            <tr>
                                <td>cyclus</td>
                                <td><a href="https://github.com/cyclus/cyclus">https://github.com/cyclus/cyclus</a></td>
                            </tr>
                            <tr>
                                <td>elasticsearch</td>
                                <td><a href="https://github.com/elastic/elasticsearch">https://github.com/elastic/elasticsearch</a></td>
                            </tr>
                            <tr>
                                <td>forcebalance</td>
                                <td><a href="https://github.com/leeping/forcebalance">https://github.com/leeping/forcebalance</a></td>
                            </tr>
                            <tr>
                                <td>galaxy</td>
                                <td><a href="https://github.com/galaxyproject/galaxy">https://github.com/galaxyproject/galaxy</a></td>
                            </tr>
                            <tr>
                                <td>GooFit</td>
                                <td><a href="https://github.com/GooFit/GooFit">https://github.com/GooFit/GooFit</a></td>
                            </tr>
                            <tr>
                                <td>hoomd-blue</td>
                                <td><a href="https://github.com/glotzerlab/hoomd-blue">https://github.com/glotzerlab/hoomd-blue</a></td>
                            </tr>
                            <tr>
                                <td>htmd</td>
                                <td><a href="https://github.com/Acellera/htmd">https://github.com/Acellera/htmd</a></td>
                            </tr>
                            <tr>
                                <td>hubzero-cms</td>
                                <td><a href="https://github.com/hubzero/hubzero-cms">https://github.com/hubzero/hubzero-cms</a></td>
                            </tr>
                            <tr>
                                <td>hydroshare</td>
                                <td><a href="https://github.com/hydroshare/hydroshare">https://github.com/hydroshare/hydroshare</a></td>
                            </tr>
                            <tr>
                                <td>irods </td>
                                <td><a href="https://github.com/irods/irods">https://github.com/irods/irods</a></td>
                            </tr>
                            <tr>
                                <td>lammps</td>
                                <td><a href="https://github.com/lammps/lammps">https://github.com/lammps/lammps</a></td>
                            </tr>
                            <tr>
                                <td>luafilesystem</td>
                                <td><a href="https://github.com/keplerproject/luafilesystem">https://github.com/keplerproject/luafilesystem</a></td>
                            </tr>
                            <tr>
                                <td>luigi</td>
                                <td><a href="https://github.com/spotify/luigi">https://github.com/spotify/luigi</a></td>
                            </tr>
                            <tr>
                                <td>madness</td>
                                <td><a href="https://github.com/m-a-d-n-e-s-s/madness">https://github.com/m-a-d-n-e-s-s/madness</a></td>
                            </tr>
                            <tr>
                                <td>MAST</td>
                                <td><a href="https://github.com/uw-cmg/MAST">https://github.com/uw-cmg/MAST</a></td>
                            </tr>
                            <tr>
                                <td>mdtraj</td>
                                <td><a href="https://github.com/mdtraj/mdtraj">https://github.com/mdtraj/mdtraj</a></td>
                            </tr>
                            <tr>
                                <td>MetPy</td>
                                <td><a href="https://github.com/Unidata/MetPy">https://github.com/Unidata/MetPy</a></td>
                            </tr>
                            <tr>
                                <td>mpqc</td>
                                <td><a href="https://github.com/ValeevGroup/mpqc">https://github.com/ValeevGroup/mpqc</a></td>
                            </tr>
                            <tr>
                                <td>ndslabs</td>
                                <td><a href="https://github.com/nds-org/ndslabs">https://github.com/nds-org/ndslabs</a></td>
                            </tr>
                            <tr>
                                <td>nwchem</td>
                                <td><a href="https://github.com/nwchemgit/nwchem">https://github.com/nwchemgit/nwchem</a></td>
                            </tr>
                            <tr>
                                <td>ompi</td>
                                <td><a href="https://github.com/open-mpi/ompi">https://github.com/open-mpi/ompi</a></td>
                            </tr>
                            <tr>
                                <td>openforcefield</td>
                                <td><a href="https://github.com/openforcefield/openforcefield">https://github.com/openforcefield/openforcefield</a></td>
                            </tr>
                            <tr>
                                <td>openmm</td>
                                <td><a href="https://github.com/pandegroup/openmm/">https://github.com/pandegroup/openmm/</a></td>
                            </tr>
                            <tr>
                                <td>openmmtools</td>
                                <td><a href="https://github.com/choderalab/openmmtools">https://github.com/choderalab/openmmtools</a></td>
                            </tr>
                            <tr>
                                <td>OpenMx</td>
                                <td><a href="https://github.com/OpenMx/OpenMx">https://github.com/OpenMx/OpenMx</a></td>
                            </tr>
                            <tr>
                                <td>orca5</td>
                                <td><a href="https://github.com/RENCI-NRIG/orca5">https://github.com/RENCI-NRIG/orca5</a></td>
                            </tr>
                            <tr>
                                <td>parsl</td>
                                <td><a href="https://github.com/Parsl/parsl">https://github.com/Parsl/parsl</a></td>
                            </tr>
                            <tr>
                                <td>pcmsolver</td>
                                <td><a href="https://github.com/PCMSolver/pcmsolver">https://github.com/PCMSolver/pcmsolver</a></td>
                            </tr>
                            <tr>
                                <td>plumed2</td>
                                <td><a href="https://github.com/plumed/plumed2">https://github.com/plumed/plumed2</a></td>
                            </tr>
                            <tr>
                                <td>plumed2</td>
                                <td><a href="https://github.com/plumed/plumed2">https://github.com/plumed/plumed2</a></td>
                            </tr>
                            <tr>
                                <td>psi4</td>
                                <td><a href="https://github.com/psi4/psi4">https://github.com/psi4/psi4</a></td>
                            </tr>
                            <tr>
                                <td>pymatgen</td>
                                <td><a href="https://github.com/materialsproject/pymatgen">https://github.com/materialsproject/pymatgen</a></td>
                            </tr>
                            <tr>
                                <td>pyscf</td>
                                <td><a href="https://github.com/pyscf/pyscf">https://github.com/pyscf/pyscf</a></td>
                            </tr>
                            <tr>
                                <td>QCFractal</td>
                                <td><a href="https://github.com/MolSSI/QCFractal">https://github.com/MolSSI/QCFractal</a></td>
                            </tr>
                            <tr>
                                <td>quantum_package</td>
                                <td><a href="https://github.com/LCPQ/quantum_package">https://github.com/LCPQ/quantum_package</a></td>
                            </tr>
                            <tr>
                                <td>radical.pilot</td>
                                <td><a href="https://github.com/radical-cybertools/radical.pilot">https://github.com/radical-cybertools/radical.pilot</a></td>
                            </tr>
                            <tr>
                                <td>RMG-Py</td>
                                <td><a href="https://github.com/ReactionMechanismGenerator/RMG-Py">https://github.com/ReactionMechanismGenerator/RMG-Py</a></td>
                            </tr>
                            <tr>
                                <td>signac</td>
                                <td><a href="https://github.com/glotzerlab/signac/">https://github.com/glotzerlab/signac/</a></td>
                            </tr>
                            <tr>
                                <td>signac-flow</td>
                                <td><a href="https://github.com/glotzerlab/signac-flow">https://github.com/glotzerlab/signac-flow</a></td>
                            </tr>
                            <tr>
                                <td>TauDEM</td>
                                <td><a href="https://github.com/dtarb/TauDEM">https://github.com/dtarb/TauDEM</a></td>
                            </tr>
                            <tr>
                                <td>trellis </td>
                                <td><a href="https://github.com/trellis-ldp/trellis">https://github.com/trellis-ldp/trellis</a></td>
                            </tr>
                            <tr>
                                <td>Trilinos</td>
                                <td><a href="https://github.com/trilinos/Trilinos">https://github.com/trilinos/Trilinos</a></td>
                            </tr>
                            <tr>
                                <td>tripal</td>
                                <td><a href="https://github.com/tripal/tripal">https://github.com/tripal/tripal</a></td>
                            </tr>
                            <tr>
                                <td>WorkflowComponents</td>
                                <td><a href="https://github.com/LearnSphere/WorkflowComponents">https://github.com/LearnSphere/WorkflowComponents</a></td>
                            </tr>
                            <tr>
                                <td>Xenon</td>
                                <td><a href="https://github.com/NLeSC/Xenon">https://github.com/NLeSC/Xenon</a></td>
                            </tr>
                            <tr>
                                <td>yank</td>
                                <td><a href="https://github.com/choderalab/yank">https://github.com/choderalab/yank</a></td>
                            </tr>
                            <tr>
                                <td>yt</td>
                                <td><a href="https://github.com/yt-project/yt">https://github.com/yt-project/yt</a></td>
                            </tr>
                            <tr>
                                <td>galaxy</td>
                                <td><a href="https://github.com/galaxyproject/galaxy">https://github.com/galaxyproject/galaxy</a></td>
                            </tr>
                            <tr>
                                <td>dealii</td>
                                <td><a href="https://github.com/dealii/dealii">https://github.com/dealii/dealii</a></td>
                            </tr>
                            <tr>
                                <td>foyer</td>
                                <td><a href="https://github.com/mosdef-hub/foyer">https://github.com/mosdef-hub/foyer</a></td>
                            </tr>
                      </table>
