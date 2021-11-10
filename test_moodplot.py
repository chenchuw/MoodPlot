import moodplot as mp

def test_invalidTopic():
	"If the topic's search result is empty, return the error message"

	assert mp.analysis("SOMETEXTthatIfiguredTHEREwillBEnoResults", '1') == \
	"No results found with the given topic... Please try again with another topic :)"


def test_emptyInputs():
	"If the user does not give topic or count, return the error message"

	assert mp.analysis("", '5') == \
	'Sorry, please try again and enter a valid topic and number of tweets...'


def test_badCount():
	"If the user inputs a non-digit string for count, return the error message"

	assert mp.analysis("Olympic", "badinput") == \
	"Sorry, please give a positive number for number of tweets..."


def test_zeroCount():
	"If the user inputs 0 or negative number for count, return the error message"

	assert mp.analysis("Olympic", '0') == \
	"Sorry, please try again and enter a valid topic and number of tweets..."

	assert mp.analysis("Olympic", '-1') == \
	"Sorry, please give a positive number for number of tweets..."