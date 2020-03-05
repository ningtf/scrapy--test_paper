#coding:utf-8
# r = '<script>down("08届高三生物遗传变异强化训练2","attach\\tkgzsw\\08jiegao1772.rar");</script>'
#需要得到 attach\\tkgzsw\\08jiegao1772.rar
# import re
# rrr = re.findall('\".*?\",\"(.*?)\"',r)[0]
# print(rrr)
# import re
# r = '<script>down("08届高三生物遗传变异强化训练2","attach\\tkgzsw\\08jiegao1772.rar");</script>'
# # pattern = '(?<=,")(.*?)(?=")'
# pa = '<script>down(.*?);</script>'
# res = re.findall(pa,r)[0]
# print(res)
# rr = '(?<=,")(.*?)(?=")'
# ree = re.findall(rr,res)[0]
# print(ree)
import re
r = '<script type="text/javascript">pagenav(48,"/chuzhong/yingyu/nianji2/list/");//PageCount in new.js</script>'
rr = '<script type="text/javascript">pagenav\((.*?),\".*?\"\);//PageCount in new.js</script>'
rrr = re.findall(rr,r)
print(rrr)