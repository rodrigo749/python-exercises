medida = float(input('Digite um número em metros: '))
cm = medida * 100
mm = medida * 1000
dam = medida / 10
dm = medida * 10
hm = medida / 100
km = medida / 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
print ('A medida de {}m, corresponde a {} dm e {} dam'.format(medida, dm, dam))
print ('A medida de  {}m, corresponde a {} hm e  {} km'.format(medida, hm, km))


