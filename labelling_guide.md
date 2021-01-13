### Commits categories:
1) Science enhancement: any core science (e.g. an equation of Pascal triangle) that is being modified.
-- New diagonalization options for Matrix.  
-- A damping factor introduced in orbital response equations, as suggested by Rendell et al. (JCP, vol. 87, pp. 5976, 1987).
-- Add cc-pwCVXZ tight functions for Li, Be, Na, Mg from Prascher 2010
2) Engineering enhancement: any other enhancements that related to code complexity (e.g. other data structures, data types, input/output, etc) 
-- DPD library now requests the memory from Proccess::evironment
-- Be a bit more efficient by using assign-once variables.
-- The purpose of this patch is to align the finite element classes with the way the mapping classes have already been converted.
3) Testing:
- Scientific testing would be testing the modeling/science aspect of the project/software
-- modified test to require displacement maximum to reach fixed coord goal.
- Engineering testing would be testing the code complexity 
-- testing integral array size 
4) Bug fixes: Fixing software faults reported or found within thedevelopment.
- Testing: evaluate the functionality of a software application (e.g.scientific calculations to output/input formats).
5) Other: not core changes, e.g. renaming or formatting changes.

### Our reviewers labeled commits using the following guidelines:
- If the commit is an enhancement, only one of (science enhancement, engineering enhancement) will be labeled as 1
- If the commit is a bug fix or testing, it can be either labeled as 1 or both can be labeled as 1 (testing and bug-fixing sometime go together). 
- A bug-fixing or testing can also be scientific or engineering (testing the science or testing the code for example) so it can overlapped with category science or engineering enhancement (also label science or engineering enhancement as 1)
- If you are unsure, please check each commit to see the code diff (there are a lot of commits just have merge PR so you need to check the PR), to categorize the commit unless you are more than 75% sure which category to label that commit in.  
- Others can only be overlapped with bug-fixes or testing 
- Examples: 
    - New diagonalization options for Matrix.  [Science Enhancement]
    - Fixed the DFMP2 Gradient functor.  DFMP2 gradients now work! Correctly this time. [Bug Fixes +  Science Enhancement]
    - DPD library now requests the memory from Proccess::evironment [Engineering Enhancement]
