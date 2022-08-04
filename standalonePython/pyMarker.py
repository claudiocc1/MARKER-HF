def pyMarker(v):
    
    """
    Input:  ordered list with [BPDIAS, CREATN, BUN, HGB, WBC, PLT, ALB]
    Output: value of Marker-HF. Return -99 if out of range.

    Units are:
    BPDIAS mm Hg
    CREATN mg/dL
    BUN    mg/dL
    HGB     g/dL
    WBC    10^3 per muL
    PLT    10^3 per muL
    ALB    g/dL
    RDW    %

    Python translation of an XML file for the C++ CERN ROOT/TMVA
    package courtesy of Nick Amin 
    https://gist.github.com/aminnj/f1c03e4919e4dd22850d58025cf67d73

    Questions to claudio@physics.ucsb.edu ayagil@physics.ucsd.edu
    """

    # the input must be a list
    if not (type(v) is list):
        print("Input must be a list")
        return -99
    
    # do we have the right number of inputs
    if len(v) != 8:
        print("Input list length = ", len(v)," ...should be 8")
        return -99

    # is everything in the list a number?
    for elem in v:
        number = type(elem)==int or type(elem)==float
        if not number:
            print(elem, "is not a valid number")
            return -99

    # read the list into variables
    BPDIAS, CREATN, BUN, HGB, WBC, PLT, ALB, RDW = v
                    
    # Check the input values
    if BPDIAS<20 or BPDIAS>120:
        print("Input out of range: BPDIAS = ", BPDIAS)
        return -99
    if CREATN<0 or CREATN>25:
        print("Input out of range: CREATN = ", CREATN)
        return -99
    if BUN<0 or BUN>160:
        print("Input out of range: BUN = ", BUN)
        return -99
    if HGB<2 or HGB>20:
        print("Input out of range: HGB = ", HGB)
        return -99
    if WBC<0 or WBC>40:
        print("Input out of range: WBC = ", WBC)
        return -99
    if PLT<0 or PLT>1500:
        print("Input out of range: PLT = ", PLT)
        return -99
    if ALB<0 or ALB>6:
        print("Input out of range: ALB = ", ALB)
        return -99
    if RDW<10 or RDW>30:
        print("Input out of range: RDW = ", RDW)
        return -99 
       

    totsum = 0.
    totsum += 0.6682739287253201*(((-1 if (PLT >= 127.55555725097656) else 1) if (ALB >= 3.3222222328186035) else 1))
    totsum += 0.45781504206836804*(((-1 if (BPDIAS >= 60.11111068725586) else 1) if (ALB >= 3.3222222328186035) else 1))
    totsum += 0.39037149754309997*((-1 if (BPDIAS >= 51.0) else 1))
    totsum += 0.5838756272902201*(((-1 if (BPDIAS >= 60.11111068725586) else 1) if (ALB >= 3.5444443225860596) else (-1 if (BPDIAS >= 80.44444274902344) else 1)))
    totsum += 0.5249642779046937*(((-1 if (WBC < 15.833333015441895) else 1) if (ALB >= 2.8333332538604736) else 1))
    totsum += 0.458958674057216*((-1 if (ALB >= 3.700000047683716) else (-1 if (PLT >= 200.6666717529297) else 1)))
    totsum += 0.3201246261639898*((-1 if (ALB >= 3.933333396911621) else 1))
    totsum += 0.5014823107505603*(((-1 if (BPDIAS >= 45.33333206176758) else 1) if (HGB >= 10.033332824707031) else 1))
    totsum += 0.3244247899805062*((-1 if (BPDIAS >= 58.44444274902344) else 1))
    totsum += 0.37897783757817666*(((-1 if (WBC < 22.72222137451172) else 1) if (ALB >= 2.700000047683716) else 1))
    totsum += 0.3296250079711166*(((-1 if (ALB >= 2.7666666507720947) else 1) if (BUN < 25.66666603088379) else 1))
    totsum += 0.22013748196818642*((-1 if (ALB >= 4.133333206176758) else 1))
    totsum += 0.3656183690795275*((-1 if (BPDIAS >= 58.88888931274414) else (-1 if (HGB >= 9.566666603088379) else 1)))
    totsum += 0.24233215952653356*((-1 if (BPDIAS >= 84.0) else (-1 if (RDW < 13.788888931274414) else 1)))
    totsum += 0.3890721150026656*(((-1 if (WBC >= 4.577777862548828) else 1) if (ALB >= 3.8000001907348633) else (-1 if (WBC < 8.677777290344238) else 1)))
    totsum += 0.2742519273367295*((-1 if (PLT >= 209.6666717529297) else 1))
    totsum += 0.13754461454253683*(((-1 if (PLT < 78.55555725097656) else 1) if (BPDIAS >= 40.22222137451172) else 1))
    totsum += 0.2884809183645409*((-1 if (ALB >= 2.8333332538604736) else 1))
    totsum += 0.37071574216804615*(((-1 if (ALB >= 3.211111068725586) else 1) if (BPDIAS >= 58.44444274902344) else 1))
    totsum += 0.2912992240238879*(((-1 if (BPDIAS >= 36.44444274902344) else 1) if (BUN < 65.77777862548828) else 1))
    totsum += 0.3133670498814721*(((-1 if (PLT >= 134.6666717529297) else 1) if (PLT < 369.6666564941406) else 1))
    totsum += 0.294088505630809*(((-1 if (BUN < 15.333333015441895) else 1) if (BPDIAS >= 45.33333206176758) else 1))
    totsum += 0.32939017713597557*((-1 if (RDW < 14.45555591583252) else 1))
    totsum += 0.18187080660957616*((-1 if (ALB >= 2.7666666507720947) else (-1 if (HGB >= 9.355555534362793) else 1)))
    totsum += 0.25907096380947126*(((-1 if (WBC < 7.344444274902344) else 1) if (WBC < 16.588890075683594) else 1))
    totsum += 0.28888151983903565*(((-1 if (ALB >= 3.0333333015441895) else 1) if (RDW < 14.144444465637207) else 1))
    totsum += 0.30145889015630806*((-1 if (ALB >= 3.933333396911621) else (-1 if (RDW >= 15.44444465637207) else 1)))
    totsum += 0.4532506261596639*(((-1 if (BPDIAS >= 43.33333206176758) else 1) if (ALB < 3.9000000953674316) else (-1 if (RDW < 14.11111068725586) else 1)))
    totsum += 0.3833391868928839*(((-1 if (BPDIAS >= 74.0) else 1) if (PLT >= 148.3333282470703) else 1))
    totsum += 0.19361314511457922*((-1 if (ALB >= 2.700000047683716) else 1))
    totsum += 0.4114494850369094*(((-1 if (BPDIAS >= 47.33333206176758) else 1) if (PLT >= 138.44444274902344) else (-1 if (HGB < 9.666666984558105) else 1)))
    totsum += 0.37005628722701145*((-1 if (ALB >= 3.8000001907348633) else (-1 if (CREATN >= 1.4955555200576782) else 1)))
    totsum += 0.3250793004173557*(((-1 if (BPDIAS >= 59.0) else 1) if (WBC < 5.877777576446533) else (-1 if (PLT >= 305.6666564941406) else 1)))
    totsum += 0.35731436645355424*(((-1 if (BUN < 40.66666793823242) else 1) if (HGB >= 7.488888740539551) else 1))
    totsum += 0.13445973399162814*((-1 if (HGB >= 14.611111640930176) else (-1 if (RDW >= 13.377778053283691) else 1)))
    totsum += 0.2629803922751463*((-1 if (ALB >= 4.055555820465088) else (-1 if (BPDIAS >= 61.11111068725586) else 1)))
    totsum += 0.2951987524848885*(((-1 if (WBC < 6.94444465637207) else 1) if (WBC < 15.677777290344238) else 1))
    totsum += 0.23555609021050178*(((-1 if (BPDIAS >= 34.88888931274414) else 1) if (RDW < 18.16666603088379) else 1))
    totsum += 0.1456916644232343*((-1 if (HGB >= 14.633333206176758) else 1))
    totsum += 0.09180673671223757*(((-1 if (HGB < 7.633333206176758) else 1) if (ALB >= 2.3777778148651123) else 1))
    totsum += 0.456163541428706*(((-1 if (BUN < 26.44444465637207) else 1) if (BPDIAS >= 58.44444274902344) else (-1 if (HGB >= 12.233333587646484) else 1)))
    totsum += 0.14842543961149254*((-1 if (ALB >= 2.788888931274414) else (-1 if (BPDIAS >= 70.66666412353516) else 1)))
    totsum += 0.3508172418287594*(((-1 if (BPDIAS >= 49.0) else 1) if (BUN >= 15.55555534362793) else (-1 if (RDW >= 15.155555725097656) else 1)))
    totsum += 0.25549485109820447*(((-1 if (CREATN < 1.6844444274902344) else 1) if (BPDIAS >= 64.44444274902344) else (-1 if (BPDIAS >= 58.66666793823242) else 1)))
    totsum += 0.253973283728722*(((-1 if (WBC < 7.0) else 1) if (WBC < 8.811111450195312) else 1))
    totsum += 0.17342475143879116*((-1 if (RDW < 13.788888931274414) else (-1 if (HGB < 13.166666030883789) else 1)))
    totsum += 0.2961320193576971*((-1 if (ALB >= 3.933333396911621) else (-1 if (RDW < 13.788888931274414) else 1)))
    totsum += 0.3731889623232079*(((-1 if (RDW >= 13.100000381469727) else 1) if (ALB >= 3.5444443225860596) else (-1 if (WBC >= 8.366666793823242) else 1)))
    totsum += 0.29541085816575785*((-1 if (CREATN >= 8.691110610961914) else 1))
    totsum += 0.23768513134737057*(((-1 if (ALB < 4.233333587646484) else 1) if (RDW < 13.922222137451172) else 1))
    totsum += 0.2741310317407058*(((-1 if (WBC >= 11.233332633972168) else 1) if (WBC < 16.899999618530273) else 1))
    totsum += 0.21098441635430049*(((-1 if (WBC >= 4.144444465637207) else 1) if (WBC < 17.16666603088379) else 1))
    totsum += 0.27953402546028155*((-1 if (WBC < 18.077777862548828) else 1))
    totsum += 0.1833385757309523*((-1 if (HGB < 7.277777671813965) else (-1 if (BUN >= 53.22222137451172) else 1)))
    totsum += 0.34131056388591785*(((-1 if (RDW >= 13.877778053283691) else 1) if (BUN < 65.77777862548828) else 1))
    totsum += 0.2952704830084072*(((-1 if (RDW >= 12.355555534362793) else 1) if (WBC < 16.744443893432617) else 1))
    totsum += 0.32857884456671343*(((-1 if (ALB >= 4.099999904632568) else 1) if (ALB >= 2.4111111164093018) else 1))
    totsum += 0.33292245888295235*((-1 if (ALB >= 2.4555556774139404) else (-1 if (CREATN < 1.0811110734939575) else 1)))
    totsum += 0.2688159995844911*((-1 if (PLT >= 230.3333282470703) else (-1 if (ALB >= 3.3222222328186035) else 1)))
    totsum += 0.09884851297635693*(((-1 if (RDW < 12.677777290344238) else 1) if (WBC < 16.366666793823242) else 1))
    totsum += 0.26560283596179046*((-1 if (WBC < 10.199999809265137) else (-1 if (BUN < 18.22222137451172) else 1)))
    totsum += 0.26441584418064007*((1 if (BUN < 27.66666603088379) else (-1 if (BUN >= 47.11111068725586) else 1)))
    totsum += 0.3661634498368807*(((-1 if (CREATN < 3.0622222423553467) else 1) if (PLT < 183.0) else (-1 if (WBC < 6.655555248260498) else 1)))
    totsum += 0.2921054588360385*((-1 if (ALB >= 3.3222222328186035) else (-1 if (BUN < 14.666666984558105) else 1)))
    totsum += 0.2531034634325277*(((-1 if (PLT < 412.1111145019531) else 1) if (PLT >= 288.5555419921875) else (-1 if (RDW < 18.433332443237305) else 1)))
    totsum += 0.22539123147747306*(((-1 if (BUN < 14.333333015441895) else 1) if (BPDIAS >= 58.44444274902344) else 1))
    totsum += 0.3399732711327725*(((-1 if (PLT >= 139.11111450195312) else 1) if (HGB >= 9.833333969116211) else (-1 if (ALB >= 2.933333396911621) else 1)))
    totsum += 0.27794026738421207*((-1 if (BUN >= 41.33333206176758) else 1))
    totsum += 0.3184077841844221*(((-1 if (PLT >= 212.0) else 1) if (BPDIAS >= 81.33333587646484) else (-1 if (HGB < 11.94444465637207) else 1)))
    totsum += 0.16441137872522898*(((-1 if (PLT >= 274.8888854980469) else 1) if (ALB >= 2.433333396911621) else 1))
    totsum += 0.3459577125253099*(((-1 if (PLT < 232.11111450195312) else 1) if (BPDIAS >= 76.55555725097656) else (-1 if (PLT >= 277.6666564941406) else 1)))
    totsum += 0.25710204067344256*(((-1 if (ALB >= 4.1666669845581055) else 1) if (PLT < 241.6666717529297) else (-1 if (BPDIAS >= 73.88888549804688) else 1)))
    totsum += 0.2392848819007343*((-1 if (BUN < 27.66666603088379) else (-1 if (RDW < 16.677778244018555) else 1)))
    totsum += 0.29837939156197996*(((-1 if (WBC >= 4.222222328186035) else 1) if (CREATN < 2.863333225250244) else (-1 if (BUN >= 44.33333206176758) else 1)))
    totsum += 0.27519084879396283*(((-1 if (PLT < 139.0) else 1) if (WBC < 12.633333206176758) else 1))
    totsum += 0.3648006396666563*(((-1 if (ALB >= 2.700000047683716) else 1) if (WBC < 5.655555725097656) else 1))
    totsum += 0.43355793125452513*(((-1 if (PLT >= 55.88888931274414) else 1) if (PLT < 448.0) else 1))
    totsum += 0.17596897310511922*((-1 if (RDW < 14.144444465637207) else 1))
    totsum += 0.23350413476206824*(((-1 if (WBC < 6.144444465637207) else 1) if (ALB >= 2.7666666507720947) else 1))
    totsum += 0.5122260427086697*((-1 if (BPDIAS >= 66.77777862548828) else (-1 if (PLT >= 235.0) else 1)))
    totsum += 0.34217221522746133*(((-1 if (BPDIAS >= 58.88888931274414) else 1) if (ALB >= 2.633333206176758) else (-1 if (ALB < 2.0444443225860596) else 1)))
    totsum += 0.3155416510250053*(((-1 if (BUN < 64.66666412353516) else 1) if (ALB >= 2.5333333015441895) else (-1 if (WBC < 7.511111259460449) else 1)))
    totsum += 0.18384080654806437*((-1 if (ALB >= 3.3222222328186035) else 1))
    totsum += 0.2513828389744962*(((-1 if (PLT >= 45.33333206176758) else 1) if (PLT < 296.77777099609375) else (-1 if (ALB >= 3.299999952316284) else 1)))
    totsum += 0.25615988275544255*(((-1 if (ALB >= 3.8000001907348633) else 1) if (CREATN >= 1.3177778720855713) else 1))
    totsum += 0.1874388345676402*(((-1 if (HGB >= 15.15555477142334) else 1) if (ALB >= 2.433333396911621) else 1))
    totsum += 0.42722029344336726*(((-1 if (BUN >= 12.88888931274414) else 1) if (ALB >= 3.1111111640930176) else (-1 if (BUN >= 36.33333206176758) else 1)))
    totsum += 0.2507494703511583*(((-1 if (PLT >= 265.6666564941406) else 1) if (HGB < 8.811110496520996) else (-1 if (BPDIAS >= 87.88888549804688) else 1)))
    totsum += 0.38680427194810313*((-1 if (BUN < 40.66666793823242) else (-1 if (BUN >= 49.11111068725586) else 1)))
    totsum += 0.2907292291731406*(((-1 if (BPDIAS >= 38.66666793823242) else 1) if (BUN < 40.0) else (-1 if (RDW < 14.677777290344238) else 1)))
    totsum += 0.29018025233757416*(((-1 if (ALB >= 2.444444417953491) else 1) if (ALB < 3.5444443225860596) else (-1 if (RDW < 14.333333015441895) else 1)))
    totsum += 0.27949592815068103*((-1 if (BPDIAS >= 47.33333206176758) else 1))
    totsum += 0.19660185712062145*((-1 if (ALB >= 2.3333334922790527) else 1))
    totsum += 0.26044230508611604*(((-1 if (BPDIAS >= 45.66666793823242) else 1) if (ALB >= 2.7666666507720947) else 1))
    totsum += 0.3201916235884313*(((-1 if (ALB >= 2.7333333492279053) else 1) if (BPDIAS < 75.66666412353516) else 1))
    totsum += 0.27317797832659513*(((-1 if (RDW < 20.811111450195312) else 1) if (ALB < 4.1666669845581055) else (-1 if (BPDIAS < 74.0) else 1)))
    totsum += 0.35265863439623374*(((-1 if (PLT < 227.44444274902344) else 1) if (WBC >= 5.47777795791626) else (-1 if (PLT >= 154.3333282470703) else 1)))
    totsum += 0.29981999448825936*(1)
    totsum += 0.3523659194098828*(((-1 if (ALB >= 2.8333332538604736) else 1) if (PLT >= 283.6666564941406) else 1))
    totsum += 0.4259121371425187*((-1 if (BPDIAS >= 60.0) else (-1 if (PLT >= 183.0) else 1)))
    totsum += 0.28294416034039493*((-1 if (ALB >= 3.155555486679077) else (-1 if (PLT >= 344.5555419921875) else 1)))
    totsum += 0.33040615410474383*(((-1 if (BPDIAS < 69.55555725097656) else 1) if (WBC < 11.300000190734863) else 1))
    totsum += 0.26639559171832033*(((-1 if (ALB < 4.44444465637207) else 1) if (PLT >= 82.77777862548828) else (-1 if (PLT >= 46.44444274902344) else 1)))
    totsum += 0.3149648087170432*((-1 if (BPDIAS >= 69.55555725097656) else (-1 if (ALB >= 4.011110782623291) else 1)))
    totsum += 0.28127014530550454*((-1 if (ALB >= 4.088889122009277) else (-1 if (HGB < 9.733332633972168) else 1)))
    totsum += 0.2194263204688998*((-1 if (ALB >= 4.088889122009277) else 1))
    totsum += 0.2638788957091032*((-1 if (RDW >= 22.833332061767578) else (-1 if (HGB >= 11.333333015441895) else 1)))
    totsum += 0.2538138140928758*(((-1 if (HGB < 15.199999809265137) else 1) if (HGB >= 9.59999942779541) else (-1 if (RDW >= 17.066667556762695) else 1)))
    totsum += 0.23424523047294932*(((-1 if (HGB < 14.199999809265137) else 1) if (WBC < 17.03333282470703) else 1))
    totsum += 0.29171455087685266*(((-1 if (BUN < 25.22222137451172) else 1) if (PLT >= 298.77777099609375) else (-1 if (ALB >= 3.433333396911621) else 1)))
    totsum += 0.1888353301725287*(1)
    totsum += 0.30060721342953906*(((-1 if (BUN < 28.88888931274414) else 1) if (HGB >= 14.166666030883789) else (-1 if (HGB < 7.722222328186035) else 1)))
    totsum += 0.30109931594841005*(((-1 if (WBC < 7.188889026641846) else 1) if (WBC < 15.833333015441895) else 1))
    totsum += 0.32135875772223166*(((-1 if (CREATN < 1.2911111116409302) else 1) if (WBC >= 11.45555591583252) else 1))
    totsum += 0.3784742913919422*(((-1 if (ALB >= 2.8333334922790527) else 1) if (ALB < 3.7666666507720947) else (-1 if (BUN >= 45.55555725097656) else 1)))
    totsum += 0.3315832320610312*(((-1 if (BPDIAS < 65.55555725097656) else 1) if (HGB >= 10.877778053283691) else (-1 if (HGB < 9.711111068725586) else 1)))
    totsum += 0.48598414244086935*((-1 if (WBC < 11.61111068725586) else (-1 if (RDW >= 17.633333206176758) else 1)))
    totsum += 0.250205101762413*(((-1 if (BPDIAS >= 43.33333206176758) else 1) if (BPDIAS < 80.66666412353516) else (-1 if (BPDIAS >= 84.66666412353516) else 1)))
    totsum += 0.3392810714798614*(((-1 if (WBC >= 6.344444751739502) else 1) if (PLT >= 150.11111450195312) else (-1 if (BUN < 18.22222137451172) else 1)))
    totsum += 0.2523745294451122*(((-1 if (CREATN < 3.3566665649414062) else 1) if (ALB < 4.244444370269775) else (-1 if (ALB >= 4.377778053283691) else 1)))
    totsum += 0.3540235626704529*(((-1 if (ALB < 3.1111111640930176) else 1) if (PLT < 181.0) else (-1 if (ALB >= 3.8000001907348633) else 1)))
    totsum += 0.3586301419938215*(((-1 if (WBC < 11.933333396911621) else 1) if (BUN < 14.333333015441895) else (-1 if (HGB >= 9.733332633972168) else 1)))
    totsum += 0.3420896685169332*(((-1 if (HGB >= 13.866666793823242) else 1) if (BUN < 29.66666603088379) else (-1 if (RDW < 14.588889122009277) else 1)))
    totsum += 0.3770518567108748*(((-1 if (BPDIAS >= 61.22222137451172) else 1) if (WBC < 8.066666603088379) else (-1 if (CREATN >= 2.753333330154419) else 1)))
    totsum += 0.25900250632820043*(((-1 if (BUN < 65.11111450195312) else 1) if (RDW < 20.811111450195312) else 1))
    totsum += 0.1755747731490244*(((-1 if (BUN < 29.11111068725586) else 1) if (BPDIAS >= 77.44444274902344) else 1))
    totsum += 0.40592758936716333*(((-1 if (ALB >= 2.344444513320923) else 1) if (HGB >= 10.166666030883789) else (-1 if (PLT >= 196.0) else 1)))
    totsum += 0.29536955808650805*(((-1 if (RDW >= 13.033332824707031) else 1) if (ALB >= 3.933333396911621) else (-1 if (ALB >= 3.3888890743255615) else 1)))
    totsum += 0.23512790557018906*(((-1 if (ALB < 4.433333396911621) else 1) if (ALB >= 3.2666666507720947) else 1))
    totsum += 0.3035972029411493*(((-1 if (BUN < 25.66666603088379) else 1) if (BPDIAS >= 74.66666412353516) else (-1 if (PLT < 76.22222137451172) else 1)))
    totsum += 0.37752599963177236*((-1 if (BPDIAS >= 70.44444274902344) else (-1 if (HGB < 11.355555534362793) else 1)))
    totsum += 0.4352015030511796*(((-1 if (ALB < 3.933333396911621) else 1) if (HGB >= 8.699999809265137) else (-1 if (PLT >= 299.8888854980469) else 1)))
    totsum += 0.28451580324562575*((-1 if (CREATN >= 6.467777729034424) else (-1 if (HGB >= 11.88888931274414) else 1)))
    totsum += 0.46389187752333627*(((-1 if (WBC < 15.177777290344238) else 1) if (WBC >= 8.244443893432617) else (-1 if (RDW < 14.655555725097656) else 1)))
    totsum += 0.2852984989358854*((-1 if (HGB < 10.0) else 1))
    totsum += 0.287657333981535*((-1 if (RDW >= 19.855554580688477) else (-1 if (PLT < 84.77777862548828) else 1)))
    totsum += 0.32769823820142147*(((-1 if (BPDIAS >= 47.66666793823242) else 1) if (PLT >= 150.6666717529297) else 1))
    totsum += 0.3011265371520211*(((-1 if (PLT >= 88.33333587646484) else 1) if (HGB < 11.633333206176758) else (-1 if (BPDIAS >= 67.33333587646484) else 1)))
    totsum += 0.3563811437208124*((-1 if (HGB >= 10.233332633972168) else (-1 if (BPDIAS >= 67.66666412353516) else 1)))
    totsum += 0.17320498667699327*((-1 if (ALB >= 4.055555820465088) else (-1 if (WBC < 16.14444351196289) else 1)))
    totsum += 0.3525439069661285*(((-1 if (ALB >= 3.155555486679077) else 1) if (WBC < 11.300000190734863) else (-1 if (PLT < 181.0) else 1)))
    totsum += 0.2780160340011981*(((-1 if (RDW < 18.433332443237305) else 1) if (ALB >= 2.7666666507720947) else 1))
    totsum += 0.309364798584623*(((-1 if (BUN >= 10.0) else 1) if (BUN < 24.77777862548828) else 1))
    totsum += 0.18895152069667145*(((-1 if (HGB >= 12.877777099609375) else 1) if (BPDIAS >= 38.66666793823242) else 1))
    totsum += 0.30031242766024524*(((-1 if (ALB >= 3.866666793823242) else 1) if (HGB >= 8.677778244018555) else (-1 if (WBC >= 13.566666603088379) else 1)))
    totsum += 0.32957512134609307*(((-1 if (BPDIAS < 78.0) else 1) if (RDW < 13.877778053283691) else (-1 if (HGB < 8.477777481079102) else 1)))
    totsum += 0.38004604254901503*(((-1 if (PLT >= 26.11111068725586) else 1) if (PLT < 179.6666717529297) else (-1 if (HGB < 13.866665840148926) else 1)))
    totsum += 0.15187131744581572*((-1 if (PLT >= 476.3333435058594) else (-1 if (ALB >= 2.7666666507720947) else 1)))
    totsum += 0.11756737985149252*(1)
    totsum += 0.35990098402805343*((-1 if (HGB >= 10.233332633972168) else (-1 if (WBC < 8.300000190734863) else 1)))
    totsum += 0.11570751328303931*(1)
    totsum += 0.32958379342650346*(((-1 if (BPDIAS < 75.66666412353516) else 1) if (BPDIAS >= 51.0) else 1))
    totsum += 0.27903240614896835*(((-1 if (ALB >= 2.3333334922790527) else 1) if (CREATN >= 1.4044444561004639) else 1))
    totsum += 0.33146503221775836*((-1 if (PLT >= 448.0) else (-1 if (BPDIAS >= 92.44444274902344) else 1)))
    totsum += 0.2409258211760562*((-1 if (BUN < 77.0) else 1))
    totsum += 0.2193471935243524*((-1 if (PLT >= 147.55555725097656) else 1))
    totsum += 0.3490184313264587*(((-1 if (PLT < 75.22222137451172) else 1) if (BPDIAS >= 54.33333206176758) else 1))
    totsum += 0.41738981059761743*(((-1 if (HGB >= 8.533333778381348) else 1) if (BUN < 35.33333206176758) else (-1 if (ALB >= 3.155555486679077) else 1)))
    totsum += 0.22852689651305333*((-1 if (PLT >= 72.11111450195312) else (-1 if (RDW >= 17.866666793823242) else 1)))
    totsum += 0.2529400025007943*((-1 if (CREATN >= 4.940000057220459) else (-1 if (RDW >= 22.14444351196289) else 1)))
    totsum += 0.22017920064367466*(((-1 if (ALB < 3.2666666507720947) else 1) if (HGB < 16.38888931274414) else 1))
    totsum += 0.2043413032435973*(((-1 if (BPDIAS >= 68.55555725097656) else 1) if (RDW < 14.144444465637207) else 1))
    totsum += 0.16927663279668625*((-1 if (ALB >= 4.055555820465088) else 1))
    totsum += 0.30246091886534393*(((-1 if (WBC >= 4.0) else 1) if (WBC < 11.45555591583252) else 1))
    totsum += 0.20435331728317088*((-1 if (RDW < 18.16666603088379) else 1))
    totsum += 0.3153402601079674*((-1 if (WBC >= 12.5) else (-1 if (ALB >= 3.5444443225860596) else 1)))
    totsum += 0.28404763810627004*(((-1 if (PLT >= 221.6666717529297) else 1) if (WBC < 15.988887786865234) else 1))
    totsum += 0.3417999979955148*(((-1 if (CREATN < 1.4044444561004639) else 1) if (PLT < 228.3333282470703) else (-1 if (WBC >= 9.300000190734863) else 1)))
    totsum += 0.2971823506603152*(((-1 if (PLT < 274.8888854980469) else 1) if (BPDIAS >= 49.66666793823242) else 1))
    totsum += 0.341578886638904*(((-1 if (CREATN < 2.545555591583252) else 1) if (BPDIAS >= 54.33333206176758) else 1))
    totsum += 0.26908564029915466*((-1 if (BPDIAS >= 83.0) else 1))
    totsum += 0.284731459758361*(((-1 if (ALB >= 2.8777778148651123) else 1) if (BPDIAS >= 49.66666793823242) else 1))
    totsum += 0.33570489712458446*((-1 if (BUN < 15.333333015441895) else (-1 if (PLT >= 242.77777099609375) else 1)))
    totsum += 0.29827996095658227*((-1 if (BPDIAS >= 75.66666412353516) else (-1 if (WBC < 9.688888549804688) else 1)))
    totsum += 0.24862026936777915*(((-1 if (RDW < 15.166666984558105) else 1) if (ALB >= 3.866666793823242) else 1))
    totsum += 0.425777216240189*(((-1 if (HGB < 13.833333015441895) else 1) if (BUN >= 15.333333015441895) else (-1 if (RDW >= 16.96666717529297) else 1)))
    totsum += 0.4519807540384305*((-1 if (HGB < 7.222222328186035) else (-1 if (WBC < 7.655555725097656) else 1)))
    totsum += 0.47305475036766476*(((-1 if (ALB >= 3.3222222328186035) else 1) if (BPDIAS >= 55.88888931274414) else 1))
    totsum += 0.4009956115716284*(((-1 if (BPDIAS >= 59.55555725097656) else 1) if (WBC >= 8.833333015441895) else (-1 if (WBC < 7.0) else 1)))
    totsum += 0.3001737821456241*((-1 if (ALB >= 3.5444443225860596) else (-1 if (RDW >= 16.91111183166504) else 1)))
    totsum += 0.3251973851834536*(((-1 if (HGB >= 9.933333396911621) else 1) if (PLT < 354.3333435058594) else 1))
    totsum += 0.34084601627761546*(((-1 if (RDW >= 13.644444465637207) else 1) if (PLT >= 196.0) else (-1 if (PLT < 153.22222900390625) else 1)))
    totsum += 0.25536741562446597*(((-1 if (RDW < 15.033332824707031) else 1) if (RDW >= 12.98888874053955) else (-1 if (BPDIAS < 65.44444274902344) else 1)))
    totsum += 0.12562391306508205*((-1 if (CREATN >= 8.06222152709961) else 1))
    totsum += 0.20744353626218237*(((-1 if (RDW >= 13.311111450195312) else 1) if (BPDIAS >= 45.33333206176758) else 1))
    totsum += 0.2714496284485598*(((-1 if (PLT < 179.6666717529297) else 1) if (ALB >= 2.788888931274414) else 1))
    totsum += 0.33649998573042655*(((-1 if (CREATN < 3.693333148956299) else 1) if (PLT >= 64.55555725097656) else (-1 if (CREATN < 0.7566666603088379) else 1)))
    totsum += 0.18378190979088269*((-1 if (HGB >= 15.54444408416748) else (-1 if (PLT >= 179.6666717529297) else 1)))
    totsum += 0.4445262800184498*(((-1 if (BUN >= 17.88888931274414) else 1) if (WBC >= 11.333333969116211) else (-1 if (BUN >= 40.66666793823242) else 1)))
    totsum += 0.18503292987166986*(((-1 if (PLT >= 204.0) else 1) if (BUN < 90.88888549804688) else 1))
    totsum += 0.16010271889609312*((-1 if (HGB >= 15.333333015441895) else (-1 if (WBC < 17.16666603088379) else 1)))
    totsum += 0.25165726280565826*(((-1 if (BUN < 24.44444465637207) else 1) if (PLT < 87.44444274902344) else (-1 if (HGB >= 11.411110877990723) else 1)))
    totsum += 0.25487220451307396*((-1 if (RDW >= 15.755555152893066) else (-1 if (HGB < 14.033332824707031) else 1)))
    totsum += 0.3015225626504445*(((-1 if (PLT >= 129.88888549804688) else 1) if (HGB >= 12.755555152893066) else (-1 if (PLT >= 293.22222900390625) else 1)))
    totsum += 0.33653787550708053*(((-1 if (CREATN >= 1.0911110639572144) else 1) if (HGB < 8.655555725097656) else 1))
    totsum += 0.11003561332065413*((-1 if (PLT >= 387.3333435058594) else (-1 if (PLT >= 55.11111068725586) else 1)))
    totsum += 0.3422831353930696*(((-1 if (BPDIAS >= 51.33333206176758) else 1) if (HGB < 12.59999942779541) else (-1 if (HGB >= 14.911110877990723) else 1)))
    totsum += 0.315283424075954*(((-1 if (BUN < 25.33333396911621) else 1) if (WBC < 7.888888359069824) else (-1 if (RDW >= 15.755555152893066) else 1)))
    totsum += 0.21427490357240445*((-1 if (BPDIAS >= 84.0) else (-1 if (PLT >= 71.88888549804688) else 1)))
    totsum += 0.43929871534063286*(((-1 if (RDW < 17.0) else 1) if (BPDIAS < 64.44444274902344) else (-1 if (PLT < 139.0) else 1)))
    return totsum/59.83754259471197
