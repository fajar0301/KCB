from kanren.core import var, eq, run
from kanren.facts import Relation, facts

parent = Relation()
facts(parent, ("Amin","Badu"),
                ("Amin","Budi"), 
                ("Anang","Didi"),
                ("Anang","Dadi"),
                ("Slamet","Amin"),
                ("Slamet","Anang"))
x = var()
child = "Budi"
ayah = run(1, x, parent(x, child))
print("\nNama ayah" + child + ": ")
for item in ayah:
    print(item)                
