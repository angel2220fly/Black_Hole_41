        def Count_adds(En, Row1, Row):

            Row += 1

            if Row == (8192 * 4) - 1:
                Row = 0

            if En == (8192 * 4) - 1:
                En = 255
            En += 1

            return En, Row1, Row
