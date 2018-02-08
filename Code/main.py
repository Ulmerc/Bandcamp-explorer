import urllib.request as urllib
from bs4 import BeautifulSoup
import numpy 
import re

selectionInt = 0

# -------------------------------------------------------------
# Get the HTML for the page of the provided link, and store it
# in a Beautiful soup format 
# -------------------------------------------------------------

def allArtistsFirstPage(mainLink):
	print("mainLink = " + mainLink)

	firstArtistPage = urllib.urlopen(mainLink)

	formattedFirstArtistPage = BeautifulSoup(firstArtistPage, "html.parser")

	return formattedFirstArtistPage


# --------------------------------------------------------------
# Find the number of pages on the first page and randomly select 
# one 
# --------------------------------------------------------------


def numberOfPages(formattedFirstPage, mainLink):

	numbers = []

	# Find unordered list with class = "pageList"
	pageList = formattedFirstPage.find('ul', {"class" : 'pagelist'})

	# Get a list of page numbers that contains the last page (the largest number of pages that need to be searched)
	for li in pageList:
		item = li.string
		
		if item.isnumeric():
			numbers.append(int(li.string))

	# The last number in the list is the largest, it is the number of pages that need to be searched
	numberOfPages = numbers[-1]
	limit = numberOfPages + 1

	# Randomly choose the page number to select the artist from
	randomPageNumber = numpy.random.randint(1, limit)

	print("Page number selected: " + str(randomPageNumber))

	url = mainLink + "?page=" + str(randomPageNumber)

	print("url = " + url)

	return url



# --------------------------------------------------------------------------------------------
# Create a list of all of the artists on the randomly selected page and randomly select one 
# --------------------------------------------------------------------------------------------

def randomlySelectArtist(url):

	allArtistLinks = []
	artistPage = urllib.urlopen(url)

	formattedArtistPage = BeautifulSoup(artistPage, "html.parser")

	# Find the unordered list where class = "item_list", this contains the relevant code
	allArtistList = formattedArtistPage.find('ul', {"class" : 'item_list'})

	# For the anchor tag in each li element in the ul tag
	for listItem in allArtistList.findAll("a"):
	# Get the link in the href
		artistHomepage = listItem.get("href")
	# Appending /music to the link will insure that all of the artists albums will be presented uniformly to the program
		allArtistLinks.append(artistHomepage)

	length = len(allArtistLinks)
	randomIndex = numpy.random.randint(0, length)

	specificArtistLink = allArtistLinks[randomIndex]

	print("specificArtistLink = " + specificArtistLink)

	return specificArtistLink


# ---------------------------------------------------------------------------------------------------
# Find all of the albums an artist has created, randomly select one and present the url to the user
# ---------------------------------------------------------------------------------------------------

def randomlySelectAlbum(specificArtistLink):
	
	artistAlbums = []
	
	searchFor = r'\S*(\.com|\.net|\.uk)'
	artistBaseLink = re.search(searchFor, specificArtistLink)

	print("artistBaseLink = " + artistBaseLink.group(0))


	# Get the HTML code from the specific artist's page
	unformattedArtistPage = urllib.urlopen(artistBaseLink.group(0))

	# Format the HTML code from the specific artist's page
	formattedArtistPage = BeautifulSoup(unformattedArtistPage, "html.parser")

	# Find the div where class = "leftMiddleColumns", this contains the relevant code
	albumSection = formattedArtistPage.find('div', {"class" : 'leftMiddleColumns'})

	# Getting the section of code that indicates if the artist has one or multiple albums
	albumNumberCheck = formattedArtistPage.find('div', {"class" : 'trackView'})

	# If the artist has more than one album
	if (albumNumberCheck == None):

		for listItem in albumSection.findAll("a"):
			albumSubLink = listItem.get("href")
			artistAlbums.append(artistBaseLink.group(0) + albumSubLink)

		randomIndex = numpy.random.randint(0, len(artistAlbums))

		selectedAlbum = artistAlbums[randomIndex]

		return selectedAlbum

	# Else the artist has only one album
	else:
		return specificArtistLink



# ------------------------------------------------------------------------
# Get user input if they want a random album or one from a specific tag 
# ------------------------------------------------------------------------

def main():

	selectionStr = input("\nPlease enter the number corresponding to the option you want to select: "
		+ "\n1. Completely random album\n2. Random album from a specific tag\n\nInput: ")

	selectionInt = int(selectionStr)

	if selectionInt == 1:

		mainLink = "https://bandcamp.com/artist_index"

		formattedFirstPage = allArtistsFirstPage(mainLink)
		url = numberOfPages(formattedFirstPage, mainLink)
		artistLink = randomlySelectArtist(url)
		albumLink = randomlySelectAlbum(artistLink)

		print("Here is your randomly selected album link: " + albumLink)
	
	elif selectionInt == 2:

		tagName = input("\nGo to the following link to find a tag you are interested in exploring:"
			+ " https://bandcamp.com/tags\nOnce you have found a tag, enter it: ")
		
		mainLink = "https://bandcamp.com/tag/" + tagName

		formattedFirstPage = allArtistsFirstPage(mainLink)
		url = numberOfPages(formattedFirstPage, mainLink)
		albumLink = randomlySelectArtist(url)

		print("Here is your randomly selected " + tagName + " album link: " + albumLink)

if __name__ == "__main__":
    main()
 import urllib.request as urllib
from bs4 import BeautifulSoup
import numpy 
import re

selectionInt = 0

# -------------------------------------------------------------
# Get the HTML for the page of the provided link, and store it
# in a Beautiful soup format 
# -------------------------------------------------------------

def allArtistsFirstPage(mainLink):
	print("mainLink = " + mainLink)

	firstArtistPage = urllib.urlopen(mainLink)

	formattedFirstArtistPage = BeautifulSoup(firstArtistPage, "html.parser")

	return formattedFirstArtistPage


# --------------------------------------------------------------
# Find the number of pages on the first page and randomly select 
# one 
# --------------------------------------------------------------


def numberOfPages(formattedFirstPage, mainLink):

	numbers = []

	# Find unordered list with class = "pageList"
	pageList = formattedFirstPage.find('ul', {"class" : 'pagelist'})

	# Get a list of page numbers that contains the last page (the largest number of pages that need to be searched)
	for li in pageList:
		item = li.string
		
		if item.isnumeric():
			numbers.append(int(li.string))

	# The last number in the list is the largest, it is the number of pages that need to be searched
	numberOfPages = numbers[-1]
	limit = numberOfPages + 1

	# Randomly choose the page number to select the artist from
	randomPageNumber = numpy.random.randint(1, limit)

	print("Page number selected: " + str(randomPageNumber))

	url = mainLink + "?page=" + str(randomPageNumber)

	print("url = " + url)

	return url



# --------------------------------------------------------------------------------------------
# Create a list of all of the artists on the randomly selected page and randomly select one 
# --------------------------------------------------------------------------------------------

def randomlySelectArtist(url):

	allArtistLinks = []
	artistPage = urllib.urlopen(url)

	formattedArtistPage = BeautifulSoup(artistPage, "html.parser")

	# Find the unordered list where class = "item_list", this contains the relevant code
	allArtistList = formattedArtistPage.find('ul', {"class" : 'item_list'})

	# For the anchor tag in each li element in the ul tag
	for listItem in allArtistList.findAll("a"):
	# Get the link in the href
		artistHomepage = listItem.get("href")
	# Appending /music to the link will insure that all of the artists albums will be presented uniformly to the program
		allArtistLinks.append(artistHomepage)

	length = len(allArtistLinks)
	randomIndex = numpy.random.randint(0, length)

	specificArtistLink = allArtistLinks[randomIndex]

	print("specificArtistLink = " + specificArtistLink)

	return specificArtistLink


# ---------------------------------------------------------------------------------------------------
# Find all of the albums an artist has created, randomly select one and present the url to the user
# ---------------------------------------------------------------------------------------------------

def randomlySelectAlbum(specificArtistLink):
	
	artistAlbums = []
	
	searchFor = r'\S*(\.com|\.net|\.uk)'
	artistBaseLink = re.search(searchFor, specificArtistLink)

	print("artistBaseLink = " + artistBaseLink.group(0))


	# Get the HTML code from the specific artist's page
	unformattedArtistPage = urllib.urlopen(artistBaseLink.group(0))

	# Format the HTML code from the specific artist's page
	formattedArtistPage = BeautifulSoup(unformattedArtistPage, "html.parser")

	# Find the div where class = "leftMiddleColumns", this contains the relevant code
	albumSection = formattedArtistPage.find('div', {"class" : 'leftMiddleColumns'})

	# Getting the section of code that indicates if the artist has one or multiple albums
	albumNumberCheck = formattedArtistPage.find('div', {"class" : 'trackView'})

	# If the artist has more than one album
	if (albumNumberCheck == None):

		for listItem in albumSection.findAll("a"):
			albumSubLink = listItem.get("href")
			artistAlbums.append(artistBaseLink.group(0) + albumSubLink)

		randomIndex = numpy.random.randint(0, len(artistAlbums))

		selectedAlbum = artistAlbums[randomIndex]

		return selectedAlbum

	# Else the artist has only one album
	else:
		return specificArtistLink



# ------------------------------------------------------------------------
# Get user input if they want a random album or one from a specific tag 
# ------------------------------------------------------------------------

def main():

	selectionStr = input("\nPlease enter the number corresponding to the option you want to select: "
		+ "\n1. Completely random album\n2. Random album from a specific tag\n\nInput: ")

	selectionInt = int(selectionStr)

	if selectionInt == 1:

		mainLink = "https://bandcamp.com/artist_index"

		formattedFirstPage = allArtistsFirstPage(mainLink)
		url = numberOfPages(formattedFirstPage, mainLink)
		artistLink = randomlySelectArtist(url)
		albumLink = randomlySelectAlbum(artistLink)

		print("Here is your randomly selected album link: " + albumLink)
	
	elif selectionInt == 2:

		tagName = input("\nGo to the following link to find a tag you are interested in exploring:"
			+ " https://bandcamp.com/tags\nOnce you have found a tag, enter it: ")
		
		mainLink = "https://bandcamp.com/tag/" + tagName

		formattedFirstPage = allArtistsFirstPage(mainLink)
		url = numberOfPages(formattedFirstPage, mainLink)
		albumLink = randomlySelectArtist(url)

		print("Here is your randomly selected " + tagName + " album link: " + albumLink)

if __name__ == "__main__":
    main()
 
