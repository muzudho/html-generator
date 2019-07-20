import pandas as pd
from attribute.query_id_sorted_table import query_id_sorted_table

#
# Note.
#
# Root directory: Visual studio code workspace root.
#

# Output.
output_css = "./html-generator/auto-generated/participants.css"

# Floor map: Csv -> Data frame. (Not record set)
fl_df = pd.read_csv("./html-generator/data/floor-map.csv",
                    sep=',', engine='python')
# print(fl_df.values.tolist())
"""
ID,X,Y,BLOCK
27,0,0,C
26,1,0,C
25,2,0,C
"""


# Participants
pa_df = query_id_sorted_table("./html-generator/data/participant.csv")
"""
ID,GENRE_CODE
1,Red
2,Red
3,Blue

print(pa_df.values.tolist())
[[30, 'Blue'], [6, 'Blue'], [56, 'Blue'], [50, 'Blue'], [40, 'Blue'], [33, 'Blue'], [27, 'Blue'], [22, 'Blue'], [17, 'Blue'], [15, 'Blue'], [8, 'Blue'], [4, 'Blue'], [3, 'Blue'], [60, 'Blue'], [5, 'Green'], [10, 'Green'], [14, 'Green'], [9, 'Green'], [29, 'Green'], [36, 'Green'], [42, 'Green'], [44, 'Green'], [53, 'Green'], [57, 'Green'], [16, 'Yellow'], [20, 'Yellow'], [26, 'Yellow'], [31, 'Yellow'], [43, 'Yellow'], [51, 'Yellow'], [58, 'Yellow'], [18, 'Yellow'], [1, 'Red'], [7, 'Red'], [2, 'Red'], [52, 'Red'], [41, 'Red'], [37, 'Red'], [21, 'Red'], [12, 'Red'], [59, 'White'], [48, 'White'], [39, 'White'], [25, 'White'], [54, 'Orange'], [46, 'Black'], [24, 'Black'], [23, 'Black'], [32, 'Orange'], [38, 'Orange'], [35, 'Gray'], [49, 'Gray'], [13, 'Violet'], [34, 'Pink'], [28, 'Pink'], [55, 'Violet'], [19, 'SkyBlue'], [11, 'Purple'], [45, 'YellowGreen'], [47, 'Brown']]
"""

# Mappings
ma_df = pd.read_csv("./html-generator/data/mappings.csv",
                    sep=',', engine='python')
"""
ID,GENRE_CODE
1,Red
2,Red
3,Blue
"""

# Join1
new_df = pa_df.merge(ma_df, left_on='ID', right_on='PARTICIPANT')
# print(new_df.head(50))
"""
    ID GENRE_CODE  PARTICIPANT  TABLE
0   30       Blue           30     30
1    6       Blue            6      6
2   56       Blue           56     56
"""

# Join2
new2_df = new_df.merge(fl_df, left_on='TABLE', right_on='ID')
# print(new2_df.head(50))
"""
    ID_x GENRE_CODE  PARTICIPANT  TABLE  ID_y   X  Y BLOCK
0     30       Blue           30     30    30   0  3     C
1      6       Blue            6      6     6  18  5     A
2     56       Blue           56     56    56   3  2     F
"""


def write():
    try:
        file = open(output_css, 'w', encoding='utf-8')
        file.write(
            """
{}
            """.format(get_boxes())
        )
    except Exception as e:
        print(e)
    finally:
        file.close()


def get_boxes():
    html = []
    for _index, new2_row in new2_df.iterrows():

        # Participant id.
        id = new2_row["PARTICIPANT"]
        # print("     id : {}".format(id))
        # print("type(id): {}".format(type(id)))

        x = new2_row["X"]
        y = new2_row["Y"]

        width = 16
        height = 16

        html.append(
            """
#box{} {{
    position: absolute;
    left    : {: >4}px;
    top     : {: >4}px;
    width   : {: >4}px;
    height  : {: >4}px;
    background-color: {};
}}
            """.format(
                id,
                x * width,
                y * height,
                width,
                height,
                new2_row["GENRE_CODE"])
        )

    return "".join(html)


write()
