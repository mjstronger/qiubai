
class QiubaiPipeline(object):
    def __init__(self):
        # 生成title.txt用于存储除内容外所有内容,分行存储
        self.cfile = open('E://qiubai/title.txt', 'a', encoding='utf8')


    def process_item(self, item, spider):
        avatar = item['avatar']
        profile_link = item['profile_link']
        content = item['content']
        name = item['name']
        age = item['age']
        content_link = item['content_link']
        up = item['up']
        comment_num = item['comment_num']
        self.cfile.write(f'头像:{avatar}\n头像链接:{profile_link}\n内容:{content}\n内容链接:{content_link}\n昵称:{name}\n年龄:{age}\n点赞数:{up}\n评论数:{comment_num}\n\n')
        # 以writelines将列表形式的内容写入.html文件
        # with open(f'E://qiubai/{avatar}.html', 'a', encoding='utf-8') as wl:
            # wl.writelines(content)
        return item
