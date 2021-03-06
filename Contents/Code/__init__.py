NAME = 'Nederland 24'
BASE_URL = 'http://www.npo.nl/live'

CHANNELS = [
	{
		'name': 'Nederland 1',
		'icon': 'https://dl.dropboxusercontent.com/u/2974527/Plex/Nederland-24/ned1.png',
		'slug': 'NL1'
	},
	{
		'name': 'Nederland 2',
		'icon': 'https://dl.dropboxusercontent.com/u/2974527/Plex/Nederland-24/ned2.png',
		'slug': 'NL2'
	},
	{
		'name': 'Nederland 3',
		'icon': 'https://dl.dropboxusercontent.com/u/2974527/Plex/Nederland-24/ned3.png',
		'slug': 'NL3'
	},
	{
		'name': '101 TV',
		'icon': '',
		'slug': '101'
	},
	{
		'name': 'Cultura 24',
		'icon': '',
		'slug': 'CUL'
	},
	{
		'name': 'Best 24',
		'icon': '',
		'slug': 'HIL'
	},
	{
		'name': 'Holland Doc 24',
		'icon': '',
		'slug': 'HOL'
	},
	{
		'name': 'Humor TV 24',
		'icon': '',
		'slug': 'HTV'
	},
	{
		'name': 'Journaal 24',
		'icon': '',
		'slug': 'N24'
	},
	{
		'name': 'Politiek 24',
		'icon': '',
		'slug': 'P24'
	},
	{
		'name': 'Zappelin/Zapp',
		'icon': '',
		'slug': 'OTV'
	},
	{
		'name': '3FM',
		'icon': 'https://dl.dropboxusercontent.com/u/2974527/Plex/Nederland-24/3fm.png',
		'slug': '3FM'
	}
]

####################################################################################################
def Start():

	ObjectContainer.title1 = NAME

####################################################################################################
@handler('/video/nederland24', NAME)
def MainMenu():

	oc = ObjectContainer()

	for channel in CHANNELS:
		oc.add(VideoClipObject(
			url = '%s#%s' % (BASE_URL, channel['slug']),
			title = channel['name'],
			thumb = Resource.ContentsOfURLWithFallback(channel['icon'])
		))

	return oc
