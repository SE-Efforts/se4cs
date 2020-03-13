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
                            <td>ABINIT</td>
                            <td><a href="https://github.com/abinit/abinit">https://github.com/abinit/abinit</a></td>
                        </tr>
                        <tr>
                            <td>ACEMD</td>
                            <td><a href="https://github.com/Acellera/htmd">https://github.com/Acellera/htmd</a></td>
                        </tr>
                        <tr>
                            <td>ACES</td>
                            <td><a href="http://www.qtp.ufl.edu/ACES/">http://www.qtp.ufl.edu/ACES/</a></td>
                        </tr>
                        <tr>
                            <td>ADF</td>
                            <td><a href="https://www.scm.com/doc/ADF/index.html">https://www.scm.com/doc/ADF/index.html</a></td>
                        </tr>
                        <tr>
                            <td>ADF -- ReaxFF</td>
                            <td><a href="https://www.scm.com/doc/ReaxFF/index.html">https://www.scm.com/doc/ReaxFF/index.html</a></td>
                        </tr>
                        <tr>
                            <td>APBS</td>
                            <td><a href="https://github.com/Electrostatics/apbs-pdb2pqr">https://github.com/Electrostatics/apbs-pdb2pqr</a></td>
                        </tr>
                        <tr>
                            <td>Abalone</td>
                            <td><a href="http://www.biomolecular-modeling.com/Abalone/">http://www.biomolecular-modeling.com/Abalone/</a></td>
                        </tr>
                        <tr>
                            <td>AMBER</td>
                            <td><a href="https://github.com/Amber-MD">https://github.com/Amber-MD</a></td>
                        </tr>
                        <tr>
                            <td>CHARMM</td>
                            <td><a href="http://charmm.chemistry.harvard.edu/">http://charmm.chemistry.harvard.edu/</a></td>
                        </tr>
                        <tr>
                            <td>HOOMD-blue</td>
                            <td><a href="https://bitbucket.org/glotzer/hoomd-blue/">https://bitbucket.org/glotzer/hoomd-blue/</a></td>
                        </tr>
                        <tr>
                            <td>LAMMPS</td>
                            <td><a href="https://github.com/lammps/lammps">https://github.com/lammps/lammps</a></td>
                        </tr>
                        <tr>
                            <td>MADNESS</td>
                            <td><a href="https://github.com/m-a-d-n-e-s-s/madness">https://github.com/m-a-d-n-e-s-s/madness</a></td>
                        </tr>
                        <tr>
                            <td>MOLCAS</td>
                            <td><a href="https://gitlab.com/Molcas/OpenMolcas">https://gitlab.com/Molcas/OpenMolcas</a></td>
                        </tr>
                        <tr>
                            <td>MPQC</td>
                            <td><a href="https://github.com/ValeevGroup/mpqc">https://github.com/ValeevGroup/mpqc</a></td>
                        </tr>
                        <tr>
                            <td>MRChem</td>
                            <td><a href="https://github.com/MRChemSoft/mrchem">https://github.com/MRChemSoft/mrchem</a></td>
                        </tr>
                        <tr>
                            <td>NWChem</td>
                            <td><a href="https://github.com/nwchemgit/nwchem">https://github.com/nwchemgit/nwchem</a></td>
                        </tr>
                        <tr>
                            <td>ORCA</td>
                            <td><a href="https://orcaforum.cec.mpg.de/">https://orcaforum.cec.mpg.de/</a></td>
                        </tr>
                        <tr>
                            <td>OpenMD</td>
                            <td><a href="https://github.com/OpenMD/OpenMD">https://github.com/OpenMD/OpenMD</a></td>
                        </tr>
                        <tr>
                            <td>OpenMM</td>
                            <td><a href="https://github.com/pandegroup/openmm/">https://github.com/pandegroup/openmm/</a></td>
                        </tr>
                        <tr>
                            <td>OpenMX</td>
                            <td><a href="https://github.com/OpenMx/OpenMx">https://github.com/OpenMx/OpenMx</a></td>
                        </tr>
                        <tr>
                            <td>PCMSolver</td>
                            <td><a href="https://github.com/PCMSolver/pcmsolver">https://github.com/PCMSolver/pcmsolver</a></td>
                        </tr>
                        <tr>
                            <td>PLUMED</td>
                            <td><a href="https://github.com/plumed/plumed2">https://github.com/plumed/plumed2</a></td>
                        </tr>
                        <tr>
                            <td>PQS</td>
                            <td><a href="http://www.pqs-chem.com/index.php">http://www.pqs-chem.com/index.php</a></td>
                        </tr>
                        <tr>
                            <td>Psi4</td>
                            <td><a href="https://github.com/psi4/psi4">https://github.com/psi4/psi4</a></td>
                        </tr>
                        <tr>
                            <td>Q-Chem</td>
                            <td><a href="http://www.q-chem.com/qchem-website/manual/qchem50_manual/index.html">http://www.q-chem.com/qchem-website/manual/qchem50_manual/index.html</a></td>
                        </tr>
                        <tr>
                            <td>QuantumEspresso</td>
                            <td><a href="https://github.com/QEF/q-e">https://github.com/QEF/q-e</a></td>
                        </tr>
                      </table>
