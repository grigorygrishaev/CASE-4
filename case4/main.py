# Case-study #4
# Developers:   Grishaev G. (35%),
#               Abrarova V. (45%),
#               Zlobinskaya L. (40%)

# Importing modules we need and giving names to columns of table.

import urllib.request
from prettytable import PrettyTable

with open('input.txt') as f_inp:
    with open('output.txt', 'w') as f_out:
        FIO = 'Name, Surname       '
        FIO.ljust(20)
        COMP_1 = 'COMP   '
        COMP_1.ljust(7)
        ATT_1 = 'ATT    '
        ATT_1.ljust(7)
        YDS_1 = 'YDS    '
        YDS_1.ljust(7)
        TD_1 = 'TD     '
        TD_1.ljust(7)
        INT_1 = 'INT    '
        INT_1.ljust(7)
        PR_1 = 'PR     '
        PR_1.ljust(7)
        columns = [FIO, COMP_1, ATT_1, YDS_1, TD_1, INT_1, PR_1]
        summ = 7
        indicator = []

        # Finding names of players.

        for line in f_inp:
            url = line
            f = urllib.request.urlopen(url)
            s = f.read()
            text = str(s)
            part_name = text.find("nfl-c-player-header__title")
            name = text[text.find('>', part_name) + 1:text.find('</h1', part_name)]
            name.ljust(20)
            indicator.append(name)

            # COMP, ATT, YDS, TD, INT и  PR (passer rating)
            # Finding Total COMP.

            part_COMP = text.find('passingCompletions')
            COMP = text[text.find('>', part_COMP) + 1:text.find('</th>', part_COMP)]
            COMP = COMP.replace(' ', '')[2:-2]
            COMP.ljust(7)
            indicator.append(COMP)

            # Finding Total ATT.

            part_ATT = text.find('passingAttempts')
            ATT = text[text.find('>', part_ATT) + 1:text.find('</th>', part_ATT)]
            ATT = ATT.replace(' ', '')[2:-2]
            ATT.ljust(7)
            indicator.append(ATT)

            # Finding Total YDS.

            part_YDS = text.find('passingYards')
            YDS = text[text.find('>', part_YDS) + 1:text.find('</th>', part_YDS)]
            YDS = YDS.replace(' ', '')[2:-2]
            YDS.ljust(7)
            indicator.append(YDS)

            # Finding Total TD.

            part_TD = text.find('passingTouchdowns')
            TD = text[text.find('>', part_TD) + 1:text.find('</th>', part_TD)]
            TD = TD.replace(' ', '')[2:-2]
            TD.ljust(7)
            indicator.append(TD)

            # Finding Total INT.

            part_INT = text.find('passingInterceptions')
            INT = text[text.find('>', part_INT) + 1:text.find('</th>', part_INT)]
            INT = INT.replace(' ', '')[2:-2]
            INT.ljust(7)
            indicator.append(INT)

            # Finding Total PR (passer rating).

            part_PR = text.find('passingPasserRating')
            PR = text[text.find('>', part_PR) + 1:text.find('</th>', part_PR)]
            PR = PR.replace(' ', '')[2:-2]

            # Making 2 symbols after comma for last culumn.

            a = PR.find('.')
            l2 = len(PR[a + 1:])
            l1 = len(PR[:a + 1])
            l = l1 + l2
            if l2 > 2:
                PR = PR[:l1 + 3]
            elif l2 < 2:
                PR = PR + '0'
            elif l2 == 2:
                PR = PR
            PR.ljust(7)
            indicator.append(PR)

        # Print of table with taken from html files information.

        table = PrettyTable(columns)
        indicator_data = indicator[:]
        while indicator_data:
            table.add_row(indicator_data[:summ])
            indicator_data = indicator_data[summ:]
        table.align = "l"
        print(table, file=f_out)