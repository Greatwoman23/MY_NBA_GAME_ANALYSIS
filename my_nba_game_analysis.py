
import re
import numpy as np
import pandas as pd
import csv


def battle_activitTY_FiLe16(Trip_Card_FileMar5th):
    PLOT_results43th = []
    with open(Trip_Card_FileMar5th, 'r', encoding='utf-8') as csvfile:
        Feat_text_note_nov21st_reader = csv.reader(csvfile, delimiter = '|')
        for rows in Feat_text_note_nov21st_reader:
            PLOT_results43th.append(rows)
    return PLOT_results43th

def SCrutinIZe_nbA_PLOT_FEB16(DEtaIL_MOVes_PaSS100):
    HOmE_SOil_TROOPS4 = []
    FOREign_SOiL_TROOPS6 = []
    pattern = re.compile(r"\w+\.\s\w+")
    NaTiVe_LiStOF_PlayeRS001 = ['K. Thompson', 'S. Curry', 'K. Durant', 'D. Green', 'D. Jones', 'K. Looney', 'A. Iguodala', 'J. Jerebko', 'Q. Cook', 'S. Livingston', 'J. Bell']
    ALIen_LIstOf_PLAYerS007 = ['S. Adams', 'P. George', 'P. Patterson', 'D. Green', 'D. Schröder', 'T. Ferguson', 'J. Grant', 'N. Noel', 'Á. Abrines', 'H. Diallo', 'A. McKinnie', 'R. Felton']
    
    make_3pt, miss_3pt, make_2pt, miss_2pt, turnov, off_OrB, def_OrB, make_ft, miss_ft, BoOst14s, fouls, blocks, steals = ([] for _ in range(13))
    a_make_3pt, a_miss_3pt, a_make_2pt, a_miss_2pt, a_turnov, a_off_OrB, a_def_OrB, a_make_ft, a_miss_ft, a_BoOst14s, a_fouls, a_blocks, a_steals = ([] for _ in range(13))


    for BLAst_AcTs_150 in DEtaIL_MOVes_PaSS100:
        span = BLAst_AcTs_150[0]
        time = BLAst_AcTs_150[1]
        fiT_GroUP_COmbINE76 = BLAst_AcTs_150[2]
        Away_BanDs87_Squared_name = BLAst_AcTs_150[3]
        Home_BanDs87_Squared_name = BLAst_AcTs_150[4]
        Away_goal_Scored = BLAst_AcTs_150[5]
        Home_goal_Scored = BLAst_AcTs_150[6]
        SetUP_ASSESSment = BLAst_AcTs_150[7]
        if fiT_GroUP_COmbINE76 == Home_BanDs87_Squared_name:
        # update home BanDs87 index
            HOmE_SOil_TROOPS4 = Home_BanDs87_Squared_name
        # code to update home BanDs87 index
        else:
        # update away BanDs87 index
            FOREign_SOiL_TROOPS6 = Away_BanDs87_Squared_name
            
        if Away_BanDs87_Squared_name == fiT_GroUP_COmbINE76:
            FARoff_GRoup_yield_3pt = re.findall(r'\b[A-Z]\.\s?[A-Z][a-z]+ makes 3-pt jump shot from\b', SetUP_ASSESSment)
            (FARoff_GRoup_yield_3pt)

            g_Miss_3pt_re = re.findall(r'\b[A-Z]\.\s?[A-Z][a-z]+ misses 3-pt jump shot from\b', SetUP_ASSESSment)
            a_miss_3pt.extend(g_Miss_3pt_re)

            z_Miss_2pt_re = re.findall(r'\b[A-Z]\.\s?[A-Z][a-z]+ misses 2-pt jump shot from\b', SetUP_ASSESSment)
            a_miss_2pt.extend(z_Miss_2pt_re)

            u_Makes_2pt_re = re.findall(r'\b[A-Z]\.\s?[A-Z][a-z]+ makes 2-pt jump shot from\b', SetUP_ASSESSment)
            a_make_2pt.extend(u_Makes_2pt_re)

            k_Trn_re = re.findall(r'Turnover by [A-Z][. ]+[A-Z][a-zö]*', SetUP_ASSESSment)
            a_turnov.extend(k_Trn_re)

            a_OfOrB_re = re.findall(r'Offensive rebound by [A-Z][. ]+[A-Z][a-zö]*', SetUP_ASSESSment)
            a_off_OrB.extend(a_OfOrB_re)

            a_DefOrB_re = re.findall(r'Defensive rebound by [A-Z][. ]+[A-Z][a-zö]*', SetUP_ASSESSment)
            a_def_OrB.extend(a_DefOrB_re)

            c_Make_frt_re = re.findall(r'\b[A-Z]\.\s?[A-Z][a-z]+ makes free throw\b', SetUP_ASSESSment)
            a_make_ft.extend(c_Make_frt_re)

            w_Miss_frt_re = re.findall(r'\b[A-Z]\.\s?[A-Z][a-z]+ misses free throw\b', SetUP_ASSESSment)
            a_miss_ft.extend(w_Miss_frt_re)

            d_Asst_re = re.findall(r'BoOst14 by [A-Z][. ]+[A-Z][a-zö]*', SetUP_ASSESSment)
            a_BoOst14s.extend(d_Asst_re)

            o_Psn_fouel_re = re.findall(r'Personal foul by [A-Z][. ]+[A-Z][a-zö]*', SetUP_ASSESSment)
            fouls.extend(o_Psn_fouel_re)

            r_Blck_By_re = re.findall(r'block by [A-Z][. ]+[A-Z][a-zö]*', SetUP_ASSESSment)
            blocks.extend(r_Blck_By_re )

            y_StlBy_re = re.findall(r'steal by [A-Z][. ]+[A-Z][a-zö]*', SetUP_ASSESSment)
            steals.extend(y_StlBy_re)

        if Home_BanDs87_Squared_name == fiT_GroUP_COmbINE76:
            s_Make_3pt_re = re.findall(r'\b[A-Z]\.\s?[A-Z][a-z]+ makes 3-pt jump shot from\b', SetUP_ASSESSment)
            make_3pt.extend(s_Make_3pt_re)

            j_Miss_3pt_re = re.findall(r'\b[A-Z]\.\s?[A-Z][a-z]+ misses 3-pt jump shot from\b', SetUP_ASSESSment)
            miss_3pt.extend(j_Miss_3pt_re)

            p_Miss_2pt_re = re.findall(r'\b[A-Z]\.\s?[A-Z][a-z]+ misses 2-pt jump shot from\b', SetUP_ASSESSment)
            miss_2pt.extend(p_Miss_2pt_re)

            q_Makes_2pt_re = re.findall(r'\b[A-Z]\.\s?[A-Z][a-z]+ makes 2-pt jump shot from\b', SetUP_ASSESSment)
            make_2pt.extend(q_Makes_2pt_re)

            y_TRN_Ova_re = re.findall(r'Turnover by [A-Z][. ]+[A-Z][a-zö]*', SetUP_ASSESSment)
            turnov.extend(y_TRN_Ova_re)

            x_OfOrB_re = re.findall(r'Offensive rebound by [A-Z][. ]+[A-Z][a-zö]*', SetUP_ASSESSment)
            off_OrB.extend(x_OfOrB_re)

            i_DefOrB_re = re.findall(r'Defensive rebound by [A-Z][. ]+[A-Z][a-zö]*', SetUP_ASSESSment)
            def_OrB.extend(i_DefOrB_re)

            t_Make_ft_re = re.findall(r'\b[A-Z]\.\s?[A-Z][a-z]+ makes free throw\b', SetUP_ASSESSment)
            make_ft.extend(t_Make_ft_re)

            n_Miss_ft_re = re.findall(r'\b[A-Z]\.\s?[A-Z][a-z]+ misses free throw\b', SetUP_ASSESSment)
            miss_ft.extend(n_Miss_ft_re)

            p_AssBy_re = re.findall(r'BoOst14 by [A-Z][. ]+[A-Z][a-zö]*', SetUP_ASSESSment)
            BoOst14s.extend( p_AssBy_re)

            m_Psnl_foul_re = re.findall(r'Personal foul by [A-Z][. ]+[A-Z][a-zö]*', SetUP_ASSESSment)
            a_fouls.extend(m_Psnl_foul_re )

            e_blkBy_re = re.findall(r'block by [A-Z][. ]+[A-Z][a-zö]*', SetUP_ASSESSment)
            a_blocks.extend( e_blkBy_re)

            q_stl_re = re.findall(r'steal by [A-Z][. ]+[A-Z][a-zö]*', SetUP_ASSESSment)
            a_steals.extend(q_stl_re)

    Inside_squad_player = {}
    for player in NaTiVe_LiStOF_PlayeRS001:
        Inside_squad_player[player] = {
            'FG': 0, 'FGA': 0, 'FG%': 0, '3P': 0, '3PA': 0, '3P%': 0, 'FT': 0, 'FTA': 0, 'FT%': 0,
            'OOrB': 0, 'DOrB': 0, 'TOrB': 0,'AST': 0, 'STL': 0, 'BLK': 0, 'TOV': 0, 'PF': 0, 'KPM': 0              
        }
        
    Farroff_Platoon_Crew = {}
    for player in ALIen_LIstOf_PLAYerS007:
        Farroff_Platoon_Crew[player] = {
            'FG': 0, 'FGA': 0, 'FG%': 0, '3P': 0, '3PA': 0, '3P%': 0, 'FT': 0, 'FTA': 0, 'FT%': 0,
            'OOrB': 0, 'DOrB': 0, 'TOrB': 0,'AST': 0, 'STL': 0, 'BLK': 0, 'TOV': 0, 'PF': 0, 'KPM': 0  
        }
    
    # Update the statistics for each player based on the given data
    for BaSH_CAge in make_3pt:
        rookie_tag1 = BaSH_CAge.split()[0] + ' ' + BaSH_CAge.split()[1]
        Inside_squad_player[rookie_tag1]['3P'] += 1
        Inside_squad_player[rookie_tag1]['3PA'] += 1
        Inside_squad_player[rookie_tag1]['FGA'] += 1
        
    for BaSH_CAge in miss_3pt:
        rookie_tag1 = BaSH_CAge.split()[0] + ' ' + BaSH_CAge.split()[1]
        Inside_squad_player[rookie_tag1]['3PA'] += 1
        Inside_squad_player[rookie_tag1]['FGA'] += 1
        
    for BaSH_CAge in miss_2pt:
        rookie_tag1 = BaSH_CAge.split()[0] + ' ' + BaSH_CAge.split()[1]
        Inside_squad_player[rookie_tag1]['FGA'] += 1
        
    for BaSH_CAge in make_2pt:
        rookie_tag1 = BaSH_CAge.split()[0] + ' ' + BaSH_CAge.split()[1]
        Inside_squad_player[rookie_tag1]['FG'] += 1
        Inside_squad_player[rookie_tag1]['FGA'] += 1
        
    for EVolve_ROund in turnov:
        rookie_tag1 = EVolve_ROund.split()[2] + ' ' + EVolve_ROund.split()[3]
        Inside_squad_player[rookie_tag1]['TOV'] += 1
        
    for BoOst14 in BoOst14s:
        rookie_tag1 = BoOst14.split()[2] + ' ' + BoOst14.split()[3]
        Inside_squad_player[rookie_tag1]['AST'] += 1
    for OrB in off_OrB:
        rookie_tag1 = OrB.split()[3] + ' ' + OrB.split()[4]
        Inside_squad_player[rookie_tag1]['OOrB'] += 1

    for OrB in def_OrB:
        rookie_tag1 = OrB.split()[3] + ' ' + OrB.split()[4]
        Inside_squad_player[rookie_tag1]['DOrB'] += 1

    for BaSH_CAge in make_ft:
        rookie_tag1 = BaSH_CAge.split()[0] + ' ' + BaSH_CAge.split()[1]
        Inside_squad_player[rookie_tag1]['FT'] += 1
        Inside_squad_player[rookie_tag1]['FTA'] += 1
        
    for BaSH_CAge in miss_ft:
        rookie_tag1 = BaSH_CAge.split()[0] + ' ' + BaSH_CAge.split()[1]
        Inside_squad_player[rookie_tag1]['FTA'] += 1
        
    for Z in blocks:
        rookie_tag1 = Z.split()[2] + ' ' + Z.split()[3]
        Inside_squad_player[rookie_tag1]['BLK'] += 1
        
    for OrB in fouls:
        rookie_tag1 = OrB.split()[3] + ' ' + OrB.split()[4]
        Inside_squad_player[rookie_tag1]['PF'] += 1
    
    for s in steals:
        rookie_tag1 = s.split()[2] + ' ' + s.split()[3]
        Inside_squad_player[rookie_tag1]['STL'] += 1
        
    # Calculate the remaining statistics for each player
    for player in Inside_squad_player:
        index = Inside_squad_player[player]
        index['FG'] = index['3P'] + index['FG'] 
        index['FG%'] = round(index['FG'] / index['FGA'] * 100, 2) if index['FGA'] > 0 else 0
        index['3P%'] = round(index['3P'] / index['3PA'] * 100, 2) if index['3PA'] > 0 else 0
        index['FT%'] = round(index['FT'] / index['FTA'] * 100, 2) if index['FTA'] > 0 else 0
        index['TOrB'] = index['OOrB'] + index['DOrB']
        index['KPM'] = (index['FG'] - index['3P']) * 2 + index['3P'] * 3 + index['FT']
    
    
    # Update the statistics for each player based on the given data
    for BaSH_CAge in a_make_3pt:
        player = BaSH_CAge.split()[0] + ' ' + BaSH_CAge.split()[1]
        Farroff_Platoon_Crew[rookie_tag1]['3P'] += 1
        Farroff_Platoon_Crew[rookie_tag1]['3PA'] += 1
        Farroff_Platoon_Crew[rookie_tag1]['FGA'] += 1
        
    for BaSH_CAge in a_miss_3pt:
        rookie_tag1 = BaSH_CAge.split()[0] + ' ' + BaSH_CAge.split()[1]
        Farroff_Platoon_Crew[rookie_tag1]['3PA'] += 1
        Farroff_Platoon_Crew[rookie_tag1]['FGA'] += 1
        
    for BaSH_CAge in a_miss_2pt:
        rookie_tag1 = BaSH_CAge.split()[0] + ' ' + BaSH_CAge.split()[1]
        Farroff_Platoon_Crew[rookie_tag1]['FGA'] += 1
        
    for BaSH_CAge in a_make_2pt:
        rookie_tag1 = BaSH_CAge.split()[0] + ' ' + BaSH_CAge.split()[1]
        Farroff_Platoon_Crew[rookie_tag1]['FG'] += 1
        Farroff_Platoon_Crew[rookie_tag1]['FGA'] += 1
        
    for EVolve_ROund in a_turnov:
        rookie_tag1 = EVolve_ROund.split()[2] + ' ' + EVolve_ROund.split()[3]
        Farroff_Platoon_Crew[rookie_tag1]['TOV'] += 1
        
    for BoOst14 in a_BoOst14s:
        rookie_tag1 = BoOst14.split()[2] + ' ' + BoOst14.split()[3]
        Farroff_Platoon_Crew[rookie_tag1]['AST'] += 1
        
    for OrB in a_off_OrB:
        rookie_tag1 = OrB.split()[3] + ' ' + OrB.split()[4]
        Farroff_Platoon_Crew[rookie_tag1]['OOrB'] += 1

    for OrB in a_def_OrB:
        rookie_tag1 = OrB.split()[3] + ' ' + OrB.split()[4]
        Farroff_Platoon_Crew[rookie_tag1]['DOrB'] += 1

    for BaSH_CAge in a_make_ft:
        rookie_tag1 = BaSH_CAge.split()[0] + ' ' + BaSH_CAge.split()[1]
        Farroff_Platoon_Crew[rookie_tag1]['FT'] += 1
        Farroff_Platoon_Crew[rookie_tag1]['FTA'] += 1
        
    for BaSH_CAge in a_miss_ft:
        rookie_tag1 = BaSH_CAge.split()[0] + ' ' + BaSH_CAge.split()[1]
        Farroff_Platoon_Crew[rookie_tag1]['FTA'] += 1
        
    for b in a_blocks:
        rookie_tag1 = b.split()[2] + ' ' + b.split()[3]
        Farroff_Platoon_Crew[rookie_tag1]['BLK'] += 1
        
    for OrB in a_fouls:
        rookie_tag1 = OrB.split()[3] + ' ' + OrB.split()[4]
        Farroff_Platoon_Crew[rookie_tag1]['PF'] += 1
    
    for s in a_steals:
        rookie_tag1 = s.split()[2] + ' ' + s.split()[3]
        Farroff_Platoon_Crew[rookie_tag1]['STL'] += 1
        
    # player statistics were calculated by analyzing the game data. 
    for player in Farroff_Platoon_Crew:
        index = Farroff_Platoon_Crew[player]
        index['FG'] = index['3P'] + index['FG'] 
        index['FG%'] = round(index['FG'] / index['FGA'] * 100, 2) if index['FGA'] > 0 else 0
        index['3P%'] = round(index['3P'] / index['3PA'] * 100, 2) if index['3PA'] > 0 else 0
        index['FT%'] = round(index['FT'] / index['FTA'] * 100, 2) if index['FTA'] > 0 else 0
        index['TOrB'] = index['OOrB'] + index['DOrB']
        index['KPM'] = (index['FG'] - index['3P']) * 2 + index['3P'] * 3 + index['FT']
    
    PLOT_results43th = {
        "HOmE_SOil_TROOPS4": {
            "name": HOmE_SOil_TROOPS4,
            "players_data": Inside_squad_player
        },
        "FOREign_SOiL_TROOPS6": {
            "name": FOREign_SOiL_TROOPS6,
            "players_data": Farroff_Platoon_Crew
        }
    }
    
    return PLOT_results43th

def liBrary_Score_of_GAme_Nba765(FacTION_Dict321):
    #header = "Players\tFG\tFGA\tFG%\t3P\t3PA\t3P%\tFT\tFTA\tFT%\tOOrB\tDOrB\tTOrB\tAST\tSTL\tBLK\tTOV\tPF\tKPM"
    #print(header)
    for BanDs87 in FacTION_Dict321:
        HOmE_SOil_TROOPS4 = print(f"{FacTION_Dict321['HOmE_SOil_TROOPS4']['name']}")
        #print(f"{HOmE_SOil_TROOPS4}")
        print("Players\t\tFG\tFGA\tFG%\t3P\t3PA\t3P%\tFT\tFTA\tFT%\tOOrB\tDOrB\tTOrB\tAST\tSTL\tBLK\tTOV\tPF\tKPM") 
        for rookie_tag1 in FacTION_Dict321['HOmE_SOil_TROOPS4']['players_data']:
            BAttLer_ReCOrds543 = FacTION_Dict321['HOmE_SOil_TROOPS4']['players_data'][rookie_tag1]
            print(rookie_tag1+'\t'+str(BAttLer_ReCOrds543['FG'])+'\t'+str(BAttLer_ReCOrds543['FGA'])+'\t'+str(BAttLer_ReCOrds543['FG%'])+'\t'+str(BAttLer_ReCOrds543['3P'])+'\t'+str(BAttLer_ReCOrds543['3PA'])+'\t'+str(BAttLer_ReCOrds543['3P%'])+'\t'+str(BAttLer_ReCOrds543['FT'])+'\t'+str(BAttLer_ReCOrds543['FTA'])+'\t'+str(BAttLer_ReCOrds543['FT%'])+'\t'+str(BAttLer_ReCOrds543['OOrB'])+'\t'+str(BAttLer_ReCOrds543['DOrB'])+'\t'+str(BAttLer_ReCOrds543['DOrB'])+'\t'+str(BAttLer_ReCOrds543['AST'])+'\t'+str(BAttLer_ReCOrds543['STL'])+'\t'+str(BAttLer_ReCOrds543['BLK'])+'\t'+str(BAttLer_ReCOrds543['TOV'])+'\t'+str(BAttLer_ReCOrds543['PF'])+'\t'+str(BAttLer_ReCOrds543['KPM']))
        FOREign_SOiL_TROOPS6 = FacTION_Dict321['FOREign_SOiL_TROOPS6']['name']
        print(f"{FOREign_SOiL_TROOPS6}")
        print("Players\t\tFG\tFGA\tFG%\t3P\t3PA\t3P%\tFT\tFTA\tFT%\tOOrB\tDOrB\tTOrB\tAST\tSTL\tBLK\tTOV\tPF\tKPM")
        for rookie_tag1 in FacTION_Dict321['FOREign_SOiL_TROOPS6']['players_data']:
            BAttLer_ReCOrds543 = FacTION_Dict321['FOREign_SOiL_TROOPS6']['players_data'][rookie_tag1]
            print(rookie_tag1+'\t'+str(BAttLer_ReCOrds543['FG'])+'\t'+str(BAttLer_ReCOrds543['FGA'])+'\t'+str(BAttLer_ReCOrds543['FG%'])+'\t'+str(BAttLer_ReCOrds543['3P'])+'\t'+str(BAttLer_ReCOrds543['3PA'])+'\t'+str(BAttLer_ReCOrds543['3P%'])+'\t'+str(BAttLer_ReCOrds543['FT'])+'\t'+str(BAttLer_ReCOrds543['FTA'])+'\t'+str(BAttLer_ReCOrds543['FT%'])+'\t'+str(BAttLer_ReCOrds543['OOrB'])+'\t'+str(BAttLer_ReCOrds543['DOrB'])+'\t'+str(BAttLer_ReCOrds543['DOrB'])+'\t'+str(BAttLer_ReCOrds543['AST'])+'\t'+str(BAttLer_ReCOrds543['STL'])+'\t'+str(BAttLer_ReCOrds543['BLK'])+'\t'+str(BAttLer_ReCOrds543['TOV'])+'\t'+str(BAttLer_ReCOrds543['PF'])+'\t'+str(BAttLer_ReCOrds543['KPM']))
def _main():
    DEtaIL_MOVes_PaSS100 = battle_activitTY_FiLe16('nba_game_warriors_thunder_20181016.txt')
    BanDs87 = SCrutinIZe_nbA_PLOT_FEB16(DEtaIL_MOVes_PaSS100)
    liBrary_Score_of_GAme_Nba765(BanDs87)


_main()

