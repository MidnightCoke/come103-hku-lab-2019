print(format("kilograms", "<15s"), format("pounds", "<15s"),
      "|", format("pounds", ">15s"), format("kilograms", ">15s"))
print("-"*65)

for x in range(10):
    KG = (x+1)*10
    POUND = 20+(x*15)
    print(format(KG, "<15d"), format(KG*2.2, "<15.2f"),
          "|", format(POUND, ">15d"), format(POUND*0.45, ">15.2f"))
