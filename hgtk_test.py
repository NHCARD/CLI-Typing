import hgtk
from articloid import ko_srt
from hgtk.checker import is_hangul

a = hgtk.text.decompose("감사합니다.   사랑합니다.", compose_code='')

b = hgtk.text.decompose("안녕", compose_code='')

# print(a)

# if is_hangul(ko_srt[0]) == False:
#     print('true')

# print(len(ko_srt[0]))
