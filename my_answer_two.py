
#字典如何删除键和合并两个字典

#del和update方法
dic={"name":"zs","age":18}
del dic["name"]
dic
{'age':18}
dic2={"name":"1s"}
dic.update(dic2)
dic
{'age':18,'name':'1s'}