import nearestneighbors as nn

nx=5
ny=4
nz=3
nxyz=nx*ny*nz
list=nn.NN3D(nx,ny,nz)

print('\n')
for k in range(nz):
	for j in range(ny):
		for i in range(nx):
			print(nx*ny*nz-k*nx*ny-(j+1)*nx+i,end=' ')
		print('')
	print('\n')
print('\n\n')
for i in range(nxyz):
	print(i,end=' : ')
	for j in range(26):
		print(list[i][j],end=' ')
	print('')

