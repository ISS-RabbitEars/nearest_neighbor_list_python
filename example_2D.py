import nearestneighbors as nn

nx=4
ny=4
nxy=nx*ny
list=nn.NN2D(nx,ny)

print('\n')
for j in range(ny):
	for i in range(nx):
		print(nx*ny-(j+1)*nx+i,end=' ')
	print('')
print('\n')
for i in range(nxy):
	print(i,end=' : ')
	for j in range(8):
		print(list[i][j],end=' ')
	print('')
