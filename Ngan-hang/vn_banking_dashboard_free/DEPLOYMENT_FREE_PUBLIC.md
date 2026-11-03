# Vietnam Banking Dashboard V1.1 — Free Public Deployment

## Mô hình miễn phí đề xuất
- Frontend: Cloudflare Pages Free (`*.pages.dev`) — website công khai.
- API: Render Free — có thể ngủ sau 15 phút không có request; lần truy cập đầu sau khi ngủ có thể mất khoảng 1 phút để khởi động.
- Database: Supabase Free — 500 MB database, 5 GB egress theo hạn mức hiện hành; dự án ít hoạt động có thể bị tạm dừng sau 1 tuần.
- Source code: GitHub Free (có thể để repository Private).
- Domain: dùng subdomain miễn phí `*.pages.dev`; không cần mua tên miền.

Đây là cấu hình thử nghiệm/public beta, không phải hạ tầng production có SLA. Các giới hạn miễn phí có thể thay đổi theo nhà cung cấp.

## A. GitHub
1. Tạo repository `vietnam-banking-dashboard` trên GitHub. Có thể chọn Private.
2. Đưa toàn bộ nội dung thư mục dự án vào repository, bao gồm `index.html`, `backend/`, `supabase/`, `render.yaml`.
3. Không commit file `.env` hoặc mật khẩu/secret thật.

## B. Supabase Free
1. Tạo project mới trên Supabase Free.
2. Vào SQL Editor > New query.
3. Mở `supabase/schema.sql`, copy toàn bộ nội dung, dán vào SQL Editor và bấm Run.
4. Vào Connect/Database, lấy connection string PostgreSQL (ưu tiên Session Pooler nếu môi trường cần IPv4).
5. Giữ kín mật khẩu database. Khi đưa vào Render, chuyển scheme thành `postgresql+psycopg://` nếu cần.
6. Không đưa `service_role` key hoặc database URL vào HTML/browser.

## C. Render Free API
1. Đăng nhập Render, chọn New > Blueprint.
2. Kết nối GitHub và chọn repository `vietnam-banking-dashboard`.
3. Render đọc `render.yaml`. File này đã đặt `plan: free`.
4. Điền `DATABASE_URL` bằng connection string Supabase.
5. `BANKING_WRITE_KEY` được Render tự tạo theo cấu hình `generateValue: true`. Nếu giao diện yêu cầu tự nhập, tạo chuỗi ngẫu nhiên dài tối thiểu 32 ký tự.
6. Tạm đặt `CORS_ORIGINS` là `*` chỉ trong giai đoạn kiểm tra ban đầu nếu chưa biết URL Pages. Sau khi Pages được tạo, thay bằng chính xác URL `https://TEN-DU-AN.pages.dev` (không thêm dấu `/` cuối). Nếu API hỗ trợ danh sách nhiều origin, phân tách bằng dấu phẩy.
7. Để trống `SSI_API_KEY` và `SSI_API_SECRET` nếu chưa được cấp quyền SSI FastConnect.
8. Deploy và kiểm tra `https://TEN-API.onrender.com/health` phải trả về trạng thái OK.

Lưu ý: Render Free web service tự spin down sau 15 phút không có request; lần truy cập kế tiếp có thể chờ khoảng 1 phút. Filesystem cục bộ không bền vững, vì vậy phải dùng Supabase, không dùng SQLite làm database online.

## D. Cloudflare Pages Free
1. Đăng ký/đăng nhập Cloudflare.
2. Mở Workers & Pages > Create application > Pages > Connect to Git.
3. Kết nối GitHub và chọn repository.
4. Project name: `minhtriinvest-banking` (hoặc tên còn trống).
5. Production branch: `main`.
6. Framework preset: None / No framework.
7. Build command: `exit 0`.
8. Build output directory: `.` (thư mục gốc, nơi có `index.html`).
9. Root directory: để mặc định.
10. Save and Deploy. Cloudflare cấp URL dạng `https://TEN-DU-AN.pages.dev`.

## E. Kết nối frontend và API
1. Trong Render, sửa `CORS_ORIGINS` thành URL `https://TEN-DU-AN.pages.dev` vừa nhận.
2. Lưu và redeploy API.
3. Mở website Pages, bấm `Kết nối API`, nhập URL `https://TEN-API.onrender.com`.
4. Kiểm tra dữ liệu từ endpoint `/dashboard/records` hiển thị trên dashboard.

## F. Public Read — Private Write
- Các endpoint GET như `/health`, `/banks`, `/observations`, `/dashboard/records`, `/metrics/catalog`, `/sources/status` có thể đọc công khai.
- Các endpoint POST và import CSV phải giữ `BANKING_WRITE_KEY` ở phía người quản trị; tuyệt đối không nhúng khóa vào JavaScript, HTML, GitHub hoặc chia sẻ công khai.
- Khách truy cập có thể xem dashboard mà không cần đăng nhập; họ không được phép ghi vào database.
- Không nhập dữ liệu cá nhân/khách hàng hoặc dữ liệu chưa có quyền công bố.
- Hiện dashboard có dữ liệu demo minh họa. Cần thay bằng dữ liệu đã kiểm chứng và ghi rõ kỳ báo cáo, đơn vị, hợp nhất/riêng lẻ, nguồn, ngày công bố và ngày cập nhật.

## G. Giới hạn / rủi ro của gói miễn phí
- Render Free có thể ngủ sau 15 phút idle và không được khuyến nghị cho production.
- Supabase Free có giới hạn dung lượng/egress; dự án ít hoạt động có thể bị pause sau 7 ngày.
- Cloudflare Pages Free phù hợp host website tĩnh; giới hạn của Functions/Workers không áp dụng nếu chỉ host file tĩnh.
- Gói miễn phí và quota thay đổi theo thời gian; theo dõi dashboard usage của từng nhà cung cấp.
- Đây là public beta, không có cam kết uptime/SLA, backup tự động dài hạn hoặc nguồn dữ liệu ngân hàng tự động.

## H. Nguồn dữ liệu
- CSV thủ công: dùng `DATA_IMPORT_TEMPLATE.csv` và endpoint `/import/csv`.
- Danh mục ngân hàng: dùng `BANK_REGISTRY_TEMPLATE.csv`, cần đối chiếu giấy phép/danh sách hiện hành của NHNN.
- SSI FastConnect adapter chỉ lấy securities master theo cấu hình hiện tại; không phải nguồn BCTC ngân hàng.
- Dữ liệu WiGroup/FiinGroup hoặc nhà cung cấp khác cần hợp đồng, API credentials và quyền hiển thị lại dữ liệu công khai.
