import pandas as pd

class DecisionTable:

    def __init__(self,csv_table_path: str ):
        self.dtdf = pd.read_csv(csv_table_path,dtype=str)
        self.l_labels = self.dtdf.keys().values
        self.last_col_name = self.l_labels[-1]
        self.decisions = set(self.dtdf[self.last_col_name])
        self.N_F = len(self.l_labels) - 1



    def __call__(self,x : dict ,func : callable = None,*args, **kwargs):
        __s__ = 0
        for i in range(len(self.dtdf)):
            for l in range(len(self.l_labels)-1) :
                try:
                    __s__ += eval("p "+str(self.dtdf.loc[i,self.l_labels[l]]).replace('$',''), {},{'p': x[self.l_labels[l]]})
                except:
                    continue
            if len(self.l_labels) - 1 == __s__:
                return self.dtdf.loc[i,self.last_col_name]

        return None

    def score_event(self,x : dict,param_w_score : dict = None):
        if param_w_score is None:
            ps= {x_key : 1 for x_key in x.keys()}
        else:
            ps = param_w_score

        score_dict_to_return = {cls : 0 for cls in self.decisions}

        for i in range(len(self.dtdf)):
            for l in range(len(self.l_labels) - 1):
                try:
                   res = eval("p " + str(self.dtdf.loc[i, self.l_labels[l]]).replace('$', ''), {}, {'p': x[self.l_labels[l]]})
                except:
                   res = 0

                score_dict_to_return[self.dtdf.loc[i,self.last_col_name]] += (res * ps[self.l_labels[l]])/self.N_F

        return score_dict_to_return
