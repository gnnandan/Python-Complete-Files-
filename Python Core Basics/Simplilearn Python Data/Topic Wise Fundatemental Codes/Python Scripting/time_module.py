import time

epc = time.time()
print(f"Number of second passed {epc}")

# ! formatting it in properway
localtime = time.localtime(epc)
print(f"The proper format of epc is {localtime}")

print(f"The treditional format of the localtime is {localtime.tm_year}")
print(f"To display the treditional format completly means {time.ctime(epc)}")