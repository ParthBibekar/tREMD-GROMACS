import os

temps = [300.00, 302.23, 304.48, 306.74, 309.01, 311.29, 313.59, 315.91, 318.23, 320.57, 
322.93, 325.30, 327.68, 330.08, 332.50, 334.92, 337.36, 339.82, 342.29, 344.78, 347.28, 
349.80, 352.33, 354.88, 357.41, 359.99, 362.58, 365.19, 367.76, 370.40, 373.04, 375.72, 
378.40, 381.11, 383.83, 386.56, 389.32, 392.09, 394.87, 397.68, 400.50, 403.34, 406.19, 
409.06, 411.95, 414.86, 417.79, 420.73, 423.69, 426.66, 429.66, 432.68, 435.71, 438.76, 
441.83, 444.91, 448.02, 451.15, 454.29, 457.46, 460.64, 463.84, 467.06, 470.30, 473.56, 
476.85, 480.15, 483.48, 486.82, 490.18, 493.56, 496.96, 500.39, 503.83, 507.29, 510.78, 
514.29, 517.82, 521.38, 524.95, 528.54, 532.16, 535.80, 539.46, 543.14, 546.85, 550.58, 
554.33, 558.10, 561.91, 565.72, 569.55, 573.42, 577.30, 581.22, 585.19, 589.15, 593.13, 
597.15, 601.18, 605.24, 609.33, 613.44, 617.57, 621.74, 625.92, 630.13, 634.37, 638.63, 
642.93, 647.24, 650.00]

def write_nvt():
    nvt = open("nvt0.mdp","r")
    nvt_lines = nvt.readlines()
    nvt_1 = nvt_lines[0:32]
    nvt_2 = nvt_lines[33:]
    l = []

    for i in range(len(temps)):
        l.append("ref_t                   =      " + str(temps[i]) + "     " + str(temps[i]) + "\n")

    for i in range(len(temps)):
        f = open(str(temps[i]) + "_nvt.mdp","w")

    for i in range(len(l)):
        for j in range(len(temps)):
            f = open(str(temps[j]) + "_nvt.mdp","w")
            for k in range(len(nvt_1)):
                f.write(nvt_1[k])
            f.write(l[j])
            for m in range(len(nvt_2)):
                f.write(nvt_2[m])

def write_npt():
    npt = open("npt0.mdp","r")
    npt_lines = npt.readlines()
    npt_1 = npt_lines[0:32]
    npt_2 = npt_lines[33:]
    l = []

    for i in range(len(temps)):
        l.append("ref_t                   =      " + str(temps[i]) + "     " + str(temps[i]) + "\n")

    for i in range(len(temps)):
        f = open(str(temps[i]) + "_npt.mdp","w")

    for i in range(len(l)):
        for j in range(len(temps)):
            f = open(str(temps[j]) + "_npt.mdp","w")
            for k in range(len(npt_1)):
                f.write(npt_1[k])
            f.write(l[j])
            for m in range(len(npt_2)):
                f.write(npt_2[m])

def write_md():
    md = open("md0.mdp","r")
    md_lines = md.readlines()
    md_1 = md_lines[0:32]
    md_2 = md_lines[33:]
    l = []

    for i in range(len(temps)):
        l.append("ref_t                   =      " + str(temps[i]) + "     " + str(temps[i]) + "\n")

    for i in range(len(temps)):
        f = open(str(temps[i]) + "_md.mdp","w")

    for i in range(len(l)):
        for j in range(len(temps)):
            f = open(str(temps[j]) + "_md.mdp","w")
            for k in range(len(md_1)):
                f.write(md_1[k])
            f.write(l[j])
            for m in range(len(md_2)):
                f.write(md_2[m])

def run_nvt():
    l = []
    for i in range(len(temps)):
        l.append("gmx_mpi grompp -f " + str(temps[i]) + "_nvt.mdp " + "-p topol.top -c em.gro -r em.gro -o " + str(temps[i]) + "_nvt.tpr " + "&&")
        l.append("gmx_mpi mdrun -v -deffnm " + str(temps[i]) + "_nvt" + " &&")
    #print(l)
    for command in range(len(l)):
        os.system(l[command])

def run_npt():
    l = []
    for i in range(len(temps)):
        l.append("gmx_mpi grompp -f " + str(temps[i]) + "_npt.mdp " + "-p topol.top -c " + str(temps[i]) + "_nvt.gro" + " -r " +  str(temps[i]) + "_nvt.gro " + "-o " + str(temps[i]) + "_npt.tpr " + "&&")
        l.append("gmx_mpi mdrun -v -deffnm " + str(temps[i]) + "_npt" + " &&")
    #print(l)
    for command in range(len(l)):
        os.system(l[command])

def run_remd():
    l = []
    g = []
    f = []

    for i in range(len(temps)):
        l.append("gmx_mpi grompp -f " + str(temps[i]) + "_md.mdp " + "-p topol.top -c " + str(temps[i]) + "_npt.gro -r "+ str(temps[i]) + "_npt.gro " + "-t " + str(temps[i]) + "_npt.cpt -o " + str(temps[i]) + "_remd.tpr " + "-maxwarn 10 " + "&&")
        #l.append("gmx_mpi mdrun -v -deffnm " + str(temps[i]) + "_remd" + " &&")
        f.append("mkdir " + str(temps[i]) + "_remd &&")
        #os.system("mkdir " + str(temps[i]) + "_remd &&")

    for command in range(len(l)):
        #os.system(l[command])
        print(l[command])
    
    for command in range(len(f)):
        os.system(f[command])
        #print(f[command])

    for i in range(len(temps)):
        #os.system("mv " + str(temps[i]) + "_remd.tpr " + str(temps[i]) + "_remd" + " && " + "cd " + str(temps[i]) + "_remd" + " && " + "mv " + str(temps[i]) + "_remd.tpr" + " remd.tpr" + "&& cd ..")
        g.append("mv " + str(temps[i]) + "_remd.tpr " + str(temps[i]) + "_remd" + " && " + "cd " + str(temps[i]) + "_remd " + "&& " + "mv " + str(temps[i]) + "_remd.tpr " + "remd.tpr " + "&& cd .. &&")
    #print(g)

    for i in range(len(g)):
        os.system(g[i])
        #print(g[i])
        
   
write_nvt()
write_npt()
write_md()
run_nvt()
run_npt()
run_remd()
