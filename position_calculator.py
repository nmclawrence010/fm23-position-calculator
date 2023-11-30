import csv
from decimal import Decimal
from datetime import datetime

filename = 'csvs/blackburns4.csv'
uid = '29175403'
epl_dict = {}

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

def output_colour(position):
    if position >= 15:
        position_color = G
    elif position <15 and position >10:
        position_color = O
    else:
        position_color = R
    return position_color

def position_score_calculator(greens, blues):
    position_score = ((greens/3)*2) + (blues/3)
    return position_score

# Function to find which list of positions is the shortest
def get_shortest_list(lst):
    return min(lst, key=len)

def get_longest_list(lst):
    return max(lst, key=len)

def calculate_best_position(uid, filename):
    now = datetime.now()
    now = now.strftime("%Y-%m-%d")
    # Open the specified sheet and loop through each record
    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            # list_of_column_names.append(row)
            # break
            player_id = row[2]
            name = row[3]
            position = row[4]
            club, nation = row[5], row[6]
            # Physical info
            height, weight, age = row[7], row[8], row[9]
            # Feet info
            pref_foot, left_foot, right_foot = row[12], row[13], row[14]
            # Personality type
            personality, media_handling = row[15], row[16]
            # Technical attributes
            corners, crossing, dribbling, finishing, first_touch, freekicks, heading = row[17], row[18], row[19], row[20], row[21], row[22], row[23]
            long_shots, long_throws, marking, passing, penalties, tackling, technical = row[24], row[25], row[26], row[27], row[28], row[29], row[30]
            # Mental attributes
            aggression, anticipation, bravery, composure, concentration, decisions, determination = row[31], row[32], row[33], row[34], row[35], row[36], row[37]
            flair, leadership, off_the_ball, positioning, teamwork, vision, work_rate = row[38], row[39], row[40], row[41], row[42], row[43], row[44]
            # Physical attributes
            acceleration, agility, balance, jumping_reach = row[45], row[46], row[47], row[48]
            natural_fitness, pace, stamina, strength = row[49], row[50], row[51], row[52]
            # Goalkeeper attributes
            aerial_reach, command_area, eccentricity, handling, kicking = row[53], row[54], row[55], row[56], row[57]
            one_v_one, punching, reflexes, rushing_out, throwing = row[58], row[59], row[60], row[61], row[62]
            # Add the attributes to a dict with the players UID as the key name
            epl_dict[player_id] = name, position, club, nation, height, weight, age, pref_foot, left_foot, right_foot, personality, media_handling, \
            corners, crossing, dribbling, finishing, first_touch, freekicks, heading, long_shots, long_throws, marking, passing, penalties, tackling, \
            technical, aggression, anticipation, bravery, composure, concentration, decisions, determination, flair, leadership, off_the_ball, \
            positioning, teamwork, vision, work_rate, acceleration, agility, balance, jumping_reach, natural_fitness, pace, stamina, strength, \
            aerial_reach, command_area, eccentricity, handling, kicking, one_v_one, punching, reflexes, rushing_out, throwing

        # Get the attributes from specific players by UID
        # Kevin De Bruyne as example 18004457
        prem_player = (epl_dict).get(uid)
        attribute_list = []
        for i in range(len(prem_player)):
            attributes = prem_player[i]
            attribute_list.append(attributes)
        del attribute_list[:-46]

        # Extracting attributes from the player dict
        corners = int(attribute_list[0])
        crossing = int(attribute_list[1])
        dribbling = int(attribute_list[2])
        finishing = int(attribute_list[3])
        first_touch = int(attribute_list[4])
        freekicks = int(attribute_list[5])
        heading = int(attribute_list[6])
        long_shots = int(attribute_list[7])
        long_throws = int(attribute_list[8])
        marking = int(attribute_list[9])
        passing = int(attribute_list[10])
        penalties = int(attribute_list[11])
        tackling = int(attribute_list[12])
        technique = int(attribute_list[13])
        aggression = int(attribute_list[14])
        anticipation = int(attribute_list[15])
        bravery = int(attribute_list[16])
        composure = int(attribute_list[17])
        concentration = int(attribute_list[18])
        decisions = int(attribute_list[19])
        determination = int(attribute_list[20])
        flair = int(attribute_list[21])
        leadership = int(attribute_list[22])
        off_the_ball = int(attribute_list[23])
        positioning = int(attribute_list[24])
        teamwork = int(attribute_list[25])
        vision = int(attribute_list[26])
        work_rate = int(attribute_list[27])
        acceleration = int(attribute_list[28])
        agility = int(attribute_list[29])
        balance = int(attribute_list[30])
        jumping_reach = int(attribute_list[31])
        natural_fitness = int(attribute_list[32])
        pace = int(attribute_list[33])
        stamina = int(attribute_list[34])
        strength = int(attribute_list[35])

        W  = '\033[0m'  # white (normal)
        R  = '\033[31m' # red
        G  = '\033[32m' # green
        O  = '\033[33m' # orange
        B  = '\033[34m' # blue
        P  = '\033[35m' # purple

    # Position calcualtions
        DRL_dict = {}
        WBRL_dict = {}
        DC_dict = {}
        DM_dict = {}
        MC_dict = {}
        AM_dict = {}
        MRL_dict = {}
        AMRL_dict = {}
        ST_dict = {}
    # DR
        # Complete Wing-Back Support
        cwbs_greens = (crossing + dribbling + first_touch + passing + technique + decisions + off_the_ball + teamwork + work_rate + acceleration \
            + pace + stamina)/12
        cwbs_blues = (tackling + anticipation + composure + flair + agility + balance)/6
        cwbs = position_score_calculator(cwbs_greens, cwbs_blues)

        final_cwbs = round(cwbs, 2)
        final_cwbs = "{:.2f}".format(final_cwbs)
        final_cwbs = Decimal(final_cwbs)

        DRL_dict["CWB-S"] = final_cwbs
        WBRL_dict["CWB-S"] = final_cwbs

        # Complete Wing-Back Attack
        cwba_greens = (crossing + dribbling + first_touch + passing + technique + decisions + off_the_ball + teamwork + work_rate + acceleration \
            + pace + stamina + flair)/13
        cwba_blues = (tackling + anticipation + composure + agility + balance)/5
        cwba = position_score_calculator(cwba_greens, cwba_blues)
        
        final_cwba = round(cwba, 2)
        final_cwba = "{:.2f}".format(final_cwba)
        final_cwba = Decimal(final_cwba)

        DRL_dict["CWB-A"] = final_cwba
        WBRL_dict["CWB-A"] = final_cwba

        # Wing-Back Defend
        wbd_greens = (marking + tackling + anticipation + positioning + teamwork + work_rate + acceleration + stamina)/8
        wbd_blues = (crossing + dribbling + first_touch + passing + technique + concentration + decisions + off_the_ball + agility + pace)/9
        wbd = position_score_calculator(wbd_greens, wbd_blues)

        final_wbd = round(wbd, 2)
        final_wbd = "{:.2f}".format(final_wbd)
        final_wbd = Decimal(final_wbd)

        DRL_dict["WB-D "] = final_wbd
        WBRL_dict["WB-D "] = final_wbd

        # Wing-Back Support
        wbs_greens = (crossing + dribbling + marking + tackling + off_the_ball + teamwork + work_rate + acceleration + stamina)/9
        wbs_blues = (first_touch + passing + technique + anticipation + concentration + decisions + positioning + agility + pace)/9
        wbs = position_score_calculator(wbs_greens, wbs_blues)

        final_wbs = round(wbs, 2)
        final_wbs = "{:.2f}".format(final_wbs)
        final_wbs = Decimal(final_wbs)

        DRL_dict["WB-S "] = final_wbs
        WBRL_dict["WB-S "] = final_wbs

        # Wing-Back Attack
        wba_greens = (crossing + dribbling + tackling + technique + off_the_ball + teamwork + work_rate + acceleration + pace + stamina)/10
        wba_blues = (first_touch + marking + passing + anticipation + concentration + decisions + flair + positioning + agility)/9
        wba = position_score_calculator(wba_greens, wba_blues)
        
        final_wba = round(wba, 2)
        final_wba = "{:.2f}".format(final_wba)
        final_wba = Decimal(final_wba)

        DRL_dict["WB-A "] = final_wba
        WBRL_dict["WB-A "] = final_wba

        # Full-Back Defend
        fbd_greens = (marking + tackling + anticipation + concentration + positioning)/5
        fbd_blues = (crossing + passing + composure + decisions + teamwork + pace + stamina)/7
        fbd = position_score_calculator(fbd_greens, fbd_blues)
        
        final_fbd = round(fbd, 2)
        final_fbd = "{:.2f}".format(final_fbd)
        final_fbd = Decimal(final_fbd)

        DRL_dict["FB-D "] = final_fbd

        # Full-Back Support
        fbs_greens = (marking + tackling + anticipation + concentration + positioning + teamwork + work_rate)/7
        fbs_blues = (crossing + dribbling + passing + technique + composure + decisions + pace + stamina)/8
        fbs = position_score_calculator(fbs_greens, fbs_blues)
        
        final_fbs = round(fbs, 2)
        final_fbs = "{:.2f}".format(final_fbs)
        final_fbs = Decimal(final_fbs)

        DRL_dict["FB-S "] = final_fbs

        # Full-Back Attack
        fba_greens =(crossing + tackling + anticipation + positioning + teamwork + work_rate + pace + stamina)/8
        fba_blues = (dribbling + first_touch + marking + passing + technique + composure + concentration + decisions + off_the_ball + acceleration + agility)/11
        fba = position_score_calculator(fba_greens, fba_blues)
        
        final_fba = round(fba, 2)
        final_fba = "{:.2f}".format(final_fba)
        final_fba = Decimal(final_fba)

        DRL_dict["FB-A "] = final_fba

        # No-Nonsense Full-Back Defend
        nnfb_greens = (marking + tackling + anticipation + positioning + strength)/5
        nnfb_blues = (heading + aggression + bravery + concentration + teamwork)/5
        nnfb = position_score_calculator(nnfb_greens, nnfb_blues)
        
        final_nnfb = round(nnfb, 2)
        final_nnfb = "{:.2f}".format(final_nnfb)
        final_nnfb = Decimal(final_nnfb)

        DRL_dict["NNFB "] = final_nnfb

        # Inverted Wing-Back Defend
        iwbd_greens = (marking + passing + tackling + anticipation + decisions + positioning + teamwork + work_rate)/8
        iwbd_blues = (dribbling + first_touch + technique + concentration + off_the_ball + acceleration + agility + stamina)/8
        iwbd = position_score_calculator(iwbd_greens, iwbd_blues)
        
        final_iwbd = round(iwbd, 2)
        final_iwbd = "{:.2f}".format(final_iwbd)
        final_iwbd = Decimal(final_iwbd)

        DRL_dict["IWB-D"] = final_iwbd
        WBRL_dict["IWB-D"] = final_iwbd

        # Inverted Wing-Back Support
        iwbs_greens = (marking + passing + tackling + decisions + off_the_ball + teamwork + work_rate + stamina)/8
        iwbs_blues = (dribbling + first_touch + technique + anticipation + composure + concentration + positioning + acceleration + agility)/9
        iwbs = position_score_calculator(iwbs_greens, iwbs_blues)
        
        final_iwbs = round(iwbs, 2)
        final_iwbs = "{:.2f}".format(final_iwbs)
        final_iwbs = Decimal(final_iwbs)

        DRL_dict["IWB-S"] = final_iwbs
        WBRL_dict["IWB-S"] = final_iwbs

        # Inverted Wing-Back Attack
        iwba_greens = (dribbling + marking + passing + tackling + technique + decisions + off_the_ball + teamwork + work_rate + acceleration + stamina)/11
        iwba_blues = (dribbling + first_touch + technique + anticipation + composure + concentration + positioning + acceleration + agility)/9
        iwba = position_score_calculator(iwba_greens, iwba_blues)
        
        final_iwba = round(iwba, 2)
        final_iwba = "{:.2f}".format(final_iwba)
        final_iwba = Decimal(final_iwba)

        DRL_dict["IWB-A"] = final_iwba
        WBRL_dict["IWB-A"] = final_iwba

    # DC
        # Central Defender Defend
        cdd_greens = (heading + marking + tackling + positioning + jumping_reach + strength)/6
        cdd_blues = (aggression + anticipation + bravery + composure + concentration + decisions + pace)/7
        cdd = position_score_calculator(cdd_greens, cdd_blues)
        
        final_cdd = round(cdd, 2)
        final_cdd = "{:.2f}".format(final_cdd)
        final_cdd = Decimal(final_cdd)

        DC_dict["  CD-D"] = final_cdd

        # Central Defender Stopper
        cds_greens = (heading + tackling + aggression + bravery + decisions + positioning + jumping_reach + strength)/8
        cds_blues = (marking + anticipation + composure + concentration)/4
        cds = position_score_calculator(cds_greens, cds_blues)
        
        final_cds = round(cds, 2)
        final_cds = "{:.2f}".format(final_cds)
        final_cds = Decimal(final_cds)

        DC_dict["  CD-S"] = final_cds

        # Central Defender Cover
        cdc_greens = (marking + tackling + anticipation + concentration + decisions + positioning + pace)/7
        cdc_blues = (heading + bravery + composure + jumping_reach + strength)/5
        cdc = position_score_calculator(cdc_greens, cdc_blues)
        
        final_cdc = round(cdc, 2)
        final_cdc = "{:.2f}".format(final_cdc)
        final_cdc = Decimal(final_cdc)

        DC_dict["  CD-C"] = final_cdc

        # No-Nonsense Centre-Back Defend
        nncbd_greens = (heading + marking + tackling + positioning + jumping_reach + strength)/6
        nncbd_blues = (aggression + anticipation + bravery + concentration + pace)/5
        nncbd = position_score_calculator(nncbd_greens, nncbd_blues)
        
        final_nncbd = round(nncbd, 2)
        final_nncbd = "{:.2f}".format(final_nncbd)
        final_nncbd = Decimal(final_nncbd)

        DC_dict["NNCB-D"] = final_nncbd

        # No-Nonsense Centre-Back Stopper
        nncbs_greens = (heading + tackling + aggression + bravery + positioning + jumping_reach + strength)/7
        nncbs_blues = (marking + anticipation + concentration)/3
        nncbs = position_score_calculator(nncbs_greens, nncbs_blues)

        final_nncbs = round(nncbs, 2)
        final_nncbs = "{:.2f}".format(final_nncbs)
        final_nncbs = Decimal(final_nncbs)

        DC_dict["NNCB-S"] = final_nncbs

        # No-Nonsense Centre-Back Cover
        nncbc_greens = (marking + tackling + anticipation + concentration + positioning + pace)/6
        nncbc_blues = (heading + bravery + jumping_reach + strength)/4
        nncbc = position_score_calculator(nncbc_greens, nncbc_blues)

        final_nncbc = round(nncbc, 2)
        final_nncbc = "{:.2f}".format(final_nncbc)
        final_nncbc = Decimal(final_nncbc)

        DC_dict["NNCB-C"] = final_nncbc

        # Ball Playing Defender Defend
        bpdd_greens = (heading + marking + passing + tackling + composure + positioning + jumping_reach + strength)/8
        bpdd_blues = (first_touch + technique + aggression + anticipation + bravery + concentration + decisions + vision + pace)/9
        bpdd = position_score_calculator(bpdd_greens, bpdd_blues)
        
        final_bpdd = round(bpdd, 2)
        final_bpdd = "{:.2f}".format(final_bpdd)
        final_bpdd = Decimal(final_bpdd)

        DC_dict[" BPD-D"] = final_bpdd

        # Ball Playing Defender Stopper
        bpds_greens = (heading + passing + tackling + aggression + bravery + composure + decisions + positioning + jumping_reach + strength)/10
        bpds_blues = (first_touch + marking + technique + anticipation + concentration + vision)/6
        bpds = position_score_calculator(bpds_greens, bpds_blues)
        
        final_bpds = round(bpds, 2)
        final_bpds = "{:.2f}".format(final_bpds)
        final_bpds = Decimal(final_bpds)

        DC_dict[" BPD-S"] = final_bpds

        # Ball Playing Defender Cover
        bpdc_greens = (marking + passing + tackling + anticipation + composure + concentration + decisions + positioning + pace)/9
        bpdc_blues = (first_touch + heading + technique + bravery + vision + jumping_reach + strength)/7
        bpdc = position_score_calculator(bpdc_greens, bpdc_blues)
        
        final_bpdc = round(bpdc, 2)
        final_bpdc = "{:.2f}".format(final_bpdc)
        final_bpdc = Decimal(final_bpdc)

        DC_dict[" BPD-C"] = final_bpdc

        # Wide Centre Back Defend
        wcbd_greens = (crossing + heading + marking + tackling + positioning + jumping_reach + stamina + strength)/8
        wcbd_blues = (dribbling + aggression + anticipation + bravery + composure + concentration + decisions + work_rate + pace)/9
        wcbd = position_score_calculator(wcbd_greens, wcbd_blues)
        
        final_wcbd = round(wcbd, 2)
        final_wcbd = "{:.2f}".format(final_wcbd)
        final_wcbd = Decimal(final_wcbd)

        DC_dict[" WCB-D"] = final_wcbd

        # Wide Centre Back Support
        wcbs_greens = (crossing + dribbling + heading + tackling + positioning + jumping_reach + pace + stamina + strength)/9
        wcbs_blues = (aggression + anticipation + bravery + composure + concentration + decisions + off_the_ball + work_rate)/8
        wcbs = position_score_calculator(wcbs_greens, wcbs_blues)
        
        final_wcbs = round(wcbs, 2)
        final_wcbs = "{:.2f}".format(final_wcbs)
        final_wcbs = Decimal(final_wcbs)

        DC_dict[" WCB-S"] = final_wcbs

        # Wide Centre Back Attack
        wcba_greens = (crossing + dribbling + heading + tackling + off_the_ball + jumping_reach + pace + stamina + strength)/9
        wcba_blues = (aggression + anticipation + bravery + composure + concentration + decisions + positioning + work_rate)/8
        wcba = position_score_calculator(wcba_greens, wcba_blues)
        
        final_wcba = round(wcba, 2)
        final_wcba = "{:.2f}".format(final_wcba)
        final_wcba = Decimal(final_wcba)

        DC_dict[" WCB-A"] = final_wcba

        # Libero Support
        libs_greens = (first_touch + marking + passing + tackling + anticipation + composure + concentration + decisions + positioning + teamwork + vision + pace)/12
        libs_blues = (dribbling + heading + technique + bravery + flair + agility + balance + jumping_reach + stamina + strength)/10
        libs = position_score_calculator(libs_greens, libs_blues)
        
        final_libs = round(libs, 2)
        final_libs = "{:.2f}".format(final_libs)
        final_libs = Decimal(final_libs)

        DC_dict[" LIB-S"] = final_libs

        # Libero Attack
        liba_greens = (dribbling + first_touch + marking + passing + tackling + anticipation + composure + concentration + decisions + flair + positioning \
            + teamwork + vision + pace)/14
        liba_blues = (heading + long_shots + technique + bravery + acceleration + agility + balance + jumping_reach + stamina + strength)/10
        liba = position_score_calculator(liba_greens, liba_blues)
        
        final_liba = round(liba, 2)
        final_liba = "{:.2f}".format(final_liba)
        final_liba = Decimal(final_liba)

        DC_dict[" LIB-A"] = final_liba

    # DM
        # Defensive Midfielder Defend
        dmd_greens = (tackling + anticipation + concentration + positioning + teamwork)/5
        dmd_blues = (marking + passing + aggression + composure + decisions + work_rate + stamina + strength)/8
        dmd = position_score_calculator(dmd_greens, dmd_blues)

        final_dmd = round(dmd, 2)
        final_dmd = "{:.2f}".format(final_dmd)
        final_dmd = Decimal(final_dmd)

        DM_dict[" DM-D"] = final_dmd

        # Defensive Midfielder Support
        dms_greens = (tackling + anticipation + concentration + positioning + teamwork)/5
        dms_blues = (first_touch + marking + passing + aggression + composure + decisions + work_rate + stamina + strength)/9
        dms = position_score_calculator(dms_greens, dms_blues)

        final_dms = round(dms, 2)
        final_dms = "{:.2f}".format(final_dms)
        final_dms = Decimal(final_dms)

        DM_dict[" DM-S"] = final_dms

        # Half Back
        hb_greens = (marking + tackling + anticipation + composure + concentration + decisions + positioning + teamwork)/8
        hb_blues = (first_touch + passing + aggression + bravery + work_rate + jumping_reach + stamina + strength)/8
        hb = position_score_calculator(hb_greens, hb_blues)

        final_hb = round(hb, 2)
        final_hb = "{:.2f}".format(final_hb)
        final_hb = Decimal(final_hb)

        DM_dict["   HB"] = final_hb

        # Anchor
        a_greens = (marking + passing + anticipation + concentration + decisions + positioning)/6
        a_blues = (composure + teamwork + strength)/3
        a = position_score_calculator(a_greens, a_blues)

        final_a = round(a, 2)
        final_a = "{:.2f}".format(final_a)
        final_a = Decimal(final_a)

        DM_dict["    A"] = final_a

        # Segundo Volante Support
        vols_greens = (marking + passing + tackling + off_the_ball + positioning + work_rate + pace + stamina)/8
        vols_blues = (finishing + first_touch + long_shots + anticipation + composure + concentration + decisions + acceleration + balance + strength)/10
        vols = position_score_calculator(vols_greens, vols_blues)

        final_vols = round(vols, 2)
        final_vols = "{:.2f}".format(final_vols)
        final_vols = Decimal(final_vols)

        DM_dict["VOL-S"] = final_vols

        # Segundo Volante Attack
        vola_greens = (finishing + long_shots + passing + tackling + anticipation + off_the_ball + positioning + work_rate + pace + stamina)/10
        vola_blues = (first_touch + marking + composure + concentration + decisions + acceleration + balance + strength)/8
        vola = position_score_calculator(vola_greens, vola_blues)

        final_vola = round(vola, 2)
        final_vola = "{:.2f}".format(final_vola)
        final_vola = Decimal(final_vola)

        DM_dict["VOL-A"] = final_vola

        # Regista
        reg_greens = (first_touch + passing + technique + composure + decisions + flair + off_the_ball + teamwork + vision)/9
        reg_blues = (dribbling + long_shots + anticipation + balance)/4
        reg = position_score_calculator(reg_greens, reg_blues)

        final_reg = round(reg, 2)
        final_reg = "{:.2f}".format(final_reg)
        final_reg = Decimal(final_reg)

        DM_dict["  REG"] = final_reg

    # MC
        # Deep Lying Playmaker Defend
        dlpd_greens = (first_touch + passing + technique + composure + decisions + teamwork + vision)/7
        dlpd_blues = (tackling + anticipation + positioning + balance)/4
        dlpd = position_score_calculator(dlpd_greens, dlpd_blues)

        final_dlpd = round(dlpd, 2)
        final_dlpd = "{:.2f}".format(final_dlpd)
        final_dlpd = Decimal(final_dlpd)

        DM_dict["DLP-D"] = final_dlpd
        MC_dict["DLP-D"] = final_dlpd

        # Deep Lying Playmaker Support
        dlps_greens = (first_touch + passing + technique + composure + decisions + teamwork + vision)/7
        dlps_blues = (anticipation + off_the_ball + positioning + balance)/4
        dlps = position_score_calculator(dlps_greens, dlps_blues)

        final_dlps = round(dlps, 2)
        final_dlps = "{:.2f}".format(final_dlps)
        final_dlps = Decimal(final_dlps)

        DM_dict["DLP-S"] = final_dlps
        MC_dict["DLP-S"] = final_dlps

        # Advanced Playmaker Support
        aps_greens = (first_touch + passing + technique + composure + decisions + off_the_ball + teamwork + vision)/8
        aps_blues = (dribbling + flair + agility)/3
        aps = position_score_calculator(aps_greens, aps_blues)

        final_aps = round(aps, 2)
        final_aps = "{:.2f}".format(final_aps)
        final_aps = Decimal(final_aps)

        MC_dict[" AP-S"] = final_aps
        AM_dict[" AP-S"] = final_aps

        # Advanced Playmaker Attack
        apa_greens = (dribbling + first_touch + passing + technique + composure + decisions + off_the_ball + teamwork + vision)/9
        apa_blues = (anticipation + flair + acceleration + agility)/4
        apa = position_score_calculator(apa_greens, apa_blues)

        final_apa = round(apa, 2)
        final_apa = "{:.2f}".format(final_apa)
        final_apa = Decimal(final_apa)

        MC_dict[" AP-A"] = final_apa
        AM_dict[" AP-A"] = final_apa

        # Roaming Playmaker Support
        rpm_greens = (first_touch + passing + technique + anticipation + composure + decisions + off_the_ball + teamwork + vision + work_rate + acceleration + stamina)/12
        rpm_blues = (dribbling + long_shots + concentration + positioning + agility + balance + pace)/7
        rpm = position_score_calculator(rpm_greens, rpm_blues)

        final_rpm = round(rpm, 2)
        final_rpm = "{:.2f}".format(final_rpm)
        final_rpm = Decimal(final_rpm)

        DM_dict["  RPM"] = final_rpm
        MC_dict["  RPM"] = final_rpm

        # Central Midfielder Defend
        cmd_greens = (tackling + concentration + decisions + positioning + teamwork)/5
        cmd_blues = (first_touch + marking + passing + technique + aggression + anticipation + composure + work_rate + stamina)/9
        cmd = position_score_calculator(cmd_greens, cmd_blues)

        final_cmd = round(cmd, 2)
        final_cmd = "{:.2f}".format(final_cmd)
        final_cmd = Decimal(final_cmd)

        MC_dict[" CM-D"] = final_cmd

        # Central Midfielder Support
        cms_greens = (first_touch + passing + tackling + decisions + teamwork)/5
        cms_blues = (technique + anticipation + composure + concentration + off_the_ball + vision + work_rate + stamina)/8
        cms = position_score_calculator(cms_greens, cms_blues)

        final_cms = round(cms, 2)
        final_cms = "{:.2f}".format(final_cms)
        final_cms = Decimal(final_cms)

        MC_dict[" CM-S"] = final_cms

        # Central Midfielder Attack
        cma_greens = (first_touch + passing + decisions + off_the_ball)/4
        cma_blues = (long_shots + tackling + technique + anticipation + composure + teamwork + vision + work_rate + acceleration + stamina)/10
        cma = position_score_calculator(cma_greens, cma_blues)

        final_cma = round(cma, 2)
        final_cma = "{:.2f}".format(final_cma)
        final_cma = Decimal(final_cma)

        MC_dict[" CM-A"] = final_cma

        # Box to Box Midfielder Support
        b2b_greens = (passing + tackling + off_the_ball + teamwork + work_rate + stamina)/6
        b2b_blues = (dribbling + finishing + first_touch + long_shots + technique + aggression + anticipation + composure + decisions + positioning + acceleration \
            + balance + pace + strength)/14
        b2b = position_score_calculator(b2b_greens, b2b_blues)

        final_b2b = round(b2b, 2)
        final_b2b = "{:.2f}".format(final_b2b)
        final_b2b = Decimal(final_b2b)

        MC_dict["  B2B"] = final_b2b

        # Ball Winning Midfielder Defend
        bwmd_greens = (tackling + aggression + anticipation + teamwork + work_rate + stamina)/6
        bwmd_blues = (marking + bravery + concentration + positioning + agility + pace + strength)/7
        bwmd = position_score_calculator(bwmd_greens, bwmd_blues)

        final_bwmd = round(bwmd, 2)
        final_bwmd = "{:.2f}".format(final_bwmd)
        final_bwmd = Decimal(final_bwmd)

        DM_dict["BWM-D"] = final_bwmd
        MC_dict["BWM-D"] = final_bwmd

        # Ball Winning Midfielder Support
        bwms_greens = (tackling + aggression + anticipation + teamwork + work_rate + stamina)/6
        bwms_blues = (marking + passing + bravery + concentration + agility + pace + strength)/7
        bwms = position_score_calculator(bwms_greens, bwms_blues)

        final_bwms = round(bwms, 2)
        final_bwms = "{:.2f}".format(final_bwms)
        final_bwms = Decimal(final_bwms)

        DM_dict["BWM-S"] = final_bwms
        MC_dict["BWM-S"] = final_bwms

        # Carrilero Support
        car_greens = (first_touch + passing + tackling + decisions + positioning + teamwork + stamina)/7
        car_blues = (technique + anticipation + composure + concentration + off_the_ball + vision + work_rate)/7
        car = position_score_calculator(car_greens, car_blues)

        final_car = round(car, 2)
        final_car = "{:.2f}".format(final_car)
        final_car = Decimal(final_car)

        MC_dict["  CAR"] = final_car

        # Mezzala Support
        mezs_greens = (passing + technique + decisions + off_the_ball + work_rate + acceleration)/6
        mezs_blues = (dribbling + first_touch + long_shots + tackling + anticipation + composure + vision + balance + stamina)/9
        mezs = position_score_calculator(mezs_greens, mezs_blues)

        final_mezs = round(mezs, 2)
        final_mezs = "{:.2f}".format(final_mezs)
        final_mezs = Decimal(final_mezs)

        MC_dict["MEZ-S"] = final_mezs

        # Mezzala Attack
        meza_greens = (dribbling + passing + technique + decisions + off_the_ball + vision + work_rate + acceleration)/8
        meza_blues = (finishing + first_touch + long_shots + anticipation + composure + flair + balance + stamina)/8
        meza = position_score_calculator(meza_greens, meza_blues)

        final_meza = round(meza, 2)
        final_meza = "{:.2f}".format(final_meza)
        final_meza = Decimal(final_meza)

        MC_dict["MEZ-A"] = final_meza

    # MR/L
        # Defensive Winger Defend
        dwd_greens = (technique + anticipation + off_the_ball + positioning + teamwork + work_rate + stamina)/7
        dwd_blues = (crossing + dribbling + first_touch + marking + tackling + aggression + concentration + decisions + acceleration)/9
        dwd = position_score_calculator(dwd_greens, dwd_blues)

        final_dwd = round(dwd, 2)
        final_dwd = "{:.2f}".format(final_dwd)
        final_dwd = Decimal(final_dwd)

        MRL_dict[" DW-D"] = final_dwd

        # Defensive Winger Support
        dws_greens = (crossing + technique + off_the_ball + teamwork + work_rate + stamina)/6
        dws_blues = (dribbling + first_touch + marking + passing + tackling + aggression + anticipation + composure + concentration + decisions + positioning \
            + acceleration)/12
        dws = position_score_calculator(dws_greens, dws_blues)

        final_dws = round(dws, 2)
        final_dws = "{:.2f}".format(final_dws)
        final_dws = Decimal(final_dws)

        MRL_dict[" DW-S"] = final_dws

        # Wide Playmaker Support
        wps_greens = (first_touch + passing + technique + composure + decisions + teamwork + vision)/7
        wps_blues = (dribbling + off_the_ball + agility)/3
        wps = position_score_calculator(wps_greens, wps_blues)

        final_wps = round(wps, 2)
        final_wps = "{:.2f}".format(final_wps)
        final_wps = Decimal(final_wps)

        MRL_dict[" WP-S"] = final_wps

        # Wide Playmaker Attack
        wpa_greens = (dribbling + first_touch + passing + technique + composure + decisions + off_the_ball + teamwork + vision)/9
        wpa_blues = (anticipation + flair + acceleration + agility)/4
        wpa = position_score_calculator(wpa_greens, wpa_blues)

        final_wpa = round(wpa, 2)
        final_wpa = "{:.2f}".format(final_wpa)
        final_wpa = Decimal(final_wpa)

        MRL_dict[" WP-A"] = final_wpa

        # Wide Midfielder Defend
        wmd_greens = (passing + tackling + concentration + decisions + positioning + teamwork + work_rate)/7
        wmd_blues = (crossing + first_touch + marking + technique + anticipation + composure + stamina)/7
        wmd = position_score_calculator(wmd_greens, wmd_blues)

        final_wmd = round(wmd, 2)
        final_wmd = "{:.2f}".format(final_wmd)
        final_wmd = Decimal(final_wmd)

        MRL_dict[" WM-D"] = final_wmd

        # Wide Midfielder Support
        wms_greens = (passing + tackling + decisions + teamwork + work_rate + stamina)/6
        wms_blues = (crossing + first_touch + technique + anticipation + composure + concentration + off_the_ball + positioning + vision)/9
        wms = position_score_calculator(wms_greens, wms_blues)

        final_wms = round(wms, 2)
        final_wms = "{:.2f}".format(final_wms)
        final_wms = Decimal(final_wms)

        MRL_dict[" WM-S"] = final_wms

        # Wide Midfielder Attack
        wma_greens = (crossing + first_touch + passing + decisions + teamwork + work_rate + stamina)/7
        wma_blues = (tackling + technique + anticipation + composure + off_the_ball + vision)/6
        wma = position_score_calculator(wma_greens, wma_blues)

        final_wma = round(wma, 2)
        final_wma = "{:.2f}".format(final_wma)
        final_wma = Decimal(final_wma)

        MRL_dict[" WM-A"] = final_wma

    # AMR/L
        # Winger Support
        ws_greens = (crossing + dribbling + technique + off_the_ball + acceleration + pace)/6
        ws_blues = (first_touch + passing + work_rate + agility + stamina)/5
        ws = position_score_calculator(ws_greens, ws_blues)

        final_ws = round(ws, 2)
        final_ws = "{:.2f}".format(final_ws)
        final_ws = Decimal(final_ws)

        MRL_dict["  W-S"] = final_ws
        AMRL_dict["  W-S"] = final_ws

        # Winger Attack
        wa_greens = (crossing + dribbling + technique + off_the_ball + acceleration + pace)/6
        wa_blues = (first_touch + passing + anticipation + flair + agility)/5
        wa = position_score_calculator(wa_greens, wa_blues)

        final_wa = round(wa, 2)
        final_wa = "{:.2f}".format(final_wa)
        final_wa = Decimal(final_wa)

        MRL_dict["  W-A"] = final_wa
        AMRL_dict["  W-A"] = final_wa

        # Inverted Winger Support
        iws_greens = (dribbling + passing + technique + off_the_ball + acceleration)/5
        iws_blues = (crossing + first_touch + long_shots + composure + decisions + vision + work_rate + agility + pace + stamina)/10
        iws = position_score_calculator(iws_greens, iws_blues)

        final_iws = round(iws, 2)
        final_iws = "{:.2f}".format(final_iws)
        final_iws = Decimal(final_iws)

        MRL_dict[" IW-S"] = final_iws
        AMRL_dict[" IW-S"] = final_iws

        # Inverted Winger Attack
        iwa_greens = (dribbling + passing + technique + off_the_ball + acceleration + agility)/6
        iwa_blues = (crossing + first_touch + long_shots + anticipation + composure + decisions + flair + vision +pace)/9
        iwa = position_score_calculator(iwa_greens, iwa_blues)

        final_iwa = round(iwa, 2)
        final_iwa = "{:.2f}".format(final_iwa)
        final_iwa = Decimal(final_iwa)

        MRL_dict[" IW-A"] = final_iwa
        AMRL_dict[" IW-A"] = final_iwa

        # Advanced Playmaker Support
        wide_aps_greens = (first_touch + passing + technique + composure + decisions + off_the_ball + teamwork + vision)/8
        wide_aps_blues = (dribbling + anticipation + flair+ agility)/4
        wide_aps = position_score_calculator(wide_aps_greens, wide_aps_blues)

        final_wide_aps = round(wide_aps, 2)
        final_wide_aps = "{:.2f}".format(final_wide_aps)
        final_wide_aps = Decimal(final_wide_aps)

        AMRL_dict[" AP-S"] = final_wide_aps

        # Advanced Playmaker Attack
        wide_apa_greens = (dribbling + first_touch + passing + technique + composure + decisions + off_the_ball + teamwork + vision)/9
        wide_apa_blues = (anticipation + flair + acceleration + agility)/4
        wide_apa = position_score_calculator(wide_apa_greens, wide_apa_blues)

        final_wide_apa = round(wide_apa, 2)
        final_wide_apa = "{:.2f}".format(final_wide_apa)
        final_wide_apa = Decimal(final_wide_apa)

        AMRL_dict[" AP-A"] = final_wide_apa

        # Inside Forward Support
        ifs_greens = (dribbling + first_touch + passing + technique + off_the_ball + acceleration + agility + balance)/8
        ifs_blues = (finishing + long_shots + anticipation + composure + flair + vision + pace)/7
        ifs = position_score_calculator(ifs_greens, ifs_blues)

        final_ifs = round(ifs, 2)
        final_ifs = "{:.2f}".format(final_ifs)
        final_ifs = Decimal(final_ifs)

        AMRL_dict[" IF-S"] = final_ifs

        # Inside Forward Attack
        ifa_greens = (dribbling + finishing + first_touch + technique + off_the_ball + acceleration + agility + balance)/8
        ifa_blues = (long_shots + passing + anticipation + composure + flair + pace)/6
        ifa = position_score_calculator(ifa_greens, ifa_blues)

        final_ifa = round(ifa, 2)
        final_ifa = "{:.2f}".format(final_ifa)
        final_ifa = Decimal(final_ifa)

        AMRL_dict[" IF-A"] = final_ifa

        # Wide Target Forward Support
        wtfs_greens = (heading + bravery + teamwork + jumping_reach + strength)/5
        wtfs_blues = (crossing + first_touch + anticipation + off_the_ball + work_rate + balance + stamina)/7
        wtfs = position_score_calculator(wtfs_greens, wtfs_blues)

        final_wtfs = round(wtfs, 2)
        final_wtfs = "{:.2f}".format(final_wtfs)
        final_wtfs = Decimal(final_wtfs)

        AMRL_dict["WTF-S"] = final_wtfs

        # Wide Target Forward Attack
        wtfa_greens = (heading + bravery + off_the_ball + jumping_reach + strength)/5
        wtfa_blues = (crossing + finishing + first_touch + anticipation + teamwork + work_rate + balance + stamina)/8
        wtfa = position_score_calculator(wtfa_greens, wtfa_blues)

        final_wtfa = round(wtfa, 2)
        final_wtfa = "{:.2f}".format(final_wtfa)
        final_wtfa = Decimal(final_wtfa)

        AMRL_dict["WTF-A"] = final_wtfa

        # Raumdeuter
        raum_greens = (finishing + anticipation + composure + concentration + decisions + off_the_ball + balance)/7
        raum_blues = (first_touch + technique + work_rate + acceleration + stamina)/5
        raum = position_score_calculator(raum_greens, raum_blues)

        final_raum = round(raum, 2)
        final_raum = "{:.2f}".format(final_raum)
        final_raum = Decimal(final_raum)

        AMRL_dict[" RAUM"] = final_raum

        # Trequartista
        treq_greens = (dribbling + first_touch + passing + technique + composure + decisions + flair + off_the_ball + vision + acceleration)/10
        treq_blues = (finishing + anticipation + agility + balance)/4
        treq = position_score_calculator(treq_greens, treq_blues)

        final_treq = round(treq, 2)
        final_treq = "{:.2f}".format(final_treq)
        final_treq = Decimal(final_treq)

        AMRL_dict[" TREQ"] = final_treq
        AM_dict[" TREQ"] = final_treq
        ST_dict[" TREQ"] = final_treq

    # AMC
        # Attacking Midfielder Support
        ams_greens = (first_touch + long_shots + passing + technique + anticipation + decisions + flair + off_the_ball)/8
        ams_blues = (dribbling + composure + vision + agility)/4
        ams = position_score_calculator(ams_greens, ams_blues)

        final_ams = round(ams, 2)
        final_ams = "{:.2f}".format(final_ams)
        final_ams = Decimal(final_ams)

        AM_dict[" AM-S"] = final_ams

        # Attacking Midfielder Attack
        ama_greens = (dribbling + first_touch + long_shots + passing + technique + anticipation + decisions + flair + off_the_ball)/9
        ama_blues = (finishing + composure + vision + agility)/4
        ama = position_score_calculator(ama_greens, ama_blues)

        final_ama = round(ama, 2)
        final_ama = "{:.2f}".format(final_ama)
        final_ama = Decimal(final_ama)

        AM_dict[" AM-A"] = final_ama

        # Shadow Striker
        ss_greens = (dribbling + finishing + first_touch + anticipation + composure + off_the_ball + acceleration)/7
        ss_blues = (passing + technique + concentration + decisions + work_rate + agility + balance + pace + stamina)/9
        ss = position_score_calculator(ss_greens, ss_blues)

        final_ss = round(ss, 2)
        final_ss = "{:.2f}".format(final_ss)
        final_ss = Decimal(final_ss)

        AM_dict["   SS"] = final_ss

        # Enganche
        eng_greens = (first_touch + passing + technique + composure + decisions + vision)/6
        eng_blues = (dribbling + anticipation + flair + off_the_ball + teamwork + agility)/6
        eng = position_score_calculator(eng_greens, eng_blues)

        final_eng = round(eng, 2)
        final_eng = "{:.2f}".format(final_eng)
        final_eng = Decimal(final_eng)

        AM_dict["  ENG"] = final_eng

    # ST
        # Advanced Forward
        af_greens = (dribbling + finishing + first_touch + technique + composure + off_the_ball + acceleration)/7
        af_blues = (passing + anticipation + decisions + work_rate + agility + balance + pace + stamina)/8
        af = position_score_calculator(af_greens, af_blues)

        final_af = round(af, 2)
        final_af = "{:.2f}".format(final_af)
        final_af = Decimal(final_af)

        ST_dict["   AF"] = final_af

        # Complete Forward Support
        cfs_greens = (dribbling + first_touch + heading + long_shots + passing + technique + anticipation + composure + decisions + off_the_ball + vision \
            + acceleration + agility + strength)/14
        cfs_blues = (finishing + teamwork + work_rate + balance + jumping_reach + pace + stamina)/7
        cfs = position_score_calculator(cfs_greens, cfs_blues)

        final_cfs = round(cfs, 2)
        final_cfs = "{:.2f}".format(final_cfs)
        final_cfs = Decimal(final_cfs)

        ST_dict[" CF-S"] = final_cfs

        # Complete Forward Attack
        cfa_greens = (dribbling + finishing + first_touch + heading + technique + anticipation + composure + off_the_ball + acceleration + agility + strength)/11
        cfa_blues = (long_shots + passing + decisions + teamwork + vision + work_rate + balance + jumping_reach + pace + stamina)/10
        cfa = position_score_calculator(cfa_greens, cfa_blues)

        final_cfa = round(cfa, 2)
        final_cfa = "{:.2f}".format(final_cfa)
        final_cfa = Decimal(final_cfa)

        ST_dict[" CF-A"] = final_cfa

        # Deep Lying Forward Support
        dlfs_greens = (first_touch + passing + technique + composure + decisions + off_the_ball + teamwork)/7
        dlfs_blues = (finishing + anticipation + flair + vision + balance + strength)/6
        dlfs = position_score_calculator(dlfs_greens, dlfs_blues)

        final_dlfs = round(dlfs, 2)
        final_dlfs = "{:.2f}".format(final_dlfs)
        final_dlfs = Decimal(final_dlfs)

        ST_dict["DLF-S"] = final_dlfs

        # Deep Lying Forward Attack
        dlfa_greens = (first_touch + passing + technique + composure + decisions + off_the_ball + teamwork)/7
        dlfa_blues = (dribbling + finishing + anticipation + flair + vision + balance + strength)/7
        dlfa = position_score_calculator(dlfa_greens, dlfa_blues)

        final_dlfa = round(dlfa, 2)
        final_dlfa = "{:.2f}".format(final_dlfa)
        final_dlfa = Decimal(final_dlfa)

        ST_dict["DLF-A"] = final_dlfa

        # Poacher Attack
        p_greens = (finishing + anticipation + composure + off_the_ball)/4
        p_blues = (first_touch + heading + technique + decisions + acceleration)/5
        p = position_score_calculator(p_greens, p_blues)

        final_p = round(p, 2)
        final_p = "{:.2f}".format(final_p)
        final_p = Decimal(final_p)

        ST_dict["    P"] = final_p

        # Pressing Forward Defend
        pfd_greens = (aggression + anticipation + bravery + decisions + teamwork + work_rate + acceleration + pace + stamina)/9
        pfd_blues = (first_touch + composure + concentration + agility + balance + strength)/6
        pfd = position_score_calculator(pfd_greens, pfd_blues)

        final_pfd = round(pfd, 2)
        final_pfd = "{:.2f}".format(final_pfd)
        final_pfd = Decimal(final_pfd)

        ST_dict[" PF-D"] = final_pfd

        # Pressing Forward Support
        pfs_greens = (aggression + anticipation + bravery + decisions + teamwork + work_rate + acceleration + pace + stamina)/9
        pfs_blues = (first_touch + passing + composure + concentration + off_the_ball + agility + balance + strength)/8
        pfs = position_score_calculator(pfs_greens, pfs_blues)

        final_pfs = round(pfs, 2)
        final_pfs = "{:.2f}".format(final_pfs)
        final_pfs = Decimal(final_pfs)

        ST_dict[" PF-S"] = final_pfs

        # Pressing Forward Attack
        pfa_greens = (aggression + anticipation + bravery + off_the_ball + teamwork + work_rate + acceleration + pace + stamina)/9
        pfa_blues = (finishing + first_touch + composure + concentration + decisions + agility + balance + strength)/8
        pfa = position_score_calculator(pfa_greens, pfa_blues)

        final_pfa = round(pfa, 2)
        final_pfa = "{:.2f}".format(final_pfa)
        final_pfa = Decimal(final_pfa)

        ST_dict[" PF-A"] = final_pfa

        # Target Forward Support
        tfs_greens = (heading + bravery + teamwork + balance + jumping_reach + strength)/6
        tfs_blues = (finishing + first_touch + aggression + anticipation + composure + decisions + off_the_ball)/7
        tfs = position_score_calculator(tfs_greens, tfs_blues)

        final_tfs = round(tfs, 2)
        final_tfs = "{:.2f}".format(final_tfs)
        final_tfs = Decimal(final_tfs)

        ST_dict[" TF-S"] = final_tfs

        # Target Forward Attack
        tfa_greens = (finishing + heading + bravery + composure + off_the_ball + balance + jumping_reach + strength)/8
        tfa_blues = (first_touch + aggression + anticipation + decisions + teamwork)/5
        tfa = position_score_calculator(tfa_greens, tfa_blues)

        final_tfa = round(tfa, 2)
        final_tfa = "{:.2f}".format(final_tfa)
        final_tfa = Decimal(final_tfa)

        ST_dict[" TF-A"] = final_tfa

        # False Nine
        f9_greens = (dribbling + first_touch + passing + technique + composure + decisions + off_the_ball + vision + acceleration + agility)/10
        f9_blues = (finishing + anticipation + flair + teamwork + balance)/5
        f9 = position_score_calculator(f9_greens, f9_blues)

        final_f9 = round(f9, 2)
        final_f9 = "{:.2f}".format(final_f9)
        final_f9 = Decimal(final_f9)

        ST_dict["   F9"] = final_f9

    # Player details
    team_name = prem_player[2]
    team_name = team_name + str(now)
    print()
    print("|",B, *prem_player[:5],prem_player[6],prem_player[7], W)
    print("|      DRL             DC            DM              MC             MRL           AM             AMRL            ST      |")
    horizontal_line = ("|________________________________________________________________________________________________________________________|")
    print(horizontal_line)
    with open(f'{team_name}.txt', 'a') as created_file:
        print(" ", file=created_file)
        print("|",B, *prem_player[:5],prem_player[6],prem_player[7], W, file=created_file)
        print("|      DRL             DC            DM              MC             MRL           AM             AMRL            ST      |",file=created_file)
        print(horizontal_line, file=created_file)
    # Sort the dicts from highest to lowest and assign the colour to the attribute average
    sorted_drl_dict = {}
    output_drl_dict = {}
    sorted_keys = reversed(sorted(DRL_dict, key=DRL_dict.get))
    for w in sorted_keys:
        sorted_drl_dict[w] = DRL_dict[w]
    for keys, value in sorted_drl_dict.items():
        coloured_value = output_colour(value)
        # Padding single digit values with a 0
        if len(str(value))<5:
            value = "0" + str(value)
            sorted_drl_dict[keys] = value
        final_colour =coloured_value+str(value)+W
        output_drl_dict[keys] = final_colour
    leftover = 14 - (len(list(output_drl_dict)))
    for p in range(leftover):
        output_drl_dict[f'    {p}'] = '     '
        sorted_drl_dict[f'    {p}'] = '     '
        p = p+1

    sorted_dc_dict = {}
    output_dc_dict = {}
    sorted_keys = reversed(sorted(DC_dict, key=DC_dict.get))
    for w in sorted_keys:
        sorted_dc_dict[w] = DC_dict[w]
    for keys, value in sorted_dc_dict.items():
        coloured_value = output_colour(value)
        if len(str(value))<5:
            value = "0" + str(value)
            sorted_dc_dict[keys] = value
        final_colour =coloured_value+str(value)+W
        output_dc_dict[keys] = final_colour
    dc_leftover = 14 - (len(list(output_dc_dict)))
    for p in range(dc_leftover):
        output_dc_dict[f'    {p}'] = '      '
        sorted_dc_dict[f'    {p}'] = '      '
        p = p+1

    sorted_dm_dict = {}
    output_dm_dict = {}
    sorted_keys = reversed(sorted(DM_dict, key=DM_dict.get))
    for w in sorted_keys:
        sorted_dm_dict[w] = DM_dict[w]
    for keys, value in sorted_dm_dict.items():
        coloured_value = output_colour(value)
        if len(str(value))<5:
            value = "0" + str(value)
            sorted_dm_dict[keys] = value
        final_colour =coloured_value+str(value)+W
        output_dm_dict[keys] = final_colour
    leftover = 14 - (len(list(output_dm_dict)))
    for p in range(leftover):
        output_dm_dict[f'    {p}'] = '     '
        sorted_dm_dict[f'    {p}'] = '     '
        p = p+1

    sorted_mc_dict = {}
    output_mc_dict = {}
    sorted_keys = reversed(sorted(MC_dict, key=MC_dict.get))
    for w in sorted_keys:
        sorted_mc_dict[w] = MC_dict[w]
    for keys, value in sorted_mc_dict.items():
        coloured_value = output_colour(value)
        if len(str(value))<5:
            value = "0" + str(value)
            sorted_mc_dict[keys] = value
        final_colour =coloured_value+str(value)+W
        output_mc_dict[keys] = final_colour
    leftover = 14 - (len(list(output_mc_dict)))
    for p in range(leftover):
        output_mc_dict[f'    {p}'] = '     '
        sorted_mc_dict[f'    {p}'] = '     '
        p = p+1

    sorted_mrl_dict = {}
    output_mrl_dict = {}
    sorted_keys = reversed(sorted(MRL_dict, key=MRL_dict.get))
    for w in sorted_keys:
        sorted_mrl_dict[w] = MRL_dict[w]
    for keys, value in sorted_mrl_dict.items():
        coloured_value = output_colour(value)
        if len(str(value))<5:
            value = "0" + str(value)
            sorted_mrl_dict[keys] = value
        final_colour =coloured_value+str(value)+W
        output_mrl_dict[keys] = final_colour
    leftover = 14 - (len(list(output_mrl_dict)))
    for p in range(leftover):
        output_mrl_dict[f'    {p}'] = '     '
        sorted_mrl_dict[f'    {p}'] = '     '
        p = p+1

    sorted_am_dict = {}
    output_am_dict = {}
    am_counter = 0
    sorted_keys = reversed(sorted(AM_dict, key=AM_dict.get))
    for w in sorted_keys:
        sorted_am_dict[w] = AM_dict[w]
    for keys, value in sorted_am_dict.items():
        coloured_value = output_colour(value)
        if len(str(value))<5:
            value = "0" + str(value)
            sorted_am_dict[keys] = value
        final_colour =coloured_value+str(value)+W
        output_am_dict[keys] = final_colour
        am_counter = am_counter + 1
    leftover = 14 - (len(list(output_am_dict)))
    for p in range(leftover):
        output_am_dict[f'    {p}'] = '     '
        sorted_am_dict[f'    {p}'] = '     '
        p = p+1

    sorted_amrl_dict = {}
    output_amrl_dict = {}
    sorted_keys = reversed(sorted(AMRL_dict, key=AMRL_dict.get))
    for w in sorted_keys:
        sorted_amrl_dict[w] = AMRL_dict[w]
    for keys, value in sorted_amrl_dict.items():
        coloured_value = output_colour(value)
        if len(str(value))<5:
            value = "0" + str(value)
            sorted_amrl_dict[keys] = value
        final_colour =coloured_value+str(value)+W 
        output_amrl_dict[keys] = final_colour
    leftover = 14 - (len(list(output_amrl_dict)))
    for p in range(leftover):
        output_amrl_dict[f'    {p}'] = '     '
        sorted_amrl_dict[f'    {p}'] = '     '
        p = p+1

    sorted_st_dict = {}
    output_st_dict = {}
    sorted_keys = reversed(sorted(ST_dict, key=ST_dict.get))
    for w in sorted_keys:
        sorted_st_dict[w] = ST_dict[w]
    for keys, value in sorted_st_dict.items():
        coloured_value = output_colour(value)
        if len(str(value))<5:
            value = "0" + str(value)
            sorted_st_dict[keys] = value
        final_colour =coloured_value+str(value)+W
        output_st_dict[keys] = final_colour
    leftover = 14 - (len(list(output_st_dict)))
    for p in range(leftover):
        output_st_dict[f'    {p}'] = '     '
        sorted_st_dict[f'    {p}'] = '     '
        p = p+1

    longest = get_longest_list([list(output_drl_dict), list(output_dc_dict), list(output_dm_dict), list(output_mc_dict), list(output_am_dict),list(output_amrl_dict),\
        list(output_st_dict), list(output_mrl_dict),])
    shortest = get_shortest_list([list(output_drl_dict), list(output_dc_dict), list(output_dm_dict), list(output_mc_dict), list(output_am_dict),list(output_amrl_dict),\
        list(output_st_dict), list(output_mrl_dict),])
    count = len(shortest)

    txt_string = ""
    # Printed Output
    for i in range(count):
        print("|",list(output_drl_dict.keys())[i] + ": " + list(output_drl_dict.values())[i],"|",list(output_dc_dict.keys())[i] + ": " + list(output_dc_dict.values())[i],"|", \
            list(output_dm_dict.keys())[i] + ": " + list(output_dm_dict.values())[i],"|", list(output_mc_dict.keys())[i] + ": " + list(output_mc_dict.values())[i],"|", \
            list(output_mrl_dict.keys())[i] + ": " + list(output_mrl_dict.values())[i],"|", list(output_am_dict.keys())[i] + ": " + list(output_am_dict.values())[i],"|", \
                list(output_amrl_dict.keys())[i] + ": " + list(output_amrl_dict.values())[i],"|", list(output_st_dict.keys())[i] + ": " + list(output_st_dict.values())[i],"|")
        with open(f'{team_name}.txt', 'a') as created_file:
                print("|",str(list(sorted_drl_dict.keys())[i]) + ": " + str(list(sorted_drl_dict.values())[i]),"|",str(list(sorted_dc_dict.keys())[i]) + ": " + str(list(sorted_dc_dict.values())[i]),"|", \
                    str(list(sorted_dm_dict.keys())[i]) + ": " + str(list(sorted_dm_dict.values())[i]),"|", str(list(sorted_mc_dict.keys())[i]) + ": " + str(list(sorted_mc_dict.values())[i]),"|", \
                    str(list(sorted_mrl_dict.keys())[i]) + ": " + str(list(sorted_mrl_dict.values())[i]),"|", str(list(sorted_am_dict.keys())[i]) + ": " + str(list(sorted_am_dict.values())[i]),"|", \
                        str(list(sorted_amrl_dict.keys())[i]) + ": " + str(list(sorted_amrl_dict.values())[i]),"|", str(list(sorted_st_dict.keys())[i]) + ": " + str(list(sorted_st_dict.values())[i]),"|", file=created_file)
    print(horizontal_line)

if __name__ == "__main__":
    calculate_best_position(uid, filename)
    print()