squares = 64
grains = 0
incrementor = 1
for i in range(0,squares):
    print(f"Square {i+1} - {incrementor} grains, increase of {incrementor*30}mg")
    grains += incrementor
    incrementor = incrementor * 2
print(f"Total weight: {grains*30:,}mg ({grains:,} grains)")    
