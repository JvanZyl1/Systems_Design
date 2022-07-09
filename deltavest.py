import matplotlib.pyplot as plt

labels = ['Orbital adjustment', 'Station keeping', 'Attitude control','Momentum wheel unloading','Stage separation']
sizes = [ 19.05, 555, 500, 30, 6]
colors = [ 'gold', 'lightskyblue', 'lightcoral', 'orchid', 'olive']
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.title("delta v uses, without launch")
plt.show()





'''import matplotlib.pyplot as plt

label = "Launch", "Orbital adjustment", "Station keeping", "Attitde control", "Momentum wheel unloading", "Stage separation"
sizes = [9708.97, 19.05, 566, 500, 30, 6]
colors = ['gold', 'yellowgreen', 'lightcoral','lightskyblue', 'magneta', 'white']
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()
'''
