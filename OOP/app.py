from kettle import Kettle

k1 = Kettle(1500, 2000, 'white')
print('K1', k1.vol, k1.pwr, k1.clr)
k2 = Kettle(1000, 1500, 'black')
print('K2', k2.vol, k2.pwr, k2.clr)
k3 = Kettle(1500, 2000, 'black')
print('K3', k3.vol, k3.pwr, k3.clr)

k1.openLid()
k2.openLid()
k1.addWater(500)
k1.addWater(500)
k1.closeLid()
k1.on()
k1.boilKettle(100,5)
k1.off()
k2.on()

