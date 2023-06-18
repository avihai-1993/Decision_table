from DecisionTable import DecisionTable as DT

e = {'x': "j" , 'y': 39 , 'z' : 39 } #get an even some how that look like that
e1 = {'x': "i" , 'y' : 41 ,'z' : 41 } #get an even some how
e2 = {'x': "t" , 'y' : 41 ,'z' : 41 } #get an even some how
path = 'dt.csv'
dt = DT(path)
res = dt(e)
res1 = dt(e1)
res2 = dt(e2)
print(res,res1,res2)
print(dt.score_event(e))
print(dt.score_event(e1))
print(dt.score_event(e2))


#print(eval("'n'"))


