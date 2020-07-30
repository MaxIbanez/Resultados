#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rdkit import Chem
from rdkit.Chem import Draw
import sys
import os
import shutil
directorio = sys.argv[1]+"-"+sys.argv[3]
archivo = sys.argv[1]+"_"+sys.argv[2]+"_"+sys.argv[3]+".txt"
path = directorio+"/"+archivo
arc = open(path, "r")
os.system("cls")
carpeta = sys.argv[2]+"_resultado"
print("Directorio:",directorio)
print("Archivo:",archivo)
print("carpeta de resultados:",carpeta)
print(path)
smiles = []
for item in arc:
    item = item[:len(item)-1]
    smiles.append(item)
arc.close()
smiles = smiles[:len(smiles)-3]
count = 0
os.mkdir(directorio+"/"+carpeta)
arc2 = open(directorio+"/"+carpeta+"/resultados.txt","w")
for item in smiles:
    mol = Chem.MolFromSmiles(item)
    if mol is not None:
        arc2.write(item+"\n")
        img = Draw.MolsToGridImage([mol],legends=item,subImgSize=(200,200))
        img.save(directorio+"/"+carpeta+"/"+str(count+1)+".png")
        count+=1
shutil.move(path,directorio+"/"+carpeta+"/"+archivo)
arc2.close()
print("compuestos validos:", count)