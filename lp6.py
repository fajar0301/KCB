from ai_pkg.planning import (HLA, Problem as PlanProblem)


library = {
        'HLA': ['Go(Home,Airport)', 
                'Go(Home,Airport)', 
                'Drive(Home,AirportParking)', 
                'Shuttle(AirportParking,Airport)', 
                'Taxi(Home,Airport)'],
        'steps':[['Drive(Home,AirportParking)','Shuttle(AirportParking,Airport)'], 
                ['Taxi(Home,Airport)'], 
                [], 
                [], 
                []],
        'precond': [['At(Home) & Have(Car)'], 
                        ['At(Home)'], 
                        ['At(Home) & Have(Car)'], 
                        ['At(AirportParking)'], 
                        ['At(Home)']],
        'effect': [['At(Airport) & ~At(Home)'], 
                        ['At(Airport) & ~At(Home) & ~Have(Cash)'], 
                        ['At(AirportParking) & ~At(Home)'],
                        ['At(Airport) & ~At(LongTermParking)'], 
                        ['At(Airport) & ~At(Home) & ~Have(Cash)']] 
                        
        
}

goto_airport = HLA('Go(Home,Airport)', precond='At(Home)', effect='At(Airport) & ~At(Home)')

problem = PlanProblem('At(Home) & Have(Cash) & Have(Car) ', 'At(Airport) & Have(Cash)', [goto_airport])


solution = PlanProblem.hierarchical_search(problem, library)
for i in range(0, len(solution)):
    print('precondition : ', solution[i].precond)
    print('action : ', solution[i].name, solution[i].args)
    print('effect : ', solution[i].effect)