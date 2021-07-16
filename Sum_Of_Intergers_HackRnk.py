def Sum_Of_Intergers(Arg_1):
    Temp_Var = 0    
    for Loop_Var in Arg_1:
        Temp_Var += int(Loop_Var)
    if(len(str(Temp_Var)) == 1):
        return Temp_Var
    else:
        return Sum_Of_Intergers(str(Temp_Var))
