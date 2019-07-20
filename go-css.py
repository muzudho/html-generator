import pandas as pd
from attribute.query_id_sorted_table import query_id_sorted_table

#
# Note.
#
# Root directory: Visual studio code workspace root.
#
pa_file_name = "./html-generator/auto-generated/participants.css"

# Participant data.
# pa_df = pd.read_csv("./html-generator/data/participant.csv",
#                     sep=',', engine='python')

# Floor map data.
fl_df = pd.read_csv("./html-generator/data/floor-map.csv",
                    sep=',', engine='python')
# print(fl_df.values.tolist())

# Data frame. (Not record set)
pa_df = query_id_sorted_table("./html-generator/data/participant.csv")
"""
print(pa_df.values.tolist())
[[30, 'Blue'], [6, 'Blue'], [56, 'Blue'], [50, 'Blue'], [40, 'Blue'], [33, 'Blue'], [27, 'Blue'], [22, 'Blue'], [17, 'Blue'], [15, 'Blue'], [8, 'Blue'], [4, 'Blue'], [3, 'Blue'], [60, 'Blue'], [5, 'Green'], [10, 'Green'], [14, 'Green'], [9, 'Green'], [29, 'Green'], [36, 'Green'], [42, 'Green'], [44, 'Green'], [53, 'Green'], [57, 'Green'], [16, 'Yellow'], [20, 'Yellow'], [26, 'Yellow'], [31, 'Yellow'], [43, 'Yellow'], [51, 'Yellow'], [58, 'Yellow'], [18, 'Yellow'], [1, 'Red'], [7, 'Red'], [2, 'Red'], [52, 'Red'], [41, 'Red'], [37, 'Red'], [21, 'Red'], [12, 'Red'], [59, 'White'], [48, 'White'], [39, 'White'], [25, 'White'], [54, 'Orange'], [46, 'Black'], [24, 'Black'], [23, 'Black'], [32, 'Orange'], [38, 'Orange'], [35, 'Gray'], [49, 'Gray'], [13, 'Violet'], [34, 'Pink'], [28, 'Pink'], [55, 'Violet'], [19, 'SkyBlue'], [11, 'Purple'], [45, 'YellowGreen'], [47, 'Brown']]
"""


def write():
    try:
        file = open(pa_file_name, 'w', encoding='utf-8')
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
    for _index, pa_row in pa_df.iterrows():

        # Participant id.
        id = pa_row["ID"]
        print("     id : {}".format(id))
        print("type(id): {}".format(type(id)))

        # Floor map.
        row2 = fl_df[fl_df["ID"] == id]
        # print("row2: {}".format(row2))

        x = row2[["X"]].values.tolist()[0][0]
        print("     x : {}".format(x))
        # x = int(row2[["X"]].values.tolist())
        # print("     x : {}".format(x))
        print("type(x): {}".format(type(x)))
        # print("x: {}".format(x))
        y = row2[["Y"]].values.tolist()[0][0]
        # print("{}={},{}".format(id, x, y))

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
                pa_row["GENRE_CODE"])
        )

    return "".join(html)


write()
