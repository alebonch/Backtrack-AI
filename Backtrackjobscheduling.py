import prob1
import prob2
import sys

class JobSchedulingProblem:
    def __init__(self,var, cons):
        self.constraints=dict(cons)
        self.variables=dict(var)
        
    
    def checkAllconstraints(self,assignment) ->bool:
        for var1 in self.constraints:
            for var2 in self.constraints[var1]:
                result=self.check_constraint(var1,var2, assignment)
                if not result:
                    return False
        return True
    
    def check_constraint(self,arg1,arg2,assignment) ->bool:
        if (arg1  not in assignment) or (arg2 not in assignment):
            return True
        if self.constraints[arg1][arg2][1]==0:
            return assignment[arg1]>=self.constraints[arg1][arg2][0]+assignment[arg2]
        if self.constraints[arg1][arg2][1]==1:
            return assignment[arg1]+self.constraints[arg1][arg2][0]<=assignment[arg2]
        if self.constraints[arg1][arg2][1]==2:
            return (assignment[arg1]+self.constraints[arg1][arg2][0]<=assignment[arg2])or(assignment[arg2]+self.constraints[arg1][arg2][0]<=assignment[arg1])

    def add_variable(self, var, domain):
        self.variables[var] = domain
       

    def add_constraint(self, arg1,arg2, value, type, assignment):
        self.constraints[arg1][arg2]=(value,type)
        if type==1:
            self.constraints[arg2][arg1]=(value,0)
        else:
            self.constraints[arg2][arg1]=(value,2)

    

            
    def removeDomains(self, assignment, value,var):
        removeddomains = {}
        for var1 in self.constraints:
            for var2 in self.constraints[var1]:
                if var2 not in assignment and var1 not in assignment:
                    
                    if(self.constraints[var1][var2][1]==1) or (self.constraints[var1][var2][1]==1) :
                        domaintoremove = range(1, self.variables[var1][0] + self.constraints[var1][var2][0])
                    
                        if var2 not in removeddomains and domaintoremove[0]>0:
                            removeddomains[var2] = domaintoremove
                        else:
                            removeddomains[var2] = range(
                                min(removeddomains[var2][0], domaintoremove[0]),
                                max(removeddomains[var2][-1], domaintoremove[-1]) + 1
                            )
                        

                        nuovoDominio = list(self.variables[var2])
                        nuovoDominio = list(filter(lambda x: x not in domaintoremove, nuovoDominio))
                        if not len(nuovoDominio)==0:
                            self.variables[var2] = range(nuovoDominio[0], nuovoDominio[-1] + 1)
               
                    

        return removeddomains

    
    def putRemovedDomains(self,tmp):
        for var1 in self.constraints:
            for var2 in self.constraints[var1]:
                if var2 in tmp:
                    lista1 = list(tmp[var2])
                    lista2 = list(self.variables[var2])
                    lista_unione = lista1 + lista2
                    # Crea un nuovo range basato sulla lista unione
                    self.variables[var2] = range(lista_unione[0], lista_unione[-1] + 1)




    def backtracking_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment
        

        var_not_assigned = [var for var in self.variables if var not in assignment]
        var = var_not_assigned[0]
    
        for value in self.variables[var]:
            new_assignment = assignment.copy()
            new_assignment[var] = value

            if self.checkAllconstraints( new_assignment):
                tmp={}
                
                tmp.update(self.removeDomains(new_assignment, value, var))
                '''
                for var2 in self.variables:
                    print(var2+" :")
                    print(self.variables[var2])
                '''    
                result = self.backtracking_search( new_assignment)
                if result is None:
                    self.putRemovedDomains(tmp)
                if result is not None:
                    return result
        return None


def main(first_argument):
    #Prende in input l'istanza scelta
    #csp=istanzascelta
    
    if first_argument=='1':
        csp = JobSchedulingProblem(prob1.variables,prob1.constraints)
    elif first_argument=='2':
       csp = JobSchedulingProblem(prob2.Variabili,prob2.Constraints)
    #Risolvo il problema CSP
    soluzione = csp.backtracking_search()
    print(soluzione)    

if __name__ == "__main__":
    
    if len(sys.argv)>1:
        first_argument = sys.argv[1]
    

    first_argument='1'
    main(first_argument)



