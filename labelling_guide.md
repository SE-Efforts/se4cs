### Commits categories:
- Science enhancement: any core science (e.g. an equation of Pascaltriangle) that is being implemented or modified.
- Engineering enhancement: any other enhancements that relatedto code complexity (e.g. data structures & types, I/O formats, etc)
- Bug fixes: Fixing software faults reported or found within thedevelopment.
- Testing: evaluate the functionality of a software application (e.g.scientific calculations to output/input formats).
- Other: not core changes, e.g. renaming or formatting changes.

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
