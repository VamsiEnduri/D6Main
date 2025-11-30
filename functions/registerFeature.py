def register__():
    name=input("enter name here :--- ")
    age=input("enter age here :--- ")
    batchNo=input("enter batchNo here :--- ")
    passedoutYear=input("enter passedoutYear here :--- ")
    stream=input("enter stream here :--- ")
    passsword=input("password here :--  ")
    cPasssword=input("confirm password here :--  ")
    if cPasssword==passsword:
        newUser={
            "n":name,
            "a":age,
            "bNo":batchNo,
            "pYear":passedoutYear,
            "s":stream,
            "p":passsword
        }
        return newUser