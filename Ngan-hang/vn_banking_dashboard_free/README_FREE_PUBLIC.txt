VIETNAM BANKING DASHBOARD V1.1 — FREE PUBLIC BETA

Hosting miễn phí đề xuất:
- Cloudflare Pages Free: giao diện public, subdomain *.pages.dev
- Render Free: API, có thể ngủ sau 15 phút không hoạt động
- Supabase Free: PostgreSQL, có thể pause nếu ít hoạt động
- GitHub Free: lưu mã nguồn

Bắt đầu bằng DEPLOYMENT_FREE_PUBLIC.md.

Bảo mật:
- Chỉ public quyền đọc.
- Không đưa BANKING_WRITE_KEY, DATABASE_URL, SSI_API_SECRET hoặc service_role key vào frontend/GitHub.
- Các endpoint ghi dữ liệu/import CSV phải dùng X-API-Key.

Lưu ý dữ liệu:
- Dữ liệu demo trong dashboard chỉ minh họa, không phải dữ liệu ngân hàng đã xác minh.
- Chưa có feed tự động báo cáo tài chính ngân hàng.
- Gói miễn phí phù hợp thử nghiệm/public beta, không có SLA.
