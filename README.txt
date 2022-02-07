-------
|ABOUT|
-------

This is my personal imitation of the Windows Snip tool.

Upon running the program, the following will occur:
- The screen freezes at the frame the program was run
- A white border surrounds the edge of your screen (visual indication that screen has frozen and awaits your cropping instructions)
- You drag your cursor around the region you'd like to crop
- A blue-filter rectangle will appear as the region you'll be cropping
- The image will instantly be cropped and saved onto your desktop as "<unixtime>_cropped.png"


-------
|USAGE|
-------

-> Just double click it

-> Personally, I prefer to be able to run the snip tool from Win+R and entering "ss", so I do these two steps:
	(1) Create a .bat file ("ss.bat") with the following content (without the '->' symbol):
		-> start /min C:\<Path to directory where ss.pyw is held>\ss.pyw %*
	(2) Place this .bat file in a directory recognised by my PATH
		-> I used "C:\Users\Willie\AppData\Local\Programs\Python\Python39\Scripts". I may have manually added this directory to my PATH variable.

