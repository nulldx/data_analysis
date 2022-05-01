import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
input_values = [1,2,3,4,5]
fig,ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
ax.set_title("平方数", fontsize=24,fontproperties="SimHei")
ax.set_xlabel("值",fontsize=14,fontproperties="SimHei")
ax.set_ylabel("值的平分", fontsize=14,fontproperties="SimHei")
ax.tick_params(axis='both', labelsize=14)

plt.show()