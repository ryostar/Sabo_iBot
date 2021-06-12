** = >> Phát bài hát 🎧**

- `/play` : Phát bài hát được yêu cầu
- `/play [yt url]` : Phát url yt đã cho
- `/play [âm thanh trả lời]` : Phát âm thanh đã trả lời
- `/dplay` : Phát bài hát qua deezer
- `/splay` : Phát bài hát qua jio saavn
- `/ytplay` : Phát trực tiếp bài hát qua Youtube Music

**=>> Phát lại ⏯**

- `/player` : Mở menu Cài đặt của trình phát
- `/skip` : Bỏ qua bản nhạc hiện tại
- `/pause` : Tạm dừng bản nhạc
- `/resume` : Tiếp tục bản nhạc đã tạm dừng
- `/end` : Dừng phát lại phương tiện
- `/current` : Hiển thị bản nhạc Đang phát hiện tại
- `/playlist` : Hiển thị danh sách phát

*Cmd trình phát và tất cả cmd khác ngoại trừ /play, /current và /playlist chỉ dành cho quản trị viên của nhóm.
""",
        
f"""
**=>> Kênh Chơi Nhạc 🛠 **

⚪️ Chỉ dành cho quản trị viên nhóm được liên kết:

- `/cplay [tên bài hát]` - phát bài hát bạn yêu cầu
- `/cdplay [tên bài hát]` - phát bài hát bạn yêu cầu qua deezer
- `/csplay [tên bài hát]` - phát bài hát bạn yêu cầu qua jio saavn
- `/cplaylist` - Hiển thị danh sách đang phát
- `/cccurrent` - Hiện đang phát
- `/cplayer` - mở bảng cài đặt trình phát nhạc
- `/cpause` - tạm dừng phát bài hát
- `/cresume` - tiếp tục phát bài hát
- `/cskip` - phát bài hát tiếp theo
- `/cend` - dừng phát nhạc
- `/userbotjoinchannel` - mời trợ lý vào cuộc trò chuyện của bạn

kênh cũng có thể được sử dụng `c` ( `/cplay` = `/channelplay` )

⚪️ Nếu bạn không muốn chơi trong nhóm được liên kết:

1) Nhận ID kênh của bạn.
2) Tạo nhóm với tên `Channel Music: your_channel_id`
3) Thêm bot làm quản trị viên Kênh với đầy đủ các quyền
4) Thêm @{ASSISTANT_NAME} vào kênh với tư cách quản trị viên.
5) Đơn giản chỉ cần gửi lệnh trong nhóm của bạn.
""",

f"""
**=>> Các công cụ khác 🧑‍🔧**

- `/musicplayer [on/off]` : Bật/Tắt Trình phát nhạc
- `/admincache` : Cập nhật thông tin quản trị viên của nhóm của bạn. Hãy thử nếu bot không nhận ra quản trị viên
- `/userbotjoin` : Mời @{ASSISTANT_NAME} Userbot tham gia cuộc trò chuyện của bạn

**=>> Lệnh cho người dùng Sudo ⚔️**

 - `/userbotleaveall` - xóa trợ lý khỏi tất cả các cuộc trò chuyện
 - `/ib <trả lời tin nhắn>` - tin nhắn đã trả lời brodcast trên toàn cầu cho tất cả các cuộc trò chuyện
 - `/pmpermit [on/off]` - bật/tắt thông báo pmpermit
*Người dùng Sudo có thể thực hiện bất kỳ lệnh nào trong bất kỳ nhóm nào
