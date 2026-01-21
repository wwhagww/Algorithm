import sys; input = sys.stdin.readline
T = int(input())
for _ in range(T):
    r, HPM = map(int,input().split())
    f = int(input())

    hpn = HPM
    resG = []
    pG = min(1, ((3*HPM - 2*hpn)/(3*HPM))*r / 255)
    s = 1
    while pG < 1 and (s==1 or hpn>1):
        nxt_hpn = max(1, hpn-f)
        if s==1 and 1.5 > ((3*HPM - 2*nxt_hpn) / (3*HPM - 2*hpn)):
            s = 1.5
            resG.append("G")
        else:
            hpn = nxt_hpn
            resG.append("F")
        pG = min(1, ((3*HPM - 2*hpn)/(3*HPM))*r*s / 255)
    resG.append("C")

    hpn = HPM
    resY = []
    pY = min(1, ((3*HPM - 2*hpn)/(3*HPM))*r / 255)
    s = 1
    wait = False
    while pY < 1 and (s==1 or hpn>1) or wait:
        if wait == True:
            s = 2.5
            wait = False
        nxt_hpn = max(1, hpn-f)
        nnxt_hpn = max(1, hpn-2*f)
        if (s==1 and wait == False) and 2.5 > ((3*HPM - 2*nnxt_hpn) / (3*HPM - 2*nxt_hpn)):
            wait = True
            resY.append("Y")
        else:
            hpn = nxt_hpn
            resY.append("F")
        pY = min(1, ((3*HPM - 2*hpn)/(3*HPM))*r*s / 255)
    resY.append("C")

    # print(pY, pG) ##
    # print(*resG) ##
    # print(*resY) ##
    if pY > pG:
        print("".join(resY))
    else:
        if len(resG) < len(resY):
            print("".join(resG))
        else:
            print("".join(resY))

