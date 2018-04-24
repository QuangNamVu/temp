Input: Ma trận kích thước [m+2]*[n+2]
Ouput: List các bước di chuyển

Đối với Block độ dài là 2 có 3 chiều x,y,z ứng với trục tọa độ

status_table: Dùng để lưu vết có kích thước [m+2]*[n+2]*[3]:

Nếu status_table[1][2][0] == 1 có nghĩa block đã đi qua ô 1 2 với chiều(dimension) x 
Nếu status_table[1][2][1] == 1 có nghĩa block đã đi qua ô 1 2 với chiều(dimension) y

Nếu status_table[1][2][2] == 1 có nghĩa block đã đi qua ô 1 2 với chiều(dimension) z
