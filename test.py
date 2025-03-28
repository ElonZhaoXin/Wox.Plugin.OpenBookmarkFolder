# # encoding=utf8

# import webbrowser

# from BookmarkFolderOpener import BOpener


# def openbookmarkfolder(toBeOpenedBookmarks):
#     for url in toBeOpenedBookmarks:
#         webbrowser.open_new_tab(url)
        
# bopener = BOpener()
# query="IP"
# toBeOpenedBookmarks = bopener.getBookmarkfolderUrls(query)

# openbookmarkfolder(toBeOpenedBookmarks)


from pypinyin import Style, pinyin, slug

hanzi = '知乎'
print(slug(hanzi, separator='', errors='ignore'))

stringWithoutHanzi = 'Test'
print(slug(stringWithoutHanzi, separator='', errors='default'))

stringWithPartHanzi = '知乎test'
print(slug(stringWithPartHanzi, separator='', errors='default'))

stringWithPartHanzi1 = '知乎Test'
print(slug(stringWithPartHanzi1, separator='', errors='default'))