    
standard_categories = {
    "Standard Batting": ["AB", "AVG", "2B", "XBH", "G", "GSH", "GIDP", "GO/AO", "HBP", "H", "HR", "IBB", 
                         "LOB", "OBP", "OPS", "PA", "ROE", "R", "RBI", "SH", "SF", "1B", "SLG", "TB", "3B", 
                         "BB", "WO"],
    "Standard Baserunning": ["CS", "SB", "SB%"],
    "Standard Pitching": ["App", "BK", "BF", "BS", "CG", "ER", "ERA", "FO", "GF", "GS", "GO", "HLD", "IR", 
                          "IP", "L", "NP", "PK", "QS", "RW", "SV", "SVO", "SV%", "SHO", "SO", "UER", "WHIP", 
                          "WP", "W", "WPCT"],
    "Standard Fielding": ["A", "CS%", "DP", "E", "FPCT", "INN", "O", "OFA", "PB", "PO", "TC", "TP"],
    "Standard Misc": ["Rate Stats Qualifiers"],
    "Standard Team": ["DIFF"]
}

advanced_categories = {
    "General Stats": ["WAR", "bWAR", "fWAR", "wOBA"],
    "Batting Stats": ["Oppo%", "O-Swing%", "LA", "HR-DIS", "Fast-swing Rate", "Contact%", "OBP", "SLG", 
                      "OPS", "OPS+", "ISO", "BABIP", "xBA", "Barrel", "Barrel%", "Blasts", "Hard-hit Rate",
                      "Sweet Spot", "EV", "LiPS", "Swing Length", "P/PA", "PA/SO", "Pull%", "RC", "wRAA",
                      "wRC+", "xSLG"],
    "Pitching Stats": ["K-BB%", "K%", "IR-A", "H/9", "HR/9", "GB/FB", "Game Score", "ERA+", "BB/9", "ERA", 
                       "xERA", "FIP", "xFIP", "FIP-", "CERA", "HR/FB", "K/BB", "K/9", "BB%", "CSW%", "VELO", 
                       "SIERA", "tERA", "MB/9", "Spin Rate", "Pitch Tempo", "Pitch Movement", 
                       "LiPS", "P/GS", "P/IP", "Putaway %", "RA9", "SwStr%"],
    "Fielding Stats": ["OAA", "FRAA", "DER", "Def", "CFR", "UZR", "DRS", "Catch Probability", "ARM", 
                       "Throwing Value", "Jump", "DCOV", "FRV", "Catcher Framing", "POP", "RAA", "RF",
                       "Shifts"],
    "Baserunning Stats": ["BsR", "Spd", "90-foot Running Splits", "SS", "LEAD", "Home to First", "Bolt"],
    "Situational Stats": ["WPA", "RE24", "LI", "BQR", "BQR-S", "LOB%", "RS/9"],
    "Batted Ball Stats": ["LD%", "GB%", "FB%", "PO%", "BBE", "Blast", "DST"],
    "Team/Context Stats": ["Ballpark Factor", "Pythagorean Winning %", "Magic Number", "Surplus Value", "WE"],
    "Advanced/Experimental Stats": ["Swords", "Active Spin", "Squared-up Rate", "PV", "EXT"]
}