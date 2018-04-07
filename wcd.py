# coding : utf-8
# author : boring

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, ImageColorGenerator
from imageio import imread

# 初始化
img = "img.jpg"
file = "听听那冷雨.txt"
font_path = "microhei.ttc"
stopwords = "stopwords.txt"
my_word_list = ['听听那冷雨']
# 设置背景图片
backcolor = imread(path.join(img))

#设置词云属性
wordcloud = WordCloud(
    font_path = font_path,
    background_color = "white",
    max_words = 2000,
    max_font_size = 100,
    random_state = 50,
    width = 1000, height = 1415, margin = 2
)

# 自定义分词
for word in my_word_list:
    jieba.add_word(word)

# 读取并显示文本内容
text = open(path.join(file)).read()

# 切词
segment = jieba.cut(text, cut_all=False)
word_list = []
words = '/ '.join(segment)
stop_file = open(stopwords)
stop_text = stop_file.read( )
stop_file.close( )
stop_segment_list=stop_text.split('\n')
for word in words.split('/'):
    if not(word.strip() in stop_segment_list) and len(word.strip()) > 1:
        word_list.append(word)
text = ''.join(word_list)

# 创建图片
wordcloud.generate(text)
image_color = ImageColorGenerator(backcolor)
plt.figure()
plt.imshow(wordcloud.recolor(color_func=image_color))
plt.axis("off")
plt.show()
# 保存图片
wordcloud.to_file(path.join('out.png'))
