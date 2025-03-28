# encoding=utf8

import urllib.parse
import webbrowser

from wox import Wox, WoxAPI

from BookmarkFolderOpener import BOpener
from util import Logger


class Main(Wox):
    
    # 必须有一个query方法，用户执行查询的时候会自动调用query方法
    def query(self, query):
        logger = Logger()
        logger.info("query is: "+query)
        
        bopener = BOpener()
        # 返回的是模糊匹配的书签文件价名称列表
        toBeOpenedBookmarkFolders = bopener.getMatchedBookmarkFolderNames(query)
        logger.info(toBeOpenedBookmarkFolders)
        results = []
        if query != '':
            for bookMarkFolder in toBeOpenedBookmarkFolders:
                bookmarksFolderUrls = bopener.getBookmarkfolderUrls(bookMarkFolder[0])
                results.append({
                    "Title": bookMarkFolder[0],
                    "SubTitle": "Open bookmark folder: {}".format(bookMarkFolder[0]),
                    "IcoPath": "Images/app.ico",
                    "JsonRPCAction": {
                        "method":"openbookmarkfolder",
                        "parameters":bookmarksFolderUrls,
                        "dontHideAfterAction":False
                    }
                })            
            if results == []:
                results.append({
                    "Title": "None",
                    "SubTitle": "Query: {}".format(query),
                    "IcoPath": "Images/app.ico"
                })
        
        logger.info("Query: {}".format(results))
        return results

    def openbookmarkfolder(self, *bookmarksFolderUrls):
        logger = Logger()
        logger.info("进入逐个打开URL")
        for encodedUrl in bookmarksFolderUrls:
            url = urllib.parse.unquote(encodedUrl)
            logger.info(url)
            webbrowser.open_new_tab(url)
        WoxAPI.change_query(url)

if __name__ == "__main__":
    Main()
