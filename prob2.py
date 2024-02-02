Variabili={'Var0': range(1, 51),
 'Var1': range(1, 51),
 'Var2': range(1, 51),
 'Var3': range(1, 51),
 'Var4': range(1, 51),
 'Var5': range(1, 51),
 'Var6': range(1, 51),
 'Var7': range(1, 51),
 'Var8': range(1, 51),
 'Var9': range(1, 51)}

Constraints={
    'Var0': {'Var1': (5, 2), 'Var2': (7, 1),'Var9': (9, 1)},
 'Var1': {'Var0': (5, 2), 'Var3': (4, 1), 'Var9': (2, 1)},
 'Var2': { 'Var4': (1, 1),'Var9': (10, 1)},
 'Var3': {'Var5': (9, 1), 'Var9': (5, 1)},
 'Var4': {'Var6': (8, 1), 'Var9': (3, 1)},
 'Var5': {'Var7': (2, 1),'Var9': (8, 1)},
 'Var6': { 'Var8': (3, 1), 'Var9': (7, 1)},
 'Var7': {'Var9': (9, 1)},
 'Var8': {'Var9': (9, 1)},
 'Var9': {}
}


'''
if(self.constraints[var1][var2][1]==0):
                        domaintoremove = range(assignment[var1]+self.constraints[var1][var2][0],self.variables[var1][-1]+1)
                        if var2 not in removeddomains and domaintoremove[0]>0:
                            removeddomains[var2] = domaintoremove

                        removeddomains[var2] = range(
                                min(removeddomains[var2][0], domaintoremove[0]),
                                max(removeddomains[var2][-1], domaintoremove[-1]) + 1
                            )
                        

                        nuovoDominio = list(self.variables[var2])
                        nuovoDominio = list(filter(lambda x: x not in domaintoremove, nuovoDominio))
                        if not len(nuovoDominio)==0:
                            self.variables[var2] = range(nuovoDominio[0], nuovoDominio[-1] + 1)
                    if(self.constraints[var1][var2][1]==2):
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
                            '''