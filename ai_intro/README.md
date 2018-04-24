
# Table of Contents

1.  [Input](#org52877a4)
2.  [Cấu trúc file:](#org2253d51)
3.  [Đối với Block độ dài là 2 có 3 chiều x,y,z ứng với trục tọa độ](#org42b77cd)
4.  [Nhận xét](#orgccb869d)


<a id="org52877a4"></a>

# Input

Input: Ma trận kích thước [m+2]\*[n+2]
Ouput: List các bước di chuyển, Với trường hợp không ra tìm được lời giải, bài toán sẽ dừng.


<a id="org2253d51"></a>

# Cấu trúc file:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">map/Tên<sub>File.txt</sub></td>
<td class="org-left">Input</td>
</tr>


<tr>
<td class="org-left">src/main.py</td>
<td class="org-left">Code thực thi</td>
</tr>


<tr>
<td class="org-left">src/display.py</td>
<td class="org-left">Hiển thị</td>
</tr>


<tr>
<td class="org-left">src/generate.py</td>
<td class="org-left">Tạo các bước di chuyển trái phải lên xuống từ 1 node</td>
</tr>
</tbody>
</table>


<a id="org42b77cd"></a>

# Đối với Block độ dài là 2 có 3 chiều x,y,z ứng với trục tọa độ

status<sub>table</sub>: Dùng để lưu vết có kích thước [m+2]\*[n+2]\*[3].
Tác Dụng: Để tránh node con giống node cha của cha, đặc biệt tránh loop trong DFS.

Nếu status<sub>table</sub>[1][2][0] `= 1 có nghĩa block đã đi qua ô 1 2 với chiều(dimension) x .
Nếu status_table[1][2][1] =` 1 có nghĩa block đã đi qua ô 1 2 với chiều(dimension) y.

Nếu status<sub>table</sub>[1][2][2] == 1 có nghĩa block đã đi qua ô 1 2 với chiều(dimension) z.


<a id="orgccb869d"></a>

# Nhận xét

Giải thuật DFS và BFS luôn chạy ra kết quả ( không loop) với luật rõ ràng vì:
Số trường hợp tối đa sinh ra trong trường hợp bài 1 là (m\*n\*3) khi block chạy hết các ô và mỗi ô có 3 status.

Tìm kiếm BFS luôn cho ra lời giải tốt nhất.

Lời giải cho BFS trong src/map/3.txt mất 9 steps.
Lời giải cho DFS trong src/map/3.txt mất 53 steps.

