# Plot-the-Result
This is a utility project to plot necessary figure of the result set.

# Project Structure:
  ### CSV file location: 
      
      GraphList.csv -> It will take handle the file name of the graph to generate plot. We are expecting same CSV file name in the input directory as graph name.
      
      LegacyModularity      -> PerIteration   -> graphName.csv
                            -> PerMove        -> graphName.csv

      LegacyTimeComplexity  -> PerIteration   -> graphName.csv
                            -> PerMove        -> graphName.csv

      Modularity            -> PerIteration   -> graphName.csv
                            -> PerMove        -> graphName.csv

      TimeComplexity        -> PerIteration   -> graphName.csv
                            -> PerMove        -> graphName.csv
  ### Python Code:
      PLM_Plot.py

# Command to run the code: python PLM_Plot.py
It will generate multiple pdf file of the plot.


### There is also a Jupyter script file to visualize the data and plot.
    Plot.ipynb
