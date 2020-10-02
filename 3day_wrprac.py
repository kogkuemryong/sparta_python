# f = open("test.txt", "w", encoding="utf-8")
# f.write("안녕, 스파르타!\n")
#
# for i in [1,2,3,4,5]:
#     f.write(f'{i} 번째 줄이에요. \n')
# f.close()

text = ''
with open("KakaoTalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines() # 한줄씩 출력
    for line in lines[5:]:
        if '] [' in line: # 시스템 메세지 안받기
            text += line.split(']')[2].replace('ㅋ','').replace('ㅠ','').replace('이모티콘\n','').replace('사진\n','').replace('웅','').replace('응','').replace('진짜','') \
                .replace('많이', '').replace('너무','').replace('내가','')
            

# print(text)

# 워드 클라우드 만들기
from wordcloud import WordCloud

# wc = WordCloud(font_path= 'C:/Windows/Fonts/malgun.ttf', background_color="white", width=600, height=400)
# wc.generate(text)
# wc.to_file("result.png")


# 마스킹된 워드 클라우드 만들기
from PIL import Image
import numpy as np

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")

# 폰트 검색
# import matplotlib.font_manager as fm
# for font in fm.fontManager.ttflist:
# # 이용 가능한 폰트 중 '고딕'만 선별
#
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)

# C:\Windows\Fonts\malgun.ttf