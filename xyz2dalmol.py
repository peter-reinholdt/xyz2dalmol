#!/usr/bin/env python

import sys

name2number = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7,
               'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mg': 12, 'Al': 13,
               'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19,
               'Ca': 20, 'Sc': 21, 'Ti': 22, 'V': 23, 'Cr': 24, 'Mn': 25,
               'Fe': 26, 'Co': 27, 'Ni': 28, 'Cu': 29, 'Zn': 30, 'Ga': 31,
               'Ge': 32, 'As': 33, 'Se': 34, 'Br': 35, 'Kr': 36, 'Rb': 37,
               'Sr': 38, 'Y': 39, 'Zr': 40, 'Nb': 41, 'Mo': 42, 'Tc': 43,
               'Ru': 44, 'Rh': 45, 'Pd': 46, 'Ag': 47, 'Cd': 48, 'In': 49,
               'Sn': 50, 'Sb': 51, 'Te': 52, 'I': 53, 'Xe': 54, 'Cs': 55,
               'Ba': 56, 'La': 57, 'Ce': 58, 'Pr': 59, 'Nd': 60, 'Pm': 61,
               'Sm': 62, 'Eu': 63, 'Gd': 64, 'Tb': 65, 'Dy': 66, 'Ho': 67,
               'Er': 68, 'Tm': 69, 'Yb': 70, 'Lu': 71, 'Hf': 72, 'Ta': 73,
               'W': 74, 'Re': 75, 'Os': 76, 'Ir': 77, 'Pt': 78, 'Au': 79,
               'Hg': 80, 'Tl': 81, 'Pb': 82, 'Bi': 83, 'Po': 84, 'At': 85,
               'Rn': 86, 'Fr': 87, 'Ra': 88}


if len(sys.argv) < 3:
    print("Usage: xyz2dalmol.py BASIS XYZFILE [CHARGE]")
    exit()
basis = sys.argv[1]
xyzfile = sys.argv[2]
if len(sys.argv) > 3:
    molcharge = sys.argv[3]
else:
    molcharge = 0

with open(xyzfile, 'r') as f:
    lines = f.read().split('\n')
atoms = int(lines[0])
atomtypes = 1
lastatom = lines[2].split()[0]
groups = []
thisgroup = [lines[2]]

for line in lines[3:atoms+2]:
    thisatom = line.split()[0]
    if lastatom == thisatom:
        thisgroup.append(line)
        continue
    else:
        atomtypes += 1
        groups.append(thisgroup)
        thisgroup = [line]
        lastatom = thisatom
groups.append(thisgroup)    

with open(xyzfile.split('.')[0] + '.mol', 'w') as f:
    f.write('BASIS\n')
    f.write('{} \n'.format(basis))
    f.write(' {} \n'.format(lines[0]))
    f.write(' {} \n'.format(lines[1]))
    print(lines[0])
    print(lines[1])

    f.write('Atomtypes={} Angstrom Charge={} NoSymmetry\n'.format(atomtypes, molcharge))
    for group in groups:
        atomtype = group[0].split()[0]
        charge = name2number[atomtype]
        atoms = len(group)
        f.write('Charge={} Atoms={}\n'.format(charge, atoms))
        for l in group:
            f.write('{}\n'.format(l))
