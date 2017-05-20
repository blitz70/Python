from content_management import Content

topics_dict = Content()

init_template = '''
@app.route(topics_dict["CURRENTTOPIC"][CURRENTINDEX][1], methods=['GET', 'POST'])
def CURRENTTITLE():
    return render_template("CURRENTHTML", curLink = topics_dict["CURRENTTOPIC"][CURRENTINDEX][1], curTitle = topics_dict["CURRENTTOPIC"][CURRENTINDEX][0],  nextLink = topics_dict["CURRENTTOPIC"][NEXTINDEX][1], nextTitle = topics_dict["CURRENTTOPIC"][NEXTINDEX][0])
'''


def convert(arg_str):
    if __name__ == '__main__':
        if __name__ == '__main__':
            return arg_str.\
                replace(' ', '').replace('-', '').\
                replace('(', '').replace(')', '').\
                replace('.', '').replace(',', '').\
                replace('"', '').replace("'", "").\
                replace(':', '').replace('/', '').replace('!', '').replace('?', '').\
                lower()

for subject in topics_dict:
    #print(subject)
    CURRENTTOPIC = str(subject)
    count_topic = 0
    for topic in topics_dict[subject]:
        CURRENTINDEX = str(count_topic)
        CURRENTTITLE = str(convert(topic[0]))
        CURRENTHTML = str('tutorials/' + convert(CURRENTTOPIC) + '/' + CURRENTTITLE + '.html')
        NEXTINDEX = str(count_topic+1)
        print(init_template.replace("CURRENTTOPIC", CURRENTTOPIC).replace("CURRENTINDEX", CURRENTINDEX).replace("NEXTINDEX", NEXTINDEX).replace("CURRENTTITLE", CURRENTTITLE).replace("CURRENTHTML", CURRENTHTML))
        count_topic += 1
