__author__ = 'stark'

import gdata.youtube
import gdata.youtube.service
import commands

class YoutubeDownload(object):

    #Class Constructor
    #@param filePath: The file path with the input data.
    def __init__(self,folder,filePath,tokensplit):
        self.path = filePath
        self.token= tokensplit
        self.names = []
        self.folder = folder

    #Just read file and show this list with youtube url
    def run(self):
        #read file and get the names on format <Author Name> <Music Name>
        self.names = self.loadData(self.path)
        for n in self.names:
            print self.search(n)

    #Read input dataset, get youtube url, download audio on m4a format and put on specific folder
    def run_download_mp3(self):
        self.names = self.loadData(self.path)
        for n in self.names:
            video = self.search(n)
            url = video['url']
            print 'Downloading... %s'%(video['title'])
            print commands.getstatusoutput('cd %s && youtube-dl %s --extract-audio'%(self.folder,url))

    #Invoke convert.sh file for convert .m4a to mp3
    #@param filePath: The file path
    def convertM4aToMp3(self):
        print commands.getstatusoutput('cd %s && ../convert.sh'%(self.folder))

    #Load the dataset
    #@param filePath: The file path
    def loadData(self,filePath):
        names = []
        fileHandle = open(filePath)
        #Ignore the first line (header)
        fileList = fileHandle.readlines()
        for line in fileList:
            # line = line.strip()
            lineSet = line.split(self.token)
            if lineSet[0].isalpha():
                # print lineSet
                names.append("%s - %s"%(lineSet[0], lineSet[1].strip('\n')))
                # self.names.append("%s - %s"%(lineSet[0], lineSet[1].strip('\n')))
        fileHandle.close()
        return names
        # print self.names

    def search(self,title):
        _id = {}
        self.client = gdata.youtube.service.YouTubeService()
        self.query = gdata.youtube.service.YouTubeVideoQuery()
        self.query.vq = title
        self.query.max_results = 1
        self.query.start_index = 1
        self.query.racy = 'exclude'
        self.query.orderby = 'relevance'
        feed = self.client.YouTubeQuery(self.query)
        #return most relevant title
        for entry in feed.entry:
            _id = {'title': title, 'url': 'https://www.youtube.com/watch?v=%s' % (entry.id.text.split('/')[-1])}
            break
        return _id

youtube = YoutubeDownload('~/PyProjects/youtube_to_mp3/musics','dataset/dataset_1.txt','\t')
youtube.run_download_mp3()
youtube.convertM4aToMp3()