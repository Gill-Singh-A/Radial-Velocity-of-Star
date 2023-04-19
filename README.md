# Exoplanets from Radial Velocity of a Star
A Program that approximates the number of exoplanets and their data (Mass, Radius of Revolution and Time Period of Revolution) present in a star system given the Radial Velocity of Star with noise.

## Requirements
Language Used = Python3<br />
Modules/Packages used:
* numpy
* math
* matplotlib

## Input
It takes 1 argument through the command by which we run the python file and that is the csv file of the astronomical data (Radial Velocity vs Time with noise)

## Output
It first plots the original data present in the csv file.<br />
Then plots the Fourier Transformation of it.<br />
Uses Reverse Fourier Transformation for the previous graph to display the Radial Velocity vs Time without Noise.<br />
Then plots the individual Sinusoidal Waves which when added, gives the previous plot.<br />
Finally, it displays the Number of Exoplanet and their data (Mass, Radius of Revolution and Time Period of Revolution) on the Command Line Interface.

### Note
If the given output is not what you expected or is not correct, then try playing with the value on line 40, because that is used to reduce the noise by only keeping the peaks in the graph (that represent the sinusoidal waves) and removing any other fluctuations present.<br />
It may be because of the fact that we might have included 1 or more peaks that were not meant to be there (included the noise).<br />
Or may be because, we excluded 1 or more peaks that was meant to be there (excluded peaks that represent sinusoidal waves that we're interested in).