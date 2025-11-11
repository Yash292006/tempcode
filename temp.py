import sys
if len(sys.argv) ==2:
    script_name = temp.argv[0]
    temp=temp.argv[1]
    print("user provided inputs")
else:
    script_name=sys.argv[0]
    temp="40"
    print("default inputs")
if temp<"15":
    state="cold"
elif temp<"15"and temp>"30":
    state="normal"
else:
    state="hot"
print("Script Name:",script_name)
print("Temperature:",temp)
print("State:",state)
