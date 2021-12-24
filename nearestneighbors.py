
def NN2D(nx,ny):
	nnl=[]
	nxy=nx*ny
	for i in range(nxy):
		temp=[]
		for j in range(8):
			temp.append(0)
		nnl.append(temp)	

	#corner 1 i=0
	nnl[0][0]=nxy-1
	nnl[0][1]=nxy-nx
	nnl[0][2]=nxy-nx+1
	nnl[0][3]=nx-1
	nnl[0][4]=1
	nnl[0][5]=2*nx-1
	nnl[0][6]=nx
	nnl[0][7]=nx+1

	#corner 2
	i=nx-1
	nnl[i][0]=nxy-2
	nnl[i][1]=nxy-1
	nnl[i][2]=nxy-nx
	nnl[i][3]=nx-2
	nnl[i][4]=0
	nnl[i][5]=2*nx-2
	nnl[i][6]=2*nx-1
	nnl[i][7]=nx

	#corner 3
	i=nxy-nx
	nnl[i][0]=i-1
	nnl[i][1]=i-nx
	nnl[i][2]=i-nx+1
	nnl[i][3]=nxy-1
	nnl[i][4]=i+1
	nnl[i][5]=nx-1
	nnl[i][6]=0
	nnl[i][7]=1

	#corner 4
	i=nxy-1
	nnl[i][0]=i-nx-1
	nnl[i][1]=i-nx
	nnl[i][2]=nxy-2*nx
	nnl[i][3]=nxy-2
	nnl[i][4]=nxy-nx
	nnl[i][5]=nx-2
	nnl[i][6]=nx-1
	nnl[i][7]=0

	#edge 1 & 2
	for i in range(1,nx-1):
		ii=nx*(ny-1)+i
		nnl[i][0]=ii-1
		nnl[i][1]=ii
		nnl[i][2]=ii+1
		nnl[i][3]=i-1
		nnl[i][4]=i+1
		nnl[i][5]=nx+i-1
		nnl[i][6]=nx+i
		nnl[i][7]=nx+i+1
		nnl[ii][0]=ii-nx-1
		nnl[ii][1]=ii-nx
		nnl[ii][2]=ii-nx+1
		nnl[ii][3]=ii-1
		nnl[ii][4]=ii+1
		nnl[ii][5]=i-1
		nnl[ii][6]=i
		nnl[ii][7]=i+1

	#edge 3 & 4
	for i in range(1,ny-1):
		i1=i*nx
		i2=(i+1)*nx-1
		nnl[i1][0]=i1-1
		nnl[i1][1]=i1-nx
		nnl[i1][2]=i1-nx+1
		nnl[i1][3]=i1+nx-1
		nnl[i1][4]=i1+1
		nnl[i1][5]=i1+2*nx-1
		nnl[i1][6]=i1+nx
		nnl[i1][7]=i1+nx+1
		nnl[i2][0]=i2-nx-1
		nnl[i2][1]=i2-nx
		nnl[i2][2]=i2-2*nx+1
		nnl[i2][3]=i2-1
		nnl[i2][4]=i2-nx+1
		nnl[i2][5]=i2+nx-1
		nnl[i2][6]=i2+nx
		nnl[i2][7]=i2+1
	#bulk
	for i in range(1,ny-1):
		for j in range(1,nx-1):
			ii=i*nx+j
			nnl[ii][0]=ii-nx-1
			nnl[ii][1]=ii-nx
			nnl[ii][2]=ii-nx+1
			nnl[ii][3]=ii-1
			nnl[ii][4]=ii+1
			nnl[ii][5]=ii+nx-1
			nnl[ii][6]=ii+nx
			nnl[ii][7]=ii+nx+1
	return nnl


def NN3D(nx,ny,nz):
	nnl=[]
	nxyz=nx*ny*nz
	nxy=nx*ny
	nyz=ny*nz
	for i in range(nxyz):
		temp=[]
		for j in range(26):
			temp.append(0)
		nnl.append(temp)

	#corner 1 i=0
	nnl[0][0]=nxyz-1
	nnl[0][1]=nx*(nyz-1)
	nnl[0][2]=nx*(nyz-1)+1
	nnl[0][3]=nx*(ny*(nz-1)+1)-1
	nnl[0][4]=nxy*(nz-1)
	nnl[0][5]=nxy*(nz-1)+1
	nnl[0][6]=nx*(ny*(nz-1)+2)-1
	nnl[0][7]=nx*(ny*(nz-1)+1)
	nnl[0][8]=nx*(ny*(nz-1)+1)+1
	nnl[0][9]=nxy-1
	nnl[0][10]=nxy-nx
	nnl[0][11]=nxy-nx+1
	nnl[0][12]=nx-1
	nnl[0][13]=1
	nnl[0][14]=2*nx-1
	nnl[0][15]=nx
	nnl[0][16]=nx+1
	nnl[0][17]=2*nxy-1
	nnl[0][18]=2*nxy-nx
	nnl[0][19]=2*nxy-nx+1
	nnl[0][20]=nxy+nx-1
	nnl[0][21]=nxy
	nnl[0][22]=nxy+1
	nnl[0][23]=nxy+2*nx-1
	nnl[0][24]=nxy+nx
	nnl[0][25]=nxy+nx+1

	#corner 2
	i=nx-1
	nnl[i][0]=nxyz-2
	nnl[i][1]=nxyz-1
	nnl[i][2]=nx*(nyz-1)
	nnl[i][3]=nx*(ny*(nz-1)+1)-2
	nnl[i][4]=nx*(ny*(nz-1)+1)-1
	nnl[i][5]=nxy*(nz-1)
	nnl[i][6]=nx*(ny*(nz-1)+2)-2
	nnl[i][7]=nx*(ny*(nz-1)+2)-1
	nnl[i][8]=nx*(ny*(nz-1)+1)
	nnl[i][9]=nxy-2
	nnl[i][10]=nxy-1
	nnl[i][11]=nx*(ny-1)
	nnl[i][12]=nx-2
	nnl[i][13]=0
	nnl[i][14]=2*nx-2
	nnl[i][15]=2*nx-1
	nnl[i][16]=nx
	nnl[i][17]=2*(nxy-1)
	nnl[i][18]=2*nxy-1
	nnl[i][19]=nx*(2*ny-1)
	nnl[i][20]=nx*(ny+1)-2
	nnl[i][21]=nx*(ny+1)-1
	nnl[i][22]=nxy
	nnl[i][23]=nx*(ny+2)-2
	nnl[i][24]=nx*(ny+2)-1
	nnl[i][25]=nx*(ny+1)

	#corner 3
	i=nx*(ny-1)
	nnl[i][0]=nx*(nyz-1)-1
	nnl[i][1]=nx*(nyz-2)
	nnl[i][2]=nx*(nyz-2)+1
	nnl[i][3]=nxyz-1
	nnl[i][4]=nx*(nyz-1)
	nnl[i][5]=nx*(nyz-1)+1
	nnl[i][6]=nx*(ny*(nz-1)+1)-1
	nnl[i][7]=nxy*(nz-1)
	nnl[i][8]=nxy*(nz-1)+1
	nnl[i][9]=nx*(ny-1)-1
	nnl[i][10]=nx*(ny-2)
	nnl[i][11]=nx*(ny-2)+1
	nnl[i][12]=nxy-1
	nnl[i][13]=nx*(ny-1)+1
	nnl[i][14]=nx-1
	nnl[i][15]=0
	nnl[i][16]=1
	nnl[i][17]=nx*(2*ny-1)-1
	nnl[i][18]=2*nx*(ny-1)
	nnl[i][19]=2*nx*(ny-1)+1
	nnl[i][20]=2*nxy-1
	nnl[i][21]=nx*(2*ny-1)
	nnl[i][22]=nx*(2*ny-1)+1
	nnl[i][23]=nx*(ny+1)-1
	nnl[i][24]=nxy
	nnl[i][25]=nxy+1

	#corner 4
	i=nxy-1
	nnl[i][0]=nx*(nyz-1)-2
	nnl[i][1]=nx*(nyz-1)-1
	nnl[i][2]=nx*(nyz-2)
	nnl[i][3]=nxyz-2
	nnl[i][4]=nxyz-1
	nnl[i][5]=nx*(nyz-1)
	nnl[i][6]=nx*(ny*(nz-1)+1)-2
	nnl[i][7]=nx*(ny*(nz-1)+1)-1
	nnl[i][8]=nxy*(nz-1)
	nnl[i][9]=nx*(ny-1)-2
	nnl[i][10]=nx*(ny-1)-1
	nnl[i][11]=nx*(ny-2)
	nnl[i][12]=nxy-2
	nnl[i][13]=nx*(ny-1)
	nnl[i][14]=nx-2
	nnl[i][15]=nx-1
	nnl[i][16]=0
	nnl[i][17]=nx*(2*ny-1)-2
	nnl[i][18]=nx*(2*ny-1)-1
	nnl[i][19]=2*nx*(ny-1)
	nnl[i][20]=2*nxy-2
	nnl[i][21]=2*nxy-1
	nnl[i][22]=nx*(2*ny-1)
	nnl[i][23]=nx*(ny+1)-2
	nnl[i][24]=nx*(ny+1)-1
	nnl[i][25]=nxy

	#corner 5
	i=nxy*(nz-1)
	nnl[i][0]=nxy*(nz-1)-1
	nnl[i][1]=nx*(ny*(nz-1)-1)
	nnl[i][2]=nx*(ny*(nz-1)-1)+1
	nnl[i][3]=nx*(ny*(nz-2)+1)-1
	nnl[i][4]=nxy*(nz-2)
	nnl[i][5]=nxy*(nz-2)+1
	nnl[i][6]=nx*(ny*(nz-2)+2)-1
	nnl[i][7]=nx*(ny*(nz-2)+1)
	nnl[i][8]=nx*(ny*(nz-2)+1)+1
	nnl[i][9]=nxyz-1
	nnl[i][10]=nx*(nyz-1)
	nnl[i][11]=nx*(nyz-1)+1
	nnl[i][12]=nx*(ny*(nz-1)+1)-1
	nnl[i][13]=nxy*(nz-1)+1
	nnl[i][14]=nx*(ny*(nz-1)+2)-1
	nnl[i][15]=nx*(ny*(nz-1)+1)
	nnl[i][16]=nx*(ny*(nz-1)+1)+1
	nnl[i][17]=nxy-1
	nnl[i][18]=nx*(ny-1)
	nnl[i][19]=nx*(ny-1)+1
	nnl[i][20]=nx-1
	nnl[i][21]=0
	nnl[i][22]=1
	nnl[i][23]=2*nx-1
	nnl[i][24]=nx
	nnl[i][25]=nx+1

	#corner 6
	i=nx*(ny*(nz-1)+1)-1
	nnl[i][0]=nxy*(nz-1)-2
	nnl[i][1]=nxy*(nz-1)-1
	nnl[i][2]=nx*(ny*(nz-1)-1)
	nnl[i][3]=nx*(ny*(nz-2)+1)-2
	nnl[i][4]=nx*(ny*(nz-2)+1)-1
	nnl[i][5]=nxy*(nz-2)
	nnl[i][6]=nx*(ny*(nz-2)+2)-2
	nnl[i][7]=nx*(ny*(nz-2)+2)-1
	nnl[i][8]=nx*(ny*(nz-2)+1)
	nnl[i][9]=nxyz-2
	nnl[i][10]=nxyz-1
	nnl[i][11]=nx*(nyz-1)
	nnl[i][12]=nx*(ny*(nz-1)+1)-2
	nnl[i][13]=nxy*(nz-1)
	nnl[i][14]=nx*(ny*(nz-1)+2)-2
	nnl[i][15]=nx*(ny*(nz-1)+2)-1
	nnl[i][16]=nx*(ny*(nz-1)+1)
	nnl[i][17]=nxy-2
	nnl[i][18]=nxy-1
	nnl[i][19]=nx*(ny-1)
	nnl[i][20]=nx-2
	nnl[i][21]=nx-1
	nnl[i][22]=0
	nnl[i][23]=2*(nx-1)
	nnl[i][24]=2*nx-1
	nnl[i][25]=nx

	#corner 7
	i=nx*(nyz-1)
	nnl[i][0]=nx*(ny*(nz-1)-1)-1
	nnl[i][1]=nx*(ny*(nz-1)-2)
	nnl[i][2]=nx*(ny*(nz-1)-2)+1
	nnl[i][3]=nxy*(nz-1)-1
	nnl[i][4]=nx*(ny*(nz-1)-1)
	nnl[i][5]=nx*(ny*(nz-1)-1)+1
	nnl[i][6]=nx*(ny*(nz-2)+1)-1
	nnl[i][7]=nxy*(nz-2)
	nnl[i][8]=nxy*(nz-2)+1
	nnl[i][9]=nx*(nyz-1)-1
	nnl[i][10]=nx*(nyz-2)
	nnl[i][11]=nx*(nyz-2)+1
	nnl[i][12]=nxyz-1
	nnl[i][13]=nx*(nyz-1)+1
	nnl[i][14]=nx*(ny*(nz-1)+1)-1
	nnl[i][15]=nxy*(nz-1)
	nnl[i][16]=nxy*(nz-1)+1
	nnl[i][17]=nx*(ny-1)-1
	nnl[i][18]=nx*(ny-2)
	nnl[i][19]=nx*(ny-2)+1
	nnl[i][20]=nxy-1
	nnl[i][21]=nx*(ny-1)
	nnl[i][22]=nx*(ny-1)+1
	nnl[i][23]=nx-1
	nnl[i][24]=0
	nnl[i][25]=1

	#corner 8
	i=nxyz-1
	nnl[i][0]=nx*(ny*(nz-1)-1)-2
	nnl[i][1]=nx*(ny*(nz-1)-1)-1
	nnl[i][2]=nx*(ny*(nz-1)-2)
	nnl[i][3]=nxy*(nz-1)-2
	nnl[i][4]=nxy*(nz-1)-1
	nnl[i][5]=nx*(ny*(nz-1)-1)
	nnl[i][6]=nx*(ny*(nz-2)+1)-2
	nnl[i][7]=nx*(ny*(nz-2)+1)-1
	nnl[i][8]=nxy*(nz-2)
	nnl[i][9]=nx*(nyz-1)-2
	nnl[i][10]=nx*(nyz-1)-1
	nnl[i][11]=nx*(nyz-2)
	nnl[i][12]=nxyz-2
	nnl[i][13]=nx*(nyz-1)
	nnl[i][14]=nx*(ny*(nz-1)+1)-2
	nnl[i][15]=nx*(ny*(nz-1)+1)-1
	nnl[i][16]=nxy*(nz-1)
	nnl[i][17]=nx*(ny-1)-2
	nnl[i][18]=nx*(ny-1)-1
	nnl[i][19]=nx*(ny-2)
	nnl[i][20]=nxy-2
	nnl[i][21]=nxy-1
	nnl[i][22]=nx*(ny-1)
	nnl[i][23]=nx-2
	nnl[i][24]=nx-1
	nnl[i][25]=0

	for i in range(1,ny-1):
		#edge 1
		i1=i*nx
		nnl[i1][0]=nx*(ny*(nz-1)+i)-1
		nnl[i1][1]=nx*(ny*(nz-1)+i-1)
		nnl[i1][2]=nx*(ny*(nz-1)+i-1)+1
		nnl[i1][3]=nx*(ny*(nz-1)+i+1)-1
		nnl[i1][4]=nx*(ny*(nz-1)+i)
		nnl[i1][5]=nx*(ny*(nz-1)+i)+1
		nnl[i1][6]=nx*(ny*(nz-1)+i+2)-1
		nnl[i1][7]=nx*(ny*(nz-1)+i+1)
		nnl[i1][8]=nx*(ny*(nz-1)+i+1)+1
		nnl[i1][9]=i*nx-1
		nnl[i1][10]=(i-1)*nx
		nnl[i1][11]=(i-1)*nx+1
		nnl[i1][12]=(i+1)*nx-1
		nnl[i1][13]=i*nx+1
		nnl[i1][14]=(i+2)*nx-1
		nnl[i1][15]=(i+1)*nx
		nnl[i1][16]=(i+1)*nx+1
		nnl[i1][17]=nx*(ny+i)-1
		nnl[i1][18]=nx*(ny+i-1)
		nnl[i1][19]=nx*(ny+i-1)+1
		nnl[i1][20]=nx*(ny+i+1)-1
		nnl[i1][21]=nx*(ny+i)
		nnl[i1][22]=nx*(ny+i)+1
		nnl[i1][23]=nx*(ny+i+2)-1
		nnl[i1][24]=nx*(ny+i+1)
		nnl[i1][25]=nx*(ny+i+1)+1
		#edge 2
		i2=nnl[i1][4]
		nnl[i2][0]=nx*(ny*(nz-2)+i)-1
		nnl[i2][1]=nx*(ny*(nz-2)+i-1)
		nnl[i2][2]=nx*(ny*(nz-2)+i-1)+1
		nnl[i2][3]=nx*(ny*(nz-2)+i+1)-1
		nnl[i2][4]=nx*(ny*(nz-2)+i)
		nnl[i2][5]=nx*(ny*(nz-2)+i)+1
		nnl[i2][6]=nx*(ny*(nz-2)+i+2)-1
		nnl[i2][7]=nx*(ny*(nz-2)+i+1)
		nnl[i2][8]=nx*(ny*(nz-2)+i+1)+1
		nnl[i2][9]=nnl[i1][0]
		nnl[i2][10]=nnl[i1][1]
		nnl[i2][11]=nnl[i1][2]
		nnl[i2][12]=nnl[i1][3]
		nnl[i2][13]=nnl[i1][5]
		nnl[i2][14]=nnl[i1][6]
		nnl[i2][15]=nnl[i1][7]
		nnl[i2][16]=nnl[i1][8]
		nnl[i2][17]=nnl[i1][9]
		nnl[i2][18]=nnl[i1][10]
		nnl[i2][19]=nnl[i1][11]
		nnl[i2][20]=nnl[i1][12]
		nnl[i2][21]=i1
		nnl[i2][22]=nnl[i1][13]
		nnl[i2][23]=nnl[i1][14]
		nnl[i2][24]=nnl[i1][15]
		nnl[i2][25]=nnl[i1][16]
		#edge 3
		i3=(i+1)*nx-1
		nnl[i3][0]=nx*(ny*(nz-1)+i)-2
		nnl[i3][1]=nx*(ny*(nz-1)+i)-1
		nnl[i3][2]=nx*(ny*(nz-1)+i-1)
		nnl[i3][3]=nx*(ny*(nz-1)+i+1)-2
		nnl[i3][4]=nx*(ny*(nz-1)+i+1)-1
		nnl[i3][5]=nx*(ny*(nz-1)+i)
		nnl[i3][6]=nx*(ny*(nz-1)+i+2)-2
		nnl[i3][7]=nx*(ny*(nz-1)+i+2)-1
		nnl[i3][8]=nx*(ny*(nz-1)+i+1)
		nnl[i3][9]=i*nx-2
		nnl[i3][10]=i*nx-1
		nnl[i3][11]=(i-1)*nx
		nnl[i3][12]=(i+1)*nx-2
		nnl[i3][13]=i*nx
		nnl[i3][14]=(i+2)*nx-2
		nnl[i3][15]=(i+2)*nx-1
		nnl[i3][16]=(i+1)*nx
		nnl[i3][17]=nx*(ny+i)-2
		nnl[i3][18]=nx*(ny+i)-1
		nnl[i3][19]=nx*(ny+i-1)
		nnl[i3][20]=nx*(ny+i+1)-2
		nnl[i3][21]=nx*(ny+i+1)-1
		nnl[i3][22]=nx*(ny+i)
		nnl[i3][23]=nx*(ny+i+2)-2
		nnl[i3][24]=nx*(ny+i+2)-1
		nnl[i3][25]=nx*(ny+i+1)
		#edge 4
		i4=nnl[i3][4]
		nnl[i4][0]=nx*(ny*(nz-2)+i)-2
		nnl[i4][1]=nx*(ny*(nz-2)+i)-1
		nnl[i4][2]=nx*(ny*(nz-2)+i-1)
		nnl[i4][3]=nx*(ny*(nz-2)+i+1)-2
		nnl[i4][4]=nx*(ny*(nz-2)+i+1)-1
		nnl[i4][5]=nx*(ny*(nz-2)+i)
		nnl[i4][6]=nx*(ny*(nz-2)+i+2)-2
		nnl[i4][7]=nx*(ny*(nz-2)+i+2)-1
		nnl[i4][8]=nx*(ny*(nz-2)+i+1)
		nnl[i4][9]=nnl[i3][0]
		nnl[i4][10]=nnl[i3][1]
		nnl[i4][11]=nnl[i3][2]
		nnl[i4][12]=nnl[i3][3]
		nnl[i4][13]=nnl[i3][5]
		nnl[i4][14]=nnl[i3][6]
		nnl[i4][15]=nnl[i3][7]
		nnl[i4][16]=nnl[i3][8]
		nnl[i4][17]=nnl[i3][9]
		nnl[i4][18]=nnl[i3][10]
		nnl[i4][19]=nnl[i3][11]
		nnl[i4][20]=nnl[i3][12]
		nnl[i4][21]=i3
		nnl[i4][22]=nnl[i3][13]
		nnl[i4][23]=nnl[i3][14]
		nnl[i4][24]=nnl[i3][15]
		nnl[i4][25]=nnl[i3][16]

	for i in range(2,nx):
		#edge 5
		ii=i-1
		nnl[ii][0]=nx*(nyz-1)+i-2
		nnl[ii][1]=nx*(nyz-1)+i-1
		nnl[ii][2]=nx*(nyz-1)+i
		nnl[ii][3]=nxy*(nz-1)+i-2
		nnl[ii][4]=nxy*(nz-1)+i-1
		nnl[ii][5]=nxy*(nz-1)+i
		nnl[ii][6]=nx*(ny*(nz-1)+1)+i-2
		nnl[ii][7]=nx*(ny*(nz-1)+1)+i-1
		nnl[ii][8]=nx*(ny*(nz-1)+1)+i
		nnl[ii][9]=nx*(ny-1)+i-2
		nnl[ii][10]=nx*(ny-1)+i-1
		nnl[ii][11]=nx*(ny-1)+i
		nnl[ii][12]=i-2
		nnl[ii][13]=i
		nnl[ii][14]=i+nx-2
		nnl[ii][15]=i+nx-1
		nnl[ii][16]=i+nx
		nnl[ii][17]=nx*(2*ny-1)+i-2
		nnl[ii][18]=nx*(2*ny-1)+i-1
		nnl[ii][19]=nx*(2*ny-1)+i
		nnl[ii][20]=nxy+i-2
		nnl[ii][21]=nxy+i-1
		nnl[ii][22]=nxy+i
		nnl[ii][23]=nx*(ny+1)+i-2
		nnl[ii][24]=nx*(ny+1)+i-1
		nnl[ii][25]=nx*(ny+1)+i
		#edge 6 
		ii=nxy*(nz-1)+i-1		
		nnl[ii][0]=nx*(ny*(nz-1)-1)+i-2
		nnl[ii][1]=nx*(ny*(nz-1)-1)+i-1
		nnl[ii][2]=nx*(ny*(nz-1)-1)+i
		nnl[ii][3]=nxy*(nz-2)+i-2
		nnl[ii][4]=nxy*(nz-2)+i-1
		nnl[ii][5]=nxy*(nz-2)+i
		nnl[ii][6]=nx*(ny*(nz-2)+1)+i-2
		nnl[ii][7]=nx*(ny*(nz-2)+1)+i-1
		nnl[ii][8]=nx*(ny*(nz-2)+1)+i
		nnl[ii][9]=nx*(nyz-1)+i-2
		nnl[ii][10]=nx*(nyz-1)+i-1
		nnl[ii][11]=nx*(nyz-1)+i
		nnl[ii][12]=nxy*(nz-1)+i-2
		nnl[ii][13]=nxy*(nz-1)+i
		nnl[ii][14]=nx*(ny*(nz-1)+1)+i-2
		nnl[ii][15]=nx*(ny*(nz-1)+1)+i-1
		nnl[ii][16]=nx*(ny*(nz-1)+1)+i
		nnl[ii][17]=nx*(ny-1)+i-2
		nnl[ii][18]=nx*(ny-1)+i-1
		nnl[ii][19]=nx*(ny-1)+i
		nnl[ii][20]=i-2
		nnl[ii][21]=i-1
		nnl[ii][22]=i
		nnl[ii][23]=i+nx-2
		nnl[ii][24]=i+nx-1
		nnl[ii][25]=i+nx
		#edge 7
		ii=nx*(ny-1)+i-1
		nnl[ii][0]=nx*(nyz-2)+i-2
		nnl[ii][1]=nx*(nyz-2)+i-1
		nnl[ii][2]=nx*(nyz-2)+i
		nnl[ii][3]=nx*(nyz-1)+i-2
		nnl[ii][4]=nx*(nyz-1)+i-1
		nnl[ii][5]=nx*(nyz-1)+i
		nnl[ii][6]=nxy*(nz-1)+i-2
		nnl[ii][7]=nxy*(nz-1)+i-1
		nnl[ii][8]=nxy*(nz-1)+i
		nnl[ii][9]=nx*(ny-2)+i-2
		nnl[ii][10]=nx*(ny-2)+i-1
		nnl[ii][11]=nx*(ny-2)+i
		nnl[ii][12]=nx*(ny-1)+i-2
		nnl[ii][13]=nx*(ny-1)+i
		nnl[ii][14]=i-2
		nnl[ii][15]=i-1
		nnl[ii][16]=i
		nnl[ii][17]=2*nx*(ny-1)+i-2
		nnl[ii][18]=2*nx*(ny-1)+i-1
		nnl[ii][19]=2*nx*(ny-1)+i
		nnl[ii][20]=nx*(2*ny-1)+i-2
		nnl[ii][21]=nx*(2*ny-1)+i-1
		nnl[ii][22]=nx*(2*ny-1)+i
		nnl[ii][23]=nxy+i-2
		nnl[ii][24]=nxy+i-1
		nnl[ii][25]=nxy+i
		#edge 8
		ii=nx*(nyz-1)+i-1
		nnl[ii][0]=nx*(ny*(nz-1)-2)+i-2
		nnl[ii][1]=nx*(ny*(nz-1)-2)+i-1
		nnl[ii][2]=nx*(ny*(nz-1)-2)+i
		nnl[ii][3]=nx*(ny*(nz-1)-1)+i-2
		nnl[ii][4]=nx*(ny*(nz-1)-1)+i-1
		nnl[ii][5]=nx*(ny*(nz-1)-1)+i
		nnl[ii][6]=nxy*(nz-2)+i-2
		nnl[ii][7]=nxy*(nz-2)+i-1
		nnl[ii][8]=nxy*(nz-2)+i
		nnl[ii][9]=nx*(nyz-2)+i-2
		nnl[ii][10]=nx*(nyz-2)+i-1
		nnl[ii][11]=nx*(nyz-2)+i
		nnl[ii][12]=nx*(nyz-1)+i-2
		nnl[ii][13]=nx*(nyz-1)+i
		nnl[ii][14]=nxy*(nz-1)+i-2
		nnl[ii][15]=nxy*(nz-1)+i-1
		nnl[ii][16]=nxy*(nz-1)+i
		nnl[ii][17]=nx*(ny-2)+i-2
		nnl[ii][18]=nx*(ny-2)+i-1
		nnl[ii][19]=nx*(ny-2)+i
		nnl[ii][20]=nx*(ny-1)+i-2
		nnl[ii][21]=nx*(ny-1)+i-1
		nnl[ii][22]=nx*(ny-1)+i
		nnl[ii][23]=i-2
		nnl[ii][24]=i-1
		nnl[ii][25]=i

	for i in range(1,nz-1):
		#edge 9
		ii=i*nxy
		nnl[ii][0]=i*nxy-1
		nnl[ii][1]=nx*(i*ny-1)
		nnl[ii][2]=nx*(i*ny-1)+1
		nnl[ii][3]=nx*((i-1)*ny+1)-1
		nnl[ii][4]=(i-1)*nxy
		nnl[ii][5]=(i-1)*nxy+1
		nnl[ii][6]=nx*((i-1)*ny+2)-1
		nnl[ii][7]=nx*((i-1)*ny+1)
		nnl[ii][8]=nx*((i-1)*ny+1)+1
		nnl[ii][9]=(i+1)*nxy-1
		nnl[ii][10]=nx*((i+1)*ny-1)
		nnl[ii][11]=nx*((i+1)*ny-1)+1
		nnl[ii][12]=nx*(i*ny+1)-1
		nnl[ii][13]=i*nxy+1
		nnl[ii][14]=nx*(i*ny+2)-1
		nnl[ii][15]=nx*(i*ny+1)
		nnl[ii][16]=nx*(i*ny+1)+1
		nnl[ii][17]=(i+2)*nxy-1
		nnl[ii][18]=nx*((i+2)*ny-1)
		nnl[ii][19]=nx*((i+2)*ny-1)+1
		nnl[ii][20]=nx*((i+1)*ny+1)-1
		nnl[ii][21]=(i+1)*nxy
		nnl[ii][22]=(i+1)*nxy+1
		nnl[ii][23]=nx*((i+1)*ny+2)-1
		nnl[ii][24]=nx*((i+1)*ny+1)
		nnl[ii][25]=nx*((i+1)*ny+1)+1
		#edge 10
		ii=nx*(i*ny+1)-1
		nnl[ii][0]=i*nxy-2
		nnl[ii][1]=i*nxy-1
		nnl[ii][2]=nx*(i*ny-1)
		nnl[ii][3]=nx*((i-1)*ny+1)-2
		nnl[ii][4]=nx*((i-1)*ny+1)-1
		nnl[ii][5]=(i-1)*nxy
		nnl[ii][6]=nx*((i-1)*ny+2)-2
		nnl[ii][7]=nx*((i-1)*ny+2)-1
		nnl[ii][8]=nx*((i-1)*ny+1)
		nnl[ii][9]=(i+1)*nxy-2
		nnl[ii][10]=(i+1)*nxy-1
		nnl[ii][11]=nx*((i+1)*ny-1)
		nnl[ii][12]=nx*(i*ny+1)-2
		nnl[ii][13]=i*nxy
		nnl[ii][14]=nx*(i*ny+2)-2
		nnl[ii][15]=nx*(i*ny+2)-1
		nnl[ii][16]=nx*(i*ny+1)
		nnl[ii][17]=(i+2)*nxy-2
		nnl[ii][18]=(i+2)*nxy-1
		nnl[ii][19]=nx*((i+2)*ny-1)
		nnl[ii][20]=nx*((i+1)*ny+1)-2
		nnl[ii][21]=nx*((i+1)*ny+1)-1
		nnl[ii][22]=(i+1)*nxy
		nnl[ii][23]=nx*((i+1)*ny+2)-2
		nnl[ii][24]=nx*((i+1)*ny+2)-1
		nnl[ii][25]=nx*((i+1)*ny+1)
		#edge 11
		ii=nx*((i+1)*ny-1)
		nnl[ii][0]=nx*(i*ny-1)-1
		nnl[ii][1]=nx*(i*ny-2)
		nnl[ii][2]=nx*(i*ny-2)+1
		nnl[ii][3]=i*nxy-1
		nnl[ii][4]=nx*(i*ny-1)
		nnl[ii][5]=nx*(i*ny-1)+1
		nnl[ii][6]=nx*((i-1)*ny+1)-1
		nnl[ii][7]=(i-1)*nxy
		nnl[ii][8]=(i-1)*nxy+1
		nnl[ii][9]=nx*((i+1)*ny-1)-1
		nnl[ii][10]=nx*((i+1)*ny-2)
		nnl[ii][11]=nx*((i+1)*ny-2)+1
		nnl[ii][12]=(i+1)*nxy-1
		nnl[ii][13]=nx*((i+1)*ny-1)+1
		nnl[ii][14]=nx*(i*ny+1)-1
		nnl[ii][15]=i*nxy
		nnl[ii][16]=i*nxy+1
		nnl[ii][17]=nx*((i+2)*ny-1)-1
		nnl[ii][18]=nx*((i+2)*ny-2)
		nnl[ii][19]=nx*((i+2)*ny-2)+1
		nnl[ii][20]=(i+2)*nxy-1
		nnl[ii][21]=nx*((i+2)*ny-1)
		nnl[ii][22]=nx*((i+2)*ny-1)+1
		nnl[ii][23]=nx*((i+1)*ny+1)-1
		nnl[ii][24]=(i+1)*nxy
		nnl[ii][25]=(i+1)*nxy+1
		#edge 12
		ii=(i+1)*nxy-1
		nnl[ii][0]=nx*(i*ny-1)-2
		nnl[ii][1]=nx*(i*ny-1)-1
		nnl[ii][2]=nx*(i*ny-2)
		nnl[ii][3]=i*nxy-2
		nnl[ii][4]=i*nxy-1
		nnl[ii][5]=nx*(i*ny-1)
		nnl[ii][6]=nx*((i-1)*ny+1)-2
		nnl[ii][7]=nx*((i-1)*ny+1)-1
		nnl[ii][8]=(i-1)*nxy
		nnl[ii][9]=nx*((i+1)*ny-1)-2
		nnl[ii][10]=nx*((i+1)*ny-1)-1
		nnl[ii][11]=nx*((i+1)*ny-2)
		nnl[ii][12]=(i+1)*nxy-2
		nnl[ii][13]=nx*((i+1)*ny-1)
		nnl[ii][14]=nx*(i*ny+1)-2
		nnl[ii][15]=nx*(i*ny+1)-1
		nnl[ii][16]=i*nxy
		nnl[ii][17]=nx*((i+2)*ny-1)-2
		nnl[ii][18]=nx*((i+2)*ny-1)-1
		nnl[ii][19]=nx*((i+2)*ny-2)
		nnl[ii][20]=(i+2)*nxy-2
		nnl[ii][21]=(i+2)*nxy-1
		nnl[ii][22]=nx*((i+2)*ny-1)
		nnl[ii][23]=nx*((i+1)*ny+1)-2
		nnl[ii][24]=nx*((i+1)*ny+1)-1
		nnl[ii][25]=(i+1)*nxy

	for i in range(1,nz-1):
		for j in range(1,ny-1):
			#face 1
			ii=nx*(i*ny+j)
			nnl[ii][0]=nx*((i-1)*ny+j)-1
			nnl[ii][1]=nx*((i-1)*ny+j-1)
			nnl[ii][2]=nx*((i-1)*ny+j-1)+1
			nnl[ii][3]=nx*((i-1)*ny+j+1)-1
			nnl[ii][4]=nx*((i-1)*ny+j)
			nnl[ii][5]=nx*((i-1)*ny+j)+1
			nnl[ii][6]=nx*((i-1)*ny+j+2)-1
			nnl[ii][7]=nx*((i-1)*ny+j+i)
			nnl[ii][8]=nx*((i-1)*ny+j+1)+1
			nnl[ii][9]=nx*(i*ny+j)-1
			nnl[ii][10]=nx*(i*ny+j-1)
			nnl[ii][11]=nx*(i*ny+j-1)+1
			nnl[ii][12]=nx*(i*ny+j+1)-1
			nnl[ii][13]=nx*(i*ny+j)+1
			nnl[ii][14]=nx*(i*ny+j+2)-1
			nnl[ii][15]=nx*(i*ny+j+i)
			nnl[ii][16]=nx*(i*ny+j+1)+1
			nnl[ii][17]=nx*((i+1)*ny+j)-1
			nnl[ii][18]=nx*((i+1)*ny+j-1)
			nnl[ii][19]=nx*((i+1)*ny+j-1)+1
			nnl[ii][20]=nx*((i+1)*ny+j+1)-1
			nnl[ii][21]=nx*((i+1)*ny+j)
			nnl[ii][22]=nx*((i+1)*ny+j)+1
			nnl[ii][23]=nx*((i+1)*ny+j+2)-1
			nnl[ii][24]=nx*((i+1)*ny+j+i)
			nnl[ii][25]=nx*((i+1)*ny+j+1)+1
			#face 2
			ii=nx*(i*ny+j+1)-1
			nnl[ii][0]=nx*((i-1)*ny+j)-2
			nnl[ii][1]=nx*((i-1)*ny+j)-1
			nnl[ii][2]=nx*((i-1)*ny+j-1)
			nnl[ii][3]=nx*((i-1)*ny+j+1)-2
			nnl[ii][4]=nx*((i-1)*ny+j+1)-1
			nnl[ii][5]=nx*((i-1)*ny+j)
			nnl[ii][6]=nx*((i-1)*ny+j+2)-2
			nnl[ii][7]=nx*((i-1)*ny+j+2)-1
			nnl[ii][8]=nx*((i-1)*ny+j+1)
			nnl[ii][9]=nx*(i*ny+j)-2
			nnl[ii][10]=nx*(i*ny+j)-1
			nnl[ii][11]=nx*(i*ny+j-1)
			nnl[ii][12]=nx*(i*ny+j+1)-2
			nnl[ii][13]=nx*(i*ny+j)
			nnl[ii][14]=nx*(i*ny+j+2)-2
			nnl[ii][15]=nx*(i*ny+j+2)-1
			nnl[ii][16]=nx*(i*ny+j+1)
			nnl[ii][17]=nx*((i+1)*ny+j)-2
			nnl[ii][18]=nx*((i+1)*ny+j)-1
			nnl[ii][19]=nx*((i+1)*ny+j-1)
			nnl[ii][20]=nx*((i+1)*ny+j+1)-2
			nnl[ii][21]=nx*((i+1)*ny+j+1)-1
			nnl[ii][22]=nx*((i+1)*ny+j)
			nnl[ii][23]=nx*((i+1)*ny+j+2)-2
			nnl[ii][24]=nx*((i+1)*ny+j+2)-1
			nnl[ii][25]=nx*((i+1)*ny+j+1)

		for j in range(2,nx):
			#face 3
			ii=i*nxy+j-1
			nnl[ii][0]=nx*(i*ny-1)+j-2
			nnl[ii][1]=nx*(i*ny-1)+j-1
			nnl[ii][2]=nx*(i*ny-1)+j
			nnl[ii][3]=(i-1)*nxy+j-2
			nnl[ii][4]=(i-1)*nxy+j-1
			nnl[ii][5]=(i-1)*nxy+j
			nnl[ii][6]=nx*((i-1)*ny+1)+j-2
			nnl[ii][7]=nx*((i-1)*ny+1)+j-1
			nnl[ii][8]=nx*((i-1)*ny+1)+j
			nnl[ii][9]=nx*((i+1)*ny-1)+j-2
			nnl[ii][10]=nx*((i+1)*ny-1)+j-1
			nnl[ii][11]=nx*((i+1)*ny-1)+j
			nnl[ii][12]=i*nxy+j-2
			nnl[ii][13]=i*nxy+j
			nnl[ii][14]=nx*(i*ny+1)+j-2
			nnl[ii][15]=nx*(i*ny+1)+j-1
			nnl[ii][16]=nx*(i*ny+1)+j
			nnl[ii][17]=nx*((i+2)*ny-1)+j-2
			nnl[ii][18]=nx*((i+2)*ny-1)+j-1
			nnl[ii][19]=nx*((i+2)*ny-1)+j
			nnl[ii][20]=(i+1)*nxy+j-2
			nnl[ii][21]=(i+1)*nxy+j-1
			nnl[ii][22]=(i+1)*nxy+j
			nnl[ii][23]=nx*((i+1)*ny+1)+j-2
			nnl[ii][24]=nx*((i+1)*ny+1)+j-1
			nnl[ii][25]=nx*((i+1)*ny+1)+j
			#face 4
			ii=nx*((i+1)*ny-1)+j-1
			nnl[ii][0]=nx*(i*ny-2)+j-2
			nnl[ii][1]=nx*(i*ny-2)+j-1
			nnl[ii][2]=nx*(i*ny-2)+j
			nnl[ii][3]=nx*(i*ny-1)+j-2
			nnl[ii][4]=nx*(i*ny-1)+j-1
			nnl[ii][5]=nx*(i*ny-1)+j
			nnl[ii][6]=(i-1)*nxy+j-2
			nnl[ii][7]=(i-1)*nxy+j-1
			nnl[ii][8]=(i-1)*nxy+j
			nnl[ii][9]=nx*((i+1)*ny-2)+j-2
			nnl[ii][10]=nx*((i+1)*ny-2)+j-1
			nnl[ii][11]=nx*((i+1)*ny-2)+j
			nnl[ii][12]=nx*((i+1)*ny-1)+j-2
			nnl[ii][13]=nx*((i+1)*ny-1)+j
			nnl[ii][14]=i*nxy+j-2
			nnl[ii][15]=i*nxy+j-1
			nnl[ii][16]=i*nxy+j
			nnl[ii][17]=nx*((i+2)*ny-2)+j-2
			nnl[ii][18]=nx*((i+2)*ny-2)+j-1
			nnl[ii][19]=nx*((i+2)*ny-2)+j
			nnl[ii][20]=nx*((i+2)*ny-1)+j-2
			nnl[ii][21]=nx*((i+2)*ny-1)+j-1
			nnl[ii][22]=nx*((i+2)*ny-1)+j
			nnl[ii][23]=(i+1)*nxy+j-2
			nnl[ii][24]=(i+1)*nxy+j-1
			nnl[ii][25]=(i+1)*nxy+j

	for i in range(1,ny-1):
		for j in range(2,nx):
			#face 5
			i1=i*nx+j-1
			i2=nx*(ny*(nz-1)+i)+j-1
			nnl[i1][0]=nx*(ny*(nz-1)+i-1)+j-2
			nnl[i1][1]=nx*(ny*(nz-1)+i-1)+j-1
			nnl[i1][2]=nx*(ny*(nz-1)+i-1)+j
			nnl[i1][3]=nx*(ny*(nz-1)+i)+j-2
			nnl[i1][4]=i2
			nnl[i1][5]=nx*(ny*(nz-1)+i)+j
			nnl[i1][6]=nx*(ny*(nz-1)+i+1)+j-2
			nnl[i1][7]=nx*(ny*(nz-1)+i+1)+j-1
			nnl[i1][8]=nx*(ny*(nz-1)+i+1)+j
			nnl[i1][9]=(i-1)*nx+j-2
			nnl[i1][10]=(i-1)*nx+j-1
			nnl[i1][11]=(i-1)*nx+j
			nnl[i1][12]=i*nx+j-2
			nnl[i1][13]=i*nx+j
			nnl[i1][14]=(i+1)*nx+j-2
			nnl[i1][15]=(i+1)*nx+j-1
			nnl[i1][16]=(i+1)*nx+j
			nnl[i1][17]=nx*(ny+i-1)+j-2
			nnl[i1][18]=nx*(ny+i-1)+j-1
			nnl[i1][19]=nx*(ny+i-1)+j
			nnl[i1][20]=nx*(ny+i)+j-2
			nnl[i1][21]=nx*(ny+i)+j-1
			nnl[i1][22]=nx*(ny+i)+j
			nnl[i1][23]=nx*(ny+i+1)+j-2
			nnl[i1][24]=nx*(ny+i+1)+j-1
			nnl[i1][25]=nx*(ny+i+1)+j
			#face 6
			nnl[i2][0]=nx*(ny*(nz-2)+i-1)+j-2
			nnl[i2][1]=nx*(ny*(nz-2)+i-1)+j-1
			nnl[i2][2]=nx*(ny*(nz-2)+i-1)+j
			nnl[i2][3]=nx*(ny*(nz-2)+i)+j-2
			nnl[i2][4]=nx*(ny*(nz-2)+i)+j-1
			nnl[i2][5]=nx*(ny*(nz-2)+i)+j
			nnl[i2][6]=nx*(ny*(nz-2)+i+1)+j-2
			nnl[i2][7]=nx*(ny*(nz-2)+i+1)+j-1
			nnl[i2][8]=nx*(ny*(nz-2)+i+1)+j
			nnl[i2][9]=nnl[i1][0]
			nnl[i2][10]=nnl[i1][1]
			nnl[i2][11]=nnl[i1][2]
			nnl[i2][12]=nnl[i1][3]
			nnl[i2][13]=nnl[i1][5]
			nnl[i2][14]=nnl[i1][6]
			nnl[i2][15]=nnl[i1][7]
			nnl[i2][16]=nnl[i1][8]
			nnl[i2][17]=nnl[i1][9]
			nnl[i2][18]=nnl[i1][10]
			nnl[i2][19]=nnl[i1][11]
			nnl[i2][20]=nnl[i1][12]
			nnl[i2][21]=i1
			nnl[i2][22]=nnl[i1][13]
			nnl[i2][23]=nnl[i1][14]
			nnl[i2][24]=nnl[i1][15]
			nnl[i2][25]=nnl[i1][16]

	for i in range(1,nz-1):
		for j in range(1,ny-1):
			for k in range(2,nx):
				#bulk
				ii=nx*(i*ny+j)+k-1
				nnl[ii][0]=nx*((i-1)*ny+j-1)+k-2
				nnl[ii][1]=nx*((i-1)*ny+j-1)+k-1
				nnl[ii][2]=nx*((i-1)*ny+j-1)+k
				nnl[ii][3]=nx*((i-1)*ny+j)+k-2
				nnl[ii][4]=nx*((i-1)*ny+j)+k-1
				nnl[ii][5]=nx*((i-1)*ny+j)+k
				nnl[ii][6]=nx*((i-1)*ny+j+1)+k-2
				nnl[ii][7]=nx*((i-1)*ny+j+1)+k-1
				nnl[ii][8]=nx*((i-1)*ny+j+1)+k
				nnl[ii][9]=nx*(i*ny+j-1)+k-2
				nnl[ii][10]=nx*(i*ny+j-1)+k-1
				nnl[ii][11]=nx*(i*ny+j-1)+k
				nnl[ii][12]=nx*(i*ny+j)+k-2
				nnl[ii][13]=nx*(i*ny+j)+k
				nnl[ii][14]=nx*(i*ny+j+1)+k-2
				nnl[ii][15]=nx*(i*ny+j+1)+k-1
				nnl[ii][16]=nx*(i*ny+j+1)+k
				nnl[ii][17]=nx*((i+1)*ny+j-1)+k-2
				nnl[ii][18]=nx*((i+1)*ny+j-1)+k-1
				nnl[ii][19]=nx*((i+1)*ny+j-1)+k
				nnl[ii][20]=nx*((i+1)*ny+j)+k-2
				nnl[ii][21]=nx*((i+1)*ny+j)+k-1
				nnl[ii][22]=nx*((i+1)*ny+j)+k
				nnl[ii][23]=nx*((i+1)*ny+j+1)+k-2
				nnl[ii][24]=nx*((i+1)*ny+j+1)+k-1
				nnl[ii][25]=nx*((i+1)*ny+j+1)+k

	return nnl

