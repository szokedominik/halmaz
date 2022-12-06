reggeli = {'tea', 'vaj', 'piritós', 'sajt'} 
ebed = set()
ebed = set(['halászlé', 'kenyér', True])  
reggeli.add('lekvár')
reggeli.pop()
reggeli.remove('sajt')
reggeli.discard('sajt')
    
reggeli1 = {'víz', 'tea', 'vaj', 'pirítós'}
ebed = {'ívz', 'halászlé', 'kenyér'}

print(reggeli1 & ebed)
print(reggeli1 | ebed)
print(reggeli1 - ebed)
print(reggeli1 ^ ebed)

gyumolcskosar = ['eper', 'alma', 'szilva', 'eper']
fajta = set()
for gyumolcs in gyumolcskosar:
    fajta.add(gyumolcs)
print(fajta)

