my image detection function using open cv
takes three parameters (needle, Haystack, threshold)
needle is the thing you are trying to find a small image like an enemys health bar
a haystack is the surface you are searching for the needle
the threshold is the confidence level of the returned points which are a list of clickable coordinates, (x, y) ( the center of the rectangles drawn around the found object ) 
A haystack will be shown with rectangles around the spots where the threshold is met and X's over the center
