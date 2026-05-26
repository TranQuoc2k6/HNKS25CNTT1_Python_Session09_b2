"""
- Sau khi chạy dòng lệnh dưới đây, danh sách express_orders thay đổi như thế nào?
express_orders.insert(0, "GE100-FAST")
    + danh sách express_order sẽ được thêm vào đầu danh sách giá trị GE100-FAST
- Vì sao dòng sau sửa nhầm đơn hàng "GE101" thay vì sửa "GE102-WRONG"?
express_orders[1] = "GE102-UPDATED"
    + trước đó đã thêm mới giá trị vào đầu danh sách nên index của "GE102-WRONG" phải là 2
- Sau khi chèn "GE100-FAST" vào đầu danh sách, "GE102-WRONG" đang nằm ở index nào?
    + "GE102-WRONG" nằm có index = 2
- Nếu muốn xóa đúng đơn hàng "GE103-CANCEL", nên dùng remove() như thế nào?
    + express_orders.remove("GE103-CANCEL")
- Phương thức pop() không truyền index sẽ lấy phần tử ở đâu trong danh sách?
    + sẽ lấy phần tử ở cuối trong danh sách
- Vì sao dòng sau lấy sai đơn hàng đang giao?
current_order = express_orders.pop()
    + Vì k chuyền index vào cho phương thức pop() sẽ mặc định là lấy phần tử cuối nên logic sẽ sai
- Muốn lấy đơn hàng đầu tiên trong danh sách ra để giao, cần viết lệnh như thế nào?
    + truyền index = 0
"""


# Danh sách đơn hàng ban đầu
express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
express_orders.append("GE104")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
express_orders.insert(0, "GE100-FAST")

# Sửa mã đơn hàng bị nhập sai
express_orders[2] = "GE102-UPDATED"

# Xóa đơn hàng bị khách hủy
express_orders.pop(3)

# Lấy đơn hàng đầu tiên ra để bắt đầu giao
current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)

