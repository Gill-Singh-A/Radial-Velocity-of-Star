# Exoplanets from Radial Velocity of a Star
A Program that approximates the number of exoplanets and their data (Mass, Radius of Revolution and Time Period of Revolution) present in a star system given the Radial Velocity of Star with noise.

## Theory
In free space, any given number of objects orbit around their center of mass.<br />
Similarly, in a Star System, every body revolves around the common center of mass of the system. Even though the Star might not appear revolving around the center of mass because of the fact that the center of mass is almost at the center of the star due to its massive mass. But it still revolves around that common point, giving it a velocity.<br />
And we use that thing to measure the radial velocity of the star by Doppler Effect shown by Electromagnetic Waves.<br />
If the star is moving away from us, then the Light comming from the star is red shifted due to which its wavelength increases.<br />
It the star is moving towards us, then the Light comming from the star is blue shifted due to which its wavelength decreases.<br/>
So, If a single exoplanet is present on a Star System, then the function of Radial Velocity vs Time would be a simple sine function.<br />
But, there can be multiple exoplanets present. So we use Fourier Transformation for reducing the noise by filtering the peaks and spliting the Final Function of Radial Velocity vs Time into its individual sinusoidal waves.<br />
And then Calculating the Time Period of Revolution by the Frequency of the sinusoidal waves, Radius of Revolution by Time Period and Mass by conserving Linear Momentum by taking the amplitude from the graph of individual sinusoidal waves.

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
If the given output is not what you expected or is not correct, then try playing with the value for filtering the peaks by providing a second argument in the running command (default value for filtering peaks = 50, values below 50 will be set to 0), because that value is used to reduce the noise by only keeping the peaks in the graph (that represent the sinusoidal waves) and removing any other fluctuations present.<br />
It may be because of the fact that we might have included 1 or more peaks that were not meant to be there (included the noise).<br />
Or may be because, we excluded 1 or more peaks that was meant to be there (excluded peaks that represent sinusoidal waves that we're interested in).