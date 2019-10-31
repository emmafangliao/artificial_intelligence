import Importable
import a1

ans = input("Do you want to run the test?")

if ans in ["y", "yes"]:
    Importable.five_x_cubed_plus_2(3)
else:
    print("Ok, we won't run the test")
    
