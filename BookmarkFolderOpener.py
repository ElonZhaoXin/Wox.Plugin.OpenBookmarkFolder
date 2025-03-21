#encoding=utf8
import json
import os
import urllib.parse

from fuzzywuzzy import process
from pypinyin import slug


class BOpener():      

    def load(self, load_name):
        with open(load_name, encoding='UTF-8') as json_file:
            data = json.load(json_file)
            return data
        
    def process_bookmarks(self):
        # windows
        bookmark_name = os.path.join(os.path.expanduser("~"), 'AppData//Local//Google//Chrome//User Data//Default','Bookmarks')
        data=self.load(bookmark_name)
        bookmarks = data['roots']['bookmark_bar']['children'] + data['roots']['other']['children']
        bookmarksDic = {}
        
        """递归处理书签数据"""
        for item in bookmarks:
            if "children" in item:  # 书签文件夹
                childUrl = []
                for childItem in item["children"]:
                    if "url" in childItem:  # 书签项
                        childUrl.append(urllib.parse.quote(childItem['url'],  safe=":/"))
                
                bookMarkFolderName = item['name'].lower()
                bookmarksDic[bookMarkFolderName]=childUrl
                # 如果文件夹名称是中文，那就存一份英文名称对应的key的映射
                bookMarkFolderNameOfPinyin= slug(bookMarkFolderName, separator='', errors='default')
                bookmarksDic[bookMarkFolderNameOfPinyin.lower()]=childUrl
                # 如果标签文件夹是中文或部分中文，不是全拼音的，也插入一份，供精确搜索
                if bookMarkFolderName != bookMarkFolderNameOfPinyin :
                    bookmarksDic[bookMarkFolderName.lower()]=childUrl
                
        return bookmarksDic 

    
    def getBookmarkfolderUrls(self, folderName):    
        bookmarksDic = self.process_bookmarks()
        toBeOpenedBookmarks = bookmarksDic[folderName.lower()]
        return toBeOpenedBookmarks
    
    # 支持书签文件夹名称部分或者模糊查询推荐
    def getMatchedBookmarkFolderNames(self, folderName):
        bookmarksDic = self.process_bookmarks()        
        matchedFolderNames = process.extract(query=folderName, choices=bookmarksDic.keys())
        return matchedFolderNames
        