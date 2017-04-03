# pdf-page-counter
We've all been there, counting the number of slides desperately the night before exam :grin:.  
pdf-page-count is a nifty little script that does this for you.  

![Example](http://i.imgur.com/uQxWjia.png)

## Installation
```
pip install pdf-page-counter
```
## Requirements
- Python 2.7
- pip
- Linux (Windows fix coming soon!)

## Usage
 - Displays the number of pages in all the pdfs in the current directory (only top level)
```
pdf-page-counter
```
 - Displays the number of pages in all the pdfs in the current directory and its subdirectories
```
pdf-page-counter -r
```  
  
 - Displays the number of pages in all the pdfs in the /path/to/folder
```
pdf-page-counter /path/to/folder
```
 - Displays the number of pages in all the pdfs from multiple folders
```
pdf-page-counter /path/to/folder_one /path/to/folder_two
```


