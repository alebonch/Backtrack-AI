import prob1
import prob2
import prob3
import prob4
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

    def printcons(self):
        for var1 in self.constraints:
            for var2 in self.constraints[var1]:
                if self.constraints[var1][var2][1]==1:
                    print(var1,"+",self.constraints[var1][var2][0],"≤",var2 )
                if self.constraints[var1][var2][1]==2:
                    print("(",var1,"+",self.constraints[var1][var2][0],"≤",var2,") or (",
                          var2,"+",self.constraints[var1][var2][0],"≤",var1,")")


            
    def removeDomains(self, assignment, value,var):
        removeddomains = {}
        for var1 in self.constraints:
            for var2 in self.constraints[var1]:
                if var2 not in assignment and var1 not in assignment:
                    
                    if(self.constraints[var1][var2][1]==1):
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
                elif(self.constraints[var1][var2][1]==2):
                    if(var1 in assignment):
                        assign=assignment[var1]
                        domaintoremove = range(assign, assign+self.constraints[var1][var2][1])
                        if var2 not in removeddomains and domaintoremove[0]>0:
                            removeddomains[var2] = domaintoremove
                        else:
                            removeddomains[var2] = range(
                                min(removeddomains[var2][0], domaintoremove[0]),
                                max(removeddomains[var2][-1], domaintoremove[-1]) + 1
                            )
                    elif(var2 in assignment):
                        assign=assignment[var2]
                        domaintoremove = range(assign, assign+self.constraints[var1][var2][1])
                        if var1 not in removeddomains and domaintoremove[0]>0:
                            removeddomains[var1] = domaintoremove
                        else:
                            removeddomains[var1] = range(
                                min(removeddomains[var1][0], domaintoremove[0]),
                                max(removeddomains[var1][-1], domaintoremove[-1]) + 1
                            )
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


    def ChooseVariable(self,variables):
        sum=0
        chosen=variables[0]
        for var in self.constraints[chosen]:
            if self.constraints[chosen][var][1]==1 or self.constraints[chosen][var][1]==2:
                sum=sum+1
        for var1 in variables:
            tmp=0
            for var2 in self.constraints[var1]:
                if self.constraints[var1][var2][1]==1 or self.constraints[var1][var2][1]==2:
                    tmp=tmp+1
            if tmp>sum:
                sum=tmp
                chosen=var1
        return chosen




    def backtracking_search(self,richiesta, assignment={} ):
        if len(assignment) == len(self.variables):
            if assignment not in solutions:
                solutions.append(assignment)
                print(assignment)
            if len(solutions)==richiesta:
                return True
            return None
        

        var_not_assigned = [var for var in self.variables if var not in assignment]
        var = self.ChooseVariable(var_not_assigned)
    
        for value in self.variables[var]:
            new_assignment = assignment.copy()
            new_assignment[var] = value

            if self.checkAllconstraints( new_assignment):
                tmp={}
                
                tmp.update(self.removeDomains(new_assignment, value, var))
                result = self.backtracking_search(richiesta, new_assignment)
                if result is None:
                    self.putRemovedDomains(tmp)
                #non sarà mai non None
                if result is not None:
                    return True
        return None
    
    def findBestSolution(self):
        best = []
        chiavi=list(solutions[0].keys())
        lastkey=chiavi[-1]
        maxim=solutions[0][lastkey]
        for solution in solutions:
            if solution[lastkey]<maxim:
                best = []
                best.append(solution)
                maxim=solution[lastkey]
            if solution[lastkey]==maxim:
                best.append(solution)
        if len(best)==1:
            print("La soluzione migliore è:")
            print(best)
        if len(best)>1:
            print("Lista delle soluzioni migliori:")
            for i in best:
                print(i)    
        return best

solutions=[]
def main(first_argument):
    #Prende in input l'istanza scelta
    #csp=istanzascelta

    print("Inserire il numero di soluzioni richieste:")
    richiesta =  input()
    richiesta = int(richiesta)

    
    if first_argument=='1':
        csp = JobSchedulingProblem(prob1.variables,prob1.constraints)
    elif first_argument=='2':
       csp = JobSchedulingProblem(prob2.Variabili,prob2.Constraints)
    elif first_argument=='3':
       csp = JobSchedulingProblem(prob3.Variabili,prob3.constraints)

    #Risolvo il problema CSP
    csp.backtracking_search(richiesta)  
    #restituisco la soluzione migliore
    csp.findBestSolution()

if __name__ == "__main__":
    #first_argument = '1'
    if len(sys.argv)>1:
        first_argument = sys.argv[1]
    main(first_argument)