This project was done using jupyter notebook and saved the finised file to say .py instead of .ipynb exytensions

In the code produced, I commented on the functions that would have changing values depending on the type of file and the size of it.
With the given files, I duplicated them: one for the assignment and the other for checking my work. The duplicated file was edited
so that the first three lines of the file were removed for the convenience of reading the file and changing the RGB triplets from a 
string to an int. The program took the RGB triplet and passed them individually into three separate functions, for the purpose of isolating 
them for readability. I used a dictionary for representing the key as the red component intensity, and the value as the frequency of that red coompnent.
With an empty dict for each of the RGB component, the rgb 2D array and the empty dict component each gets passed through their respective component.
Each component essentially perform the same function of counting the frequency of each RGB value of the triplet from each line:

for loop through the 2d array
	check if the R G or B component is in the dict
		yes: +1
		no: update the dict with the key as that intensity and set value to one

Once the frequency for each component has been obtained, the next function was to normalize them.
With a function to normalize the RGB frequencies, I passed in the generated dict for RGB component and an empty dict as well.
From the canvas site, we were given a description of how to normalize them:

Number of frequency for that key's value / the total number of pixels

The key and the normalized value woudld then be updated to the empty dict to represent the normalization of those values.
Matplotlib.pylot was used to generate the histogram of the RGB components. To avoid overlapping the histograms with each other, i commented out the R, G, or B
to make sure i would get a clear picture of the trend and shape of the histogram.
After i outputted and saved my generated histogram, I used the given image viewer to check my work for the shape of my graph, the normalized values 
and the frequencies of each component for each file.



To use the program, i made comments in all caps to indicate where the values have change.
To produce the histogram, comments were also made to let you know that while plotting the histogram for a component, the other two component histograms cannot 
be active so that it can avoid picture overlap.