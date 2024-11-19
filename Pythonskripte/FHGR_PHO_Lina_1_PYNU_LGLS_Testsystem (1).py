# AUEM Kommentare by Carla
# 2024-10-10
# Begin
# --------------------------------------------------------------------------------------
# Python initialisieren:
import numpy as np;
# Python konfigurieren:
np.set_printoptions(linewidth=np.nan);
# Rahmen
print('--------------------------------------------------------------------------------------');
print(__file__);
print('--------------------------------------------------------------------------------------');
# Parameter:
n=2; pr=7;
# Berechnungen:
k_data=np.linspace(1,n,n);
[i_data,j_data]=np.meshgrid(k_data,k_data);
A=1/(i_data+j_data-1);
s=np.sum(A,axis=1)[np.newaxis];
b=s.T;
G=np.block([A,b]);
L=np.linalg.solve(A,b);
C=np.linalg.cond(A);
# Ausgabe:
print(f"G =\n{np.array2string(G,precision=pr)}\n");
print(f"L =\n{np.array2string(L.T,precision=pr)}\n");
print(f"C = {C:#.2g}");
print('--------------------------------------------------------------------------------------');
#
# --------------------------------------------------------------------------------------
# End
