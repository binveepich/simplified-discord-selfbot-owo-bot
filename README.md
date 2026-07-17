# Simplified OwO Discord Selfbot ✨

> Một công cụ tự động hoá cho Discord, tập trung vào hệ thống lệnh **OwO** với giao diện terminal gọn gàng, cấu hình linh hoạt và nhiều chế độ chạy thông minh.

---

## 📌 Giới thiệu

**Simplified OwO Discord Selfbot** là một project Python được thiết kế để tự động hoá các tác vụ thường dùng trong kênh Discord, đặc biệt là các lệnh liên quan đến **OwO** như:

- `hunt`
- `battle`
- `pray`
- `daily`
- `sell`
- `exp / owo`
- `gems`

Project được chia thành nhiều module rõ ràng: `main.py` điều phối luồng chính, `gems.py` xử lý logic gems, `data.py` quản lý cấu hình, `menu.py` lo phần giao diện terminal, `color.py` xử lý màu sắc, và `exception.py` ghi nhận lỗi khi phát sinh.  

---

## ✨ Tính năng nổi bật

- Tự động gửi lệnh `hunt` và `battle` theo chu kỳ.
- Hỗ trợ `pray`, `daily`, `sell`, `exp` và `gems`.
- Có cơ chế kiểm tra captcha / ban để dừng bot kịp thời.
- Hỗ trợ webhook thông báo khi có sự cố.
- Có lệnh selfbot riêng để bật/tắt từng chế độ ngay trong Discord.
- Giao diện console có logo, màu sắc và hiển thị trạng thái hoạt động đẹp mắt.
- Đọc toàn bộ cấu hình từ `settings.json`, dễ chỉnh sửa và bảo trì.

---

## 🧩 Công nghệ sử dụng

- Python 3.x
- `discum`
- `requests`
- `inputimeout`
- `discord-webhook`

---

## 📂 Cấu trúc dự án

```bash
.
├── main.py
├── gems.py
├── menu.py
├── data.py
├── color.py
├── exception.py
├── version.py
├── settings.json
├── requirements.txt
└── README.md
````

---

## ⚙️ Yêu cầu cài đặt

Hãy đảm bảo bạn đã cài:

* Python 3.10+ (khuyên dùng)
* pip

Sau đó cài dependencies:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Cấu hình

Toàn bộ cấu hình nằm trong file `settings.json`.

### Mẫu cấu hình:

```json
{
  "token": "",
  "channel": "",
  "gm": "YES",
  "sm": "YES",
  "pm": "YES",
  "em": {
    "text": "YES",
    "owo": "YES"
  },
  "webhook": {
    "link": null,
    "ping": null
  },
  "sbcommands": {
    "enable": "NO",
    "prefix": ".",
    "allowedid": null
  },
  "daily": "YES",
  "stop": "9000",
  "sell": {
    "enable": "YES",
    "types": "all"
  }
}
```

### Ý nghĩa một số trường quan trọng

* `token`: token tài khoản Discord
* `channel`: ID kênh cần bot hoạt động
* `gm`: bật/tắt chế độ gems
* `sm`: bật/tắt sleep mode
* `pm`: bật/tắt pray mode
* `em.text`: bật/tắt gửi text ngẫu nhiên
* `em.owo`: bật/tắt gửi `owo / uwu`
* `webhook.link`: đường dẫn webhook Discord
* `webhook.ping`: ID người nhận ping khi có cảnh báo
* `sbcommands.prefix`: tiền tố lệnh selfbot
* `sbcommands.allowedid`: ID được phép dùng lệnh selfbot
* `daily`: bật/tắt tự claim daily
* `stop`: thời gian dừng sau bao nhiêu giây
* `sell.enable`: bật/tắt auto sell
* `sell.types`: loại vật phẩm cần sell

---

## 🚀 Cách chạy

Sau khi cấu hình xong `settings.json`, chạy:

```bash
python main.py
```

---

## ⌨️ Lệnh selfbot hỗ trợ

Nếu bật `sbcommands`, bạn có thể dùng:

* `.send <nội dung>` — gửi tin nhắn tuỳ ý
* `.restart` — khởi động lại chương trình
* `.exit` — thoát chương trình
* `.gm on/off` — bật/tắt gems mode
* `.pm on/off` — bật/tắt pray mode
* `.sm on/off` — bật/tắt sleep mode
* `.em on/off` — bật/tắt exp mode
* `.gems` — kích hoạt xử lý gems thủ công

> Lưu ý: thay dấu `.` bằng prefix bạn đặt trong `settings.json`.

---

## 🔒 An toàn & lưu ý

* Hãy kiểm tra kỹ `token` và `channel` trước khi chạy.
* Nên dùng trên môi trường thử nghiệm trước khi áp dụng thực tế.
* Project có cơ chế phát hiện lỗi, captcha/ban và sẽ dừng khi gặp tình huống bất thường.
* Một số tính năng có thể thay đổi tuỳ vào cập nhật từ phía Discord hoặc bot đích.

---

## Câu hỏi thường gặp

#### Có thể kiếm được bao nhiêu tiền trong một ngày?


Khoảng 1.500.000 Cowoncy với Kim cương Huyền thoại trở lên

#### Selfbot này có hoạt động hiệu quả trên tài khoản mới không?

Không, Selfbot này không thể hoạt động hiệu quả trên tài khoản mới. Bạn cần ít nhất một đội hình chiến đấu và một số Kim cương trước vì Selfbot này không thể xây dựng một tài khoản hoàn hảo từ con số không.

#### Tôi có thể bị cấm khỏi OwO không?

Có, chỉ khi bạn không giải được Captcha của OwO. Selfbot này sẽ tự động xử lý nếu được yêu cầu Captcha. Nhưng bạn vẫn cần phải giải nó.

#### Tôi có thể chạy nó trên điện thoại Android của mình không?

Có, ứng dụng Termux có thể chạy mã Python và các ngôn ngữ lập trình khác như Git hoặc Javascript. Bạn có thể sử dụng nó để cài đặt Selfbot theo hướng dẫn được cung cấp. Thông tin thêm: https://termux.com/

Còn câu hỏi nào khác? Hãy thoải mái mở vấn đề hoặc liên hệ với tôi trên Discord: [tham gia máy chủ Discord của tôi](https://discord.gg/c7tRHWKhhP) rồi gắn thẻ @youzke

---

## 🏷️ Phiên bản

Hiện tại project đang ở phiên bản:

```bash
0.0.1
```

---

## 📜 License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

---

## 🙌 Kết

Cảm ơn bạn đã ghé qua project này.
Nếu thấy hữu ích, hãy để lại ⭐ để ủng hộ nhé!
