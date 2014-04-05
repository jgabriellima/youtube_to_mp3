__author__ = 'stark'

import gdata.youtube
import gdata.youtube.service
import commands

class YoutubeDownload(object):

    #Class Constructor
    #@param filePath: The file path with the input data.
    def __init__(self,filePath,tokensplit):
        self.path = filePath
        self.token= tokensplit
        self.names = []

    def run(self):
        # print commands.getstatusoutput('ls /bin/ls')
        self.names = self.loadData(self.path)
        for n in self.names:
            self.search(n)

    def run_download_mp3(self):
        self.names = self.loadData(self.path)
        for n in self.names:
            self.search(n)

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
        _id = ''
        self.client = gdata.youtube.service.YouTubeService()
        self.query = gdata.youtube.service.YouTubeVideoQuery()
        self.query.vq = title
        self.query.max_results = 25
        self.query.start_index = 1
        self.query.racy = 'exclude'

        self.query.orderby = 'relevance'
        feed = self.client.YouTubeQuery(self.query)
        #return most relevant title
        for entry in feed.entry:
            _id = 'https://www.youtube.com/watch?v=%s'%(entry.id.text.split('/')[-1])
            print '%s = %s'%(title,_id)
            break
        return _id

youtube = YoutubeDownload('dataset/dataset.txt','\t')
youtube.run()